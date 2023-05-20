from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request, 'index.html')



def analyze(request):
    # fetching text from user
    text = request.POST.get('textarea','default')

    #fetching request of operation to be perform
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('fullcaps','off')
    newline = request.POST.get('newlineremover','off')
    space = request.POST.get('spaceremove','off')
    counttext = request.POST.get('counttext','off')

    #analysing the text

    #->            !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

    #defining purposes
    purpose = ""
    if removepunc == 'on': 
        analyzed = ""
        for char in text:
            if char not in string.punctuation:
                analyzed += char
        purpose  += ' Remove Punctuations'
        text = analyzed
        # return render(request,'analyze.html',params)
    
    if capitalize == 'on':
        analyzed = ""                                               #default
        analyzed = text.upper()
        
        purpose += ' Capitalization'
        text = analyzed
        # return render(request,'analyze.html',params)
    
    if newline == 'on':
        analyzed = ''
        for char in text:
            if char != '\n' and char != '\r':
                analyzed  += char
        purpose += ' New Line Remover'
        text = analyzed

        # return render(request,'analyze.html',params)
    
    if space == 'on':
        analyzed = ''
        for char in text:
            if char != ' ':
                analyzed  += char
        
        purpose += ' Space Remover'
        text = analyzed
        # return render(request,'analyze.html',params)
    
    if counttext == 'on':
        analyzed = """No. of Character in your text '""" + text +""" ' is """
        temp = ''
        for char in text:
            if char != ' ':
                temp += char
        analyzed += str(len(temp))
        purpose += ' Counting Character'
        text += " " + analyzed
        # return render(request,'analyze.html',params)

    params = {
        'purpose': purpose,
        'analyzed_text' : text
    }
    
    return render(request,'analyze.html',params)