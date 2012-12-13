from polls.models import Poll
from polls.models import Choice

from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 2


class PollAdmin(admin.ModelAdmin):
	fields = ['pub_date','question']
	inlines = [ChoiceInline]
	list_display = ('question','pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question','pub_date']
	date_hierarchy = 'pub_date'
admin.site.register(Poll,PollAdmin)

admin.site.register(Choice)

