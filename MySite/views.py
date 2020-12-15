from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from datetime import datetime
from .models import Stud_info
from . import forms
from .forms import NewStudent
from django.views.generic import TemplateView
# Create your views here.

def index(request):

    # context_dict = {
    #     'text':"And hello    hello 'mscit' students   sdsdsdsd",
    #     'number': 100,
    #     'dt': datetime.now(),
    #     'fruit':"cherries",
    #     'link':'http://hardikchavda.tech'
    # }
    users_list = Stud_info.objects.order_by('s_name')
    user_data = {'Data': users_list}
    return render(request, "index.html", context=user_data)


def about(request, id):

    # studentForm = NewStudent()
    # if request.method == "POST":
    #     studentForm = NewStudent(request.POST)
    #     if studentForm.is_valid():
    #         studentForm.save(commit=True)
    #         return about(request)
    #     else:
    #         print('Error Form Invalid')

    instance = Stud_info.objects.get(id=id)
    stud_frm = NewStudent(request.POST or None, instance=instance)

    if stud_frm.is_valid():
        stud_frm.save()

    context = {
        'form': stud_frm
    }

    return render(request, "about.html", context=context)


def contact(request):
    dataform = forms.FormName(request.POST or None)
    if dataform.is_valid():
        print("Validation Success")
        print("Student Name:"+dataform.cleaned_data['s_name'])
        print("Student Address:"+dataform.cleaned_data['s_address'])

    return render(request, "contactus.html", {'form': dataform})


def delete_data(request, id):
    if request.method == "POST":
        di = Stud_info.objects.get(id=id)
        di.delete()
        return HttpResponseRedirect('/')
    else:
        print("Something is wrong")


def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('college', 'Geetanjali')
    return response


def getcookie(request):
    clgname = request.COOKIES['college']
    return HttpResponse('College'+clgname)


def setsession(request):
    request.session['lecturer'] = 'HardikChavda'
    request.session['email'] = 'hardikkchavda@gmail.com'
    return HttpResponse("Session is Created")

def getsession(request):
    sname = request.session['lecturer']
    semail = request.session['email']
    return HttpResponse(sname+":"+semail)

class TestView(TemplateView):
    template_name = 'test.html'