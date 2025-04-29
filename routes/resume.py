from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    Blueprint,
)

resume_bp = Blueprint(
    "resume", __name__, template_folder="../templates/routes"
)


@resume_bp.route("/")
def get_resume():
    return render_template("resume.html")

@resume_bp.route("/academic")
def get_academic():
    return render_template("academic.html")

@resume_bp.route("/certifications")
def get_certifications():
    return render_template("certifications.html")

@resume_bp.route("/projects")
def get_projects():
    return render_template("projects.html")

@resume_bp.route("/techstack")
def get_techstack():
    return render_template("techstack.html")