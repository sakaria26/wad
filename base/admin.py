from django.contrib import admin

# Register your models here.

from .models import User, Postal_Address, Address, Organisation, Author, Paper, Venue, Schedule, Accomadation, Speaker, Reviews

admin.site.register( User)
admin.site.register( Postal_Address)
admin.site.register( Address)
admin.site.register( Organisation)
admin.site.register( Author)
admin.site.register( Paper)
admin.site.register( Venue)
admin.site.register( Schedule)
admin.site.register( Accomadation)
admin.site.register( Speaker)
admin.site.register( Reviews)
