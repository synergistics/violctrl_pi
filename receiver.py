import json
import asyncio
import websockets
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.bcm)
gpio.setup(25, gpio.OUT)
p = gpio.PWM(25, 50)
p.start(50)
sleep(0.1)
p.stop()
gpio.cleanup()

APP_URI = 'wss://violctrl.herokuapp.com'
DEV_URI = 'ws://10.0.0.201:3000'

async def connect():
    async with websockets.connect(DEV_URI) as socket:
        # of course don't actually hardcode this
        connect_msg = {'type': 'receiver_connect', 'ruid': 'peyote', 'key': 'wile.e.'}
        await socket.send(json.dumps(connect_msg))
        while True:
            msg = await socket.recv()
            instruction = json.loads(msg)
            handle_instruction(instruction) 

        # task = asyncio.ensure_future(handler(socket))
        # done, pending = await asyncio.wait([task], return_when=asyncio.FIRST_COMPLETED)

def handle_instruction(instruction):
    typ = instruction['type']
    if typ == 'speedsLR':
        left_speed = instruction['leftSpeed']
        right_speed = instruction['rightSpeed']

loop = asyncio.get_event_loop()
loop.run_until_complete(connect())
# event_loop.run_forever()
