from django.shortcuts import render
from .forms import PostsForm
from .models import Posts
from django.contrib.auth.models import User
from django.conf import settings
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
    #posts = Posts.objects.select_related('author').order_by('-author__last_login')
        
    return render(request,'blog/pages.html',{
        'pages': pagesList
    })


def pageDetailView(request,id):

    print("id: ", id)

    return render(request,'blog/pageDetails.html')