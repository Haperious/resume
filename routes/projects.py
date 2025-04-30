from repositories.repository_manager import get_projects


def get_projects_list():
    projects_repo = get_projects()
    projects = projects_repo.get_projects()  # should return a list

    if projects is not None:
        return projects
    else:
        return None