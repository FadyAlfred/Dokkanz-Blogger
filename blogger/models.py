from django.db import models
from . import hashing


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    @staticmethod
    def register(user_name, password, email_address):
        user = User(
            username=user_name,
            password=password,
            email=email_address
        )
        user.save()
        return user

    @staticmethod
    def login(email, password):
        if User.check_email(email):
            user = User.check_email(email)
            hashed = user.password
            if hashing.Hashing().valiedPassword(email, password, hashed):
                return user

    @staticmethod
    def check_username(username):
        try:
            user = User.objects.get(
                username=username
            )
        except User.DoesNotExist:
            user = None
        return user

    @staticmethod
    def check_email(email):
        try:
            user = User.objects.get(
                email=email
            )
        except User.DoesNotExist:
            user = None
        return user


class Post(models.Model):
    username = models.CharField(max_length=100)
    post_body = models.TextField(max_length=5000)

    @staticmethod
    def add_post(username, body):
        post = Post(
            username=username,
            post_body=body,
        )
        post.save()
        return post

    @staticmethod
    def find_post(post_id):
        try:
            post = Post.objects.get(
                id=post_id
            )
        except Post.DoesNotExist:
            post = None
        return post

    @staticmethod
    def edit_post(id, body):
        post = Post.find_post(id)
        post.post_body = body
        post.save()
        return post

    @staticmethod
    def delete_post(id):
        post = Post.find_post(id)
        post.delete()
        return True

    @staticmethod
    def get_all():
        posts = Post.objects.all().order_by('-id')
        return posts
