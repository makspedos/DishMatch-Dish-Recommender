from flask import Flask
from culinary.culinary import culinary_bp
from database import connect_db
from culinary.variables import ENV_VARS

def create_app():
    app = Flask(__name__)
    app.secret_key = ENV_VARS['SECRET_KEY']
    app.register_blueprint(culinary_bp, url_prefix='')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
