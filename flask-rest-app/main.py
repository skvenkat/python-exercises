# main.py
from flask import Flask
from blueprints.basic_endpoints import blueprint as basic_endpoints
from blueprints.v2 import blueprint_v2 as v2
from blueprints.jinja_endpoint import blueprint as jinja_template_blueprint

app = Flask(__name__)
app.register_blueprint(basic_endpoints)
app.register_blueprint(v2)
app.register_blueprint(jinja_template_blueprint)

if __name__ == "__main__":
    app.run()