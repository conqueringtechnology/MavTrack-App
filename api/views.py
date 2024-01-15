from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_auth.views import PasswordResetView
from rest_framework.views import APIView

from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.views.decorators.cache import never_cache
from .serializers import ForgotPasswordSerializer
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


# Fun Exercise Facts
class FunFactList(generics.ListCreateAPIView):
    queryset = FunFact.objects.all()
    serializer_class = FunFactSerializer
    permission_classes = (AllowAny,)


# Daily Hints
class DailyHintList(generics.ListCreateAPIView):
    queryset = DailyHint.objects.all()
    serializer_class = DailyHintSerializer
    permission_classes = (AllowAny,)


# Recommended Exercise
class RecommendedExerciseList(generics.ListCreateAPIView):
    queryset = RecommendedExercise.objects.all()
    serializer_class = RecommendedExerciseSerializer
    permission_classes = (AllowAny,)


# Customer Prompt of Encouragement
class PromptsEncouragementList(generics.ListCreateAPIView):
    queryset = PromptsEncouragement.objects.all()
    serializer_class = PromptsEncouragementSerializer
    permission_classes = (AllowAny,)


# Training Categories - Get
class TrainingCategoryList(generics.ListCreateAPIView):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer


# Training Goals - Get
class TrainingGoalList(generics.ListCreateAPIView):
    queryset = TrainingGoal.objects.all()
    serializer_class = TrainingGoalSerializer
    permission_classes = (AllowAny,)


# Training Goals - Detail
class TrainingGoalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingGoal.objects.all()
    serializer_class = TrainingGoalSerializer
    permission_classes = (AllowAny,)


# Training Levels - Get
class TrainingLevelList(generics.ListCreateAPIView):
    queryset = TrainingLevel.objects.all()
    serializer_class = TrainingLevelSerializer
    permission_classes = (AllowAny,)


# Training Preferences - Get (preferences, and preferences with user) & Create
@csrf_exempt
@api_view(['GET', 'POST'])
def TrainingPreferenceList(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        preference = TrainingPreference.objects.all()
        serializer = TrainingPreferenceGetSerializer(preference, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = TrainingPreferenceCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Training Preferences - Get, Update, & Delete
@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getTrainingPreferences(request, pk):
    try:
        preferences = TrainingPreference.objects.get(pk=pk, user=request.user)
    except TrainingPreference.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrainingPreferenceGetSerializer(preferences, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TrainingPreferenceCreateSerializer(preferences, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        preferences.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Training Preferences - Create
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def TrainingPreferenceCreate(request):
    serializer = TrainingPreferenceCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create Training Schedules
@csrf_exempt
@api_view(['GET', 'POST'])
def TrainingScheduleAll(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        schedules = TrainingSchedule.objects.all()
        serializer = TrainingScheduleGetSerializer(schedules, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = TrainingScheduleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update Training Schedule
class UpdateTrainingSchedule(APIView):
    def put(self, request, pk):
        try:
            schedule = TrainingSchedule.objects.get(pk=pk)
        except TrainingSchedule.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TrainingScheduleCreateSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Register User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Forgot Password
class ForgotPasswordView(PasswordResetView):
    @never_cache
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
            # Generate password reset token
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            # Build password reset URL
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f'https://lustrous-kheer-25cf4a.netlify.app/#/reset-password/{uidb64}/{token}/'
            # reset_url = f'http://localhost:8080/#/reset-password/{uidb64}/{token}/'
            # Send password reset email to user
            subject = 'Password Reset Request'
            message = f'Hi {user.username},\n\nPlease use the following link to reset your password:\n\n{reset_url}\n\nIf you did not request a password reset, please ignore this email.\n\nThanks,\nThe Example.com Team'
            from_email = 'mavtrackapp@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Reset Password
class ResetPasswordView(APIView):
    @never_cache
    def post(self, request, uidb64, token):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


# Customer
@csrf_exempt
@api_view(['GET', 'POST'])
def customer_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getCustomer(request, pk):
    """ Retrieve, update or delete a customer instance. """
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
