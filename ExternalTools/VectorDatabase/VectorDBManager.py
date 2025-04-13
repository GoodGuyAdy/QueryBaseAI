"""All vector operations of platform should call this class"""

import functools
from ExternalTools.VectorDatabase.Provider.Milvus.Main import milvus_provider_obj

provider_map = {"Milvus": milvus_provider_obj}
current_provider = "Milvus"


class VectorDBManager:
    """Vector Database Manager"""

    def __init__(self):
        """Initialize the provider."""
        self.provider = provider_map[current_provider]

    def check_health(func):
        """Decorator to check provider health before executing a method."""

        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            self.provider.check_health()
            return func(self, *args, **kwargs)

        return wrap

    @check_health
    def create_collection(self, org):
        """Create collection for vector db"""
        self.provider.create_collection(org)

    @check_health
    def delete_collection(self, org):
        """Deletes collection for vector db"""
        self.provider.delete_collection(org)

    @check_health
    def vector_search(self, query, org, file_id=None):
        """Search for similar vectors"""
        return self.provider.vector_search(query, org, file_id)

    @check_health
    def insert_vector_data(self, file_id, data, org):
        """Add or update vector"""
        return self.provider.insert_vector_data(file_id, data, org)

    @check_health
    def delete_vector(self, file_id, org):
        """Delete vector"""
        return self.provider.delete_vector(file_id, org)

    @check_health
    def check_file_existence(self, file_id, org):
        """Check existance of a vector"""
        return self.provider.check_file_existence(file_id, org)

    @check_health
    def check_collection_existence(self, org):
        """Check existance of a collection"""
        return self.provider.check_collection_existence(org)


vector_db = VectorDBManager()
