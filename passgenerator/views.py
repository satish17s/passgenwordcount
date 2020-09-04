from django.shortcuts import render
from django.http import HttpResponse
import random
import operator

# Create your views here.
def home(request):
    return render(request,'passgenerator/home.html')


def takepass(request):
    return render(request,'passgenerator/takepass.html')

def takecount(request):
    return render(request,'passgenerator/takecount.html')


def password(request):
    length=int(request.GET.get('length',12))
    character=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        character.extend(list('1234567890'))

    if request.GET.get('special'):
        character.extend(list('!@#$%&*()_'))

    thepassword=''
    for x in range(length):
        thepassword +=random.choice(character)

    return render(request,'passgenerator/password.html',{'password':thepassword})


def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()

    worddict={}
    for word in wordlist:
        if word in worddict:
            worddict[word] +=1

        else:
            worddict[word]=1

    sortedworddict=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'passgenerator/count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedworddict':sortedworddict})
