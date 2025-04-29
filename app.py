from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    session,
)
from config import Config
from repositories.db import init_db
from routes.resume import resume_bp
from datetime import datetime

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(Config)

# init_db(app, Config)

app.register_blueprint(resume_bp, url_prefix="/resume")


@app.route("/")
def home():
    return redirect(url_for("resume.get_resume"))


@app.context_processor
def inject_current_year():
    return {"current_year": datetime.now().year}

@app.context_processor
def my_age():
    age = datetime.now().year - 1998
    return {"current_age": age}



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
