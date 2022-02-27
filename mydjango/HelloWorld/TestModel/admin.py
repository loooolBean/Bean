from django.contrib import admin
from .models import demo, Contact, Tag


# Register your models here.
# Register your models here.

# 定义一个ContactAdmin类，用来说明管理页面的显示格式，field属性定义了要显示的字段。
# 内联
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([demo, Tag])
