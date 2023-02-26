from django.contrib import admin
from .models import *


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


@admin.register(Speed)
class SpeedAdmin(admin.ModelAdmin):
    list_display  = ['id','name',]
    search_fields = ['id','name',]


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display  = ['id','name',]
    search_fields = ['id','name',]


@admin.register(Crossing)
class CrossingAdmin(admin.ModelAdmin):
    list_display  = ['id','date','temperature','camera','place',]
    search_fields = ['id','date','temperature','camera__name','place__name',]


@admin.register(AnimalToCrossing)
class AnimalToCrossingAdmin(admin.ModelAdmin):
    list_display  = ['id','animal','crossing','behaviour',]
    search_fields = ['id','animal__name','crossing__name','behaviour__name',]
