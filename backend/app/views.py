from datetime import datetime, timedelta

from django.utils import timezone
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .authentication import create_access_token, create_refresh_token, JWTAuthentication, decode_refresh_token
from .models import User, UserToken, Note
from .serializers import UserSerializer, NoteSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        if data.get('password') != data.get('password_confirm'):
            raise exceptions.APIException('Passwords don\'t match')

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if not user:
            raise exceptions.AuthenticationFailed('Invalid email')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid password')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        UserToken.objects.create(
            user_id=user.id,
            token=refresh_token,
            expired_at=timezone.now() + timedelta(days=7),
        )

        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'token': access_token,
        }
        return response


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        UserToken.objects.filter(user_id=request.user.id).all().delete()

        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message': 'Successfully logged out',
        }
        return response


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        user_id = decode_refresh_token(refresh_token)

        db_user_token = UserToken.objects.filter(
            token=refresh_token,
            user_id=user_id,
            expired_at__gt=datetime.utcnow(),
        )
        if not db_user_token:
            raise exceptions.AuthenticationFailed("Unauthenticated")

        access_token = create_access_token(user_id)
        return Response({'token': access_token})


class UserViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user.email)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class NoteViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def list(self, request, *args, **kwargs):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        title = request.data.get("title")
        text = request.data.get("text")
        note = Note.objects.create(user_id=request.user.id, title=title, text=text)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
