from django.shortcuts import render

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all().order_by('-post_date')
    users = User.objects.all()  
    current = request.user
    likes = Like.objects.all().count()
    
    return render(request, 'index.html',{"images":images,'users':users,'current':current,"likes":likes})