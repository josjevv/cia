from django.db import models

# Create your models here.

class NameModelBase(models.Model):
    name = models.CharField('Name', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Client(NameModelBase):
    id = models.CharField('Debtor ID', primary_key=True, max_length=10)

class Project(NameModelBase):
    client = models.ForeignKey(Client)
    start_date = models.DateField()
    end_date = models.DateField()

class Milestone(NameModelBase):
    project = models.ForeignKey(Project)
    start_date = models.DateField()
    end_date = models.DateField()
