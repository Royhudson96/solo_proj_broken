from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create', views.create_user),
    path('user/success', views.dashboard),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('user/account/<int:user_id>', views.account),
    path('user/contentcreator/<int:user_id>', views.content_creator),
    path('user/createportfolio', views.create_portfolio),
    path('user/update/pic', views.profile_pic_update),
    path('user/update/info/<int:user_id>', views.personal_info),
    path('user/addcart/<int:user_id>', views.add_to_cart),
    path('user/viewcart', views.view_cart),
    path('user/removecart/<int:line_id>', views.remove_from_cart),
    path('user/checkout', views.checkout),
    path('user/media/<int:user_id>', views.media)
]