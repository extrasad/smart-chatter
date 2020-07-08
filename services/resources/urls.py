from django.conf.urls import url
from .chatterbot.views import ChatterMessage
from graphene_django.views import GraphQLView
from services.resources.schema import schema

urlpatterns = [
    url(r"^message", ChatterMessage.as_view()),
    url(r"^graphql$", GraphQLView.as_view(graphiql=True, schema=schema)),
]
