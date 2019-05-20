from django.contrib import admin

# Register your models here.
from book.models import BookInfo, HeroInfo

# admin.site.register(BookInfo)
# admin.site.register(HeroInfo)


# 自定义管理器对象
class BookInfoAdmin(admin.ModelAdmin):
    # 1. 列表中的列显示哪些字段
    list_display = ['id', 'btitle','bpub_date']
    # 2.每页中显示多少条数据,默认100
    list_per_page = 2
    '''3 "操作选项"的位置
顶部显示的属性，设置为True在顶部显示，设置为False不在顶部显示，默认为True。'''
    actions_on_top = True
    # 底部显示的属性，设置为True在底部显示，设置为False不在底部显示，默认为False。
    # actions_on_bottom = False
    # 4.右侧栏过滤器,属性如下，只能接收字段，会将对应字段的值列出来，用于快速过滤。一般用于有重复值的字段。
    list_filter = ['btitle', 'bpub_date']



admin.site.register(BookInfo, BookInfoAdmin)  # 注册方式一


@admin.register(HeroInfo)    # 注册方式二
class HeroInfoAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_filter = ['hbook', 'hgender']
    # 5 搜索框，属性如下，用于对指定字段的值进行搜索，支持模糊查询。列表类型，表示在这些字段上进行搜索。
    search_fields = ['hname']


# 站点首页设置
admin.site.site_header = '星空书城'
admin.site.site_title = '星空书城MIS'
admin.site.index_title = '欢迎使用星空书城MIS'
