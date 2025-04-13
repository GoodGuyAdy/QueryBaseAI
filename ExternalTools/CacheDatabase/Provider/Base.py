"""Base class file for Storage Provider"""

from abc import ABC, abstractmethod


class BaseStorageProvider(ABC):
    """Abstract base class for Elasticsearch vector database provider"""

    @abstractmethod
    def create_index(self, org):
        """Create index for vectors"""
        pass

    @abstractmethod
    def delete_index(self, org):
        """Delete an index"""
        pass

    @abstractmethod
    def insert_data(self, file_id, data, org):
        """Add or update a vector"""
        pass

    @abstractmethod
    def delete_data(self, file_id, org):
        """Delete a vector"""
        pass

    @abstractmethod
    def keyword_search(self, query, org, file_id=None):
        """Perform keyword-based search"""
        pass

    @abstractmethod
    def check_file_existence(self, file_id, org):
        """Check if a file exists in the index"""
        pass

    @abstractmethod
    def check_index_existence(self, org):
        """Check if an index exists"""
        pass
