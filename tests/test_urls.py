from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import TrainingPreferenceList, TrainingPreferenceCreate, TrainingScheduleAll

# Checking the Urls are going to the right view
class TestUrls(SimpleTestCase):

    # Training Plan Page
    def test_training_plan_url_is_resolved(self):
        url = reverse('training-preference-list')
        print(resolve(url))
        self.assertEqual(resolve(url).func, TrainingPreferenceList)

    # Training Preference Page
    def test_training_preference_url_is_resolved(self):
        url = reverse('training-preference-create')
        print(resolve(url))
        self.assertEqual(resolve(url).func, TrainingPreferenceCreate)

    # Training Schedule Page
    def test_training_schedule_url_is_resolved(self):
        url = reverse('training-schedule-create')
        print(resolve(url))
        self.assertEqual(resolve(url).func, TrainingScheduleAll)
