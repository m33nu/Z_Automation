import os
import slack

client = slack.WebClient(token=os.environ['SLACK_ZYLLU_API_TOKEN'])

response = client.chat_postMessage(
    channel='#taknator-emails',
    text="shan test")
assert response["ok"]
assert response["message"]["text"] == "shan test"