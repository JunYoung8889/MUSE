from django.contrib import admin
from .models import (
    ActorArticle,
    ActorComment,
    DirectorArticle,
    DirectorComment,
    PeopleArticle,
    PeopleComment,
)


# Register your models here.
admin.site.register(ActorArticle)
admin.site.register(ActorComment)
admin.site.register(DirectorArticle)
admin.site.register(DirectorComment)
admin.site.register(PeopleArticle)
admin.site.register(PeopleComment)
