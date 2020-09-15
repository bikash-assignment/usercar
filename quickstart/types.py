from graphene_django.types import DjangoObjectType
from .models import Car
from django.contrib.auth.models import User, Group


class CarType(DjangoObjectType):
    class Meta:
        model = Car


class UserType(DjangoObjectType):
    class Meta:
        model = User


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


