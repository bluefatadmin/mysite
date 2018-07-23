from django.contrib import admin
from .models import ReadNum ,ReadDetail  # 引用ReadNum


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num','contebt_object')

@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date','read_num', 'contebt_object')



