from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from . import util
import  markdown2
from markdown2 import Markdown
import re
import numpy as np


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "pages":"All Pages"
    })
def index1(request,name):
    return render(request,"encyclopedia/editpage.html",{'title':name,"string":Markdown().convert(util.get_entry(name))})

def search(request):
    name=request.POST.get("q")
    li=[]
    if name in util.list_entries():
        return HttpResponseRedirect(reverse("encyclopedia:index1", kwargs={"name":name}))
    else:
        pattern=re.compile(name.lower())
        for word in util.list_entries():
            if pattern.search(word.lower()):
                li.append(word)
        if len(li)==0:
            return HttpResponse("<h1>No result found</h1>")
        else:
            return render(request,"encyclopedia/index.html", {
                "entries":li,"pages":"Search Result" })
def mywords(request):
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("text")
        if title in util.list_entries():
            return HttpResponse("<h1>page have the same title</h1>")
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:index1", kwargs={"name":title}))
    else:
        return render(request,"encyclopedia/mywords.html")

def random(request):
    list1=[]
    for i in util.list_entries():
        list1.append(i)
    ran=np.random.randint(0,len(list1))
    val=list1[ran]
    return HttpResponseRedirect(reverse("encyclopedia:index1", kwargs={"name":val}))

def edit(request,name):
    if request.method=="POST":
        content=request.POST.get("text")
        util.save_entry(name, content)
        return HttpResponseRedirect(reverse("encyclopedia:index1", kwargs={"name":name}))



    else:
        return render(request,"encyclopedia/edit.html",{"title":name,"content":util.get_entry(name)})
