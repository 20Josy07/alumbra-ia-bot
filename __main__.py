import importlib
import time
import re
from sys import argv
from typing import Optional

from HunterAlpha import (  #ojazo con esto, hay que cambiarlo
    ALLOW_EXCL,
    CERT_PATH,
    LOGGER,
    PORT,
    SUPPORT_CHAT,
    TOKEN,
    URL,
    WEBHOOK,
    SUPPORT_CHAT,
    dispatcher,
    StartTime,
    telethn,
    updater,
)

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    NetworkError,
    TelegramError,
    TimedOut,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown


PM_START_TEXT = """
**Hola {}, Mi Nombre es {}!** 
Te ayudo a detectar señales de abuso psicológico en tus conversaciones.
Usa /help para ver lo que puedo hacer.

"""

INFO_TEXT= """
*Alumbra IA* es un proyecto dedicado a ayudarte a detectar señales de abuso psicológico. 💭
Identifica dinámicas como humillación, chantaje emocional, manipulación o control.

Para más información y testimonios, visita nuestra página oficial:  
👉 [Alumbra.ai](http://alumbraia.com)
"""

FEEDBACK_TEXT= """
*Tu opinión nos importa*  
¡Queremos mejorar AlumbraIA contigo!

Completa esta breve encuesta y cuéntanos tu experiencia:  
👉 [Ir a la encuesta](https://encuestaahiquehagamosenformsdevalidacionons.com)
"""

HELP_STRINGS = """
Hola! mi nombre es *{}*.
Estoy aquí para ayudarte a ver tus conversaciones desde otra perspectiva 💜

*Comandos principales disponibles:*
 - /start: Mensaje de bienvenida e introducción breve a AlumbraIA.
 - /info: Descripción breve de la funcionalidad de AlumbraIA.
 - /help: Lista de comandos y guía rápida para usar AlumbraIA (este mensaje).
 - /analizar: Envía o copia tu conversación para que AlumbraIA la revise.
 - /resultados: Muestra el análisis más reciente de tus conversaciones.
 - /consejos: Obtén tips para cuidar tu bienestar emocional.
 - /feedback: Envía tu opinión o sugerencias para mejorar a AlumbraIA (incluye enlace a encuesta).

{}
""".format(dispatcher.bot.first_name, "" if not ALLOW_EXCL else "\nTodos los comandos pueden usarse con / o !.\n")


# do not async
def start_command(update: Update, context: CallbackContext) -> None:
    ALUMBRA_IMG = "https://telegra.ph/file/7e2f7a8b2d52c61bf5ced.jpg" #CAMBIAR

def info_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        INFO_TEXT,
        parse_mode=ParseMode.MARKDOWN_V2
    )

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        HELP_STRINGS,
        parse_mode= ParseMode.MARKDOWN_V2
    )

def analizar_command(update: Update, context: CallbackContext):
    pass

def resultados_command(update: Update, context: CallbackContext):
    pass

def consejos_command(update: Update, context: CallbackContext):
    pass

def feedback_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        FEEDBACK_TEXT,
        parse_mode=ParseMode.MARKDOWN_V2
    )

# for test purposes
def error_callback(update: Update, context: CallbackContext):
    error = context.error
    try:
        raise error
    except Unauthorized:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors


def main():
    start_handler = CommandHandler("start", start_command)
    help_handler = CommandHandler("help", help_command)
    info_handler = CommandHandler("info", info_command)
    analizar_handler = CommandHandler("analizar", analizar_command) #Creo que debemos de añadir que run_async=True a estos tres
    resultados_handler = CommandHandler("resultados", resultados_command) #Este
    consejos_handler = CommandHandler("consejos", consejos_command) #Y esteee
    feedback_handler = CommandHandler("feedback", feedback_command)
    

    # dispatcher.add_handler(test_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(info_handler)
    dispatcher.add_handler(analizar_handler)
    dispatcher.add_handler(resultados_handler)
    dispatcher.add_handler(consejos_handler)
    dispatcher.add_handler(feedback_handler)
    dispatcher.add_error_handler(error_callback)

    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN, certificate=open(CERT_PATH, "rb"))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)

    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()

    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)  
    main()