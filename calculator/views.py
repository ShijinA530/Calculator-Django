from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    return render(request,'index.html')

def submit(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        d = {
            'q': q,
            'ans': ans,
            'error': False,
            'result': True
        }
        return render(request,'index.html',context=d)
    except:
        d={
            'error': True,
            'result': False
        }
        return render(request,'index.html',context=d)