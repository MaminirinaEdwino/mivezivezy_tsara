from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json
import uuid
from main_recup import main_recup
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
connected_clients = {}  # Dictionnaire pour stocker {uid: websocket}
depart = {}
destination = {}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

"""@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    client_id = str(uuid.uuid4())  # Générer un UID unique pour le client
    connected_clients[client_id] = websocket
    print(
        f"Client connecté avec UID: {client_id}, total connectés: {len(connected_clients)}")
    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            #main_recup(data[0], data[1])
            print(f"Message reçu de l'UID {client_id}: {data}")
            message_data = {"sender_uid": client_id, "payload": data}
            # Diffuser le message à tous les autres clients (facultatif: inclure l'émetteur)
            for uid, client in connected_clients.items():
                try:
                    await client.send_text(json.dumps(message_data))
                except WebSocketDisconnect:
                    print(
                        f"Client déconnecté pendant la diffusion, suppression de l'UID: {uid}")
                    del connected_clients[uid]
                except Exception as e:
                    print(f"Erreur lors de l'envoi à l'UID {uid}: {e}")
                    del connected_clients[uid]
    except WebSocketDisconnect:
        print(f"Client avec UID {client_id} déconnecté.")
    finally:
        # Supprimer le client lors de la déconnexion
        del connected_clients[client_id]
        print(
            f"Client avec UID {client_id} retiré, total restants: {len(connected_clients)}")
"""
class coordonnees (BaseModel):
    latitude_depart:float
    longitude_depart:float
    latitude_destination:float
    longitude_destination:float
    
@app.post('/destination/')
async def destination(coords:coordonnees):
	return main_recup([coords.latitude_depart, coords.longitude_depart], [coords.latitude_destination, coords.longitude_destination])