import logging
from pyrogram import Client, filters

logger = logging.getLogger(__name__)

# Pyrogram setup
api_id = "29930260"
api_hash = "39ce391df95a43d32fd09dac7a4eabbf"
phone_number = "+14025109303"

# Destination chats for ULP and logs
ulp_destination_chat = -1001227119708  # Destination chat ID for ULP files
logs_destination_chat = -10012345678  # Destination chat ID for log files (example)

# Chat IDs for file types
ulp_file_chats = [-100032763]  # List of ULP chat IDs
logs_file_chats = [-1007326373]  # List of log chat IDs

user_client = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

@user_client.on_message(filters.chat(ulp_file_chats) & filters.document)
async def forward_ulp_file(_, message):
    try:
        logger.debug(f"Trying to forward ULP file to {ulp_destination_chat}")
        await user_client.copy_message(chat_id=ulp_destination_chat, from_chat_id=message.chat.id, message_id=message.id)
        logger.debug(f"ULP file forwarded to {ulp_destination_chat} successfully.")
    except Exception as e:
        logger.error(f"Failed to forward ULP file to {ulp_destination_chat}: {e}")

@user_client.on_message(filters.chat(logs_file_chats) & filters.document)
async def forward_log_file(_, message):
    try:
        logger.debug(f"Trying to forward log file to {logs_destination_chat}")
        await user_client.copy_message(chat_id=logs_destination_chat, from_chat_id=message.chat.id, message_id=message.id)
        logger.debug(f"Log file forwarded to {logs_destination_chat} successfully.")
    except Exception as e:
        logger.error(f"Failed to forward log file to {logs_destination_chat}: {e}")

user_client.run()
