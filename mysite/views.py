from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("<h1>hello abhishek how are you doing</h1>")

def analyze(request):



    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    charcount = request.GET.get('charcount','off')

    
    
    #analyzed=djtext
    if (removepunc =='on'):

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
       
    
       
        for char in djtext :


            if char not in punctuations:
                analyzed = analyzed + " ".join(char)
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=='on'):
        
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "changed to upper", 'analyzed_text': analyzed}
        djtext = analyzed
       # return render(request,'analyze.html',params)

    if(newlineremover =='on'):
        analyzed =""
        for char in djtext:
            if char != "/n":
                analyzed = analyzed + char
        params = {'purpose': "remove new line", 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)

    if(charcount=='on'):

        analyzed = ""
        
        
       
        analyzed = djtext  +"is the string"  + "  "  +('there are {} characters' .format(len(djtext)))

        

        params = {'purpose': " count the char",'analyzed_text': analyzed}

        
    if(removepunc != "on" and newlineremover!="on" and charcount!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")   

    return render(request,'analyze.html',params)
        
        
        

        #return render(request,'analyze.html',params)


    #else:
       # return HttpResponse("error")
    




   
    
   #Get the text

   

#def removepunc(request):
    #djtext = request.GET.get('text','default')
    #print(djtext)
    #return HttpResponse("remove punc")
    

#def ex1(request):



   # s='''<h2> Navigation Bar <br> </h2>
   # <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    #<a href="https://www.facebook.com/"> Facebook </a> <br>
   # <a href="https://www.flipkart.com/"> Flipkart </a> <br>
   # <a href="https://www.hindustantimes.com/"> News </a> <br>
    #<a href="https://www.google.com/"> Google </a> <br>'''

    #return HttpResponse(s)
    
    

    
    