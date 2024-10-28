from flask import Flask
from flask_smorest import Api
from resources.dev import blp as DevBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Devs REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(DevBlueprint)

# @app.get("/devs")
# def get_devs():
#     return devs

# @app.post("/create_dev")
# def create_dev():
#     dev_data = request.get_json()
#     dev_id = uuid.uuid4().hex
#     new_dev = {**dev_data, "id": dev_id}
#     devs[dev_id] = new_dev
#     return new_dev, 201
