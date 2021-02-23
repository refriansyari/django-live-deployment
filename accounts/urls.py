from django.urls import path
from django.contrib.auth import views as auth_views
from . import accviews
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('signup/', accviews.SignUp.as_view(), name='signup'),
    path('<int:pk>/personal/', accviews.personal, name='personal'),
    path('<int:pk>/edit_accounts/', accviews.edit_account, name='edit-account'),
    
    path('<int:pk>/change_password/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html',success_url=reverse_lazy('accounts:change-password-done')), name='change-password'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='change-password-done'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html',success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete'),

    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


