from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.contrib.auth.views import LoginView 
from django.views import generic
from django.urls import reverse_lazy
from .models import Book ,CustomUser
from .form import LoginForm, RegisterForm,Booksform
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


from django.contrib.auth import logout

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('dashbord')

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class Dashbord(TemplateView):
    template_name = 'dashboard.html'

class Allbook(ListView):
    template_name = 'allbook.html'
    queryset = Book.objects.all()
    context_object_name = "object_list"    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Allbook, self).get_context_data(**kwargs)
        s=CustomUser.objects.filter(email=self.request.user.email,type='admin').first()
        print(s)
        context['object'] = s
        return context    
from django.shortcuts import redirect


def delete(request, id):
    if request.user.is_superuser: 
        Book.objects.filter(id=id).delete()
        return redirect('dashbord')

 


def Createbook(request):
    form = Booksform(request.POST or None)

    if request.method == "POST":
        if request.user.is_superuser:
            if form.is_valid():
                form.save()
                return redirect ('dashbord')
    context = {
        "form":form
    }
    return render(request, 'create_book.html', context)

                                      
from django.views.generic.edit import CreateView



def book_update(request, id):
    context ={}
    obj = get_object_or_404(Book, id = id)
    form = Booksform(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect ('dashbord')
    context["form"] = form
    return render(request, "update.html", context)

def user_logout(request):
    logout(request)
    return redirect ('/')