from django.http import HttpResponse
from django.shortcuts import render

import re
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = re.split(' |\.|\,',fulltext)
    while '' in wordlist:
        wordlist.remove('')

    print(wordlist)
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':sortedwords})
