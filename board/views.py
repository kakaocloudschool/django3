from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from board.models import Appcreate

# 로그인 시 처음 보이는 페이지
def list(request):
    appcreate = Appcreate.objects.all()
    context = {'appcreates': appcreate}
    return render(request, 'index.html', context)

def appcreate(request):
    print("hello")
    return render(request, 'appcreate.html')

def appdistribute(request):
    print("hello")
    return render(request, 'appdistribute.html')

def appupdate(request):
    print("hello")
    return render(request, 'appupdate.html')

def apphistory(request):
    print("hello")
    return render(request, 'apphistory.html')

#@login_required(login_url='/user/login')
def delete(request, bid):
    appcreate = Appcreate.objects.get(id=bid)
    appcreate.delete() # +
    return redirect('/board/list') # +
    
    # user 추가 시 응용
    #if request.user != post.writer:
    #    return redirect('/board/read/'+str(bid))
    #hpadata.delete()
    #return redirect('/board/list')


""" def read(request, bid):
    hpadata = Hpadata.objects.get(id=bid)
    context = {'hpadata': hpadata}
    return render(request, 'index.html', context) """

""" @login_required(login_url='/user/login')
def create(request):
    if request.method == "GET":
        postForm = PostForm()
        context = {'postForm': postForm}
        return render(request, "board/create.html", context)
    elif request.method == "POST":
        postForm = PostForm(request.POST)

        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.writer = request.user
            post.save()
        return redirect('/board/read/'+str(post.id)) """




""" @login_required(login_url='/user/login')
def update(request, bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/board/read/'+str(bid))

    if request.method=="GET":
        postForm = PostForm(instance=post)
        context = {'postForm': postForm}
        return render(request, "board/create.html", context)

    elif request.method=="POST":
        postForm = PostForm(request.POST ,instance=post)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
        return redirect('/board/read/'+str(bid))
 """