from django.shortcuts import render

def services(request):
    context={'service':'active'}
    return render(request,'serv/services.html', context)
