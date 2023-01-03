from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout,login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from django.core.paginator import Paginator

from main.utils import DataMixin
from .forms import *
from .models import *
# Create your views here.


menu = [{"title":'About us'},
        {"title":'Contact'}]


class Home(DataMixin,ListView):
    model = Women
    template_name = 'index.html'
    context_object_name = 'posts'
    extra_context = {"title":'Home'}
    
    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Home'
        return context
    
    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')
    
    
# def index(request):
#     posts = Women.objects.all()
#     cats = Category.objects.all()

#     context = {
#         'posts': posts,
#         'cats': cats,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }

#     return render(request, 'index.html', context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class ShowPost(DetailView):
    model = Women
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    #pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    
    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context["title"] = context['post']
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Women,slug=post_slug)
#     context = {
#         "post":post,
#         "title":post.title,
#         "cat_selected":post.cat_id,
#     }
#     return render(request,'post.html',context)
# def showCat(request):
#     if len(post)==0:
#         raise Http404


class AddStatus(CreateView):
    form_class = AddPostForm
    template_name = 'add-page.html'
    success_url = reverse_lazy('main:home')
    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context["title"] = 'Add status'
        return context
# def add_status(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST,request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # try:
#             #     # Women.objects.create(**form.cleaned_data) modelga ulanmagan bolsa
#             #     form.save() #modelga meta bn ulangan bolsa
#             #     return redirect('main:home')
#             # except:
#             #     form.add_error(None,"Oshibka yest")
#             form.save()
#             return redirect('main:home')
#     else:
#         form = AddPostForm()
#     return render(request,'add-page.html',{"title":"Add status",'form':form})

class Category(DataMixin,ListView):
    model = Women
    template_name = 'index.html'
    context_object_name = 'posts'
    allow_empty = False
    
    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],is_published=True).select_related('cat')
    
    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = menu
        context["title"] = "Category -" + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        return context
    
    
# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()

#     if len(posts) == 0:
#         raise Http404()

#     context = {
#         'posts': posts,
#         'cats': cats,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }

#     return render(request, 'index.html', context)

def about(request):
    women_list = Women.objects.all()
    paginator = Paginator(women_list,3)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(dir(paginator))
    print(dir(page_obj))
    return render(request,'about.html',{'page_obj':page_obj,'menu':menu,'title':'About Site'})


class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('main:home')
    
    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title="Register")
        return dict(list(context.items()))
    
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('main:home')
    

class LoginUser(DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    
    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title="Register")
        return dict(list(context.items()))
    
    # def get_success_url(self):
    #     return reverse_lazy('main:home')
    
def logout_user(request):
    logout(request)
    return redirect('main:login')