from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return HttpResponse('<h1>Page Accueil</h1>')


def registration(request):
    return HttpResponse('<h1>Inscription</h1> <p>Inscrivez-vous</p>')


def flow(request):
    return HttpResponse('<h1>Flux</h1>')


def subscription(request):
    return HttpResponse('<h1>Abonnements</h1>')


def ticket_creation(request):
    return HttpResponse('<h1>Creer un ticket</h1>')


def critical_creation_no_answering_ticket(request):
    return HttpResponse('<h1>Creer une critique (pas en reponse au ticket</h1>')


def critical_creation_answering_ticket(request):
    return HttpResponse('<h1>Creer une critique (en reponse au ticket</h1>')


def own_post_view(request):
    return HttpResponse('<h1>Voir vos propres posts</h1>')


def critical_modification(request):
    return HttpResponse('<h1>Modifier votre propre critique</h1>')


def ticket_modification(request):
    return HttpResponse('<h1>Modifier votre propre ticket</h1>')
