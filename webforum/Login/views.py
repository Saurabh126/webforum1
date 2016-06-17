from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import User

def loggingin(request):
    return render(request, 'Login/loginhtml.html')

def rr(request):
    user1 = get_object_or_404(User,user_username=request.POST['username'])
    if user1.user_password == request.POST['userpassword'] :
        return HttpResponseRedirect('/Threads/' + user1.user_username +'/')
    else :
        return render(request, 'Login/loginhtml.html', {
            'error_message': "Incorrect password.",
        })

def register(request):
    return render(request, 'Login/registerhtml.html')

def addeduser(request):
    if (request.POST['newpassword'] == request.POST['repassword']) :
        user=User.objects.create(user_username = request.POST['newuserid'])
        user.user_password = request.POST['newpassword']
        user.save()
        template = loader.get_template('Login/addedhtml.html')
        return HttpResponse(template.render(request))
    else :
        return render(request, 'Login/registerhtml.html', {
            'error_message': "Both passwords do not match.",
        } )
