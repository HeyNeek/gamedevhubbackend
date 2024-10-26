from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "WinCo",
        "location": "Beaverton, OR"
    }
]

@app.get("/stores")
def get_stores():
    return stores

@app.post("/create_store")
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": "Whole Foods",
        "location": "Portland, OR"
    }
    stores.append(new_store)
    return new_store, 201

#going to add new get method for specific store

