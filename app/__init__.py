from flask import Flask, render_template
import os

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
    )

    @app.errorhandler(500)
    def not_found(error):
        return render_template('500.html', error=error)

    from . import portfolio
    from waitress import serve
    app.register_blueprint(portfolio.bp)

    return app