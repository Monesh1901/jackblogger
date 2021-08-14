from django.http import request
from blogs.forms import InfoForm
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from blogs.models import Info
from blogs.models import Blog
from blogs.models import Comment
from blogs.models import Images
from blogs.forms import ImagesForm
from blogs.forms import BlogForm
    
   
def index(r):
    context = {'form': InfoForm}
    comment=Comment.objects
    blogs=Blog.objects
    images=Images.objects
    return render(r, 'jackmedia/index.html',{'comment':comment,'blogs':blogs, 'images':images}, context )

def contact(r):
    if r.method == 'POST':
       
        contacts=Info()
        contacts.title=r.POST.get('title')
        contacts.mail=r.POST.get('mail')
        contacts.sub=r.POST.get('sub')
        contacts.message=r.POST.get('message')
                      
        contacts.save()
        return redirect('index')
    else:
         return render(r, 'jackmedia/contact.html')
    
def comment(r):
    if r.method == 'POST':
        
            contacts=Comment()
            contacts.title=r.POST.get('title')
            contacts.email=r.POST.get('email')
            contacts.body=r.POST.get('body')
            contacts.save()
            return redirect('index')
    else:
        return render(r ,'products/index.html',{'error':'all  fiels are required to fill'})

def base(r):
    context = {'form': InfoForm}
    return render(r, 'jackpluto/base.html', context)     


def blog(r):
    
    content={   
        "blogs":Blog.objects.all(), 
        'comment':Comment.objects.all(),    
    }
    
    return render(r, 'jackmedia/blog.html',content)

def about(r):
    return render(r, 'jackmedia/about.html')

def marketing(r):
    return render(r, 'jackmedia/marketing.html')
#------------------------------------------->


def calendar(r):
    return render(r, 'jackpluto/calendar.html')

def charts(r):
    return render(r, 'jackpluto/charts.html')

def contact1(r):
    return render(r, 'jackpluto/contact1.html', {'context':Info.objects.all})



def dashboard_2(r):
    return render(r, 'jackpluto/dashboard_2.html')

def dashboard(r):
    return render(r, 'jackpluto/dashboard.html')

def email(r):
    return render(r, 'jackpluto/email.html')

def general_elements(r):
    return render(r, 'jackpluto/general_elements.html')

def icons(r):
    return render(r, 'jackpluto/icons.html')

def index1(r):
    return render(r, 'jackpluto/index1.html')

def invoice(r):
    return render(r, 'jackpluto/invoice.html')

def login(r):
    return render(r, 'jackpluto/login.html')

def map(r):
    return render(r, 'jackpluto/map.html')

def media_gallery(r):
    return render(r, 'jackpluto/media_gallery.html')

def price(r):
    return render(r, 'jackpluto/price.html')

def profile(r):
    return render(r, 'jackpluto/profile.html')

def project(r):
    return render(r, 'jackpluto/project.html')

def settings(r):
    return render(r, 'jackpluto/settings.html')

def tables(r):
    return render(r, 'jackpluto/tables.html')


def comments(r):
    comment=Comment.objects
    return render(r, 'jackpluto/comments.html',{'comment':comment})



def images(request):
    return render(request, 'jackpluto/images.html',{'context':Images.objects.all()})

def edit_1(request,id):
    get_id = Images.objects.get(id = id)
    form = ImagesForm(request.POST or None, request.FILES or None, instance=get_id)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('images') 
    else:       
      return render(request, 'jackpluto/edit_1.html',{'context': Images.objects.all(),'form': form})
    
def delete_1(request,id):
    get_id = Images.objects.get(id=id)
    get_id.delete ()
    return redirect ('images')

def add_1(request):
    forms_ = ImagesForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if forms_.is_valid():
            forms_.save()
            return redirect('images')
    return render(request, 'jackpluto/add_1.html',{'context': Images.objects.all(),'form': forms_})
    
#------------------------------BLOGS------------------------


def blogs1(request):
    return render(request, 'jackpluto/blogs1.html',{'context':Blog.objects.all()})

def edit_blog(request,id):
    get_id = Blog.objects.get(id = id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=get_id)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blogs1') 
    else:       
      return render(request, 'jackpluto/edit_blog.html',{'context': Blog.objects.all(),'form': form})
    
def delete_blog(request,id):
    get_id = Blog.objects.get(id=id)
    get_id.delete ()
    return redirect ('blogs1')

def add_blog(request):
    forms_ = BlogForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if forms_.is_valid():
            forms_.save()
            return redirect('blogs1')
    return render(request, 'jackpluto/add_blog.html',{'context': Blog.objects.all(),'form': forms_})