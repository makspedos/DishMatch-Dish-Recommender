from flask import Flask
from culinary.culinary import culinary_bp
from database import connect_db

def create_app():
    app = Flask(__name__)

    app.register_blueprint(culinary_bp, url_prefix='')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
