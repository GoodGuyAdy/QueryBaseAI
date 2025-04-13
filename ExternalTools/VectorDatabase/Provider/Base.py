"""Base class for Vector Database Providers"""

from abc import ABC, abstractmethod


class BaseVectorProvider(ABC):
    """Abstract base class for vector database providers."""

    @abstractmethod
    def create_collection(self):
        """Create a collection for vector storage."""
        pass

    @abstractmethod
    def delete_collection(self):
        """Delete a collection by name."""
        pass

    @abstractmethod
    def insert_vector_data(self):
        """Insert vector data into a collection."""
        pass

    @abstractmethod
    def delete_vector(self):
        """Delete a vector by file ID."""
        pass

    @abstractmethod
    def vector_search(self):
        """Perform a vector-based semantic search."""
        pass

    @abstractmethod
    def check_file_existence(self):
        """Check if a file exists in the collection."""
        pass

    @abstractmethod
    def check_collection_existence(self):
        """Check if a collection exists."""
        pass
