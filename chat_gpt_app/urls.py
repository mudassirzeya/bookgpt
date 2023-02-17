from django.urls import path
from .views import search_page_gpt
urlpatterns = [
    path('', search_page_gpt, name='search_gpt_page'),
]
