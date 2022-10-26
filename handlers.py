from settings import EMOJI, BARS, BEERS
from utils import get_menu_buttons, validate_age, get_query


def get_start(update, context):
    print("Вызван/start")
    update.message.reply_text(
        f"Вам уже исполнилось 18 лет?"
        f"{EMOJI[1]}Чрезмерное упортребление алкоголя вредит Вашему здоровью.",
        reply_markup=validate_age(),
    )


def get_validate_answer(update, context):
    query = update.callback_query
    variant = query.data
    query.answer()
    if variant == "Да":
        query.message.reply_text(
            f"Здравствуй, любитель {EMOJI[0]}!", reply_markup=get_menu_buttons()
        )
    if variant == "Нет":
        query.message.reply_text(f"{EMOJI[2]} Извините, но Вам сюда нельзя!", reply_markup=None)


def get_all_bars(update, context):
    bars = get_query(BARS[0])
    bars = bars["results"]
    for bar in bars:
        text = bar["name"]
        update.message.reply_text(text)


def get_all_beers(update, context):
    beers = get_query(BEERS[0])
    beers = beers["results"]
    for beer in beers:
        text = (
            beer["name"]
            + "\n\n"
            + "Цена:"
            + str(int(beer["price"] / 200))
            + "\n\n"
            + beer["description"]
        )
        update.message.reply_text(text)


def get_user_location(update, context):
    coordinates = update.message.location
    print(coordinates)
