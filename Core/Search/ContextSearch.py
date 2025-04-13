from ExternalTools.VectorDatabase.VectorDBManager import vector_db
from ExternalTools.CacheDatabase.CacheDBManager import cache_db


def semantic_search(query, org, file_id=None):
    """
    Searches query from vector db.
    """
    context = vector_db.vector_search(query, org, file_id)
    return context


def keyword_search(query, org, file_id=None):
    """
    Searches query from cache db.
    """
    context = cache_db.keyword_search(query, org, file_id)
    return context
