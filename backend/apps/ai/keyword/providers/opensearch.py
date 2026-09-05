from backend.apps.ai.keyword.base import BaseKeywordRetriever


class OpenSearchKeywordRetriever(BaseKeywordRetriever):

    def __init__(self, client, index_name):
        self.client = client
        self.index_name = index_name

    def index(self, chunks):
        # OpenSearch indexing logic
        pass

    def search(self, query, k=5, filters=None):
        # OpenSearch BM25 query
        pass

    def delete(self, filters=None):
        # OpenSearch deletion logic
        pass