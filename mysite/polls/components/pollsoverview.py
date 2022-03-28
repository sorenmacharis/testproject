from django_unicorn.components import UnicornView, QuerySetType
from polls.models import Question


class PollsoverviewView(UnicornView):
    latest_question_list: QuerySetType[Question] = Question.objects.none()
    


    def mount(self):
        self.latest_question_list = Question.objects.order_by('-pub_date')[:5]
        
