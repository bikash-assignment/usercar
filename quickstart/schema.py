import graphene
from graphene_django.types import DjangoObjectType, ObjectType
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


class CarInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class GroupInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    groups = graphene.List(GroupInput)


class CreateCar(graphene.Mutation):
    class Arguments:
        input = CarInput(required=True)

    ok = graphene.Boolean()
    car = graphene.Field(CarType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        car_instance = Car(car_name=input.name)
        car_instance.save()
        return CreateCar(ok=ok, car=car_instance)


class UpdateCar(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = CarInput(required=True)

    ok = graphene.Boolean()
    car = graphene.Field(CarType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        car_instance = Car.objects.get(pk=id)
        if car_instance:
            ok = True
            car_instance.car_name = input.name
            car_instance.save()
            return UpdateCar(ok=ok, car=car_instance)
        return UpdateCar(ok=ok, car=None)


class DeleteCar(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    car = graphene.Field(CarType)

    @staticmethod
    def mutate(root, info, id):
        ok = False
        car_instance = Car.objects.get(pk=id)
        if car_instance:
            ok = True
            car_instance.delete()
            return DeleteCar(ok=ok, car=car_instance)
        return DeleteCar(ok=ok, car=None)


class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        groups = []
        for group_input in input.groups:
            print('Here')
            group = Group.objects.get(pk=group_input.id)
            if group is None:
                return CreateUser(ok=ok, user=None)
            groups.append(group)
        user_instance = User(username=input.username, email=input.email)
        user_instance.save()
        user_instance.groups.set(groups)
        return CreateUser(ok=ok, user=user_instance)


class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = UserInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        user_instance = User.objects.get(pk=id)
        if user_instance:
            ok =True
            groups = []
            for group_input in input.groups:
                print('Here')
                group = Group.objects.get(pk=group_input.id)
                if group is None:
                    return CreateUser(ok=ok, user=None)
                groups.append(group)
            user_instance.username = input.username
            user_instance.email = input.email
            user_instance.save()
            user_instance.groups.set(groups)
            return UpdateUser(ok=ok, user=user_instance)
        return UpdateUser(ok=ok, user=None)


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id):
        ok = False
        user_instance = User.objects.get(pk=id)
        if user_instance:
            ok=True
            user_instance.delete()
            return DeleteUser(ok=ok, user=user_instance)
        return DeleteUser(ok=ok, user=None)


class CreateGroup(graphene.Mutation):
    class Arguments:
        input = GroupInput(required=True)

    ok = graphene.Boolean()
    group = graphene.Field(GroupType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        group_instance = Group(name=input.name)
        group_instance.save()
        return CreateGroup(ok=ok, group=group_instance)


class UpdateGroup(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = GroupInput(required=True)

    ok = graphene.Boolean()
    group = graphene.Field(GroupType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        group_instance = Group.objects.get(pk=id)
        if group_instance:
            ok = True
            group_instance.name = input.name
            group_instance.save()
            return UpdateGroup(ok=ok, group=group_instance)
        return UpdateGroup(ok=ok, group=None)


class DeleteGroup(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    group = graphene.Field(GroupType)

    @staticmethod
    def mutate(root, info, id):
        ok = False
        group_instance = Group.objects.get(pk=id)
        if group_instance:
            ok = True
            group_instance.delete()
            return DeleteGroup(ok=ok, group=group_instance)
        return DeleteGroup(ok=ok, group=None)


class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()
    update_car = UpdateCar.Field()
    delete_car = DeleteCar.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_group = CreateGroup.Field()
    update_group = UpdateGroup.Field()
    delete_group = DeleteGroup.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
