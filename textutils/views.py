# I have created this file -Sanjh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Hello</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> This is a link</a>''')



def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # checkbox value 
    removepunc = request.POST.get('removepunc', 'Off')
    FULLCaps = request.POST.get('fullcaps', 'Off')
    newlinerem = request.POST.get('newlinerem', 'off')
    extraspacerem = request.POST.get('extraspacerem', 'off')
    
    # check which checkbox is on 
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
    
    if FULLCaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed

    if extraspacerem == "on":
        analyzed = ""
        for index, char in enumerate (djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
    
    if newlinerem == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        djtext = analyzed
    
    if (removepunc != "on" and FULLCaps != "on" and extraspacerem != "on" and newlinerem != "on"):
        return render(request, 'message.html')

    params = {'analyzed_text':djtext}
    return render(request, 'analyze.html', params)

    

def about(request):
    return render(request, 'about.html')