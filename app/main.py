from fastapi import FastAPI
from app.routes import song_routes
from app.core.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Initialise a FastAPI application
app = FastAPI(
    title='CEAC Technical Computer Graphics Songs Directory Application')


load_dotenv()

# Register routes
app.include_router(song_routes.router)


# Configure allowed origins for CORS
origins = [
    os.environ.get("FRONTEND_ALLOWED_ORIGINS")
]


app.add_middleware(
    CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    print("Starting application")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
