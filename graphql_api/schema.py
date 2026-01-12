import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'email')

class Query(graphene.ObjectType):
    health = graphene.String()
    me = graphene.Field(UserType)

    def resolve_health(root, info):
        return 'ok'

    def resolve_me(root, info):
        user = info.context.user
        return None if user.is_anonymous else user

schema = graphene.Schema(query=Query)
