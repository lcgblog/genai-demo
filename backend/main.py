import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.table_controller import table_controller as table_controller
app = FastAPI()
#for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with the specific origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(table_controller, prefix="/table", tags=["table"])

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8008, log_level="info", workers=1)
