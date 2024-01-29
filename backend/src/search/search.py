from tantivy import Collector, Index, QueryParser, SchemaBuilder, Term

# Create a schema
schema_builder = SchemaBuilder()
title_field = schema_builder.add_text_field("title", stored=True)
body_field = schema_builder.add_text_field("body", stored=True)
schema = schema_builder.build()

# Create an index with the schema
index = Index(schema)

# Add documents to the index
with index.writer() as writer:
    writer.add_document({"title": "First document", "body": "This is the first document."})
    writer.add_document({"title": "Second document", "body": "This is the second document."})
    writer.commit()

# Create a query parser
query_parser = QueryParser(schema, ["title", "body"])

# Basic search
query = query_parser.parse_query("first")
collector = Collector.top_docs(10)
search_result = index.searcher().search(query, collector)

print("Basic search results:")
for doc in search_result.docs():
    print(doc)

# Fuzzy search
fuzzy_query = query_parser.parse_query("frst~1")  # Allows one edit distance
fuzzy_collector = Collector.top_docs(10)
fuzzy_search_result = index.searcher().search(fuzzy_query, fuzzy_collector)

print("Fuzzy search results:")
for doc in fuzzy_search_result.docs():
    print(doc)

# Filtered search
title_term = Term(title_field, "first")
body_term = Term(body_field, "first")
filter_query = schema.new_boolean_query().add_term(title_term).add_term(body_term)
filtered_collector = Collector.top_docs(10)
filtered_search_result = index.searcher().search(filter_query, filtered_collector)

print("Filtered search results:")
for doc in filtered_search_result.docs():
    print(doc)