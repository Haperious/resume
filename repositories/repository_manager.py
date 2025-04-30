from flask import g
from repositories.certifications.certificates import CertificatesRepo
from repositories.project.projects import ProjectsRepo
from repositories.techstack.techstack import TechStackRepo


def get_certificates():
    g.certificates_repo = CertificatesRepo()
    return g.certificates_repo

def get_projects():
    g.projects_repo = ProjectsRepo()
    return g.projects_repo

def get_techstack():
    g.techstack_repo = TechStackRepo()
    return g.techstack_repo

