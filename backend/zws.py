import websocket

def on_open(ws):
    print("Connection opened")
    ws.send("MEssage")

def on_message(ws, message):
    print(f"New notification: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Closed connection")

headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyNDgzMDA0LCJpYXQiOjE3MzI0ODI3MDQsImp0aSI6ImVjYTE2YTZiZTRhZDQxMGRhOGUyMzMyNTQ4MzVjN2RiIiwidXNlcl9pZCI6Mn0.bCFAb1f_JQKwgrrce6Orql3-08jqM3NuwNYlaW05wr0",
} #güncel jwt access token

ws = websocket.WebSocketApp(
    "ws://127.0.0.1:8000/ws/notifications/2/", #user id olacak 2 -  (2. post sahibi - 1. yorum yapan id)
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
    header=headers
)
ws.on_open = on_open
ws.run_forever()
