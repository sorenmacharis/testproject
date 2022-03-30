from django_unicorn.components import UnicornView
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice

class VoteView(UnicornView):
    which : str = 0
    error_message : str = ''
    votesuccess : str = None
    q : Question = None

    def mount(self):
        self.q = get_object_or_404(Question, pk=self.request.GET.get('question_id',''))
        
    
    def addVote(self):
        try:
            selected_choice = self.q.choice_set.get(pk=self.which)
        except (KeyError, Choice.DoesNotExist):
        
            self.error_message = "You didn't select a choice!"
        else:
            selected_choice.votes += 1
            selected_choice.save()
        
            self.votesuccess = 'success'

    class Meta:
        # Zonder dit zijn er bepaalde problemen met de votesuccess & radiobuttons
        javascript_exclude = ("which","error_message", "q","votesuccess",)