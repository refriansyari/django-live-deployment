from django.urls import path
from .views import tutorial, product, contact, landing_page, aboutus, newsletter, privacy, terms

app_name = 'landing_page'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
    path('about-us/', aboutus, name='about-us'),
    path('tutorials/', tutorial, name='tutorial' ),
    path('privacy_policy/', privacy, name='privacy-policy' ),
    path('terms_of_service/', terms, name='terms-of-service' ),
    # path('news_letter/', newsletter, name='news-letter' ),
    

]