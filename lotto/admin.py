from django.contrib import admin

from .models import LottoCategory, LottoResultItem, LottoResultNumber

admin.site.register(LottoCategory)


# admin.site.register(LottoResultItem)
# admin.site.register(LottoResultNumber)


class LottoResultNumberInline(admin.TabularInline):
    model = LottoResultNumber
    extra = 1


class LottoResultItemAdmin(admin.ModelAdmin):
    model = LottoResultItem
    inlines = [
        LottoResultNumberInline,
    ]


admin.site.register(LottoResultItem, LottoResultItemAdmin)
