# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:28:58 2022

@author: Usuario
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import codecs

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

tornar = '\n\nTorna al principi amb /start\n\n'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update: Update, context: CallbackContext) -> None:

    name = update.message.from_user.username
    update.message.reply_text(
        f"Hola {name}, soy el *bot de la catedra de Programacion de la\'Facultad De Cs. Exactas Unsa* \U0001F3EB. ", parse_mode='Markdown'
    )
    update.message.reply_text(
        'Que necesitas saber:\n\n'
        '0. Ubicacion de la Facultad de Cs. Exactas/ ubicacion \n'
        '1. ¿Cuando inician las clases? / inicioClases \n'
        '2. ¿Donde me inscribo? / inscripcion \n'
        '3. Registracion en AulaVirtual / aulaVirtual \n'
        '4. Acceso al Aula Virtual / accesoAlAulaVirtual \n'
        '5. Modalidad de Cursado / modalidadDeCursado \n'
        '6. Parciales / parciales \n'
        '7  Nota sobre la pandemia  / pandemia \n'
        '8  Carga horaria  / cargaHoraria \n'
        '9  Aulas  / aulas \n'
        '10  Docentes / docentes \n'
        '![Foto de l\'Facultad de Ciensas Exactas Unsa\'](https://th.bing.com/th/id/OIP.vAPnbqwJ-x7TagICAYot1AHaHa?w=203&h=203&c=7&r=0&o=5&dpr=1.25&pid=1.7)', parse_mode='Markdown'
    )
    update.message.reply_text(tornar)


def aulaVirtual(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
         'La catedra te matricularà en el aula virtual (AV) \n'
         'Para matricularte usamos el correo electronico que proporcionaste en el formulario de inscripcion \n'
         'El aula virtual se encuentra instalada en : '
        'https://exavirtual.unsa.edu.ar/enrol/index.php?id=533'
        '\n\nRetorna al principio /start\n\n'
    )
    update.message.reply_text(tornar)


def inicioClases(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'La clases inician el dia 17 de agosto de 2022'
        '\n\nRetorna al principio  /start\n\n'
    )

def inscripcion(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'debes completar el formulario que te enviamos por mail \n'
        'Formulario:  \n'
        'Importante En el formulario te preguntaremos el esquema de vacunacion Sea cual sea tu respuesta, nada impide que curses la materia'
        '\n\nRetorna al principio  /start\n\n'
    )

def accesoAlAulaVirtual(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'una vez que  llenes el formulario podras acceder al AV desde el dia 17/08/2022 \n'
        'Importante: Si llenas el formulario despues del 17/08/2022 para acceder al V debes esperar 24 hs habiles de haber llenado el formulario'
        '\n\nRetorna al principio  /start\n\n'
        )

def modalidadDeCursado(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'La modalidad de cursado de Programacion es bimodal;presencial y virtual. Las clases y las consultas se ofreceran, algunas virtuales y otras presenciales.'
        '\n\nRetorna al principio  /start\n\n'
    )

def parciales(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'Las evaluaciones parciales seran presenciales'
        '\n\nRetorna al principio  /start\n\n'
    )

def pandemia(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'Por cuestiones de aforo,el/la alumno/a debe asistir solamente a las clases asignadas.'
        '\n\nRetorna al principio /start\n\n'
    )

def aulas(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'las aulas seran publicadas , el  dia 17/08/2022 tanto en el AV como en la pizarra de la catedra \n '
        '\n\nRetorna al principio /start\n\n'

    )

def docentes(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'Teoria :\n\n'
        '* Lic. Marcela Lopez BOX 19\n'
        '* Lic. Ariel  Rivera  BOX 27\n\n'
        'Practica :\n\n'
        '* Carina Reyes BOX 3\n'
        '* Eduardo Fernandez BOX 3\n'
        '* Cecilia Espinoza BOX 3\n'
        '* Claudio Vargas BOX 3\n'
        '* Claudia Ibarra BOX 3\n'
         'Ayudante : \n\n'
         '* Sr. Facundo Darfe BOX 3\n'

        '\n\nRetorna al principio /start\n\n'


    )

def ubicacion(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'Avenida Bolivia 5150 4400 Salta Salta · \n\n'
        '![Hacer click](https://www.bing.com/maps?q=unsa+exactas+salta+&qs=n&form=QBRE&sp=-1&pq=unsa+exactas+salta+&sc=1-19&sk=&cvid=A4D1391BED334A29A182DDB528C9A718)', parse_mode='Markdown'
        '\n\nRetorna al principio /start\n\n'
    )

def cargaHoraria(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        'Programacion tiene una carga semanal de 10 horas; 4 horas de teoria y 6 de practica. Se cursa los dias lunes, miercoles y viernes.\n\n'
        '\n\nRetorna al principio /start\n\n'

    )


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def telegram(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Telegram es una aplicación de mensajería instantánea de código abierto, segura, privada, multi-plataforma, rápida, basada en la nube y gratuita'
    )


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        "5379249312:AAEBnT6hUER08neR1DigCPQ-ZKZQBpl2RSM", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ubicacion", ubicacion))
    dispatcher.add_handler(CommandHandler("telegram", telegram))

    dispatcher.add_handler(CommandHandler("inicioClases", inicioClases))
    dispatcher.add_handler(CommandHandler("inscripcion", inscripcion))
    dispatcher.add_handler(CommandHandler("aulaVirtual", aulaVirtual))
    dispatcher.add_handler(CommandHandler("accesoAlAulaVirtual", accesoAlAulaVirtual))
    dispatcher.add_handler(CommandHandler("modalidadDeCursado", modalidadDeCursado))
    dispatcher.add_handler(CommandHandler("parciales", parciales))
    dispatcher.add_handler(CommandHandler("pandemia", pandemia))
    dispatcher.add_handler(CommandHandler("docentes", docentes))
    dispatcher.add_handler(CommandHandler("aulas", aulas))
    dispatcher.add_handler(CommandHandler("cargaHoraria", cargaHoraria))


    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
