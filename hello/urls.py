from django.urls import path
from .views import packageHealthView, packageView

urlpatterns = [
    path(
        "package/health/<str:package_name>/<str:version>",
        packageHealthView,
        name="package_health",
    ),
    path("package/releases/<str:package_name>", packageView, name="package_view"),
]
