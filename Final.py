from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws")
async def simple_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Message reçu du client: {data}")
            await websocket.send_text(f"Serveur a reçu: {data}")
    except WebSocketDisconnect:
        print("Client déconnecté")