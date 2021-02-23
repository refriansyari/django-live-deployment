from django.urls import path
from .dashboardviews import dashboard, overview, preprocessing, processing, validation, visualization, profile, edit_profile

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('<int:pk>/profile/',profile,  name='profile'),
    path('<int:pk>/edit_profile/',edit_profile,  name='edit_profile'),  
    path('overview/',overview,  name='overview'),
    path('preprocessing/',preprocessing,  name='preprocessing'),
    path('processing/',processing,  name='processing'),
    path('validation/',validation,  name='validation'),
    path('visualization/',visualization,  name='visualization'),


    # path('<int:pk>/update/',UserUpdateView.as_view(template_name='dashboard/user_update.html'), name='user_update'),
    # path('files/upload/', dashboardviews.file_upload,  name='file_upload'),
    # path('files/upload/<int:pk>', dashboardviews.delete_file, name='delete_file'),
    
]