from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Question,Answer
from Login.models import User

def questionspage(request):
    question_list = Question.objects.all()
    template = loader.get_template('Threads/questionspagehtml.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))

    

def answerpage(request,user_id,question_id):
    question = get_object_or_404(Question, pk=question_id)
    user = get_object_or_404(User, pk = user_user_username)
    if request.POST:
        ans = Answer()
        ans.answer_text = request.POST.get('newanswer',"")
        ans.user = user
        ans.question = question
        ans.save()
        return HttpResponseRedirect('.')
    answer_list = question.answer_set.all()
    for answer1 in answer_list :
        if answer1.answer_text == "" :
            answer1.delete()
    answer_list = question.answer_set.all()
    template = loader.get_template('Threads/answerpagehtml.html')
    context = {
        'idnmber' : question_id ,
        'answer_list': answer_list,
    }
    return HttpResponse(template.render(context, request))


