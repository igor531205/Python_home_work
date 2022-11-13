import logging
import os
from telegrambot import telegram_bot


if __name__ == '__main__':

    # Upload librarys to requirements.txt
    os.system('pip freeze > requirements.txt')

    # Clear Terminal
    os.system('cls')

    # Init logger
    logging.basicConfig(filename='logging.log', filemode='a',
                        format='; '.join([
                            f'%(asctime)s',
                            f'%(name)s',
                            f'%(levelname)s',
                            f'%(message)s']),
                        level=logging.INFO, encoding='utf-8')

    # Init Bot Token and Username owner of Bot "@GB_for_HomeWork_bot"
    BOT_TOKEN = '5484436077:AAHRLCdLdDzLyRbU2M3iWsRkOHIM_DmFQeE'

    # Run bot
    telegram_bot(BOT_TOKEN)
