from django.urls import path, include
from logs import views as log_views
urlpatterns = [
    path('', log_views.ListLogsViewset.as_view()),
    path('<pk>/', log_views.LogViewset.as_view()),
]
