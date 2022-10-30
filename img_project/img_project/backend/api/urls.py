from rest_framework.routers import DefaultRouter
from backend.views.member import MemberViewSet
from backend.views.panel import PanelViewSet
from backend.views.question import QuestionViewset
from backend.views.student import studentViewSet
from backend.views.user import UserViewSet
from backend.views import *
from django.urls import path

router = DefaultRouter()


router.register(r"questions",QuestionViewset, "question-viewset")
router.register(r"members", MemberViewSet , "members-viewset")
router.register(r"panels",PanelViewSet, "panels-viewset")
router.register(r"students",studentViewSet, "applicant-viewset")
router.register(r"user", UserViewSet, "current-user-viewset")



urlpatterns = router.urls

