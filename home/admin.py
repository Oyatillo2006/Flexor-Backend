from django.contrib import admin

from .models import About, Team, Portfolio, Service, Card, Post, \
    News, Contact, Partner, Support, Category, Question, \
    Image_portfolio_details, Price

admin.site.register([
    About, Team, Portfolio, Service, Card, Post,
    News, Contact, Partner, Support, Category, Question,
    Image_portfolio_details, Price
])