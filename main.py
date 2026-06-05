import asyncio
import json
import websockets
from dataclasses import dataclass
from decimal import Decimal


URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"

@dataclass
class Trade():
  symbol: str
  price: Decimal
  quantity: int
  timestamp: int
  is_buyer_maker: bool

def normalize(raw: dict) -> Trade:
  return Trade(
    symbol = raw["s"],
    price = Decimal(raw['p']),
    quantity = Decimal(raw['q']),
    timestamp = raw['T'],
    is_buyer_maker=raw['m']

  )


async def connect():
  while True:
    try:
      print("Connecting to websocket...")

      async with websockets.connect(URL) as ws:
        print("Connected")

        while True:
          message = await ws.recv()
          raw = json.loads(message)
          trade = normalize(raw)


          print(trade)
    
    except websockets.ConnectionClosed as e:
      print(f"Connection closed: {e}. Reconnecting...")

    except Exception as e:
      print(f"Unexpected error: {e}. Reconnecting")

    finally:
      print("Cleanup done (If needed)")
   


asyncio.run(connect())