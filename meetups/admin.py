from django.contrib import admin
from .models import Meetup, Location, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')    # show column in admin
    list_filter = ('location', 'date')    #adding on admin
    prepopulated_fields = {'slug': ('title',)}  # to generate slug name automatically with title in admin

# To show options on admin screen
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)