from fastapi import FastAPI
app=FastAPI()

@app.get ("/")

def mensaje():
    return {"mundo"}