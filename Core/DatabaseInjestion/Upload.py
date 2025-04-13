from ExternalTools.CacheDatabase.CacheDBManager import cache_db
from ExternalTools.VectorDatabase.VectorDBManager import vector_db
from Core.Utilities.Document import extract_text_from_file


def create_organisation(org_name):
    """
    Creates an organisation in the database
    """
    vector_db.create_collection(org_name)
    cache_db.create_index(org_name)


def upload_doucment(file_id, file, org):
    """
    Upload a file in the database
    """
    data = extract_text_from_file(file)

    vector_db.insert_vector_data(file_id, data, org)
    cache_db.insert_data(file_id, data, org)
