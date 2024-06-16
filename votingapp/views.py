from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

arr = ['Java','Python','C++','C','.NET','JavaScript','PHP','Swift','SQL','Ruby','Perl','MATLAB','Assemblylanguage','Delphi','Objective-C','Go']
cnt = dict()

def index(request):
    d = {
        'arr' : arr
    }
    return render(request,'index.html',context=d)

def getquerry(request):
    q = request.GET['languages']
    cnt[q] = cnt.get(q,0)+1
    dict = {
        'arr' : arr,
        'cnt' : cnt
    }
    return render(request,'index.html',context=dict)

def sortdata(req):
    global cnt
    cnt = dict(sorted(cnt.items(),key=lambda x:x[1],reverse=True))
    d = {
        'arr' : arr,
        'cnt' : cnt
    }
    return render(req,'index.html',context=d)