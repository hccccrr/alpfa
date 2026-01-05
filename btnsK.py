from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

# ================= MAIN MENU KEYBOARD =================
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
    one_time_keyboard=False,
    selective=False
)

# ================= CLASS SELECTION KEYBOARD =================
# 10th + 12th SAME ROW (EXACT SCREENSHOT LOOK)
class_reply_kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("10TH KA QUESTIONS CHAHIYE"),
            KeyboardButton("12TH QUESTION CHAHIYE"),
        ],
        [KeyboardButton("Main Menu")],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    selective=False
)

# ================= PAYMENT KEYBOARD =================
payment_reply_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("PAYMENT ABHI KRNA H")],
        [KeyboardButton("PAYMENT BAAD ME KRENGE")],
        [KeyboardButton("OR CODE DIJIYE SIR")],
        [KeyboardButton("Main Menu")],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    selective=False
)
