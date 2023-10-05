from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



 # at last, the bottom of the file/module
if __name__ == "__main__":
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)
    uvicorn.run(app, host='0.0.0.0',port=port)
    