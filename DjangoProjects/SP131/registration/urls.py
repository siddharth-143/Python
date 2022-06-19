from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('profile/', login_required(views.ProfileTemplateView.as_view()), name='profile'),
]
