import factory
from sphinxdoc.models import Project


class ProjectFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'Project #{n}')
    slug = factory.Sequence(lambda n: f'project-{n}')
    path = factory.Sequence(lambda n: f'tests/docs-{n}/')

    class Meta:
        model = Project
