import ssl
import json

import websocket

def buy():
    pass

def sell():
    pass

def on_open(ws):
    print('Opened conection')

    json_subscribe = """
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}
"""
    ws.send(json_subscribe)

def on_close(ws, close_status_code, close_msg):
    print('Closed conection')

def on_error(ws, error):
    print('Error')
    print(error)

def on_message(ws, message):
    message = json.loads(message)

    if message.get('event') != 'trade':
        return
    
    price = message['data']['price']
    print(price)
    if price > 9000:
        sell()
    elif price < 8000:
        buy()
    else:
        print('Waiting...')

if __name__ == '__main__':
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                on_open=on_open,
                                on_close=on_close,
                                on_message=on_message,
                                on_error=on_error)
    
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    