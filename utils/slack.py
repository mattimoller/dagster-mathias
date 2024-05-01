import json

import requests


# Function to send a message to Slack
def send_slack_message(payload: dict, webhook_url: str):
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        raise ValueError(
            f"Request to slack returned an error {response.status_code}, the response is:\n{response.text}"
        )
