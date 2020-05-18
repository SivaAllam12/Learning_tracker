from django.urls import path
from . import views
 
app_name='learning_logs'

urlpatterns = [
    path('', views.home,name='home'),
    path('courses/',views.courses,name='courses'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('entrypage/<int:cid>',views.entrypage,name='entrypage'),
    path('entriespage',views.entries,name='entries'),
    path('delete_course/<int:cid>',views.deletecourse,name='delete_course'),
    path('addentry/<int:cid>',views.addentry,name='addentry'),
    ]