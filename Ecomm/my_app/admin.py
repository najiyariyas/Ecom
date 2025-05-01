from django.contrib import admin
from my_app.models import Category,Product,Orders,BestSellers,NewRelease
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(BestSellers)
admin.site.register(NewRelease)


