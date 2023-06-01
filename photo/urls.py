from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'photo'


urlpatterns = [
    # photoアプリへのアクセスはviewモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name = 'index'),
]