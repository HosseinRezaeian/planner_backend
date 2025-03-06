from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Note.api.views import NoteViewSet, FolderViewSet
from planner_bsckend.settings import SPACE_URL_SEPARATOR

# ایجاد Router
router = DefaultRouter()
router.register(r'', NoteViewSet)
router_folder = DefaultRouter()
router_folder.register(r'', FolderViewSet)


urlpatterns = [
    path(f'{SPACE_URL_SEPARATOR}/note/', include(router.urls)),
    path(f'{SPACE_URL_SEPARATOR}/folder/', include(router_folder.urls)),

]
