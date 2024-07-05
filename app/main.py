from fastapi import FastAPI
from app.routes import song_routes
from app.core.database import create_db_and_tables

# Initialise a FastAPI application
app = FastAPI(
    title='CEAC Technical Computer Graphics Songs Directory Application')

# Register routes
app.include_router(song_routes.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    print("Starting application")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
