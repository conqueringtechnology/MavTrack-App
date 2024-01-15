from .models import *
from django.contrib.auth import get_user_model, authenticate
from rest_framework_jwt.serializers import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers

User = get_user_model()


# Fun Exercise Facts
class FunFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunFact
        fields = ['id', 'fact']


# Daily Hints
class DailyHintSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyHint
        fields = ['id', 'hint']


# Recommended Exercise
class RecommendedExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedExercise
        fields = ['id', 'name', 'recommended']


# Customer Prompts of Encouragement
class PromptsEncouragementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptsEncouragement
        fields = '__all__'


# Training Categories
class TrainingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCategory
        fields = ['id', 'name', 'created_date', 'updated_date']


# Training Goals
class TrainingGoalSerializer(serializers.ModelSerializer):
    train_cat = TrainingCategorySerializer(many=True, read_only=True)

    class Meta:
        model = TrainingGoal
        fields = ['id', 'short_descr', 'long_descr', 'level', 'train_cat', 'user', 'created_date', 'updated_date']


# Training Levels
class TrainingLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingLevel
        fields = '__all__'


# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# Training Schedules - Get
class TrainingScheduleGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TrainingSchedule
        fields = '__all__'


# Training Schedule - Create
class TrainingScheduleCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TrainingSchedule
        fields = '__all__'


# Training Preference - Create
class TrainingPreferenceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingPreference
        fields = '__all__'


# Training Preferences - Get
class TrainingPreferenceGetSerializer(serializers.ModelSerializer):
    train_cat = TrainingCategorySerializer(read_only=True)
    train_goal = TrainingGoalSerializer(read_only=True)
    current_train_level = TrainingLevelSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = TrainingPreference
        fields = '__all__'

    # # Example of how to Print out what is being validated
    # def create(self, validated_data):
    #     print('Creating new TrainingTest object with data:', validated_data)
    #     training_test = TrainingPreference.objects.create(**validated_data)
    #     return training_test

    # def create(self, validated_data):
    #     print('Creating new TrainingPreference object with data:', validated_data)
    #     training_test = TrainingPreference.objects.create(
    #         name=validated_data['name'],
    #         train_cat=validated_data['train_cat'],
    #         user=validated_data['user']
    #     )
    #     print('Created new TrainingPreference object:', training_test)
    #     return training_test


# Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True, style={'input_type': 'password'},
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True,
                         'min_length': 6},
            'password2': {'write_only': True,
                          'min_length': 6}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Forgot Password
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('User with this email address does not exist')
        return value


# Reset Password
class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    token = serializers.CharField()
    uidb64 = serializers.CharField()

    def validate(self, data):
        try:
            uid = force_text(urlsafe_base64_decode(data['uidb64']))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError('Invalid token')

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, data['token']):
            raise serializers.ValidationError('Invalid token')

        return data

    def save(self):
        user = User.objects.get(pk=force_text(urlsafe_base64_decode(self.validated_data['uidb64'])))
        user.set_password(self.validated_data['password'])
        user.save()


# Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'cell_phone')
