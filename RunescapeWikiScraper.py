import re

import requests
from bs4 import BeautifulSoup


def get_armour(nameOfEntity):
    request_response = requests.get(build_url(nameOfEntity))
    parsed_response = str(BeautifulSoup(request_response.content, 'html.parser'))

    # the armour attribute looks like this:
    # armour = 1924\n|
    # armour1 = 1486|armour2 = 1486| ...
    start_of_attribute = parsed_response.find("armour")
    end_of_attribute = start_of_attribute + parsed_response[start_of_attribute:].find('|')
    start_of_armour_value = start_of_attribute + parsed_response[start_of_attribute:end_of_attribute].rfind(" ")

    return parsed_response[start_of_armour_value:end_of_attribute].replace("\\n", "")


def build_url(nameOfEntity):
    runescape_wiki_entity_name = to_runescape_wiki_entity_name(nameOfEntity)
    return "https://runescape.wiki/api.php?action=query&prop=revisions&rvprop=content&titles=" + runescape_wiki_entity_name + "&format=json"


def to_runescape_wiki_entity_name(rawName):
    words_in_entity_name = re.sub("[ ]+", " ", rawName).strip().split(" ")

    words_all_lower = [word.lower() for index, word in enumerate(words_in_entity_name)]

    if len(words_all_lower) > 0:
        words_all_lower[0].capitalize()

    return "_".join(words_all_lower)
