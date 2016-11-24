import factory
from sphinxdoc.models import Project


class ProjectFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Project #%d' % n)
    slug = factory.Sequence(lambda n: 'project-%d' % n)
    path = factory.Sequence(lambda n: 'tests/docs-%d/' % n)

    class Meta:
        model = Project
