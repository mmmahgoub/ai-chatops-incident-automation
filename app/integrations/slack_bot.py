import os
from slack_bolt import App
from app.services.incident import handle_query

slack_app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@slack_app.event("app_mention")
def handle_mention(event, say):
    user_input = event["text"]

    response = handle_query(user_input)

    say(f"🤖 {response}")