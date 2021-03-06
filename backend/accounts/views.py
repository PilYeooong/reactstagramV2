from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import SignupSerializer, UserSerializer, SuggestionUserSerializer

User = get_user_model()


class SignupView(CreateAPIView):
    model = User
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny
    ]


class SuggestionListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = SuggestionUserSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.exclude(pk=self.request.user.pk)
        qs = qs.exclude(pk__in=self.request.user.followings.all())
        return qs


class ProfileView(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username=username, is_active=True)
        serializer = UserSerializer(user, context={'request': self.request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        print(dir(self.request))
        obj = get_object_or_404(User, username=self.request.user)
        return obj


# frontend로 부터 data를 받아와 follow 동작
@api_view(['POST'])
def user_follow(request):
    username = request.data['username']

    follow_user = get_object_or_404(User, username=username, is_active=True)
    request.user.followings.add(follow_user)
    follow_user.followers.add(request.user)
    return Response(status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def user_unfollow(request):
    username = request.data['username']

    unfollow_user = get_object_or_404(User, username=username, is_active=True)
    request.user.followings.remove(unfollow_user)
    unfollow_user.followers.remove(request.user)
    return Response(status.HTTP_204_NO_CONTENT)
