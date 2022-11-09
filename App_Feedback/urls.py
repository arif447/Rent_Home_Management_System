from django.urls import path
from .views import *
app_name = 'App_Feedback'

urlpatterns = [
    path('feedback/', Renter_Feedback, name='renterfeedback'),
    path('replay/<id>/', ReplayFeedback, name='Replayfeedback'),
    path('feedbackshow/', feedbackshow, name='feedbackshow'),
    path('Historyfeedback/', Feedback_History, name='feedback_history'),
]


