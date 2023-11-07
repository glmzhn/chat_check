from pyrogram import Client
import asyncio
import os
import random
from pyrogram import errors

filepath = os.path.abspath(__file__)
channels = filepath.replace('\\main.py', '\\channels')
proxy_dir = filepath.replace("\\main.py", "\\proxy")

with open(f'{proxy_dir}/' + 'proxy.txt', 'r') as fl:
    proxy_list = fl.read().split('\n')

with open(f'{channels}/' + 'channels.txt', 'r') as fl:
    channels_list = fl.readlines()

api_id =

api_hash =

cur_proxy = random.choice(proxy_list)

proxy = {
    "scheme": "socks5",
    "hostname": cur_proxy.split(':')[0],
    "port": int(cur_proxy.split(':')[1]),
    "username": cur_proxy.split(':')[2],
    "password": cur_proxy.split(':')[3],
}

app = Client(name='me_client', api_id=api_id, api_hash=api_hash, proxy=proxy)


async def check_chat():
    for channel_url in channels_list:
        try:

            chat_obj = await app.get_chat(channel_url)
            if chat_obj.linked_chat:
                print(f'Channel: {channel_url}\nhas a chat: {chat_obj.linked_chat.title}')
                async for message in app.get_chat_history(channel_url, limit=1):
                    last_post_time = message.date
                    print(f'Last post was uploaded {last_post_time} in the channel {channel_url}')
                await asyncio.sleep(30)
            else:
                print(f'Channel {channel_url}has no chat')
                async for message in app.get_chat_history(channel_url, limit=1):
                    last_post_time = message.date
                    print(f'Last post was uploaded {last_post_time} in the channel {channel_url}')
                await asyncio.sleep(30)
        except errors.UsernameNotOccupied:
            print(f"Wrong channel's id!")
            await asyncio.sleep(30)
        except Exception as e:
            print(f'There is an error: {e}')
            await asyncio.sleep(30)

if __name__ == "__main__":
    app.start()
    asyncio.get_event_loop().run_until_complete(check_chat())
