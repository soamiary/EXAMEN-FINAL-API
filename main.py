from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/health")
def get_health():
    return {"message": f"OK"}
   