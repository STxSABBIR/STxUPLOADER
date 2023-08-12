

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Button(object):

      BUTTONS01 = InlineKeyboardMarkup( [ [ InlineKeyboardButton(text="ʏᴛs 📁", callback_data='00'),
                                            InlineKeyboardButton(text="sᴇᴀʀᴄʜ 🔍", switch_inline_query_current_chat="1 ") ],
                                          [ InlineKeyboardButton(text="ᴀɴɪᴍᴇ 📁", callback_data='00'),
                                            InlineKeyboardButton(text="sᴇᴀʀᴄʜ 🔍", switch_inline_query_current_chat="2 ") ],
                                          [ InlineKeyboardButton(text="1337x 📁", callback_data='00'),
                                            InlineKeyboardButton(text="sᴇᴀʀᴄʜ 🔍", switch_inline_query_current_chat="3 " ) ],
                                          [ InlineKeyboardButton(text="ᴛʜᴇᴘɪʀᴀᴛᴇʙᴀʏ 📁", callback_data='00'),
                                            InlineKeyboardButton(text="sᴇᴀʀᴄʜ 🔍", switch_inline_query_current_chat="4 ") ],
                                          [ InlineKeyboardButton(text="❌", callback_data="X0") ] ] )
