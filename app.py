from flask import Flask, request

app = Flask(__name__)

devs = [
    {
        "name": "Catcom",
        "location": "Remote, USA"
    }
]

@app.get("/devs")
def get_stores():
    return devs

@app.post("/create_dev")
def create_dev():
    request_data = request.get_json()
    new_dev = {"name": request_data["name"], "location": request_data["location"]}
    devs.append(new_dev)
    return new_dev, 201

#going to add new get method for specific store

