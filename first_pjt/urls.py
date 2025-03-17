"""
URL configuration for first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

## urls.py: 요청이 들어왔을 때 views중에서 사용하면 좋을 법한 view를 찾아주는 역할

from django.contrib import admin
from django.urls import path
from first_app import views
from my_app import views as my_views # first_app이라는 app 폴더에서 views.py라는 파일을 불러온다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), #서버 주소에 index를 입력하면 views.index를 실행하게 해준다
    path('hello/', views.hello),
    path('lunch/', views.lunch),
    path('lotto/', views.lotto),
    #variable routing
    path('profile/<username>/', views.profile),
    path('cube/<int:number>', views.cube), #integer로 바꾸려면 int:을 앞에 붙이자
    path('articles/', views.articles),
    path('lotto2/', my_views.lotto2),
    path('profile2/<username>/', my_views.profile2),
    path('phone_books/', my_views.phone_books),
    path('god/<myname>/',my_views.god)
]
