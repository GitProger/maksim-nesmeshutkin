from telethon import TelegramClient, events, sync
import time, random, asyncio
import config

client = TelegramClient('session_storage', config.API_ID, config.API_HASH)
client.start()

downvoted = set()

def downvote():
    global client, downvoted
    m3839 = client.get_entity(config.M3839_CHAT_ID)
    msgs = client.get_messages(m3839, limit=config.LIMIT)
    downvote_candidates = []
    for m in msgs:
        if m.sender.username == config.NESMESHUTKIN and m.id not in downvoted:
            downvote_candidates.append(m)
    
    to_downvote = random.choice(downvote_candidates).id
    if client.send_message(entity=m3839, message="-", reply_to=to_downvote):
        downvoted.add(to_downvote)

while True:
    try:
        downvote()
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
    time.sleep(random.randint(15 * 60, 60 * 60))
