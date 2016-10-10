from django.conf.urls import include, url
from django.views.generic import TemplateView

from students.views import ListCreateStudent, GetUpdateStudent, StudentSearch
from classes.views import ListCreateClass, GetUpdateClass

urlpatterns = [
    # Web App
    url(r'^$', TemplateView.as_view(template_name="app/index.html"), name='index'),

    # API Routes
    url(r'^api/v1/', include([
        # Student Routes
        url(r'^students/?$', ListCreateStudent.as_view(), name='list_create_student'),
        url(r'^students/(?P<pk>[0-9]+)/?$', GetUpdateStudent.as_view(), name='get_update_student'),
        url(r'^students/search/?$', StudentSearch.as_view(), name='student_search'),
        # Class Routes
        url(r'^classes/?$', ListCreateClass.as_view(), name='list_create_class'),
        url(r'^classes/(?P<pk>[0-9]+)/?$', GetUpdateClass.as_view(), name='get_update_class'),
    ])),
]