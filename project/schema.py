import graphene
from snippets.schema import Query as snippets_Query


class Query(snippets_Query):
    pass



schema = graphene.Schema(query=Query)
