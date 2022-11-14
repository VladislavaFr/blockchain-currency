# download and import libraries
import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert
cg = CoinGeckoAPI()

# enter your token
bot = telebot.TeleBot('Token')

# start the bot on command 'start' and creating buttons
@bot.message_handler(commands=['start'])
def main(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Курс крипты'), types.KeyboardButton('Курс фиата'), types.KeyboardButton('Конвертер'))
    cr = bot.send_message(message.chat.id, 'Мы на главной', reply_markup=b1)
    bot.register_next_step_handler(cr, step)

def step(message):
    if message.text == 'Курс крипты':
        step2(message)
    elif message.text == 'Курс фиата':
        fiat(message)
    elif message.text == 'Конвертер':
        convert1(message)
# creating buttons with cryptocurrency for converting
def convert1(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Bitcoin'), types.KeyboardButton('Ethereum'), types.KeyboardButton('Litecoin'),
           types.KeyboardButton('Polygon'), types.KeyboardButton('Uniswap'), types.KeyboardButton('Назад'))
    msg = bot.send_message(message.chat.id, 'Выберите криптовалюту', reply_markup=b1)
    bot.register_next_step_handler(msg, convert2)

def convert2(message):
    if message.text == 'Bitcoin':
         msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать BTC?')
         bot.register_next_step_handler(msg, bbtc)
    elif message.text == 'Ethereum':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать ETH?')
        bot.register_next_step_handler(msg, eeth)
    elif message.text == 'Litecoin':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать LTC?')
        bot.register_next_step_handler(msg, lltc)
    elif message.text == 'Polygon':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать MATIC?')
        bot.register_next_step_handler(msg, mmatic)
    elif message.text == 'Uniswap':
        msg = bot.send_message(message.chat.id, 'Сколько вы хотите конвертировать UNI?')
        bot.register_next_step_handler(msg, uuni)
    elif message.text == 'Назад':
        main(message)
# formulas for cryptocurrency conversion
def bbtc(message):
    convert2 = message.text
    convert2 = int(convert2)

    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} BTC == {price["bitcoin"]["usd"] * convert2} BTC')
    main(message)

def eeth(message):
    convert2 = message.text
    convert2 = int(convert2)

    price = cg.get_price(ids='ethereum', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} ETH == {price["ethereum"]["usd"] * convert2} ETH')
    main(message)

def lltc(message):
    convert2 = message.text
    convert2 = int(convert2)

    price = cg.get_price(ids='litecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} LTC == {price["litecoin"]["usd"] * convert2} LTC')
    main(message)

def mmatic(message):
    convert2 = message.text
    convert2 = int(convert2)

    price = cg.get_price(ids='matic-network', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} MATIC == {price["matic-network"]["usd"] * convert2} MATIC')
    main(message)

def uuni(message):
    convert2 = message.text
    convert2 = int(convert2)

    price = cg.get_price(ids='uniswap', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} UNI == {price["uniswap"]["usd"] * convert2} UNI')
    main(message)
# creating buttons for currencies at the fiat rate
def fiat(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('USD'), types.KeyboardButton('RUB'), types.KeyboardButton('Главная'))
    q = bot.send_message(message.chat.id, 'Курс фиата', reply_markup=b1)
    bot.register_next_step_handler(q, fiat_step2)
# formulas for converting currencies at the fiat rate
def fiat_step2(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Назад'))
    if message.text == 'USD':
        price = convert(base='USD', amount=1, to=['RUB', 'EUR', 'UAH', 'KZT'])
        bot.send_message(message.chat.id, f'1 USD == {price["RUB"]} RUB\n'
                                          f'1 USD == {price["EUR"]} EUR\n'
                        f'1 USD == {price["UAH"]} UAH\n'
                        f'1 USD == {price["KZT"]} KZT')
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    if message.text == 'RUB':
        price = convert(base='RUB', amount=1, to=['USD', 'EUR', 'UAH', 'KZT'])
        bot.send_message(message.chat.id, f'1 RUB == {price["USD"]} USD\n'
                                          f'1 RUB == {price["EUR"]} EUR\n'
                                          f'1 RUB == {price["UAH"]} UAH\n'
                                          f'1 RUB == {price["KZT"]} KZT')
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    if message.text == 'EUR':
        price = convert(base='EUR', amount=1, to=['USD', 'RUB', 'UAH', 'KZT'])
        bot.send_message(message.chat.id, f'1 EUR == {price["USD"]} USD\n'
                                          f'1 EUR == {price["RUB"]} RUB\n'
                                          f'1 EUR == {price["UAH"]} UAH\n'
                                          f'1 EUR == {price["KZT"]} KZT')
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    if message.text == 'UAH':
        price = convert(base='UAH', amount=1, to=['USD', 'EUR', 'RUS', 'KZT'])
        bot.send_message(message.chat.id, f'1 UAH == {price["USD"]} USD\n'
                                          f'1 UAH == {price["RUB"]} RUB\n'
                                          f'1 UAH == {price["EUR"]} EUR\n'
                                          f'1 UAH == {price["KZT"]} KZT')
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    if message.text == 'KZT':
        price = convert(base='KZT', amount=1, to=['USD', 'EUR', 'UAH', 'RUS'])
        bot.send_message(message.chat.id, f'1 KZT == {price["USD"]} USD\n'
                                          f'1 KZT == {price["RUB"]} RUB\n'
                                          f'1 KZT == {price["UAH"]} UAH\n'
                                          f'1 KZT == {price["EUR"]} EUR')
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    if message.text == 'Главная':
        main(message)

def step2(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Курс к RUB'), types.KeyboardButton('Главная'))
    q = bot.send_message(message.chat.id, 'Курс моих токенов', reply_markup=b1)
    bot.register_next_step_handler(q, step3)

def step3(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Назад'))


# functions for the rate of my tokens
    if message.text == 'Курс к RUB':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, matic-network, uniswap', vs_currencies='rub')
        bot.send_message(message.chat.id, f'Мои токены:\n\n'
                                              f'Bitcoin == {price["bitcoin"]["rub"]} RUB\n'
                                              f'Ethereum == {price["ethereum"]["rub"]} RUB\n'
                                              f'litecoin == {price["litecoin"]["rub"]} RUB\n'
                                              f'Polygon == {price["matic-network"]["rub"]} RUB\n'
                                              f'uniswap == {price["uniswap"]["rub"]} RUB', reply_markup=b1)
        go_main = bot.send_message(message.chat.id, 'Вернуться назад?', reply_markup=b1)
        bot.register_next_step_handler(go_main, step2)

    elif message.text == 'Главная':
        main(message)
bot.polling()

