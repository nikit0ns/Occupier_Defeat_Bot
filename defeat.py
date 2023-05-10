from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandObject
import asyncio

import aiohttp
import config


bot = Bot(token = config.TOKEN, parse_mode = 'HTML') #Ваш токен
dp = Dispatcher()

@dp.message(Command(commands = ['start']))
async def cmd_start(message: types.Message):
    await message.answer('<b>👋 Привіт, я Бот Втрати Окупанта.\n'
                         '🪖 Загальні бойові втрати російського окупанта.\n'
                         '🚢 Російський військовий кораблю, іди нахуй!\n\n'
                         '🗑 Втрати окупанта - /defeat\n'
                         '⁉️ Технічна підтримка - /help</b>')

@dp.message(Command(commands = ['defeat']))
async def cmd_defeat(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer('⚠️ <b>Неправильно вибрана команда.</b>')
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://russianwarship.rip/api/v2/statistics/latest') as resp:
                data = await resp.json()
        
        await message.answer(f'''<b>🪖 Загальні бойові втрати російського окупанта.\n'''
                             f'''📋 <a href = "{data["data"]["resource"]}">Станом на {data["data"]["date"]}</a>\n'''
                             f'''🗓 День війни: {data["data"]["day"]}-й \n\n'''
                             f'''- Особовий склад: {data["data"]["stats"]["personnel_units"]} {f"(+{data['data']['increase']['personnel_units']})" if data['data']['increase']['personnel_units'] > 0 else ''}\n'''
                             f'''- Танки: {data["data"]["stats"]["tanks"]} {f"(+{data['data']['increase']['tanks']})" if data['data']['increase']['tanks'] > 0 else ''}\n'''
                             f'''- ББМ: {data['data']['stats']['armoured_fighting_vehicles']} {f"(+{data['data']['increase']['armoured_fighting_vehicles']})" if data['data']['increase']['armoured_fighting_vehicles'] > 0 else ''}\n'''
                             f'''- Арт. системи: {data['data']['stats']['artillery_systems']} {f"(+{data['data']['increase']['artillery_systems']})" if data['data']['increase']['artillery_systems'] > 0 else ''}\n'''
                             f'''- РСЗВ: {data['data']['stats']['mlrs']} {f"(+{data['data']['increase']['mlrs']})" if data['data']['increase']['mlrs'] > 0 else ''}\n'''
                             f'''- Засоби ППО: {data['data']['stats']['aa_warfare_systems']} {f"(+{data['data']['increase']['aa_warfare_systems']})" if data['data']['increase']['aa_warfare_systems'] > 0 else ''}\n'''
                             f'''- Літаки: {data['data']['stats']['planes']} {f"(+{data['data']['increase']['planes']})" if data['data']['increase']['planes'] > 0 else ''}\n'''
                             f'''- Гелікоптери: {data['data']['stats']['helicopters']} {f"(+{data['data']['increase']['helicopters']})" if data['data']['increase']['helicopters'] > 0 else ''}\n'''
                             f'''- Автотехніка/автоцистерни: {data['data']['stats']['vehicles_fuel_tanks']} {f"(+{data['data']['increase']['vehicles_fuel_tanks']})" if data['data']['increase']['vehicles_fuel_tanks'] > 0 else ''}\n'''
                             f'''- Кораблі/катери: {data['data']['stats']['warships_cutters']} {f"(+{data['data']['increase']['warships_cutters']})" if data['data']['increase']['warships_cutters'] > 0 else ''}\n'''
                             f'''- БПЛА: {data['data']['stats']['uav_systems']} {f"(+{data['data']['increase']['uav_systems']})" if data['data']['increase']['uav_systems'] > 0 else ''}\n'''
                             f'''- Спец. техніка: {data['data']['stats']['special_military_equip']} { f"(+{data['data']['increase']['special_military_equip']})" if data['data']['increase']['special_military_equip'] > 0 else ''}\n'''
                             f'''- Установки ОТРК/ТРК: {data['data']['stats']['atgm_srbm_systems']} {f"(+{data['data']['increase']['atgm_srbm_systems']})" if data['data']['increase']['atgm_srbm_systems'] > 0 else ''}\n'''
                             f'''- Крилаті ракети: {data['data']['stats']['cruise_missiles']} {f"(+{data['data']['increase']['cruise_missiles']})" if data['data']['increase']['cruise_missiles'] > 0 else ''}\n\n'''
                             f'''🇺🇦 Слава Україні! Героям Слава!</b>''', disable_web_page_preview = True)


@dp.message(Command(commands = ['help']))
async def cmd_help(message: types.Message):
    await message.answer("⁉️<b> Якщо у вас є проблеми.</b> \n"
                         "✉️ <b>Напишіть мені</b> <a href = 'https://t.me/nikit0ns'>@nikit0ns</a><b>.</b>", 
                         disable_web_page_preview = True)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())