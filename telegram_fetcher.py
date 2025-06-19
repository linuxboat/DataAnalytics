from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
import json

# Telegram API credentials
api_id = '23836401'
api_hash = 'f0f2b8517cabcd298102635aa46f27cc'
phone = '+918985115690'

# Group details
group_username = 'APEMPLOYEES'
channel_id = 1809967083  # Use /get_entity to find this

# Initialize client
client = TelegramClient('session_name', api_id, api_hash).start(phone=phone)

async def fetch_messages():
    channel = await client.get_entity(group_username)
    messages = []
    async for msg in client.iter_messages(channel, limit=1000):  # Adjust limit
        messages.append({
            'id': msg.id,
            'date': msg.date.isoformat(),
            'sender': msg.sender_id,
            'text': msg.text,
        })
    return messages

with client:
    messages = client.loop.run_until_complete(fetch_messages())
    with open('telegram_data.json', 'w') as f:
        json.dump(messages, f)