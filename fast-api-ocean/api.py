from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn 

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


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
