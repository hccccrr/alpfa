from pyrogram import Client, filters
from pyrogram.types import Message
from btnsK import main_reply_kb, class_reply_kb

BOT_TOKEN = "8433474851:AAGFt_WZ2agAWcM-UVmLxzhSrH-aySkIcaw"
API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"

app = Client(
    "SonusirBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)

# ===== START =====
@app.on_message(filters.command("start"))
async def start_cmd(_, msg: Message):
    await msg.reply(
        "Main Menu",
        reply_markup=main_reply_kb
    )

# ===== QUESTIONS =====
@app.on_message(filters.text & filters.regex("^QUESTIONS CHAHIYE$"))
async def questions(_, msg: Message):
    await msg.reply(
        "Konse class ka questions chahiye",
        reply_markup=class_reply_kb
    )

# ===== 10TH =====
@app.on_message(filters.text & filters.regex("^10TH KA QUESTIONS CHAHIYE$"))
async def ten(_, msg: Message):
    await msg.reply(
        "Mil jayega\n"
        "Payment Krna padega ₹999 agar real question chahiye toh\n"
        "Exam se 4 hours pehle milega questions aur answers\n\n"
        "10TH KA PROOF DIJIYE SIR"
    )

# ===== 12TH =====
@app.on_message(filters.text & filters.regex("^12TH QUESTION CHAHIYE$"))
async def twelve(_, msg: Message):
    await msg.reply(
        "Mil jayega\n"
        "Payment Krna padega ₹999 agar real question chahiye toh\n"
        "Exam se 4 hours pehle milega questions\n\n"
        "12TH KA PROOF DIJIYE SIR"
    )

# ===== PAYMENT NOW =====
@app.on_message(filters.text & filters.regex("^PAYMENT ABHI KRNA H$"))
async def pay_now(_, msg: Message):
    await msg.reply(
        "Okay\n\n"
        "Message @sonusir2026 for payment"
    )

# ===== PAYMENT LATER =====
@app.on_message(filters.text & filters.regex("^PAYMENT BAAD ME KRENGE$"))
async def pay_later(_, msg: Message):
    await msg.reply("Okay")

# ===== QR / CODE =====
@app.on_message(filters.text & filters.regex("^OR CODE DIJIYE SIR$"))
async def qr(_, msg: Message):
    await msg.reply(
        "Message @sonusir2026 for payment"
    )

# ===== MAIN MENU =====
@app.on_message(filters.text & filters.regex("^Main Menu$"))
async def menu(_, msg: Message):
    await msg.reply(
        "Main Menu",
        reply_markup=main_reply_kb
    )

app.run()
