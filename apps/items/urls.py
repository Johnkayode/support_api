from django.urls import path

from apps.items.views import ItemAPI


urlpatterns = [
    path('', ItemAPI.as_view(), name='create_item'),
    path('<int:item_id>/', ItemAPI.as_view(), name='retrieve_item'),
] 