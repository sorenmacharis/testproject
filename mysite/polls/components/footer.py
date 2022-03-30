from django_unicorn.components import UnicornView, QuerySetType
from polls.models import Question, Choice

class FooterView(UnicornView):
    nq : int = 0
    nv : int = 0
    
    def mount(self):
        self.nq = Question.objects.count()

        result = 0
        cs = Choice.objects.all()
        for c in cs :
            result = result + c.votes
        self.nv = result

    def get_updates(self):
        self.nq = Question.objects.count()

        result = 0
        cs = Choice.objects.all()
        for c in cs :
            result = result + c.votes
        self.nv = result