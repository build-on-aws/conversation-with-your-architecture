# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json

def get_tool_spec():
    """
    Returns the JSON Schema specification for the Joy Count tool. The tool specification
    defines the input schema and describes the tool's functionality.
    For more information, see https://json-schema.org/understanding-json-schema/reference.

    :return: The tool specification for the Joy Count tool.
    """
    return {
        "toolSpec": {
            "name": "Joy_Count_Tool",
            "description": "Get the current joy count for the system.",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {},
                }
            },
        }
    }


def fetch_joy_count_data():
    """
    Fetches joy count data for the system using the joy count API
    (which in this demo is the demo/joy-count.json file).
    Returns the joy count data or an error message if the request fails.

    :return: The joy count data or an error message.
    """

    # open json file joy-count.json
    with open("demo/joy-count.json", "r") as f:
        joy_count_data = json.load(f)

    return joy_count_data
