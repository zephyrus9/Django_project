from django.contrib import admin
from polls import models


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]


# Register your models here.
admin.site.register(models.Question) # 注册Question模型
# admin.site.register(models.Choice)					
