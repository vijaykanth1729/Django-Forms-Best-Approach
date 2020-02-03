from django.contrib import admin

from .models import Book, Contact, Forum

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','pub_date','author']
    list_filter = ['title']
    list_editable = ['author']

admin.site.register(Book, BookAdmin)

admin.site.register(Contact)
admin.site.register(Forum)