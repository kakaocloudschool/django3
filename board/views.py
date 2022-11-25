from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from board.models import Hpadata

# 로그인 시 처음 보이는 페이지
def list(request):
    hpadata = Hpadata.objects.all()
    context = {'hpadatas': hpadata}
    return render(request, 'index.html', context)

def popup(request):
    print("hello")
    return render(request, 'addschedule.html')

@login_required(login_url='/user/login')
def delete(request, bid):
    hpadata = Hpadata.objects.get(id=bid)
    #if request.user != post.writer:
    #    return redirect('/board/read/'+str(bid))
    hpadata.delete()
    return redirect('/board/list')


""" def read(request, bid):
    post = Post.objects.get(id=bid)
    context = {'post': post}
    return render(request, 'board/read.html', context) """

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