from django.shortcuts import render

# Create your views here.
def settings(request):
    context = {
        'title': 'Главное',
        'description': 'я бакэнд студент'
    }
    return render (request,'index.html',context=context)