"""Main file for Milvus Vector Database"""

from sentence_transformers import SentenceTransformer
from ExternalTools.VectorDatabase.Provider.Base import BaseVectorProvider
from pymilvus import (
    connections,
    Collection,
    utility,
    CollectionSchema,
    FieldSchema,
    DataType,
    exceptions,
)
from QueryBaseAI.settings import (
    MILVUS_HOST,
    MILVUS_PORT,
    VECTOR_DIMENSION,
)


class MilvusProvider(BaseVectorProvider):
    """Milvus vector database provider class"""

    def __init__(self):
        self.client = connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)

    def check_health(self):
        """Check the health of the Milvus server."""
        try:
            utility.get_server_version()
            return True
        except exceptions.MilvusException:
            raise exceptions.MilvusException("There is an issue with Milvus")

    def create_collection(self, org):
        """Create collection for vectors with text content"""

        if utility.has_collection(org):
            return

        schema = CollectionSchema(
            [
                FieldSchema(
                    name="file_id", dtype=DataType.INT64, is_primary=True, auto_id=False
                ),
                FieldSchema(
                    name="embedding", dtype=DataType.FLOAT_VECTOR, dim=VECTOR_DIMENSION
                ),
                FieldSchema(
                    name="text_content", dtype=DataType.VARCHAR, max_length=65535
                ),
            ]
        )
        collection = Collection(org, schema)
        index_params = {
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {"nlist": 1024},
        }

        collection.create_index("embedding", index_params)
        collection.load()

    def delete_collection(self, org):
        if utility.has_collection(org):
            utility.drop_collection(org)

    def insert_vector_data(self, file_id, data, org):
        """Add or update a vector"""

        collection = Collection(org)
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        vector = model.encode(data).tolist()
        collection.insert(
            [
                [file_id],
                [vector],
                [data],
            ]
        )

    def delete_vector(self, file_id, org):
        """Delete a vector"""

        collection = Collection(org)
        res = collection.query(
            expr=f"file_id in {[file_id]}", output_fields=["file_id"]
        )
        deleting_doc_pk_list = []
        for x in res:
            deleting_doc_pk_list.append(x["file_id"])

        expr = f"file_id in {deleting_doc_pk_list}"
        collection.delete(expr)
        deleting_doc_pk_list.clear()

    def vector_search(self, query, org, file_id=None):
        """Perform semantic search"""
        collection = Collection(org)
        collection.load()

        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        query_vector = model.encode(query).tolist()

        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}

        if file_id is not None:
            expr = f"file_id == {file_id}"
            results = collection.search(
                data=[query_vector],
                anns_field="embedding",
                param=search_params,
                limit=5,
                expr=expr,
                output_fields=["text_content"],
            )
        else:
            results = collection.search(
                data=[query_vector],
                anns_field="embedding",
                param=search_params,
                limit=5,
                output_fields=["text_content"],
            )

        contexts = []
        for hits in results:
            for hit in hits:
                text_content = hit.entity.get("text_content")
                if text_content:
                    contexts.append(text_content)

        if not contexts:
            return "No relevant information found for your query."

        context_text = "\n\n".join(contexts)

        return context_text

    def check_file_existence(self, file_id, org):
        try:
            collection = Collection(org)
        except Exception:
            return False
        result = collection.query(
            expr=f"file_id in {[file_id]}", output_fields=["file_id"]
        )

        if len(result) == 0:
            return False
        else:
            return True

    def check_collection_existence(self, org):
        try:
            _ = Collection(org)
        except Exception:
            return False

        return True


milvus_provider_obj = MilvusProvider()
