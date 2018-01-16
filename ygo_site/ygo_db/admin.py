from django.contrib import admin

from .models import CardDatas, CardTexts, CardAttribute

class CardDatasInline(admin.TabularInline):
    model = CardDatas

class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['id', 'name', 'desc']
            }),
        ('Strings', {
            'fields': [
                'str1', 'str2', 'str3', 'str4', 'str5', 'str6', 'str7', 'str8', 'str9', 'str10',
                'str11', 'str12', 'str13', 'str14', 'str15', 'str16'
            ],
            'classes': ['collapse']
        }),
    ]
    list_display = ('id', 'name')
    inlines = [CardDatasInline]
    search_fields = ['name', 'desc']

admin.site.register(CardTexts, CardAdmin)
admin.site.register(CardAttribute)
