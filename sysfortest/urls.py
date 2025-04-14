from django.urls import path
from . import views

urlpatterns = [
    path("", views.first, name="index"),
    path("test",views.test, name="test"),
    path("api",views.api, name="api"),
    path("t", views.t, name="d"),
    path("reg", views.registration, name="s"),
    path("primeri",views.primer_ex),
    path("words",views.words_test),
    path("api/<int:number>", views.api),
    path("profile", views.profile),
    path("api/results", views.results_sender),
    path("leaderboard",views.leaderboard)


]

