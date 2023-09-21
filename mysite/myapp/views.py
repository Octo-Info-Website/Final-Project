from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
from .models import Question
from .models import Answer
# Create your views here.
def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, "myapp/index.html", context)

def facts(request):
    return render(request, "myapp/facts.html")

def UserPage(request, member_id):
    user = User.objects.get(pk = member_id)
    answers = user.answer_set.all()
    context = {'user':user, 'answers':answers }
    return render(request, "myapp/UserPage.html", context)
