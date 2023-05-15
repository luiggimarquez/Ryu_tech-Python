from django.shortcuts import render, redirect
from .forms import PostsForm, PostsEditForm
from .models import Posts
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


def createPage(request):


    if(request.user.has_perm('blog.can_view')):

        messages.error(request, 'No tienes permisos para realizar esta operación')
        return redirect('pages')


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
    print("ver: ",request.user.has_perm('blog.can_view'))
    print(request.user.username)


    post = Posts.objects.filter(id=id)
    return render(request,'blog/pageDetails.html',{
        'post' : post
    })


def pageEdit(request,id):

    user=request.user
    posts = Posts.objects.get(id=id)
   
    
    if (user.has_perm('blog.can_view')):
        messages.error(request, 'No tienes permisos para realizar esta operación')
        return redirect('details', id)
   
    if (request.method == 'GET'):
            return render(request, "blog/pageEdit.html",{
            'form': PostsEditForm(instance=posts)
            })
   
    else:
        
        form = PostsEditForm(request.POST,request.FILES, instance=posts)
        print(form)
        if form.is_valid():
            
            
            if(user.has_perm('blog.can_edit')):
                messages.error(request, 'Access Denied - No tienes permisos para cambiar la imagen')
                return render(request,'blog/pageEdit.html',{'form': PostsEditForm(instance=posts)})
            else:
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

    user = request.user
    if(user.has_perm('blog.can_view') or (user.has_perm('blog.can_edit'))):
  
        messages.error(request, 'No tienes permisos para realizar esta operación')
        return redirect('details', id)
    else:
        post = Posts.objects.get(id=id)
        post.delete()

    return redirect('pages')
    