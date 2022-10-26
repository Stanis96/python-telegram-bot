import logging
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers import get_start, get_user_location, get_all_beers, get_validate_answer, get_all_bars


logging.basicConfig(filename="bot.log", level=logging.INFO)


def main():
    bot = Updater(settings.TOKEN, use_context=True)

    dp = bot.dispatcher
    dp.add_handler(CommandHandler("start", get_start))
    dp.add_handler(CallbackQueryHandler(get_validate_answer))
    dp.add_handler(CommandHandler("bars", get_all_bars))
    dp.add_handler(CommandHandler("beers", get_all_beers))
    dp.add_handler(MessageHandler(Filters.location, get_user_location))

    logging.info("Bot start")
    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
