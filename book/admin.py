from django.contrib import admin

# Register your models here.
from book.models import BookInfo, HeroInfo

admin.site.register(BookInfo)
admin.site.register(HeroInfo)

# 站点首页设置
admin.site.site_header = '星空书城'
admin.site.site_title = '星空书城MIS'
admin.site.index_title = '欢迎使用星空书城MIS'
