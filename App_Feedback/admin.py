from django.contrib import admin
from App_Feedback.models import Feedback


class AdminFeedback(admin.ModelAdmin):
    list_display = ['user', 'house_name', 'flat_number',  'feedback', 'created']


# Register your models here.
admin.site.register(Feedback, AdminFeedback)

