# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

def header():
    """
    Logs the welcome message and usage guide for the demo.
    """
    print("\033[0m")
    separator("=")
    print("Welcome to the Conversation With Your Architecture demo!")
    separator("=")
    print("This assistant provides a way to chat with your architecture to analyze architecture diagrams, evaluate")
    print("effectiveness, get recommendations and make informed decisions, and generate new diagrams that reflect your")
    print("environment, system, and company standards.")
    print("")
    print("In this demo, we'll chat with an architecture diagram of your choice, located in the demos directory. Use the")
    print("sample diagram 'fluffy-puppy-joy-generator.png' to start.")
    print("")
    print("Sample queries:")
    print("- List the AWS Services used in the architecture diagram by official AWS name and excluding any sub-titles.")
    print("- What are the recommended strategies for unit testing this architecture?")
    print("- How well does this architecture adhere to the AWS Well Architected Framework?")
    print("- What improvements should be made to the resiliency of this architecture?")
    print("- Convert the data flow from this architecture into a Mermaid formatted sequence diagram.")
    print("- What are the quotas or limits in this architecture?")
    print("- Can you generate the Cloudformation/CDK/Terraform code to provision this architecture?")
    print("- What is the joy count of this system?")
    print("")
    print("To exit the program, simply type 'x' and press Enter.")
    print("")

def footer():
    """
    Logs the footer information for the demo.
    """
    print("\033[0m")
    separator("=")
    print("Thank you for checking out the Conversation With Your Architecture demo. We hope you")
    print("learned something new or got some inspiration for your own apps today!")
    print("")
    print(
        "For more Bedrock examples in different programming languages, have a look at:"
    )
    print(
        "https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples.html"
    )
    separator("=")


def call_to_bedrock(conversation):
    """
    Logs information about the call to Amazon Bedrock.

    :param conversation: The conversation history.
    """
    if "toolResult" in conversation[-1]["content"][0]:
        print("\033[0;90mReturning the tool response(s) to the model...\033[0m")
    else:
        print("\033[0;90mSending the query to the model...\033[0m")


def tool_use(tool_name, input_data):
    """
    Logs information about the tool use.

    :param tool_name: The name of the tool being used.
    :param input_data: The input data for the tool.
    """
    print(f"\033[0;90mExecuting tool: {tool_name} with input: {input_data}...\033[0m")


def model_response(message):
    """
    Logs the model's response.

    :param message: The model's response message.
    """
    print("\033[0;90mThe model's response:\033[0m")
    print(message)


def separator(char="-"):
    """
    Logs a separator line.

    :param char: The character to use for the separator line.
    """
    print(char * 80)