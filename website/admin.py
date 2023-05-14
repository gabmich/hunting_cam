from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
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
class VideoAdmin(admin.ModelAdmin):
    def video_tag(self, obj):
        return format_html(f"""<video height="200"
                                      controls>
                                        <source src="{settings.NAS_URL}/{obj.place.name}/{obj.name}?ssid={settings.NAS_SSID}&openfolder=normal&filename={obj.name}&path=/{obj.place.name}"
                                        type="video/mp4">
                                </video>""")

    list_display  = ['id','date','name','video_tag','videofile','animal_crossings','temperature','camera','place',]
    list_filter   = ['place',]
    list_per_page = 5
    search_fields = ['id','name','date','temperature','camera__name','place__name',]
    inlines       = [CrossingsInline,]

# @admin.register(AnimalToCrossing)
# class AnimalToCrossingAdmin(admin.ModelAdmin):
#     list_display  = ['id','animal','video','behaviour',]
#     search_fields = ['id','animal__name','behaviour__name',]
