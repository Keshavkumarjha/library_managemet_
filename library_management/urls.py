from unittest.mock import NonCallableMagicMock
from django.contrib import admin
from django.urls import path,include
from account.views import Dashbord, LoginView,Allbook,delete,book_update,Createbook,user_logout
from account.views import RegisterView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('delete/<int:id>',delete,name='delete'),
    path('dashbord',Allbook.as_view(),name='dashbord'),
    path('book_update/<int:id>',book_update,name='book_update'),
    path('create-book',Createbook,name='create-book'),
    path('logout',user_logout,name='logout'),
]