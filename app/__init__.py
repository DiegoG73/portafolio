from . import portfolio
from flask import Flask 
import os

app = Flask(__name__)
def create_app():
    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
    )

app.register_blueprint(portfolio.bp)

if __name__ == '__main__':
    app.run()