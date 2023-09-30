from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
from config import App_Config


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(App_Config)
if app.config["SQLALCHEMY_DATABASE_URI"]:
    print(f"using db: {app.config['SQLALCHEMY_DATABASE_URI']}")

# Initialize CORS
CORS(app, supports_credentials=True)

# Initialize SQLAlchemy
db.init_app(app)


# create db tables from models if not exists
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
