from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required

from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

@login_required(login_url='/accounts/login/')
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'polls/profile.html')

  
@permission_required('polls.view_question', raise_exception=True)       
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
@login_required(login_url='/accounts/login/')
def vote(request, question_id):
    
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
        
            return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
        
            return render(request, 'polls/detail.html',{
                'votesuccess': "success",
            })
    

def numberofpolls(request):
    nq = Question.objects.count()
    return HttpResponse("%s" % nq)

def numberofvotes(request):
    result = 0
    cs = Choice.objects.all()
    for c in cs :
        result = result + c.votes
    
    return HttpResponse("%i" % result)

def about(request):
    return render(request, 'polls/about.html')