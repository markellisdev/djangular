from django.conf.urls import url

from . import views

app_name = "quick"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^register$', views.register_user, name='register_user'),
    url(r'^products$', views.list_products, name='list_products'),
    url(r'^product$', views.add_product, name='add_product'),
]