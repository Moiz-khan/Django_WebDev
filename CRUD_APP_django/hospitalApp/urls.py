from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("Home/", views.FormRegister, name="Home"),
    path("views/", views.displayData,name="views"),
    path("updatingInfo/", views.updateInfo,name="updatingInfo"),
    path("updateRecord/<int:id>", views.updateRecord,name="updateRecord"),
    path("edit/<int:id>", views.editData, name="edit")
    # path("updatecustData/<int:id>", views.tuka, name="updateData")

]