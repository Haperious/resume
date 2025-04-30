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
from .certificates import get_certificates_list
from .projects import get_projects_list
from .techstack import get_techstack_list

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
    certificates=get_certificates_list()
    return render_template("certifications.html",certificates=certificates)

@resume_bp.route("/projects")
def get_projects():
    projects=get_projects_list()
    return render_template("projects.html",projects=projects)

@resume_bp.route("/techstack")
def get_techstack():
    techstack=get_techstack_list()
    return render_template("techstack.html",techstack=techstack)