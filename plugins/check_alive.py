import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("𝖡𝗎𝖽𝖽𝗒 𝖨𝖺𝗆 𝖠𝗅𝗂𝗏𝖾 :) 𝖧𝗂𝗍 /start \n\n𝖧𝗂𝗍 /help 𝖥𝗈𝗋 𝖧𝖾𝗅𝗉 ;)\n\n\n𝖧𝗂𝗍 /ping 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 𝖡𝗈𝗍 𝖯𝗂𝗇𝗀 😁")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("𝖧𝗂𝗍 /movie 𝖥𝗈𝗋 𝖬𝗈𝗏𝗂𝖾 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃\n\n𝖧𝗂𝗍 /series 𝖥𝗈𝗋 𝖲𝖾𝗋𝗂𝖾𝗌 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃\n\n\n𝖧𝗂𝗍 /tutorial 𝖥𝗈𝗋 𝖯𝗋𝗈𝗉𝖾𝗋 𝖳𝗎𝗍𝗈𝗋𝗂𝖺𝗅 𝖵𝗂𝖽𝖾𝗈𝗌 🤗")


@Client.on_message(filters.command("movie", CMD))
async def movie(_, message):
    await message.reply_text("⚠️❗️ 𝗠𝗼𝘃𝗶𝗲 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗙𝗼𝗿𝗺𝗮𝘁 ❗️⚠️\n\n📝 𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾, 𝖸𝖾𝖺𝗋,(𝖨𝖿 𝗒𝗈𝗎 𝖪𝗇𝗈𝗐) 𝖶𝗂𝗍𝗁 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀 📚\n\n🗣 𝖨𝖿 𝖨𝗍 𝗂𝗌 𝖺 𝖥𝗂𝗅𝗆 𝖲𝖾𝗋𝗂𝖾𝗌. 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖮𝗇𝖾 𝖡𝗒 𝖮𝗇𝖾 𝖶𝗂𝗍𝗁 𝖯𝗋𝗈𝗉𝖾𝗋 𝖭𝖺𝗆𝖾 🧠\n\n🖇𝐄𝐱𝐚𝐦𝐩𝐥𝐞:\n\n• Robin Hood ✅\n• Robin Hood 2010✅\n• Kurup 2021 Kan✅ \n• Harry Potter and the Philosophers Stone✅\n• Harry Potter and the Prisoner of Azkaban✅\n\n🥱 𝖥𝗈𝗋 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖠𝗎𝖽𝗂𝗈𝗌 - 𝖪𝖺𝗇 𝖿𝗈𝗋 𝖪𝖺𝗇𝗇𝖺𝖽𝖺, 𝖬𝖺𝗅 - 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆, 𝖳𝖺𝗆 - 𝖳𝖺𝗆𝗂𝗅\n\n🔎 𝖴𝗌𝖾 𝖥𝗂𝗋𝗌𝗍 3 𝖫𝖾𝗍𝗍𝖾𝗋𝗌 𝖮𝖿 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖥𝗈𝗋 𝖠𝗎𝖽𝗂𝗈𝗌 [𝖪𝖺𝗇 𝖳𝖺𝗆 𝖳𝖾𝗅 𝖬𝖺𝗅 𝖧𝗂𝗇 𝖲𝗉𝖺 𝖤𝗇𝗀 𝖪𝗈𝗋 𝖾𝗍𝖼...]\n\n❌ [𝗗𝗼𝗻𝘁 𝗨𝘀𝗲 𝘄𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗗𝘂𝗯𝗯𝗲𝗱/𝗠𝗼𝘃𝗶𝗲𝘀/𝗦𝗲𝗻𝗱/𝗛𝗗 , . : - 𝗲𝘁𝗰] ❌")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("<b>⚠️❗️ تــنـسـق الــبـحــث عــن مـسـلـسـل ❗️⚠️</b>\n\n<b><u>للبحث العادي</u></b>\n🗣 اسم المسلسل والموسم (الموسم الذي تريده) 🧠\n\n<b><u>للبحث المتقدم</u></b>\\nاسم المسلسل ، الموسم ، الجودة (720p) ، الترميز (<a href= https://telegra.ph/معدل-الترميز-04-23><b>x265</b></a>)\n\n🖇<b>مــثــال>/b>: \n\n• Game Of Thrones S03 720𝗉✅\n• Dark S02E03 ✅ \n• Breaking Bad S01E05 1080p✅ \n• Prison Break S01 1080p x265✅ \n• Witcher S02E01 x264✅\n\n🥱 للموسم الأول S01 ، للموسم التاني S02،،[𝖲03,𝖲04 ,𝖲06,𝖲10,𝖲17]\n\n🔎 للحلقة الاولي  E01 ، للحلقة التانية  E02 [𝖤03,𝖤07,𝖤17,𝖤21] \n\n❌ [لا تكتب Season 1 ,, الحلقة الاولي ,, الموسم الأول] ❌\n\n❌ [لا تستخدم الرموز مثل * / : " - . & ]\n ")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"𝖯𝗂𝗇𝗀!\n{time_taken_s:.3f} ms")
