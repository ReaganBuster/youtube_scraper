from pickle import TRUE
from bot.scraper import Bot

with Bot(teardown=TRUE) as bot:
    bot.load_video(url='https://www.youtube.com/watch?v=yXCMU72z0Ms')