from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="about/image")
    video = models.URLField()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=70)
    text = models.TextField()
    icon = models.CharField(max_length=20)
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Partner(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images/partner")

    def __str__(self):
        return self.name

class Service(models.Model):
    icon = models.CharField(max_length=70)
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title

class Post(models.Model):
    name = models.CharField(max_length=28)
    text = models.TextField()
    image = models.ImageField(upload_to="images/post")

    def __str__(self):
        return self.name

class Support(models.Model):
    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=30)
    docs = models.TextField()
    image = models.ImageField(upload_to="images/sepports")

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/Portfolio")

    def __str__(self):
        return self.name


class Image_portfolio_details(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to="images/Portfolio_details")

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images/Team")
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Price(models.Model):
    title = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()


    def __str__(self):
        return self.title

class Question(models.Model):
    ask = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.ask


class Contact(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    docs = models.CharField(max_length=100)
    docs_2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name



