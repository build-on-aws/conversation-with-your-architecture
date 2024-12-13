# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json

def get_tool_spec():
    """
    Returns the JSON Schema specification for the Audit Info tool. The tool specification
    defines the input schema and describes the tool's functionality.
    For more information, see https://json-schema.org/understanding-json-schema/reference.

    :return: The tool specification for the Audit Info tool.
    """
    return {
        "toolSpec": {
            "name": "Audit_Info_Tool",
            "description": "Get the current audit info for a given system based on it's name.",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the system.",
                        },
                    },
                    "required": ["name"],
                }
            },
        }
    }


def fetch_audit_info_data(input_data):
    """
    Fetches audit info data for the given system name using the audit info API
    (which in this demo is the demo/audit-info.json file).
    Returns the audit info data or an error message if the request fails.

    :param input_data: The input data containing the system name.
    :return: The audit info data or an error message.
    """

    name = input_data.get("name")

    # open json file audit-info.json
    with open("demo/audit-info.json", "r") as f:
        audit_info_data = json.load(f)

    return audit_info_data
