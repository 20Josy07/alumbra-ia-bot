from .progress import progress
from .tools import human_to_bytes, humanbytes, md5, time_formatter
from telegram.ext import Updater

updater = Updater(token=TOKEN, use_context=True) 
dispatcher = updater.dispatcher