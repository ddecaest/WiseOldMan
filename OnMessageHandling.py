from typing import List, Any


class OnMessageHandling:
    def __init__(self, handlers: List[Any]):
        self.handlers = handlers

    def handle_message(self, message):
        responses = []
        for handler in self.handlers:
            response = handler(message)
            responses.append(response)
        return responses


def find_armour_handler(message):
    command = "?armour "

    if (message.content.startswith(command)):
        from RunescapeWikiScraper import get_armour
        armour = get_armour(message.content[len(command):])
        return armour
    else:
        return ""