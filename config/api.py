from rest_framework import routers
from apiapp import views
from . import urls


router = routers.DefaultRouter()
router.register(r'Books',views.BooksViewSet, basename='books')
router.register(r'Lib-Users',views.LibuserViewSet)
router.register(r'Rent-Book',views.RentbookViewSet)
