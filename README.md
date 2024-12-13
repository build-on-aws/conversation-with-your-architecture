# Conversation with your architecture

A demo app to chat with your architecture diagram. Implemented in Python, this app uses the Amazon Bedrock Converse API to carry out a conversation between a large language model and the user. Shows how to use tools for function calling and incorporate an Amazon Bedrock Knowledge Base for more custom insights.

This demo is based on the [Amazon Bedrock Tool Use Demo](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/bedrock-runtime/cross-model-scenarios/tool_use_demo) and parts of [Amazon Bedrock: Enhance HR Support with Function Calling & Knowledge Bases blog post](https://community.aws/content/2izvh9HlmMvgYyRMoOUbkR0bNPV/enhancing-hr-support-with-function-calling-and-knowledge-bases-in-amazon-bedrock).

## ⚠️ Warning

Running this app may result in charges to your AWS account.

## Prerequisites

To run this demo, you'll need a few bits set up first:

- An AWS account. You can create your account [here](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).
- Request access to an AI model (we'll use Claude Sonnet) on Amazon Bedrock before you can use it. Learn about model access [here](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).
- [Python 3.6.0 or later](https://www.python.org/) setup and configured on your system.
- A [python virtual environment setup](https://docs.python.org/3/library/venv.html) with packages installed via [requirements.txt](requirements.txt).

## Run the app

To run the app, run the following command in your virtual environment:

```bash
python architecture_chat_demo.py
```

Enter `fluffy-puppy-joy-generator.png` when prompted for a diagram to chat with (or check out the next section to use your own). Then enter one of the example queries to interact with the diagram.

## Bring your own diagram

Want to chat with your own diagram? Drop an image file (jpg, jpeg, or png) into the `demo` folder and rerun the app. When prompted, enter the full name (excluding the path) of that diagram to chat with.

## Sample queries

Below are some sample queries you could use to chat with an architecture diagram in this app:

- List the AWS Services used in the architecture diagram by official AWS name and excluding any sub-titles.
- What are the recommended strategies for unit testing this architecture?
- How well does this architecture adhere to the AWS Well Architected Framework?
- What improvements should be made to the resiliency of this architecture?
- Convert the data flow from this architecture into a Mermaid formatted sequence diagram.
- What are the quotas or limits in this architecture?

## Bonus: Generate the infrastructure code

Depending on the type of diagram you're chatting with, you could also enter the following query to generate the infrastructure code:

```plaintext
Can you generate the Terraform code to provision this architecture?
```

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
