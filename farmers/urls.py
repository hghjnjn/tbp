# farmers/urls.py
from django.urls import path
from .views import register_user, login_user, nearby_markets, choose_crop_type, display_prices ,home
from .views import choose_state

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_user, name='register'),
    path('<str:username>/choose-state/', choose_state, name='choose_state'),
    path('login/', login_user, name='login'),
    path('<str:username>/<str:state>/nearby-markets/', nearby_markets, name='nearby_markets'),
    path('<str:username>/<str:state>/<str:market>/choose-crop-type/', choose_crop_type, name='choose_crop_type'),
    path('<str:username>/<str:state>/<str:market>/<str:crop_type>/display-prices/', display_prices, name='display_prices'),
]

