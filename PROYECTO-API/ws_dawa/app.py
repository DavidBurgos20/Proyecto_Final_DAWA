import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
import json
from datetime import date

from src.api.Routes.routes import load_routes
from src.utils.general.logs import HandleLogs

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
CORS(app)
api = Api(app)
load_routes(api)

#definiciones del swagger
SWAGGER_URL = '/ws/dawa/'
API_URL = '/static/swagger.json'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL, API_URL,
                                              config={
                                                  'app_name': 'dawa-ws-restfulapi'
                                              })

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    try:
        HandleLogs.write_log("Servicio Iniciado")
        port = int(os.environ.get('PORT', 1013))
        app.run(debug=True, host='0.0.0.0', port=port, threaded=True)
    except Exception as err:
        HandleLogs.write_error(err)
    finally:
        HandleLogs.write_log("Servicio Finalizado")

