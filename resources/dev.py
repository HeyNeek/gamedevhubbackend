import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import devs

blp = Blueprint("devs", __name__, description="Operations on devs")

@blp.route("/devs")
class Dev(MethodView):
    def get(self):
        return {"devs": list(devs.values())}

    def post(self):
        dev_data = request.get_json()
        if "name" not in dev_data:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON payload"
            )
        
        for dev in devs.values():
            if dev_data["name"] == dev["name"]:
                abort(400, message=f"Dev already exists")
        
        dev_id = uuid.uuid4().hex
        new_dev = {**dev_data, "id": dev_id}
        devs[dev_id] = new_dev
        
        return new_dev, 201