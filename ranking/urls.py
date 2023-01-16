from django.urls import path

from .views import DevelopersListView

app_name = 'ranking'

urlpatterns = [
    path('', DevelopersListView.as_view(), name='ranking')
]
