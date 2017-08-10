import json
import asyncio
import websockets

APP_URI = 'wss://violctrl.herokuapp.com'
DEV_URI = 'ws://10.0.0.201:3000'

# async def handler(socket):

async def connect():
    async with websockets.connect(DEV_URI) as socket:
        # of course don't actually hardcode this
        connectMsg = {'type': 'receiver_connect', 'ruid': 'peyote', 'key': 'wile.e.'}
        await socket.send(json.dumps(connectMsg))
        while True:
            message = await socket.recv()
            print(message) 

        # task = asyncio.ensure_future(handler(socket))
        # done, pending = await asyncio.wait([task], return_when=asyncio.FIRST_COMPLETED)

loop = asyncio.get_event_loop()
loop.run_until_complete(connect())
# event_loop.run_forever()
