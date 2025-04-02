from django.contrib import admin
from .models import ApprovedPost , PendingPost

@admin.register(ApprovedPost)
class ApprovedPostAdmin(admin.ModelAdmin):
    list_display=['id','title','image','date','description','postby']

@admin.register(PendingPost)
class PendingPostAdmin(admin.ModelAdmin):
    list_display=['id','title','image','date','description','postby']

