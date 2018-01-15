from django.db import models
from datetime import datetime

# Create your models here.
class Upload(models.Model):  # 自定义model时候，一般都需要继承models.Model
	DownloadDocount = models.IntegerField(verbose_name=u"visiting times",default=0)

	code = models.CharField(max_length=8, verbose_name=u"code")

	Datetime = models.DateTimeField(default=datetime.now, verbose_name=u"Add time")

	path = models.CharField(max_length=32,verbose_name=u"download path")

	name = models.CharField(max_length=32, verbose_name=u"filename",default="")

	Filesize = models.CharField(max_length=10,verbose_name=u"filesize")

	PCIP = models.CharField(max_length=32, verbose_name=u"IPaddr",default="")
	# PCIP 上传文件的IP

	class Mete():  # Meta 可以用于定义数据表名，排序方式             
		verbose_name="download"
		db_table = "download"

	def __str__(self):
		return self.name