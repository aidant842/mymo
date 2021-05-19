from django.urls import path
from . import views

urlpatterns = [
    path('', views.estate_agents, name='estate_agents'),
    path('<name>/<int:profile_id>/', views.estate_agents_profile, name='estate_agents_profile'),
    path('contact_agent/', views.contact_agent, name='contact_agent'),
]