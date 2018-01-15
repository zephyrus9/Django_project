from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.StackedInline):   # 使用TabularInline使对象显示成紧凑的、基于表格形式的。
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),

	]
	inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)