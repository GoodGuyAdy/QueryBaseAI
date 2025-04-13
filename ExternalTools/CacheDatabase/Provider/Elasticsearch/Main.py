"""Main file for Elasticsearch Database"""

import requests
from QueryBaseAI.settings import ELASTIC_URL, ELASTIC_HEADER
from elasticsearch import Elasticsearch, exceptions as es_exceptions
from ExternalTools.CacheDatabase.Provider.Base import BaseStorageProvider


class ElasticSearchProvider(BaseStorageProvider):
    """Elasticsearch database provider class"""

    def __init__(self):
        self.client = Elasticsearch(ELASTIC_URL)

    def check_health(self):
        """Check the health of the Elasticsearch cluster."""
        res = requests.get(f"{ELASTIC_URL}/_cluster/health", headers=ELASTIC_HEADER)
        if res.status_code != 200:
            raise es_exceptions.ConnectionError("There is an issue with Elasticsearch")
        return res.status_code == 200

    def create_index(self, org):
        """Create index for data"""
        if self.client.indices.exists(index=org):
            return

        index_body = {
            "mappings": {
                "properties": {
                    "file_id": {"type": "long"},
                    "text_content": {"type": "text"},
                }
            }
        }

        self.client.indices.create(index=org, body=index_body)

    def delete_index(self, org):
        """Deletes index for data"""
        if self.client.indices.exists(index=org):
            self.client.indices.delete(index=org)

    def insert_data(self, file_id, data, org):
        """Add or update data"""

        doc = {"file_id": file_id, "text_content": data}

        self.client.index(index=org, id=file_id, body=doc)

    def delete_data(self, file_id, org):
        """Delete a file"""

        try:
            self.client.delete(index=org, id=file_id)
        except es_exceptions.NotFoundError:
            pass

    def keyword_search(self, query, org, file_id=None):
        """Perform keyword-based search"""
        base_query = {"query": {"match": {"text_content": query}}}

        if file_id is not None:
            base_query["query"] = {
                "bool": {
                    "must": {"match": {"text_content": query}},
                    "filter": {"term": {"file_id": file_id}},
                }
            }

        try:
            response = self.client.search(index=org, body=base_query)
            hits = response.get("hits", {}).get("hits", [])
        except es_exceptions.NotFoundError:
            return "No relevant information found for your query."

        contexts = [
            hit["_source"]["text_content"]
            for hit in hits
            if "text_content" in hit["_source"]
        ]

        if not contexts:
            return "No relevant information found for your query."

        return "\n\n".join(contexts)

    def check_file_existence(self, file_id, org):
        """Checks if a file is present or not in Elastic"""
        try:
            res = self.client.get(index=org, id=file_id)
            return res["found"]
        except es_exceptions.NotFoundError:
            return False

    def check_index_existence(self, org):
        """Checks if a index is present or not in Elastic"""
        return self.client.indices.exists(index=org)


elasticsearch_provider_obj = ElasticSearchProvider()
