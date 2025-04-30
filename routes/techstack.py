from repositories.repository_manager import get_techstack


def get_techstack_list():
    techstack_repo = get_techstack()
    techstack = techstack_repo.get_techstack()  # should return a list

    if techstack is not None:
        return techstack
    else:
        return None