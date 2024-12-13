# Conversation With Your Architecture Demo

This project demonstrates how to chat with your architecture using Amazon Bedrock's Converse API, tool use, and a knowledge base. Implemented in Python, the demo allows users to analyze architecture diagrams, evaluate effectiveness, get recommendations, and make informed decisions about their system architecture.

The application interacts with a foundation model on Amazon Bedrock to provide information based on an architecture diagram and user input. It utilizes three custom tools to gather information:

1. Audit Info Tool: Provides audit information about a system based on the system name inferred from the architecture diagram file name.
2. Joy Count Tool: Provides joy count data about a system.
3. Best Practices Tool: Provides a company's best practices information, including best practices around how much joy the application is generating.

This demo is based on the [Amazon Bedrock Tool Use Demo](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime/cross-model-scenarios/tool_use_demo) and parts of [Amazon Bedrock: Enhance HR Support with Function Calling & Knowledge Bases blog post](https://community.aws/content/2izvh9HlmMvgYyRMoOUbkR0bNPV/enhancing-hr-support-with-function-calling-and-knowledge-bases-in-amazon-bedrock).

## ⚠️ Warning

Running this app may result in charges to your AWS account.

## Repository Structure

- `architecture_chat_demo.py`: Main entry point for the demo application.
- `audit_info_tool.py`: Implementation of the Audit Info Tool.
- `best_practices_tool.py`: Implementation of the Best Practices Tool.
- `joy_count_tool.py`: Implementation of the Joy Count Tool.
- `demo/`: Directory containing sample data files.
  - `audit-info.json`: Sample audit information for the Fluffy Puppy Joy Generator system.
  - `best-practices-data.md`: Sample best practices data for the organization
  - `joy-count.json`: Sample joy count data for the Fluffy Puppy Joy Generator system.
- `util/`: Directory containing utility functions.
  - `demo_print_utils.py`: Utility functions for printing demo-related messages.
- `README.md`: This file, containing project documentation.

## Usage Instructions

### Prerequisites

To run this demo, you'll need a few bits set up first:

- An AWS account. You can create your account [here](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).
- Request access to an AI model (we'll use Claude Sonnet) on Amazon Bedrock before you can use it. Learn about model access [here](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).
- [Python 3.6.0 or later](https://www.python.org/) setup and configured on your system.
- A [python virtual environment setup](https://docs.python.org/3/library/venv.html) with packages installed via [requirements.txt](requirements.txt).

### Setup

Set up your custom environmeng variables by creating a `.env` file in the project root directory with the following content:
     
```
AWS_REGION=<your-aws-region>
KNOWLEDGE_BASE_ID=<your-knowledge-base-id>
```

### Run the app

To run the app, run the following command in your virtual environment:

```bash
python architecture_chat_demo.py
```

2. When prompted, enter `fluffy-puppy-joy-generator.png` when prompted for a diagram to chat with (or check out the next section to use your own).

3. Then enter one of the example queries to interact with the diagram or ask your questions about the architecture.

4. To exit the demo, type `x` and press Enter.

### Bring your own diagram

Want to chat with your own diagram? Drop an image file (jpg, jpeg, or png) into the `demo` folder and rerun the app. When prompted, enter the full name (excluding the path) of that diagram to chat with.

### Sample queries

Below are some sample queries you could use to chat with an architecture diagram in this app:

- List the AWS Services used in the architecture diagram by official AWS name and excluding any sub-titles.
- What are the recommended strategies for unit testing this architecture?
- How well does this architecture adhere to the AWS Well Architected Framework?
- What improvements should be made to the resiliency of this architecture?
- Convert the data flow from this architecture into a Mermaid formatted sequence diagram.
- What are the quotas or limits in this architecture?

### Bonus: Generate the infrastructure code

Depending on the type of diagram you're chatting with, you could also enter the following query to generate the infrastructure code:

```plaintext
Can you generate the Terraform code to provision this architecture?
```

## Data Flow

1. User Input: The user provides input through the command-line interface.
2. Architecture Chat Demo: The main `ArchitectureChatDemo` class processes the user input and manages the conversation flow.
3. Amazon Bedrock: The user's input is sent to Amazon Bedrock's Converse API along with the system prompt and tool configurations.
4. Tool Invocation: Based on the model's response, the appropriate tool (Audit Info, Joy Count, or Best Practices) is invoked.
5. Tool Processing: The invoked tool fetches data from its respective source (JSON files or knowledge base).
6. Response Generation: The tool's output is sent back to Amazon Bedrock for further processing and response generation.
7. User Output: The final response is displayed to the user through the command-line interface.

See [sequence diagram](sequencediagram.mmd).

## Troubleshooting

- If you encounter authentication errors, ensure your AWS credentials are correctly set up in your environment or AWS credentials file.
- If the demo fails to start, check that all required environment variables are set in the `.env` file.
- For issues with tool invocations, verify that the JSON files in the `demo/` directory are present and correctly formatted.

To enable debug mode, set the `logging` level to `DEBUG` in the `architecture_chat_demo.py` file:

```python
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
```

This will provide more detailed output about the conversation flow and tool invocations.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
