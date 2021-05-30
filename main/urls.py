from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('task', views.TaskView, basename='tasks')

urlpatterns = router.urls