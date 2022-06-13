from django.contrib import admin

# Register your models here.
from .models import Flower, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'flower', 'text', 'datetime_created',)


admin.site.register(Flower)
admin.site.register(Comment, CommentAdmin)
