import graphene

from services.resources.chatterbot import schema as main_schema


class Query(main_schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
