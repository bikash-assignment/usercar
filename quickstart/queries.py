import graphene
from graphene_django.types import ObjectType
from .types import UserType, CarType, GroupType
from .models import Car
from django.contrib.auth.models import User, Group


class Query(ObjectType):
    car = graphene.Field(CarType, id=graphene.Int())
    user = graphene.Field(UserType, id=graphene.Int())
    group = graphene.Field(GroupType, id=graphene.Int())
    cars = graphene.List(CarType)
    users = graphene.List(UserType)
    groups = graphene.List(GroupType)

    def resolve_car(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Car.objects.get(pk=id)
        return None

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return User.objects.get(pk=id)
        return None

    def resolve_group(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Group.objects.get(pk=id)
        return None

    def resolve_cars(self, info, **kwargs):
        return Car.objects.all()

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_groups(self, info, **kwargs):
        return Group.objects.all()