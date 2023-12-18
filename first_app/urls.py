from django.urls import path     
from . import views    # le .   indique que le fichier de vues(views.py) se trouve dans le même répertoire que ce fichier(urls.py)
urlpatterns = [
    #Redirecting
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    # **Bonus**
    path('blogs/json', views.json_method), 
]