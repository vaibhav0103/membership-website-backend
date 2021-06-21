from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from users.serializers import RegisterSerializer, UserSerializer, ProfileSerializer
from courses.serializers import CourseSerializer
from courses.models import Course


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
@permission_classes([IsAuthenticated])
def user_details(request):    
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

# class ProfileAPI(APIView):    
#     def get(self, request, *args, **kwargs):
#         user = get_object_or_404(User, pk=kwargs['user_id'])
#         profile_serializer = ProfileSerializer(user.profile)
#         return Response(profile_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_user(request, *args, **kwargs):
    if request.method == 'POST':
        
        if request.user.is_authenticated:
            course_id = request.data.get('course_id')
            course = Course.objects.get(pk=course_id)
            current_user = request.user            
            if current_user.membership.pricing == course.pricing_tier or current_user.membership.pricing.price >= course.pricing_tier.price:
                print("Yes")
                current_user.profile.enrolled_courses.add(course)
                return Response(data="You have succesfully enrolled in course",status=status.HTTP_200_OK)
            return Response(data="You need to upgrade membership to access this course", status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_enrolled_courses(request):
    if request.method == 'GET':
        
        if request.user.is_authenticated:
            # course = Course.objects.get(pk=course_id)
            current_user = request.user            
            user_courses = current_user.profile.enrolled_courses.all()
            serializer = CourseSerializer(user_courses, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        #    return Response(data="You need to upgrade membership to access this course", status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_401_UNAUTHORIZED)