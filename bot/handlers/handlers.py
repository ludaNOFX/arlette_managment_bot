from aiogram import types, Dispatcher

from bot.db.requests import register_check, add_user, get_users, set_active


ID = None


async def admin(message: types.Message):
    global ID
    ID = message.from_user.id
    await message.bot.send_message(message.from_user.id, 'Прив, Админ 🤡')


async def start(message: types.Message):
    db_session = message.bot.get("db")
    user_id = message.from_user.id
    if message.chat.type == 'private':
        x = await register_check(db_session, user_id)
        if x:
            await message.answer(
                'Привет, красотка!\nЭтот бот мы с командой Arlette Management создали для того, чтобы ты всегда была в курсе новых кастингов в нашей группе ВКонтакте.\nКаждый раз, когда наши букеры публикуют кастинг, в боте будет приходить уведомление ❤️'
            )
            await message.delete()
        if not x:
            await add_user(db_session, user_id)
            await message.answer(
                'Привет, красотка!\nЭтот бот мы с командой Arlette Management создали для того, чтобы ты всегда была в курсе новых кастингов в нашей группе ВКонтакте.\nКаждый раз, когда наши букеры публикуют кастинг, в боте будет приходить уведомление ❤️'
            )
            await message.delete()


async def send_all(message: types.Message):
    if message.from_user.id == ID:
        db_session = message.bot.get("db")
        if message.chat.type == 'private':
            text = message.text[6:]
            users = await get_users(db_session)
            for row in users:
                try:
                    await message.bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        await set_active(db_session, row[0], 1)
                except:
                    await set_active(db_session, row[0], 0)
            await message.bot.send_message(message.from_user.id, 'Done 😤')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(send_all, commands=['send'])
    dp.register_message_handler(admin, commands=['admin'], is_chat_admin=True)