from flask import Flask,render_template
from config import Config
from models import db, login_manager, bcrypt
from models.user import User
from routes.auth_routes import auth
from routes.transaction_routes import transactions
from routes.dashboard_routes import dashboard
from routes.budget_routes import budget
from routes.insight_routes import insight
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route("/")
    def home():
        return render_template("home.html")

    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth)
    app.register_blueprint(transactions)
    app.register_blueprint(dashboard)
    app.register_blueprint(budget)
    app.register_blueprint(insight)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)