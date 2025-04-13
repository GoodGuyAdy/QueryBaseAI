"""All cache operations of platform should call this class"""

import functools
from ExternalTools.CacheDatabase.Provider.Elasticsearch.Main import (
    elasticsearch_provider_obj,
)

provider_map = {"Elastic": elasticsearch_provider_obj}
current_provider = "Elastic"


class CacheDbManager:
    """Manages cache DB operations with provider health checks."""

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
    def create_index(self, org):
        """Create an index for the organization."""
        return self.provider.create_index(org)

    @check_health
    def delete_index(self, org):
        """Delete the organization's index."""
        return self.provider.delete_index(org)

    @check_health
    def insert_data(self, file_id, data, org):
        """Insert data into the cache."""
        return self.provider.insert_data(file_id, data, org)

    @check_health
    def delete_data(self, file_id, org):
        """Delete data from the cache."""
        return self.provider.delete_data(file_id, org)

    @check_health
    def keyword_search(self, query, org, file_id=None):
        """Search cached data using keywords."""
        return self.provider.keyword_search(query, org, file_id)

    @check_health
    def check_file_existence(self, file_id, org):
        """Check if a file exists in the cache."""
        return self.provider.check_file_existence(file_id, org)

    @check_health
    def check_index_existence(self, org):
        """Check if an index exists for the organization."""
        return self.provider.check_index_existence(org)


cache_db = CacheDbManager()
