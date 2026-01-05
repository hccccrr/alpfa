from pyrogram import Client, filters
from pyrogram.types import Message
from btnsK import *

BOT_TOKEN = "8433474851:AAGFt_WZ2agAWcM-UVmLxzhSrH-aySkIcaw"
API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"

QR_IMAGE_URL = "https://files.catbox.moe/9bk3ll.jpg"
PROOF_CHANNEL = "https://t.me/+eD91tgZztvUxNDQ1"

app = Client(
    "SonusirBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# ===== START =====
@app.on_message(filters.command("start"))
async def start(_, m: Message):
    await m.reply("Main Menu", reply_markup=start_kb)

# ===== QUESTIONS =====
@app.on_message(filters.regex("^QUESTIONS CHAHIYE$"))
async def questions(_, m: Message):
    await m.reply("Konse class ka questions chahiye", reply_markup=class_kb)

# ===== 10TH =====
@app.on_message(filters.regex("^10TH KA QUESTIONS CHAHIYE$"))
async def ten(_, m: Message):
    await m.reply(
        "Mil jayega\nPayment ₹999\nExam se 4 hours pehle milega questions aur answers",
        reply_markup=proof_10_kb
    )

# ===== 12TH =====
@app.on_message(filters.regex("^12TH QUESTION CHAHIYE$"))
async def twelve(_, m: Message):
    await m.reply(
        "Mil jayega\nPayment ₹999\nExam se 4 hours pehle milega questions",
        reply_markup=proof_12_kb
    )

# ===== PROOF =====
@app.on_message(filters.regex("KA PROOF DIJIYE"))
async def proof(_, m: Message):
    await m.reply(
        f"Is channel me proof hai 👇\n{PROOF_CHANNEL}",
        reply_markup=payment_choice_kb
    )

# ===== PAYMENT NOW =====
@app.on_message(filters.regex("^PAYMENT ABHI KRNA H$"))
async def pay_now(_, m: Message):
    await m.reply(
        "QR code se payment kar sakte ho 👇",
        reply_markup=qr_kb
    )

# ===== QR IMAGE =====
@app.on_message(filters.regex("^QR CODE DIJIYE SIR$"))
async def qr(_, m: Message):
    await m.reply_photo(
        photo=QR_IMAGE_URL,
        caption="📸 Scan QR & complete payment\n\nPayment ke baad @sonusir2026 ko message kare",
        reply_markup=qr_kb
    )

# ===== PAYMENT LATER =====
@app.on_message(filters.regex("^PAYMENT BAAD ME KRENGE SIR$"))
async def pay_later(_, m: Message):
    await m.reply("Okay 👍")

# ===== BACK =====
@app.on_message(filters.regex("^Back$"))
async def back(_, m: Message):
    await m.reply("Konse class ka questions chahiye", reply_markup=class_kb)

# ===== MAIN MENU =====
@app.on_message(filters.regex("^Main Menu$"))
async def menu(_, m: Message):
    await m.reply("Main Menu", reply_markup=start_kb)

app.run()
