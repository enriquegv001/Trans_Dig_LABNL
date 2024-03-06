from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn 

# Create instance class
app = FastAPI() 

# Define Allowed Origins, from everywhere
origins = ['*']

# Cross-Origin Resource Sharing, handle request from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

# Define Route function for application response after operation GET
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}




# Run app if script run directly not run as module
if __name__ == "__main__":
    """
    Server as uvicorn
    Host in all network interfaces
    Listen to por 8000
    """
    uvicorn.run(app, host='0.0.0.0', port=8000)

    # Create table inside Postgres
    models.Base.metadata.create_all(bind=engine)
    app.include_router(posts.router)
