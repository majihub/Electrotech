from django.urls import path
from eletrotechapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('products',views.products,name='products'),
    path('logout',views.logout,name='logout'),
    path('shoppingitems/<str:productitem>/',views.shoppingitems,name='shoppingitem'),
    path('additem/<int:id>',views.add_to_cart,name='additem'),
    path('mycart',views.mycart,name='mycart'),
    path('payment',views.payment,name='payment'),
    path('delete-cart-item/<int:id>',views.delete_cart_item,name='delete_cart_item'),
    path('update-cart/<int:id>/<str:op>',views.update_cart,name='update_cart'),
    path('add-to-fav/<int:id>',views.add_to_fav,name='add_to_fav'),
    path('favourites',views.my_favourites,name='favourites'),
    path('delete_item/<int:id>',views.delete_item,name='delete_item'),
    path('clear',views.clear,name='clear'),
]