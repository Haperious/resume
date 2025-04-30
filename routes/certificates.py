from repositories.repository_manager import get_certificates


def get_certificates_list():
    certificates_repo = get_certificates()
    certificates = certificates_repo.get_certificates()  # should return a list

    if certificates is not None:
        return certificates
    else:
        return None