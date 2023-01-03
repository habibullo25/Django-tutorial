from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path("",views.Home.as_view(),name='home'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.Category.as_view(), name='category'),
    path('add-page',views.AddStatus.as_view(),name='add_status'),
    path('about/',views.about,name='about'),
    path('login/',views.LoginUser.as_view(),name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.RegisterUser.as_view(),name='register'),
]
