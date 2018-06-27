from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':
        ['collapse']}),
        ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
