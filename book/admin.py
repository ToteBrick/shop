from django.contrib import admin

# Register your models here.
from book.models import BookInfo, HeroInfo

admin.site.register(BookInfo)
admin.site.register(HeroInfo)
