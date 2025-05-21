from .progress import progress
from .tools import human_to_bytes, humanbytes, md5, time_formatter
from telegram.ext import Updater

updater = Updater(token=TOKEN, use_context=True) #hay que poner el token de botfather
dispatcher = updater.dispatcher