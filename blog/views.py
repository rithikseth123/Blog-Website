from django.shortcuts import render
from django.views.generic import View,ListView,CreateView,TemplateView
from django.views.generic import DetailView
from .forms import BlogForm
from .models import Blog
# Create your views here.


class IndexView(View):
    def get(self,request):
        posts=Blog.objects.order_by('-id')[:3]
        return render (request,"blog/index.html",{"posts":posts})
    
class AllPostsView(ListView):
    template_name="blog/all_posts.html"
    model=Blog
    context_object_name="posts"

class RecentPostsView(ListView):
    template_name="blog/recent_posts.html"
    model=Blog
    def get_context_data(self, **kwargs)  :
        context = super().get_context_data(**kwargs)
        context["posts"] = Blog.objects.order_by('-id')[:3]
        return context


class CreateBlogView(CreateView):
    template_name="blog/forms.html"
    model=Blog
    fields="__all__"
    success_url="thank-you/"

class ThankYouView(TemplateView):
    template_name="blog/thankyou.html"
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["message"] = "ThankYou! For Submitting This Blog"
        return context

class SinglePostView(DetailView):
    template_name="blog/single_post.html"
    model=Blog

# def SinglePostView(request,title):
#     blog = Blog.objects.get(title=title)
#     print=blog
#     return render(request, 'blog/single_post.html', {"blog":blog})

class AuthorView(ListView):
    template_name="blog/all_authors.html"
    model=Blog
    context_object_name="posts"

# class SingleAuthorPostView(DetailView):
#     template_name="blog/authorpost.html"
#     model=Blog


def SingleAuthorPostView(request,author):
    blog = Blog.objects.get(author=author)
    print=blog
    return render(request, 'blog/authorpost.html', {"blog":blog})
    
    
