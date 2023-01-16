from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from netconf.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from netconf.firewall.routes import firewall
    from netconf.switch.routes import switch
    from netconf.wifi.routes import wifi
    from netconf.main.routes import main
    app.register_blueprint(firewall)
    app.register_blueprint(switch)
    app.register_blueprint(wifi)
    app.register_blueprint(main)

    return app