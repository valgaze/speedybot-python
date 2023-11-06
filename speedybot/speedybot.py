import requests
import json
from .SpeedyCard import SpeedyCard
from typing import NamedTuple


class MessageResponse(NamedTuple):
    id: str
    roomId: str
    toPersonEmail: str
    roomType: str
    text: str
    personId: str
    personEmail: str
    markdown: str
    html: str
    created: str


class SpeedyBot:
    def __init__(self, token: str, make_request=requests.request):
        self.token = token
        self.middlewares = []
        self.top_middleware = None
        self.reject_middleware = None
        self.make_request = make_request
        self.API = {
            "messages": "https://webexapis.com/v1/messages",
            "attachments": "https://webexapis.com/v1/attachment/actions",
            "user": {
                "self": "https://webexapis.com/v1/people/me",
                "get_person_details": "https://webexapis.com/v1/people",
            },
            "rooms": "https://developer.webex.com/docs/api/v1/rooms/list-rooms",
            "room_details": "https://webexapis.com/v1/rooms",
            "webhooks": "https://webexapis.com/v1/webhooks",
        }

    def set_token(self, token):
        self.token = token

    def card(self):
        return SpeedyCard()

    def send_card_to(
        self,
        email_or_room_id: str,
        card: SpeedyCard,
        fallback="Your client does not support adaptive cards",
    ) -> MessageResponse:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        payload = {
            "toPersonEmail": email_or_room_id if "@" in email_or_room_id else None,
            "roomId": email_or_room_id if "@" not in email_or_room_id else None,
            "markdown": fallback,
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": card.build(),
                }
            ],
        }
        response = self.make_request(
            "POST", self.API["messages"], headers=headers, data=json.dumps(payload)
        )
        return response.json()

    def send_to(self, email_or_room_id, message) -> MessageResponse:
        """
        Send a message to an email or room. The message can be either a string or a SpeedyCard

        :param email_or_room_id: email address OR room id
        :param message: The message content to reply with.
        """

        if isinstance(message, SpeedyCard):
            return self.send_card_to(email_or_room_id, message)

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        payload = {"toPersonEmail": email_or_room_id, "markdown": message}
        response = self.make_request(
            "POST", self.API["messages"], headers=headers, data=json.dumps(payload)
        )
        return response.json()

    def reply(self, roomId, messageId, message: str) -> MessageResponse:
        """
        Reply to a message in a chat room.

        :param roomId: The ID of the chat room (not name)
        :param messageId: The ID of the message to reply, this message must exist or else the request will fail
        :param message: The message content to reply with.
        :return: The result of the reply operation as a string.
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        payload = {
            "parentId": messageId,
            "roomId": roomId,
            "text": message,
            "markdown": message,
        }
        response = self.make_request(
            "POST", self.API["messages"], headers=headers, data=json.dumps(payload)
        )
        return response.json()

    ## will unlock this later
    ## see https://speedybot.js.org to roll your own (not hard, just bunch of steps)
    # def add_middleware(self, middleware):
    #     self.middlewares.append(middleware)

    # def run_middleware(self, ctx):
    #     if self.top_middleware:
    #         result = self.top_middleware(ctx)
    #         if not result and self.reject_middleware:
    #             self.reject_middleware(ctx)
    #             return False
    #     for middleware in self.middlewares:
    #         result = middleware(ctx)
    #         if not result:
    #             if self.reject_middleware:
    #                 self.reject_middleware(ctx)
    #             break
    #     return True
