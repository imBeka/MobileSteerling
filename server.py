import logging
import time
import vgamepad as vg
# from websocket_server import WebsocketServer

import asyncio
import websockets

# HOST = '192.168.100.10'
# PORT = 2000

gamepad = vg.VX360Gamepad()
stick_mid = 32767
# server = WebsocketServer(host=HOST, port=PORT, loglevel=logging.INFO)


# def new_client(client, server):
# 	print("Hey all, a new client has joined us")

async def handler(websocket, path):
	global stick_mid
	message = await websocket.recv()
	print("It is said: " + message)

	if message == 'gas':
		gamepad.right_trigger(value=255)
		gamepad.update()
	elif message == '!gas':
		gamepad.right_trigger(value=0)
		gamepad.update()
	elif message == 'break':
		gamepad.left_trigger(value=255)
		gamepad.update()
	elif message == '!break':
		gamepad.left_trigger(value=0)
		gamepad.update()
	elif message == 'ers':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER )
		gamepad.update()
	elif message == '!ers':
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
		gamepad.update()
	elif message == 'drs':
		gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y )
		gamepad.update()
		time.sleep(0.5)
		gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
		gamepad.update()
	elif message != 'Succesfully connected' and message != 'null' and message != '!gas':
		res = (stick_mid * (abs(float(message)) / 10))
		if float(message) < 0:
			gamepad.left_joystick(x_value=-int(res), y_value=0)
			gamepad.update()
		else:
			gamepad.left_joystick(x_value=int(res), y_value=0)
			gamepad.update()


# server.set_fn_new_client(new_client)
# server.set_fn_message_received(message_received)
# server.run_forever()
start_server = websockets.serve(handler, "localhost", 8000)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()