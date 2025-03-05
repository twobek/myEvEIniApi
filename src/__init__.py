from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config.dbconfig import config_by_name

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
def create_app(config_name: str):
    app = Flask(__name__, template_folder='../../templates')

    print(f'src.config.dbconfig.{config_name.capitalize()}Config')
    # Load configuration from config.py
    app.config.from_object(config_by_name.get(config_name))

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from src.routes.universe_types import universe_types_bp
    app.register_blueprint(universe_types_bp)
    #app.register_blueprint(universe_types_bp, url_prefix='/types')

    """
    @app.before_request
    def setup():
        from src.models.universe_types import universeTypeIds
        universeTypeIds.metadata.create_all(bind=db_instance.engine)
    """

    return app
