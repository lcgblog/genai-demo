from fastapi import WebSocket
from typing import List, Dict
from schema.position_schema import Position
import json


class TableService:
    def __init__(self):
        self.table_data: Dict[str, Position] = {}
        self.clients: List[WebSocket] = []
        self.mock_data()  # Populate with mock data

    async def notify_clients(self):
        # Convert Position objects to JSON-serializable dictionaries before sending
        table_data_dicts = await self.get_table_data()
        for client in self.clients:
            await client.send_json(table_data_dicts)

    async def add_position(self, position: Position):
        self.table_data[position.key] = position
        await self.notify_clients()

    async def clear_table(self):
        self.table_data.clear()
        await self.notify_clients()

    async def get_table_data(self):
        return [json.loads(position.model_dump_json()) for position in self.table_data.values()]
    
    def mock_data(self):
        # Mock some data similar to the Java service
        positions = [
            Position(key="1", cusip="123456", account="Account1", netposition=100.0, price=10.0),
            Position(key="2", cusip="654321", account="Account2", netposition=200.0, price=20.0),
            Position(key="3", cusip="111111", account="Account3", netposition=300.0, price=30.0),
        ]
        for position in positions:
            self.table_data[position.key] = position