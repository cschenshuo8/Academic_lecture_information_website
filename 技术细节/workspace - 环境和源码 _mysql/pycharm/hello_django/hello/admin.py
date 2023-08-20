from django.contrib import admin

# Register your models here.
from django.contrib import admin
from hello.models import Publisher, Author, AuthorDetail,Book,Device


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'address', 'city', 'state_province', 'country', 'website')


admin.site.register(Publisher, ContactAdmin)
admin.site.register([AuthorDetail, Author, Book] )
admin.site.register(Device)