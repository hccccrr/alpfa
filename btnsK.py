from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

# ================= START =================
start_kb = ReplyKeyboardMarkup(
    [[KeyboardButton("QUESTIONS CHAHIYE")]],
    resize_keyboard=True
)

# ================= CLASS =================
class_kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("10TH KA QUESTIONS CHAHIYE"),
            KeyboardButton("12TH QUESTION CHAHIYE"),
        ],
        [KeyboardButton("Main Menu")],
    ],
    resize_keyboard=True
)

# ================= PROOF =================
proof_10_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("10TH KA PROOF DIJIYE")],
        [KeyboardButton("Back")],
        [KeyboardButton("Main Menu")],
    ],
    resize_keyboard=True
)

proof_12_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("12TH KA PROOF DIJIYE")],
        [KeyboardButton("Back")],
        [KeyboardButton("Main Menu")],
    ],
    resize_keyboard=True
)

# ================= PAYMENT CHOICE =================
payment_choice_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("PAYMENT ABHI KRNA H")],
        [KeyboardButton("PAYMENT BAAD ME KRENGE SIR")],
        [KeyboardButton("Back")],
        [KeyboardButton("Main Menu")],
    ],
    resize_keyboard=True
)

# ================= QR ONLY =================
qr_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton("QR CODE DIJIYE SIR")],
        [KeyboardButton("Back")],
        [KeyboardButton("Main Menu")],
    ],
    resize_keyboard=True
)
