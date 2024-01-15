"""mavtrackbe URL Configuration"""
from api.views import TrainingCategoryList, TrainingGoalList, FunFactList, DailyHintList, \
    RecommendedExerciseList, TrainingLevelList, PromptsEncouragementList, \
    UpdateTrainingSchedule, TrainingPreferenceCreate

from django.contrib import admin
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', TrainingCategoryList.as_view(), name='training-category-list'),
    url(r'^api/customers/$', views.customer_list),
    url(r'^api/customers/(?P<pk>[0-9]+)$', views.getCustomer),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('fun-facts/', FunFactList.as_view(), name='fun-fact-list'),
    path('daily-hints/', DailyHintList.as_view(), name='daily-hint-list'),
    path('recommended-exercises/', RecommendedExerciseList.as_view(), name='recommended-exercise'),
    path('prompts-encouragement/', PromptsEncouragementList.as_view(), name='prompts-encouragement'),
    path('training-categories/', TrainingCategoryList.as_view(), name='training-category-list'),
    path('training-goals/', TrainingGoalList.as_view(), name='training-goal-list'),
    path('training-levels/', TrainingLevelList.as_view(), name='training-level-list'),
    path('training-preferences-create/', TrainingPreferenceCreate, name='training-preference-create'),
    # Get user and list training plans
    url(r'^training-preferences/$', views.TrainingPreferenceList, name='training-preference-list'),
    url(r'^training-preferences/(?P<pk>[0-9]+)$', views.getTrainingPreferences, name='training-preference-delete'),
    # Get user and list schedule
    url(r'^training-schedules/$', views.TrainingScheduleAll, name='training-schedule-create'),
    path('training-schedules/<int:pk>/update/', UpdateTrainingSchedule.as_view(), name='training-schedule-update'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<str:uidb64>/<str:token>/', views.ResetPasswordView.as_view(), name='reset-password'),
    path('rest-auth/', include('rest_auth.urls')),
]
