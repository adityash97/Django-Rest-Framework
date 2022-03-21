from django.urls import path
from .views import home,create,update,delete


urlpatterns = [
    path("",home,name="user-input-register"),
    path("profile/", create, name="product-create"),
    path("<int:pk>/update/",update,name="product-update"),
    path("<int:pk>/delete/", delete, name="product-delete")

]
