# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import boto3
from langchain.prompts import PromptTemplate

PROMPT_TEMPLATE = """
DOCUMENT:
{document_text}
QUESTION:
{message}
INSTRUCTIONS:
Answer the user's QUESTION using only the DOCUMENT text above.
Keep your answer strictly grounded in the facts provided. Do not refer to the "DOCUMENT," "documents," "provided text," "based on" or any similar phrases in your answer.
If the provided text contains the facts to answer the QUESTION, include all relevant details in your answer.
If the provided text doesn’t contain the facts to answer the QUESTION, respond only with "I don't know" and do not add any further information.
"""

def get_tool_spec():
    """
    Returns the JSON Schema specification for the Best Practices tool. The tool specification
    defines the input schema and describes the tool's functionality.
    For more information, see https://json-schema.org/understanding-json-schema/reference.

    :return: The tool specification for the Best Practices tool.
    """
    return {
        "toolSpec": {
            "name": "Best_Practices_Tool",
            "description": "Gets the company best practices",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "The question to query the knowledge base.",
                        },
                    },
                    "required": ["question"],
                }
            },
        }
    }

def retrieve(query, number_of_results=3):
    """
    Retrieves the most relevant documents from the knowledge base using the given query.

    :param query: The query to search the knowledge base.
    :param number_of_results: The number of results to retrieve; defaults to 3.
    :return: The retrieval results.
    """

    aws_region = os.getenv('AWS_REGION')
    knowledge_base_id = os.getenv('KNOWLEDGE_BASE_ID')

    bedrock_agent_runtime_client = boto3.client(
        "bedrock-agent-runtime", region_name=aws_region
    )
    return bedrock_agent_runtime_client.retrieve(
        retrievalQuery= {
            'text': query
        },
        knowledgeBaseId=knowledge_base_id,
        retrievalConfiguration= {
            'vectorSearchConfiguration': {
                'numberOfResults': number_of_results,
                'overrideSearchType': "HYBRID"
            }
        }
    )

def get_retrieval_result_texts(retrieval_results):
    """
    Retrieves the text content from the retrieval results.

    :param retrieval_results: The retrieval results.
    :return: The text content, joined as a comma-separated string.
    """
    texts = []
    for retrieval_result in retrieval_results:
        text = retrieval_result['content']['text']
        texts.append(text)
    texts_string = ', '.join(texts)
    return texts_string

def fetch_best_practices_data(input_data):
    """
    Fetches best practices data from a knowledgebase using the given question to query.
    Returns the answer or an error message if the request fails.

    :param input_data: The input data containing the question.
    :return: The knowledgebase response or an error message.
    """
    question = input_data.get("question")

    retrieval_results = retrieve(question)["retrievalResults"]
    document_text = get_retrieval_result_texts(retrieval_results)

    prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["document_text", "message"])
    prompt_final = prompt.format(document_text=document_text, message=question)

    return { "prompt" : prompt_final }
