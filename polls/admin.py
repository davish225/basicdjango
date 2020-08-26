from django.contrib import admin

# Register your models here.

from .models import Question, Choice


admin.site.site_header = "Poll Admin"
admin.site.site_title = "Poll Admin area"
admin.site.index_title = "Welcome to the Poll Admin area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}), ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInLine]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)