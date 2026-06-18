Writing this out randomly gonna reformat it later

Steps to making the file

> Installation
> python -m env env

Once its created then you do below to activate it
venv\Scripts\Activate.ps1S

I tried polygon.io but it requires me to register and request an API key, for simplicity sake I've gone with binance since it has a websocket stream as well and was pretty easy to setup.

T vs E

E is when Binance's server generated and sent the event to you
T is when the trade actually matched on the exchange

There's network and processing lag between a trade happening and Binance packaging it into an event. For backtesting you want to replay trades in the order they happened, not the order you received them. Hence T.

3. TimescaleDB setup
   - Spin up container
   - Create trades hypertable
   - Write async DB writer into consumer

4. Batching
   - Don't write one trade at a time
   - Batch inserts every N trades or every X seconds

5. Multiple symbols
   - Extend producer to handle more than BTCUSDT
   - Same normalization, same queue

6. Order book stream
   - Separate stream type (@depth)
   - Normalized order book schema
   - Same queue architecture

7. Backtesting engine
   - Query trades from TimescaleDB by time range
   - Replay engine that feeds normalized trades in order
   - Strategy interface

8. Order book matching engine
   - In-memory order book
   - Feed live normalized trades into it
   - Match logic

Working on setting up docker now for timescaleDB



