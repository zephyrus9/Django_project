from django.contrib import admin
from Sites import models


# Register your models here.
class SitesAdmin(admin.ModelAdmin):
	# title, timestamp均在models.py中定义；
	list_display = ('title', 'timestamp')


admin.site.register(models.Sites, SitesAdmin) 