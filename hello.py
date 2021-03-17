# Create the Hello Class
class hello:

    # Create a constant that contains the default text for the message
    HELLO_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey!!!....\n I am ChatBot.\n Type 'help' if you don't know what i can do. :-)\n"
            ),
        },
    }

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel


    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.HELLO_BLOCK,
            ],
        }
