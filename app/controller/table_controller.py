from typing import List
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from service.table_service import TableService
from schema.position_schema import Position

table_controller = APIRouter()
table_service = TableService()

# # 存储活动WebSocket连接
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    def connect(self, websocket: WebSocket):
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            print('broadcasting:', message)
            await connection.send_json(message)
            
manager = ConnectionManager()

@table_controller.websocket("/ws/{subscription}")
async def websocket_endpoint(websocket: WebSocket, subscription: str):
    await websocket.accept()
    manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            positions = await table_service.get_table_data()
            await manager.send_personal_message(positions, websocket)      
                
    except WebSocketDisconnect:
        print("WebSocket disconnected")
        manager.disconnect(websocket)

@table_controller.post("/addPosition")
async def add_position(position: Position = Position(key="")):
    print('received position:', position)
    await table_service.add_position(position)
    positions = await table_service.get_table_data()
    print("added position current:", positions)
    await manager.broadcast(positions)
    return {"message": "Position added"}

# @table_controller.post("/clearTable")
# async def clear_table():
#     await table_service.clear_table()
#     await manager.send_to_subscription("Table cleared", "/topic/fullPosition")
#     return {"message": "Table cleared"}