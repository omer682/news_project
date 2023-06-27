from . import views
from django.urls import path

urlpatterns = [
    path('', views.serve_home, name='home'),
    path('logout/', views.site_logout, name='logout'),
    path('test', views.test),
    path('login', views.site_login, name='login'),
    path('signup', views.serve_signup, name='signup'),
    path('user/update', views.serve_update_account, name='update_user'),
    path("display/user", views.test_display_users, name='display_users'),
    path("staff/user/update/<int:user_id>", views.serve_staff_edit_accounts, name='staffuseredit'),
    path('staff/post', views.add_post, name='posting'),
    path('sport', views.serve_sport, name='sport'),
    path('health', views.serve_health, name='health'),
    path('article/<int:article_id>', views.serve_article, name='article')
    ]