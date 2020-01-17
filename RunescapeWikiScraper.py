import requests
from bs4 import BeautifulSoup


def get_armour(nameOfEntity):
    page = requests.get(
        "https://runescape.wiki/api.php?action=query&prop=revisions&rvprop=content&titles=" + nameOfEntity + "&format=json")
    soup = BeautifulSoup(page.content, 'html.parser')

    html = str(soup)

    startOfArmourBullshit = html.find("armour")
    firstPipeThing = startOfArmourBullshit + html[startOfArmourBullshit:].find('|')
    lastSpace = startOfArmourBullshit + html[startOfArmourBullshit:firstPipeThing].rfind(" ")

    return html[lastSpace:firstPipeThing].replace("\\n", "")