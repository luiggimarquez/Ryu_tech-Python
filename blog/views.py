from django.shortcuts import render, redirect
from .forms import PostsForm, PostsEditForm
from .models import Posts
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.cache import never_cache
# Create your views here.
def createPage(request):

    if(request.method == "POST"):
        
        form = PostsForm(request.POST,request.FILES)
        print(form)
        if(form.is_valid()):

            info = form.cleaned_data
            usertable= User.objects.get(username=request.user.username)
            image = request.FILES['imageMain']
        
            blog = Posts.objects.create(user=usertable, title = info['title'], subtitle=info['subtitle'], imageMain = image, Message = info['Message'])
            blog.save()

            return render(request, 'blog/newpage.html',{
            'form': PostsForm})
   
    return render(request, 'blog/newpage.html',{
        'form': PostsForm
    })

def pagesListView(request):

    pagesList=Posts.objects.all()    
    return render(request,'blog/pages.html',{
        'pages': pagesList
    })


def pageDetailView(request,id):

    print(id)
    post = Posts.objects.filter(id=id)
    return render(request,'blog/pageDetails.html',{
        'post' : post
    })

@never_cache
def pageEdit(request,id):

    posts = Posts.objects.get(id=id)
    print(posts.title)
  
    if (request.method == 'GET'):
            return render(request, "blog/pageEdit.html",{
            'form': PostsEditForm(instance=posts)
            })
   
    else:
         
        form = PostsEditForm(request.POST,request.FILES, instance=posts)
        print(form)
        if form.is_valid():
            post_instance = form.save(commit=False)
        
            if form.cleaned_data.get('delete_image'):
                if (post_instance.imageMain):
                    post_instance.imageMain.delete()
                    post_instance.imageMain = None
            
            # Guardar los cambios en la publicación
            post_instance.save()
   


   
    return render(request,'blog/pageEdit.html',{
        'form': PostsEditForm(instance=posts)
    })

def deletePage(request,id):

    
    post = Posts.objects.get(id=id)
    post.delete()

    return redirect('pages')