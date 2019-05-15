from django.shortcuts import render,HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import myForm,social_postForm
from django.contrib.auth.models import User
from  .models import user_plan,social_post
# Create your views here.

class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def ChoosePlan(request):
    if request.method == 'POST':
        form = myForm(request.POST)
        if form.is_valid():
            username_v = User.objects.get(username = request.user.username)
            choice_v = form.cleaned_data['choice']
            data = user_plan(username=username_v,choosen_plan=choice_v)
            data.save()
            print(choice_v)
            return render(request,'plan.html')
    else:
        username_v = user_plan.objects.filter(username=request.user.username).count()
        print(username_v)
        if username_v == 0:
            form = myForm()
            print('hello')
            return render(request,'plan.html',{'form':form})
        else:
            form = social_postForm()
            return  render(request,'home.html',{'form':form})


def post(request):
    if request.method == 'POST':
        form = social_postForm(request.POST)
        if form.is_valid():
            username_v = form.cleaned_data['username']
            post_v = form.cleaned_data['post']
            print(username_v)
            print(post_v)
            return render(request,'home.html')
    return HttpResponse({{request.POST['post']}})