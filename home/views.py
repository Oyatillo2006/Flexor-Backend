from django.shortcuts import render
from .models import Card, About, News, Partner, \
    Service, Post, Support, Portfolio, Image_portfolio_details, \
    Team, Price, Question

def home(request):
    data = {
        "cards": Card.objects.all(),
        "about": About.objects.all(),
        "news": [],
        "partners": Partner.objects.all(),
        "services": Service.objects.all(),
        "posts": Post.objects.all(),
        "support": Support.objects.all(),
        "portfolio": Portfolio.objects.all(),
        "team": Team.objects.all(),
        "prices": Price.objects.all(),
        "questions": Question.objects.all(),
    }

    for i in About.objects.all():
        for n in News.objects.all():
            if i.id == n.about.id:
                data["news"].append(n)

    return render(request, "index.html", data)


def portfolio_details(request,id):
    data = {
        "photo": Portfolio.objects.get(id=id)
    }
    return render(request, "portfolio-details.html", data)