from django.db import models

# Create your models here.
class Note(models.Model):
	sid models.charField(max_length=20)
	type_id models.IntegerField(default='1')
	date_created models.DateTimeField()
	date_modified models.DateTimeField()
	state models.BooleanField(default='false')
	content models.textField(default='')
	tag models.textField(default='')
	privacy models.charField(max_length=8, default='public')
	lattitude charField(max_length=20, default='')
	longitude charField(max_length=20, default='')