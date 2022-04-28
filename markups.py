from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='🗯️Меню🗯️',callback_data='menu')
menu.insert(btn1)

menu2 = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='🕕Режим работы🕕',callback_data='rezhim')
btn2 = InlineKeyboardButton(text='🏩Адрес🏩',callback_data='adres')
btn3 = InlineKeyboardButton(text='☎Контактные данные☎',callback_data='contact')
btn4 = InlineKeyboardButton(text='🤩Товар в наличии🤩',callback_data='tovar')
btn6 = InlineKeyboardButton(text='📩Подписка на рассылку📩',callback_data='podpis')
btn7 = InlineKeyboardButton(text='❌Отменить подписку на рассылку❌',callback_data='otpodpis')
menu2.insert(btn1)
menu2.insert(btn2)
menu2.insert(btn3)
menu2.insert(btn4)
menu2.insert(btn6)
menu2.insert(btn7)


back = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton(text='↩Вернуться назад в меню↩',callback_data='menu')
back.insert(btn1)