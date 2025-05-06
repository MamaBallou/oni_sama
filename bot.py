import schedule as Schedule
import time
import threading
from test_asynchrone import main
import asyncio

from src.main import run_bot

#permet d'appeler la fonction tout les jours à 18h10
def scheduler():
    async def run_main():
        await main()

    Schedule.every().days.at("18:10", "Europe/Paris").do(lambda: asyncio.run(run_main()))

    while True:
        Schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=scheduler, daemon=True) #garder daemon, permet de kill le thread en même temps que le bot
    scheduler_thread.start()
    run_bot()