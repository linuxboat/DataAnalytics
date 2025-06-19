from telethon.sync import TelegramClient
import pandas as pd
import json
from datetime import datetime

# Telegram API credentials
api_id = '23836401'
api_hash = 'f0f2b8517cabcd298102635aa46f27cc'
phone = '+918985115690'

# List of groups/channels to monitor (usernames or IDs)
groups = [
    'APEMPLOYEES',
    'tptdaniel',
    -1001153610080  # Example channel ID
]

client = TelegramClient('session_name', api_id, api_hash).start(phone=phone)

async def fetch_group_messages(group_identifier):
    """Fetch messages from a single group/channel"""
    try:
        channel = await client.get_entity(group_identifier)
        messages = []
        async for msg in client.iter_messages(channel, limit=500):  # Messages per group
            messages.append({
                'group': channel.title,
                'message_id': msg.id,
                'date': msg.date.replace(tzinfo=None),  # Remove timezone
                'sender_id': msg.sender_id,
                'text': msg.text,
            })
        return messages
    except Exception as e:
        print(f"Error fetching {group_identifier}: {str(e)}")
        return []

async def main():
    """Fetch data from all groups"""
    all_messages = []
    for group in groups:
        print(f"Fetching data from: {group}")
        messages = await fetch_group_messages(group)
        all_messages.extend(messages)
    return all_messages

with client:
    messages = client.loop.run_until_complete(main())
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(messages)
    
    # Save to CSV/Excel
    df.to_csv('telegram_groups_data.csv', index=False)
    df.to_excel('telegram_groups_data.xlsx', index=False)

print("Data collection complete!")