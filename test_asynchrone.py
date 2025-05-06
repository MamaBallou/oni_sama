import asyncio
from playwright.async_api import async_playwright, Playwright, Response, Request, Union
from datetime import (
    datetime as DateTime,
)  # pas toucher ça marche même si ça fait bugé le cerveau
import json as Json



# TODO
# Stockage en Json fait
# récuperer les données sur json fait 
# comparaison du json et des jeux amazones fait
# le script est appelé tout les jours à 18h10 # https://schedule.readthedocs.io/en/stable/ fait
# Si changement dans la liste de jeux : notification si il y a des nouveaux jeux, abs de notif si des jeux abs et la liste est refaite
# notification quand il reste plus que 24h pour récupérer un jeu => préparer des jobs (pour le moment non)
# commande pour afficher les jeux disponibles
# type affichage : nom des jeux ?, nom + image ?, une page par jeux ?, liste déroulante pour avoir une description plus détailler


# permet de stocker les données d'amazones
class AmazonGame(dict):
    id: str
    title: str
    description: str
    startTime: str
    endTime: str
    image: str

    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        startTime: str,
        endTime: str,
        image: str,
    ):
        dict.__init__(
            self,
            id=id,
            title=title,
            description=description,
            startTime=startTime,
            endTime=endTime,
            image=image,
        )


# offers > 0 > (startTime, endTime), assets > (title, shortformDescription); assets > cardMedia > defaultMedia > (src1x, src2x)


async def checkRequestAndStore(request: Request):
    """Check if the request is for retrieving games. If so, it gets the list of games from AmazonGaming website.
    
    :param request: The request to test if it 
    """
    # permet d'afficher que les urls contenant les infos pour les jeux
    if (
        "/graphql" in request.url
        and request.post_data_json["operationName"] == "OffersContext_Offers_And_Items"
    ):  # permet de récupérer la liste de jeux du moment
        response: Union[Response, None] = (
            await request.response()
        )  # permet de récupérer la réponse
        json: dict = (
            await response.json()
        )  # de la on prend le json qui est un dictionnaire
        if "data" in json.keys():
            if "games" in json["data"].keys():
                amazonGames: list[AmazonGame] = list(
                    map(
                        lambda game: AmazonGame(
                            id=game["id"],
                            title=game["assets"]["title"],
                            description=game["assets"]["shortformDescription"],
                            startTime=game["offers"][0]["startTime"],
                            endTime=game["offers"][0]["endTime"],
                            image=game["assets"]["cardMedia"]["defaultMedia"]["src1x"],
                        ),
                        json["data"]["games"]["items"],
                    )
                )
                comparison("test.json", amazonGames)
                #print(*amazonGames)

#Permet de comparer les de
def comparison(jsonPath: str, amazonGames: list[AmazonGame]):
    """Allow to compare the stored list of game and the new fetched one.

    :param jsonPath: The path to the json file where the last save of games is stored.
    :param amazonGames: List or the new fetched games.
    """
    # charger le ficher json
    with open(jsonPath, "r") as f:
        storedAmazonGames: list[AmazonGame] = list(Json.load(f))
    newGames = [x for x in amazonGames if x not in storedAmazonGames]
    #TODO penser à mettre un message que pour les nouveaux jeux
    oldGames = [x for x in storedAmazonGames if x not in amazonGames]
    if newGames or oldGames:
        with open("test.json", "w") as f:
            Json.dump(amazonGames, f)  # permet de sauvegarder les jeux


async def run(playwright: Playwright):
    print("RUNNING")
    chromium = playwright.chromium
    browser = await chromium.launch()
    page = await browser.new_page()
    # Subscribe to "request" and "response" events.
    page.on(
        "request", lambda request: checkRequestAndStore(request)
    )  # ça c'est comment on le cherche
    # page.on("response", lambda response: show_response(response)) #c'est la réponse
    await page.goto("https://gaming.amazon.com/home")  # la page ou on veut aller
    await asyncio.sleep(5)
    await browser.close()


async def main():
    print("Starting the script")
    async with async_playwright() as playwright:
        await run(playwright)
