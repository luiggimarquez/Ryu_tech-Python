from django.shortcuts import render
from .forms import PostsForm

# Create your views here.
def createPage(request):

    if(request.method == "POST"):
        
        form = PostsForm(request.POST)
        print(form)
        if(form.is_valid()):

            info = form.cleaned_data

            print(info)
            return render(request, 'blog/newpage.html',{
            'form': PostsForm })
   



    return render(request, 'blog/newpage.html',{
        'form': PostsForm
    })