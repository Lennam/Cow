from django.contrib import admin
from .models import Fodder,Reslut,Vol


# Register your models here.
class FodderAll(admin.ModelAdmin):
    list_display = ('id', 'date', 'nameOne', 'nameTwo', 'nameThree', 'nameFour', 'nameFive')


class ReslutAll(admin.ModelAdmin):
    list_display = ('id', 'date', 'tdnfc', 'tdcpf', 'tdcpc', 'tdfa', 'tdndf', 'tdn', 'de1x', 'mep', 'nelp')


class VolAll(admin.ModelAdmin):
    list_display = ('id', 'date', 'volOne', 'volTwo', 'volThree', 'volFour', 'volFive')

admin.site.register(Fodder, FodderAll)
admin.site.register(Reslut, ReslutAll)
admin.site.register(Vol, VolAll)
