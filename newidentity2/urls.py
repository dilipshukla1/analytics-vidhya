from django.urls import path
from graphene_django.views import GraphQLView
from identity.views import login_view, public_info, user_profile
from graphql_api.schema import schema

urlpatterns = [
    path('api/login', login_view),
    path('api/rest-galaxy/public-info', public_info),
    path('api/user-rest-galaxy/profile', user_profile),
    path('api/query-galaxy', GraphQLView.as_view(schema=schema, graphiql=True)),
    path('api/user-query-galaxy', GraphQLView.as_view(schema=schema, graphiql=True)),
]
