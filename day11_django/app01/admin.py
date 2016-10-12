from django.contrib import admin
from app01.models import  SecondModel, FirstModel, Book, AuthorList

# Register your models here.


admin.site.register(SecondModel)
admin.site.register(FirstModel)
admin.site.register(Book)
admin.site.register(AuthorList)