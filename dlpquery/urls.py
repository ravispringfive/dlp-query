from django.conf.urls import url
from dlpquery import views

urlpatterns = [
    url(r'^api/dlpquery-booking$', views.dlpquery_booking),
    url(r'^api/dlpquery-custom-object$', views.dlpquery_custom_object)
]
