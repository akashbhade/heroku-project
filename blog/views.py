from django.shortcuts import render, HttpResponse,  redirect
from blog.models import Blog, Contact
from django.contrib import messages
import math
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, "index.html")

def blog(request):
    no_of_posts = 3
    # if request.GET['pageno']
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    '''
    1 :0 -5
    2 :5 -10
    3 :10 -15
    4 :15 -20

    1: 0 - 0 + no_of_posts
    2: no_of_posts to no_of posts + no_of_posts
    3: no_of_posts + no_of_posts to no_of_posts + no_of_posts + no_of_posts

    (page_no-1) to page_no*no_of_posts

    '''
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = Blog.objects.all()[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page<math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, "bloghome.html", context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}
    return render(request, "blogpost.html", context)

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        state= request.POST.get("state")
        desc = request.POST.get("desc")
        # instance = Contact(fname=fname, lname=lname, email=email, phone=phone, city=city, state=state, desc=desc)
        # instance.save()

        if len(fname)<2 or len(email)<4 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please fill the details correctely")
        else:
            instance = Contact(fname=fname, lname=lname, email=email, phone=phone, city=city, state=state, desc=desc)
            instance.save()
            messages.success(request, "Your form has been sent successfully")


    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")


def search(request):
    query = request.GET['query']
    if len(query)>90:
        blogs = Blog.objects.none()
    else:
        blogsTitle = Blog.objects.filter(title__icontains=query)
        blogsContent = Blog.objects.filter(content__icontains=query)
        blogs = blogsTitle.union(blogsContent)
        
    if blogs.count() == 0:
        []
    params = {'blogs':blogs, 'query': query}
    return render(request, 'search.html', params)

    # return render(request, "search.html")

# def login(request):
#     return render(request, 'index.html' )

# def logout(request):
#     return render(request, 'index.html' )

# def signup(request):
#     return render(request, 'index.html' )


    

