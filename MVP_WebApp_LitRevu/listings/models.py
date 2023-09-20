from django.db import models


class Ticket(models.Model):
    title = models.fields.CharField(max_length=128),
    description = models.fields.TextField(max_length=2048, blank=True),
    user = models.fields.models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                          on_delete=models.CASCADE),
    image = models.fields.models.ImageField(null=True,
                                           blank=True,
                                           upload_to=None,
                                           height_field=None,
                                           width_field=None,
                                           max_length=None),
    time_created = models.fields.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    user = models.fields.models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                          on_delete=models.CASCADE,
                                          related_name='following'),
    followed_user = models.fields.models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                                    on_delete=models.CASCADE,
                                                    related_name='followed_by')
    # class Meta ??????


class Review(models.Model):
    ticket = models.fields.models.ForeignKey(to=Ticket,
                                             on_delete=models.CASCADE),
    rating = models.fields.PositiveSmallIntegerField(max_length=1024,
                                                                   validators=[
                                                                       MinValueValidator(0),
                                                                       MaxValueValidator(5)
                                                                   ]),
    user = models.fields.models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                          on_delete=models.CASCADE),
    headline = models.fields.CharField(max_length=128),
    body = models.fields.TextField(max_length=8192),
    time_created = models.fields.DateTimeField(auto_now_add=True)


# class User(models.Model):
    # django.contrib.auth.models.User
