from django.urls import path

from .views import (ClientListView, ClientCreateView,
                    ClientUpdateView, ClientDeleteView,
                    MessageListView)

from .views import (NewsletterListView, NewsletterCreateView,
                    NewsletterUpdateView, NewsletterDeleteView)

urlpatterns = [
    path("clients/list/", ClientListView.as_view()),
    path("clients/create/", ClientCreateView.as_view()),
    path("clients/<int:id>/update", ClientUpdateView.as_view()),
    path("clients/<int:id>/delete", ClientDeleteView.as_view()),

    path("newsletter/list", NewsletterListView.as_view()),
    path("newsletter/create", NewsletterCreateView.as_view()),
    path("newsletter/<int:id>/update", NewsletterUpdateView.as_view()),
    path("newsletter/<int:id>/delete", NewsletterDeleteView.as_view()),

    path("messages/stats/<int:id>", MessageListView.as_view())
]

