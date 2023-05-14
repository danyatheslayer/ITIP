from .models import Article
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def archive(request):
    return render(request, "archive.html", {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, "article.html", {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {"text": request.POST["text"], "title": request.POST["title"]}
        # в словаре form будет храниться информация, введенная пользователем
        if form["title"] in Article.objects.all().values_list("title", flat=True):
            # проверка на уникальность названия
            form["errors"] = "Статья с таким названием уже есть"
            return render(request, "create_post.html", {"form": form})
        elif form["text"] and form["title"]:
            # если поля заполнены без ошибок
            Article.objects.create(
                text=form["text"], title=form["title"], author=request.user
            )
            print(form["title"])
            return redirect("get_article", article_id=Article.objects.last().id)
        else:
            # если введенные данные некорректны
            form["errors"] = "Не все поля заполнены"
            return render(request, "create_post.html", {"form": form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, "create_post.html", {})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("/")

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})