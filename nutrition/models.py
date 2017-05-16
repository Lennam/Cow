from django.db import models

# Create your models here.
from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('gb18030')


class Fodder(models.Model):
    date = models.DateField()
    nameOne = models.CharField(max_length=30)
    nameTwo = models.CharField(max_length=30)
    nameThree = models.CharField(max_length=30)
    nameFour = models.CharField(max_length=30)
    nameFive = models.CharField(max_length=30)

    def __unicode__(self):
        return str(self.date)


class Reslut(models.Model):
    date = models.DateField()
    tdnfc = models.FloatField()
    tdcpf = models.FloatField()
    tdcpc = models.FloatField()
    tdfa = models.FloatField()
    tdndf = models.FloatField()
    tdn = models.FloatField()
    de1x = models.FloatField()
    mep = models.FloatField()
    nelp = models.FloatField()

    def __unicode__(self):
        return str(self.date)


class Vol(models.Model):
    date = models.DateField()
    volOne = models.FloatField()
    volTwo = models.FloatField()
    volThree = models.FloatField()
    volFour = models.FloatField()
    volFive = models.FloatField()

    def __unicode__(self):
        return str(self.date)



