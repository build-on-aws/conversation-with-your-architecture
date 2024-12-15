# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""
This demo illustrates how to chat with your architecture to analyze architecture diagrams, evaluate
effectiveness, get recommendations and make informed decisions, and generate new diagrams that reflect your
environment, system, and company standards. It uses Amazon Bedrock's Converse API.
The script interacts with a foundation model on Amazon Bedrock to provide information based on an architecture diagram
and user input.
"""

import boto3
import logging
import os
from enum import Enum
from dotenv import load_dotenv

import util.demo_print_utils as output

logging.basicConfig(level=logging.INFO, format="%(message)s")

load_dotenv()
AWS_REGION = os.getenv('AWS_REGION')

# For the most recent list of models supported by the Converse API's tool use functionality, visit:
# https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html
class SupportedModels(Enum):
    CLAUDE_OPUS = "anthropic.claude-3-opus-20240229-v1:0"
    CLAUDE_SONNET = "anthropic.claude-3-sonnet-20240229-v1:0"
    CLAUDE_SONNET_35 = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    CLAUDE_HAIKU = "anthropic.claude-3-haiku-20240307-v1:0"
    COHERE_COMMAND_R = "cohere.command-r-v1:0"
    COHERE_COMMAND_R_PLUS = "cohere.command-r-plus-v1:0"

# Supported image formats
image_formats = {
    "png": "png",
    "jpg": "jpeg",
    "jpeg": "jpeg"
}

# Set the model ID
MODEL_ID = SupportedModels.CLAUDE_SONNET_35.value

SYSTEM_PROMPT = """
You are an AWS Solutions Architect who can answer questions about an architecture diagram.
"""

# The maximum number of recursive calls allowed in the run function.
# This helps prevent infinite loops and potential performance issues.
MAX_RECURSIONS = 5

class ArchitectureChatDemo:
    """
    Demonstrates how to chat with your architecture using the Amazon Bedrock Converse API.
    """

    def __init__(self):
        # Prepare the system prompt
        self.system_prompt = [{"text": SYSTEM_PROMPT}]

        # Create a Bedrock Runtime client in the specified AWS Region.
        self.bedrock_runtime_client = boto3.client(
            "bedrock-runtime", region_name=AWS_REGION
        )

    def run(self):
        """
        Starts the conversation with the user and handles the interaction with Bedrock.
        """
        # Print the greeting and a short user guide
        output.header()

        # Start with an emtpy conversation
        conversation = []

        # Architecture diagram to use
        architecture_diagram_file = self._get_user_input("What is the name of the file you want to chat with? File must be located in the demo/ directory.")
        if architecture_diagram_file is None:
          output.footer()
          return

        # Get the first user input
        user_input = self._get_user_input()

        while user_input is not None:

            # Send the architecture_diagram_file if there is one
            if architecture_diagram_file:
              # All diagrams must reside in demo directory
              architecture_diagram_file = f"demo/{architecture_diagram_file}"

              _, file_extension = os.path.splitext(architecture_diagram_file)
              file_extension = file_extension.lstrip('.').lower()

              if file_extension in image_formats:

                  with open(architecture_diagram_file, "rb") as image_file:
                      image_bytes = image_file.read()

                      # Claude works best when images come before text.
                      # https://docs.anthropic.com/en/docs/build-with-claude/vision#prompt-examples
                      message = {
                          "role": "user",
                          "content": [
                              {
                                  "image": {
                                      "format": image_formats[file_extension],
                                      "source": {
                                          "bytes": image_bytes
                                      }
                                  }
                              },
                              { "text": "Referencing " + architecture_diagram_file + ", " + user_input }
                          ],
                      }
                      architecture_diagram_file = None

              else:
                  architecture_diagram_file = None
                  print(f"Unsupported image format: '{file_extension}' not in {list(image_formats.keys())}")
                  break

            else:
              # Create a new message with the user input and append it to the conversation

              message = {"role": "user", "content": [{"text": user_input}]}

            conversation.append(message)

            # Send the conversation to Amazon Bedrock
            bedrock_response = self._send_conversation_to_bedrock(conversation)

            # Recursively handle the model's response until the model has returned
            # its final response or the recursion counter has reached 0
            self._process_model_response(
                bedrock_response, conversation, max_recursion=MAX_RECURSIONS
            )

            # Repeat the loop until the user decides to exit the application
            user_input = self._get_user_input()

        output.footer()

    def _send_conversation_to_bedrock(self, conversation):
        """
        Sends the conversation and the system prompt to Amazon Bedrock, and returns the response.

        :param conversation: The conversation history including the next message to send.
        :return: The response from Amazon Bedrock.
        """
        output.call_to_bedrock(conversation)

        # Send the conversation and system prompt, and return the response
        return self.bedrock_runtime_client.converse(
            modelId=MODEL_ID,
            messages=conversation,
            system=self.system_prompt,
        )

    def _process_model_response(
        self, model_response, conversation, max_recursion=MAX_RECURSIONS
    ):
        """
        Processes the response received via Amazon Bedrock and performs the necessary actions
        based on the stop reason.

        :param model_response: The model's response returned via Amazon Bedrock.
        :param conversation: The conversation history.
        :param max_recursion: The maximum number of recursive calls allowed.
        """

        if max_recursion <= 0:
            # Stop the process, the number of recursive calls could indicate an infinite loop
            logging.warning(
                "Warning: Maximum number of recursions reached. Please try again."
            )
            exit(1)

        # Append the model's response to the ongoing conversation
        message = model_response["output"]["message"]
        conversation.append(message)

        if model_response["stopReason"] == "end_turn":
            # If the stop reason is "end_turn", print the model's response text, and finish the process
            output.model_response(message["content"][0]["text"])
            return

    @staticmethod
    def _get_user_input(prompt="Your query"):
        """
        Prompts the user for input and returns the user's response.
        Returns None if the user enters 'x' to exit.

        :param prompt: The prompt to display to the user.
        :return: The user's input or None if the user chooses to exit.
        """
        output.separator()
        user_input = input(f"{prompt} (x to exit): ")

        if user_input == "":
            prompt = "Please enter your query"
            return ArchitectureChatDemo._get_user_input(prompt)

        elif user_input.lower() == "x":
            return None

        else:
            return user_input


if __name__ == "__main__":
    architecture_chat_demo = ArchitectureChatDemo()
    architecture_chat_demo.run()