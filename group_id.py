from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Your Telegram API credentials
api_id = '23836401'  # Replace with your API ID
api_hash = 'f0f2b8517cabcd298102635aa46f27cc'  # Replace with your API hash
phone = '+918985115690'  # e.g., '+1234567890'

# Public group/channel username or invite link
group_username = 'APEMPLOYEES'  # e.g., 'elonmusk'

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def get_channel_id():
    # Fetch the entity (channel/group) using its username
    entity = await client.get_entity(group_username)
    print(f"Channel/Group ID: {entity.id}")
    print(f"Entity Details: {entity}")

with client:
    client.loop.run_until_complete(get_channel_id())