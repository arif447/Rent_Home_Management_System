from django.shortcuts import render,  HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Feedback
from .forms import Feedback_Form, Replay_Form

# Create your views here.


@login_required
def Renter_Feedback(request):
    form = Feedback_Form()
    if request.method == 'POST':
        form = Feedback_Form(request.POST)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Feedback:feedback_history'))
    return render(request, 'App_Feedback/feedback.html', context={'form': form})


@login_required
def ReplayFeedback(request, id):
    replay_feedback = Feedback.objects.get(id=id)
    form = Replay_Form(instance=replay_feedback)
    if request.method == 'POST':
        form = Replay_Form(request.POST, instance=replay_feedback)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Feedback:feedbackshow'))

    return render(request, 'App_Feedback/replay_feedback.html', context={'form': form})


@login_required
def feedbackshow(request):
    feedback = Feedback.objects.all()
    diction = {'feedback': feedback}
    return render(request, 'App_Feedback/feedback_show.html', context=diction)



@login_required
def Feedback_History(request):
    student_feedback = Feedback.objects.filter(user=request.user)
    diction = {'student_feedback': student_feedback}
    return render(request, 'App_Feedback/feedbackhistory.html', context=diction)

