from django.urls import path
from . import views


urlpatterns = [
path('',views.home, name='home'),
path('about/',views.about,name='about'),
path('donkeys/', views.donkey_index, name='index'),
path('donkeys/<int:donkey_id>',views.donkey_detail,name='detail'),
path('donkeys/create/', views.DonkeyCreate.as_view(), name="donkeys_create"),
path('donkeys/<int:pk>/update', views.DonkeyUpdate.as_view(), name="donkeys_update"),
path('donkeys/<int:pk>/delete', views.DonkeyDelete.as_view(), name="donkeys_delete"),
path('donkeys/<int:donkey_id>/add_feeding',views.add_feeding,name="add_feeding")
]