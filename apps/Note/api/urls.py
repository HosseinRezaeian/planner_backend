from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Note.api.views import NoteViewSet, FolderViewSet, NoteContentViewSet
from planner_bsckend.settings import SPACE_URL_SEPARATOR

# ایجاد Router
router = DefaultRouter()
router.register(r'', NoteViewSet)

router_folder = DefaultRouter()
router_folder.register(r'', FolderViewSet)

router_content = DefaultRouter()
router_content.register(r'', NoteContentViewSet)

urlpatterns = [
    path(f"{SPACE_URL_SEPARATOR}/folders/", include(router_folder.urls)),  # مدیریت پوشه‌ها
    path(f"{SPACE_URL_SEPARATOR}/folders/<str:folder>/notes/", include(router.urls)),  # مدیریت نوت‌های یک پوشه
    path(f"{SPACE_URL_SEPARATOR}/folders/<str:folder>/notes/<str:note>/content/", include(router_content.urls)),  # محتوای یک نوت خاص
]
