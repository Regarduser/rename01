import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','5986754548:AAGXsx-_uqaX00pCrItRu__0ov2jccsfxJg')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"""<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: #bj
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙺𝙾𝚈𝙴𝙱
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: [ 𝙼𝙰𝙹𝙾𝚁 ]
✯ 𝚃𝚘𝚝𝚊𝚕 𝚄𝚜𝚎𝚛: {total_user()}
✯ 𝚃𝚘𝚝𝚊𝚕 𝚁𝚎𝚗𝚊𝚖𝚎𝚍 𝙵𝚒𝚕𝚎: {total_rename}
✯ 𝚃𝚘𝚝𝚊𝚕 𝚂𝚒𝚣𝚎 𝚁𝚎𝚗𝚊𝚖𝚎𝚍: {humanbytes(int(total_size))}</b>
""",quote=True)


