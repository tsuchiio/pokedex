from django.urls import path
from . import views

app_name='pokebook'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path("dex/",views.PokedexView.as_view(),name='pokedex'),
    path("post/",views.PokepostView.as_view(),name='pokepost'),
    path("post_done",views.PokepostSuccess.as_view(),name='pokesuccess'),
    path("post/<int:pk>/delete/",views.PokeDeleteView.as_view(),name='pokedelete'),
    path("poke-detail/<int:pk>/", views.PokeDetail.as_view(), name="pokedetail"),
    path("poke-detail/<int:pk>/edit/",views.PokeUpdata.as_view(),name="pokeedit"),
    path('mypage/', views.PokeMypageView.as_view(), name = 'pokemypage'),
    path("FAQs/",views.ContactView.as_view(),name="poke_contact"),
    path("FAQs_success",views.ContactSuccess.as_view(),name='contact_success'),
]
