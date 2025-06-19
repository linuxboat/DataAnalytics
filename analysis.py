import pandas as pd

# Load data
df = pd.read_csv('telegram_groups_data.csv')

# 1. Basic Statistics
print("\n=== Basic Stats ===")
print(f"Total Messages: {len(df)}")
print(f"Groups: {df['group'].unique().tolist()}")
print(f"Unique Senders: {df['sender_id'].nunique()}")

# 2. Messages per Group
print("\n=== Messages per Group ===")
print(df['group'].value_counts())

# 3. Most Active Users
print("\n=== Top 10 Active Users ===")
print(df['sender_id'].value_counts().head(10))

# 4. Text Analysis (e.g., keyword "news")
print("\n=== Messages Containing 'news' ===")
news_messages = df[df['text'].str.contains('news', case=False, na=False)]
print(news_messages[['group', 'date', 'text']])
