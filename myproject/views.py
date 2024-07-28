from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'chotu'.capitalize(),'role':'villain'}
    return render(request,'index.html',params)
    
def about(request):
    return HttpResponse("<H2>Chotu is a Ferocious Boy</H2> <button><a href='/'>Go Back</a></button>")
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    ucase=request.POST.get('ucase','off')
    nlr=request.POST.get('nlr','off')
    esr=request.POST.get('esr','off')
    if removepunc=="on":
        analyzed=''
        puncs='''!()-[]{};:'"'\',<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in puncs:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations',"analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,"analyze.html",params)
    if ucase=='on':
        djtext=djtext.upper()
        analyzed=djtext
        params={'purpose':'Uppercase',"analyzed_text":analyzed}
        djtext=analyzed
        # return render(request,"analyze.html",params)
    if(nlr=='on'):
        analyzed=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'Remove New Lines','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,"analyze.html",params)
    if(esr=='on'):
        analyzed=''
        for i,char in enumerate(djtext):
            if not(djtext[i]==' ' and djtext[i+1]==' '):
                analyzed=analyzed+djtext[i]
        params={'purpose':'Extra space Remover','analyzed_text':analyzed}

        return render(request,"analyze.html",params)
    if((esr=='off' and nlr=='off') and (removepunc=='off' and ucase=='off')):
        return HttpResponse("Error")
    return render(request,'analyze.html',params)
    

