from django.contrib import admin
from django.urls import path
from api.views import DocumentView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/<str:n>',DocumentView.as_view()),
    path('upload/<str:name>', DocumentView.as_view())
]
