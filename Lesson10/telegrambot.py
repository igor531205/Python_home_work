import os
import logging
import signal
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""

    log.info(', '.join([
        f'Chat: {update.message.chat_id}',
        f'User: {update.message.from_user.username}',
        f'FullName: {update.message.from_user.full_name}',
        f'Message: {update.message.text}']))

    init_result()

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(f'Calculator: {result[0]}', reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""

    def action(data: str):
        """Action +,-,*,/."""

        if result[2]:
            calculate(result)

        if type(result[0]) == int:
            result[2] = data
            result[1] = result[0]
            result[0] = 0

    query = update.callback_query

    await query.answer()

    reply_markup = InlineKeyboardMarkup(keyboard)

    if query.data == '=':
        calculate(result)
        result[0] = str(result[0])

    elif query.data == '+':
        action(query.data)

    elif query.data == '-':
        action(query.data)

    elif query.data == '*':
        action(query.data)

    elif query.data == '/':
        action(query.data)

    else:
        result[0] = int(str(result[0]) + query.data)

    if type(result[0]) == str:
        await query.edit_message_text(text=f'Calculator: {result[0]}')
    else:
        await query.edit_message_text(text=f'Calculator: {result[0]}', reply_markup=reply_markup)


def calculate(result: list):
    """Calculator."""

    match result[2]:
        case '+':
            result[0] = result[1] + result[0]
            result[2] = ''
        case '-':
            result[0] = result[1] - result[0]
            result[2] = ''
        case '/':
            result[0] = result[1] // result[0] if result[0] \
                else 'ERROR: "Division by 0"'
            result[2] = ''
        case '*':
            result[0] = result[1] * result[0]
            result[2] = ''
        case _:
            result[0] = str(result[0])


def init_result():
    """Create result list."""
    global result
    result = [int(), int(), str()]


async def unknown(update, context):
    """Parses unknown commands."""

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Sorry, I didn't understand that command.")


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Parses and updates the message text."""

    await update.message.reply_text(update.message.text)


async def bot_kill(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Command kill for bot."""

    log.info(', '.join([
        f'Chat: {update.message.chat_id}',
        f'User: {update.message.from_user.username}',
        f'FullName: {update.message.from_user.full_name}',
        f'Message: {update.message.text}']))

    await update.message.reply_text(f'You "Kill" me, {update.message.from_user.full_name}')

    os.kill(os.getpid(), signal.SIGABRT)


def telegram_bot(BOT_TOKEN: str):
    """Start the Telegram Bot.
    Args:
        BOT_TOKEN: Key for bot.
    """

    # Create the Logger
    global log
    log = logging.getLogger(__name__)

    # Create the Application and pass bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    init_result()

    global keyboard
    keyboard = [
        [
            InlineKeyboardButton('7', callback_data='7'),
            InlineKeyboardButton('8', callback_data='8'),
            InlineKeyboardButton('9', callback_data='9'),
            InlineKeyboardButton('/', callback_data='/'),
        ],
        [
            InlineKeyboardButton('4', callback_data='4'),
            InlineKeyboardButton('5', callback_data='5'),
            InlineKeyboardButton('6', callback_data='6'),
            InlineKeyboardButton('*', callback_data='*'),
        ],
        [
            InlineKeyboardButton('1', callback_data='1'),
            InlineKeyboardButton('2', callback_data='2'),
            InlineKeyboardButton('3', callback_data='3'),
            InlineKeyboardButton('-', callback_data='-'),
        ],
        [
            InlineKeyboardButton('=', callback_data='='),
            InlineKeyboardButton('0', callback_data='0'),
            InlineKeyboardButton('.', callback_data='.'),
            InlineKeyboardButton('+', callback_data='+'),
        ],
    ]

    # On different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, message))
    application.add_handler(CommandHandler('kill', bot_kill))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()
