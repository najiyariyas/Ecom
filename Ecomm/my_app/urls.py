from django.urls import path
from my_app import views

urlpatterns=[
   path('',views.home, name='home'),
   path('products',views.pro,name='pro'),
   path('new',views.new, name='new'),
   path('Ecom',views.home,name='home'),
   path('add',views.add,name='add_product'),
   path('delete/<int:pro_id>',views.delete_product,name='delete'),
   path('edit/<int:pro_id>',views.edit,name='delete'),
   path('search',views.search,name='search'),
   path('home',views.home,name='home'),
   path('signup',views.signup,name='signup'),
   path('signin',views.signin,name='signin'),
   path('signout',views.signout,name='signout'),
   path('cart/', views.view_cart, name='view_cart'),
   path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
   path('product/<int:product_id>/', views.product_detail, name='product_detail'),
   path('favourite',views.cache_product_view,name='favourite')
]