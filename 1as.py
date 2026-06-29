import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

TOKEN = "8849162870:AAGaPzyBOsqq3Q3GQ2o1yoMWiRD7npHEqcE"

bot = Bot(token=TOKEN)
dp = Dispatcher()


def get_stars_reward():
    return random.choices([25, 50, 100], weights=[90, 8, 2])[0]


@dp.message()
async def casino_handler(message: Message):
    # ❗ проверяем что это dice вообще
    if not message.dice:
        return

    # ❗ проверяем emoji
    if message.dice.emoji != "🎰":
        return

    value = message.dice.value

    print("DICE:", value)  # <-- ДЛЯ ПРОВЕРКИ В КОНСОЛИ

    if value == 64:
        msg = await message.reply("🎰 7️⃣7️⃣7️⃣ ДЖЕКПОТ!")

        await asyncio.sleep(1)
        await msg.edit_text("🎡 Крутим...")

        await asyncio.sleep(1)

        stars = get_stars_reward()

        await msg.edit_text(
            f"🎰 7️⃣7️⃣7️⃣ ДЖЕКПОТ!\n"
            f"🌟 +{stars} ⭐"
        )
    else:
        await message.reply("🎰 Не повезло 😢")


async def main():
    print("BOT STARTED")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
