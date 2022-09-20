"""organize URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from org_api.views import register_user, login_user
from org_api.views import (RoomView, EventView, ItemView,
                           CategoryView, OrganizerView, ItemDetailView, StatusView, LikeView)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'rooms', RoomView, 'room')
router.register(r'events', EventView, 'event')
router.register(r'items', ItemView, 'item')
router.register(r'categories', CategoryView, 'category')
router.register(r'organizers', OrganizerView, 'organizer')
router.register(r'item_details', ItemDetailView, 'item_detail')
router.register(r'status', StatusView, 'status')
router.register(r'likes', LikeView, 'like')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
