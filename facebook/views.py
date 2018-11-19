from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Comment
# Create your views here.

def play(request):
    return render(request, 'play.html')


count = 0
def play2(request):
    kimhoekwang = '김회광'
    age = 35
    diary=['11월2일 그를 봤다','벌써4번째 봤다','그도 나란 사람을 좋게 생각한다','여기서 더 욕심내면 안된다']

    global count
    count = count + 1

    if age > 19:
        status = '성인'

    else:
        status = '청소년'

    return render(request, 'play2.html' , {'name': kimhoekwang, 'cnt': count, 'age':status, 'diary':diary})

def event(request):

    kimhoekwang = '김회광'
    age = 35


    global count
    count = count + 1

    if age > 19:
        status = '성인'

    else:
        status = '청소년'

    if count is 7:
        lottery = '당첨!'

    else:
        lottery = '꽝...'


    return render(request, 'event.html',{'name': kimhoekwang, 'cnt': count, 'age':status, 'lottery':lottery})

def warn(request):
    return render(request, 'warn.html')

def fail(request):
    return render(request, 'fail.html')

def help(request):
    return render(request, 'help.html')

def newsfeed(request):
    articles = Article.objects.all()

    return render(request, 'newsfeed.html',{'articles':articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':  # new comment
        Comment.objects.create(
            article=article,
            author=request.POST['author'],
            text=request.POST['text'],
            password=request.POST['password']
        )

        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html',{'feed':article})

def new_feed(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            author=request.POST['author'],
            title = request.POST['title'],
            text = request.POST['content'],
            password = request.POST['password']
        )

    return render(request, 'new_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'remove_feed.html', {'feed': article})


def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article.author = request.POST['author']
        article.title = request.POST['title']
        article.text = request.POST['content']
        article.save()
        return redirect(f'/feed/{ article.pk }')

    return render(request, 'edit_feed.html', {'feed': article})




