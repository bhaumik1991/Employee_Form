from django.urls import path
from emp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.profile, name="employee_form"),
    path('emp/', views.preview, name="employee_list"),
    path('emp/<int:pk>', views.deleteEmployee, name='profile'),
]

if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


