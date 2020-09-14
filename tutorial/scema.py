import graphene
import quickstart.schema


class Query(quickstart.schema.Query, graphene.ObjectType):
    pass


class Mutation(quickstart.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
