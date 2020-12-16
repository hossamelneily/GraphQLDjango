import graphene
from graphene_django.types import DjangoObjectType
from .models import Snippet, Project


class SnippetType(DjangoObjectType):
    class Meta:
        model = Snippet
        filter_fields = ['name', 'ingredients']


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


class Query(graphene.ObjectType):
    all_snippets = graphene.List(SnippetType)
    all_projects = graphene.List(ProjectType)
    snippet_by_title = graphene.Field(SnippetType, title=graphene.String(required=True))

    def resolve_all_snippets(self, info, **kwargs):
        return Snippet.objects.select_related('project').all()

    def resolve_all_projects(self, info, **kwargs):
        return Project.objects.all()

    def resolve_snippet_by_title(self, info, **kwargs):
        return Snippet.objects.get(title__icontains=kwargs.get('title'))


schema = graphene.Schema(query=Query)
