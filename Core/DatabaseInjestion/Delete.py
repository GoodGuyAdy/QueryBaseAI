from ExternalTools.CacheDatabase.CacheDBManager import cache_db
from ExternalTools.VectorDatabase.VectorDBManager import vector_db


def delete_organisation(org_name):
    """
    Deletes an organisation from the database
    """
    vector_db.delete_collection(org_name)
    cache_db.delete_index(org_name)


def delete_doucment(file_id, org):
    """
    Deletes a file from the database
    """
    vector_db.delete_vector(file_id, org)
    cache_db.delete_data(file_id, org)
