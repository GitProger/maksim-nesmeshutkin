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


print(client.get_entity(config.M3839_CHAT_ID))

# {"_": "MessageFwdHeader", "date": "2023-10-10T21:01:53+00:00", "imported": false, "from_id": {"_": "PeerUser", "user_id": 914625128} , "from_name": null, "channel_post": null, "post_author": null, "saved_from_peer": {"_": "PeerChannel", "channel_id": 1611367150}, "saved_from_msg_id": 80653, "psa_type": null}
# {"_": "MessageFwdHeader", "date": "2023-10-10T19:04:44+00:00", "imported": false, "from_id": {"_": "PeerUser", "user_id": 1015167729}, "from_name": null, "channel_post": null, "post_author": null, "saved_from_peer": {"_": "PeerChat", "chat_id": 4096545363}, "saved_from_msg_id": 41898, "psa_type": null}

# while True:
#    try:
#        downvote()
#    except Exception as e:
#        print(f'{type(e).__name__}: {e}')
#    time.sleep(random.randint(15 * 60, 60 * 60))
