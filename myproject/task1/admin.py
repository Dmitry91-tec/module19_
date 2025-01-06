from django.contrib import admin
from .models import Bayer, Game, News

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost',)             #Фильтрацию по полям size и cost.
    list_display = ('title', 'cost', 'size',)   #Отображение полей title, cost и size при отображении всех полей списком
    search_fields = ('title',)                  #Поиск по полю title.
    list_per_page = 20                          #Ограничение кол-ва записей до 20.

@admin.register(Bayer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age',)
    list_display = ('name', 'balance', 'age',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)

admin.site.register(News)