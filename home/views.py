from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse('Hello world')
    context = {
        'user': request.user
    }
    return render(request, 'home/index.html', context)
