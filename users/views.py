from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User
from users.serializers import RegisterSerializer


@api_view(['POST'])
def register_user(request):
    
    if(request.method == 'POST'):
        serializers = RegisterSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer


@api_view(['POST'])
def logout_by_blacklist(request):
    if(request.method == 'POST'):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("Successful Logout", status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def check_user(request):
    user_authenticated = False
    if request.user.is_authenticated:
        user_authenticated = True
        data= { 'is_authenticated': user_authenticated, 'user_id': request.user.id}
        return Response(data, status=status.HTTP_200_OK)
    data= { 'is_authenticated': user_authenticated}
    return Response(data, status=status.HTTP_401_UNAUTHORIZED)