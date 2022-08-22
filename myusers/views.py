from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView,TemplateView
from myusers.forms import UserRegistrationForm
from myusers.models import User
from django.contrib.auth import authenticate,login

from django.core.mail import send_mail


# Create your views here.


class EmpCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "reg.html"
    success_url = reverse_lazy("signin")
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            form.save()
            send_mail(
                "accound activation",
                "your accound is created",
                "arunmadambathl@gmail.com",
                [email,],
                fail_silently=False,
            )
            return redirect("signin")
        else:
            return render(request,self.template_name,{"form":form})

class LoginView(TemplateView):
    template_name = "login.html"

    def post(self,request,*args,**kwargs):
        uname=request.POST.get("username")
        pwd=request.POST.get("pwd")
        user=authenticate(request,username=uname,password=pwd)
        if user:
            login(request,user)
            print("success")
            if request.user.role=="faculty":
                return render(request,"f_home.html")
            else:
                return render(request,"s_home.html")



