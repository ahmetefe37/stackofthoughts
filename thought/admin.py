from django.contrib import admin

# my models
from thought.models import Thought,User

class ThoughtAdmin(admin.ModelAdmin):
    list_display = ("title","date_created","score","category")

class UserAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","email","age")

admin.site.register(Thought,ThoughtAdmin)
admin.site.register(User,UserAdmin)
