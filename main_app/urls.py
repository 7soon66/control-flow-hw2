from django.urls import path
from . import views


urlpatterns = [
path('',views.home, name='home'),
path('about/',views.about,name='about'),
path('donkeys/', views.donkey_index, name='index'),
path('donkeys/<int:donkey_id>',views.donkey_detail,name='detail'),
path('donkeys/create/', views.DonkeyCreate.as_view(), name="donkeys_create"),
# we are using the pk for update and delete
path('donkeys/<int:pk>/update', views.DonkeyUpdate.as_view(), name="donkeys_update"),
path('donkeys/<int:pk>/delete', views.DonkeyDelete.as_view(), name="donkeys_delete"),
# we are using the id for the adding 
path('donkeys/<int:donkey_id>/add_feeding',views.add_feeding,name="add_feeding"),

#CRUD for toys using cbvs
path('toys/',views.ToyList.as_view(),name='toys_index'),
path('toys/<int:pk>/', views.ToyDetail.as_view(),name="toys_detail"),
path('toys/create/', views.ToyCreate.as_view(),name="toys_create"),
path('toys/<int:pk>/update/',views.ToyUpdate.as_view(),name="toys_update"),
path('toys/<int:pk>/delete/',views.ToyDelete.as_view(),name="toys_delete"),
# Associate a Toy with a Donkey (M:M) 
path('donkeys/<int:donkey_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

# Unassociate a Toy from a Donkey (M:M) 
path('donkeys/<int:donkey_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
path('accounts/signup/', views.signup, name='signup'),
]