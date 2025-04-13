from ExternalTools.CacheDatabase.CacheDBManager import cache_db
from ExternalTools.VectorDatabase.VectorDBManager import vector_db


def check_doucment(file_id, org):
    """
    Checks if a file is present in the database
    """
    vector_db_exists = vector_db.check_file_existence(file_id, org)
    cache_db_exists = cache_db.check_file_existence(file_id, org)

    if vector_db_exists and cache_db_exists:
        return True
    else:
        return False


def check_org(org):
    """
    Checks if an organisation is present in the database
    """
    vector_db_exists = vector_db.check_collection_existence(org)
    cache_db_exists = cache_db.check_index_existence(org)

    if vector_db_exists and cache_db_exists:
        return True
    else:
        return False
