import asyncio
import json
import websockets

URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"


async def main():
    async with websockets.connect(URL) as ws:
        while True:
            message = await ws.recv()
            data = json.loads(message)

            # print(
            #     f"Symbol: {data['s']} | "
            #     f"Price: {data['p']} | "
            #     f"Qty: {data['q']}"
            # )
            print(data)


asyncio.run(main())