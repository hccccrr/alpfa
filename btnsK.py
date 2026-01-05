from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

# ===== MAIN REPLY KEYBOARD =====
main_reply_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("QUESTIONS CHAHIYE")],
        [
            KeyboardButton("PAYMENT ABHI KRNA H"),
            KeyboardButton("PAYMENT BAAD ME KRENGE"),
        ],
        [KeyboardButton("OR CODE DIJIYE SIR")],
        [KeyboardButton("Main Menu")],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

# ===== CLASS SELECTION KEYBOARD =====
class_reply_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("10TH KA QUESTIONS CHAHIYE")],
        [KeyboardButton("12TH QUESTION CHAHIYE")],
        [KeyboardButton("Main Menu")],
    ],
    resize_keyboard=True
)
