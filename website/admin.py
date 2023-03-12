from django.contrib import admin
from .models import *


class CrossingsInline(admin.TabularInline):
    model = Video.animals.through


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display  = ['id','name','latitude','longitude',]
    search_fields = ['id','name','latitude','longitude',]


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display  = ['id','name',]
    search_fields = ['id','name',]


@admin.register(Behaviour)
class BehaviourAdmin(admin.ModelAdmin):
    list_display  = ['id','name',]
    search_fields = ['id','name',]


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display  = ['id','name',]
    search_fields = ['id','name',]


@admin.register(Video)
class CrossingAdmin(admin.ModelAdmin):
    list_display  = ['id','date','temperature','camera','place',]
    search_fields = ['id','date','temperature','camera__name','place__name',]
    inlines       = [CrossingsInline,]

# @admin.register(AnimalToCrossing)
# class AnimalToCrossingAdmin(admin.ModelAdmin):
#     list_display  = ['id','animal','video','behaviour',]
#     search_fields = ['id','animal__name','behaviour__name',]
