""" All the views related to admin"""

from rest_framework import status
from django.core.paginator import Paginator
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.learner import Learner
from ..models.admin import Admin
from ..models.course import Course
from ..serializers.learner import LearnerSerializer, LearnerUpdateSerializer
from ..serializers.course import CourseSerializer
from ..utils.jwt_utils import generate_token, get_user_from_request

@api_view(['POST', 'GET'])
def create_learner(request):
    """Get the list of learners or create a new learner"""

    if request.method == 'POST':
        serializer = LearnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Learner created successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        response = {
            'message':'Something went wrong',
            'error': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':

        user = get_user_from_request(request)
        # if token not passed or not valid
        if not user:
            response_data = {
                "message": "Not authenticated",
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        
        # If user not an admin, only admins can get the list of learners
        if not isinstance(user, Admin):
            response_data = {
                "message": "Not allowed",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)    
        
        queryset = Learner.objects.all()

        # Filter learners based on query string parameters
        first_name = request.query_params.get('firstName', None)
        last_name = request.query_params.get('lastName', None)
        email = request.query_params.get('email', None)
        phone_number = request.query_params.get('phoneNumber', None)
        is_active = request.query_params.get('isActive', None)

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)

        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)

        if email:
            queryset = queryset.filter(email__icontains=email)

        if phone_number:
            queryset = queryset.filter(phone_number__icontains=phone_number)

        if is_active:
            queryset = queryset.filter(is_active=is_active)
        
        paginator = Paginator(queryset, request.query_params.get('page_size', 10)) # Default page size is 10
        page = paginator.get_page(request.query_params.get('page', 1)) # Default page is 1
        

        serializer = LearnerSerializer(page, many=True)
        return Response({
            'meassage': 'Learners fetched',
            'count': paginator.count,
            'page_size': paginator.per_page,
            'page': page.number,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
@api_view(['GET', 'PUT', 'DELETE'])
def learner_details(request, id):
    '''
    GET: Return details of the user with the passed id
    PUT: Update the user info(request body with the info to be updated)
    DELETE: Delete the user
    '''
    user = get_user_from_request(request)
    # if token not passed or not valid
    if not user:
        response_data = {
            "message": "Not authenticated",
        }
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
    
    # A learner can not updateor get another learner's info
    if isinstance(user, Learner) and user.id != id:
        response_data = {
            "message": "Not allowed",
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)
    
    try:
        learner = Learner.objects.get(pk=id)
    except Learner.DoesNotExist:
        response_data = {
            "Message": "User not found"
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LearnerSerializer(learner)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        password = request.data.get('password')
        if password is not None:
            request.data['password'] = make_password(password)
        serializer = LearnerUpdateSerializer(learner, data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Details updated successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_202_ACCEPTED)
        response = {
            'message':'Something went wrong',
            'error': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        # If user not an admin, only admins can delete a learner
        if not isinstance(user, Admin):
            response_data = {
                "message": "Not allowed",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN) 
        learner.delete()
        response_data = {
            "message": "User deleted successfully"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
    
# login 
@api_view(['POST'])
def learner_login(request):
    '''This view handles learner login'''
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    user = None
    if not password or not email:
        return Response({
            "message": "email and password are required to login"
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = Learner.objects.get(email__iexact=email.lower())
    except Learner.DoesNotExist:
        pass
    if user and check_password(password, user.password) and user.is_active:
        token = generate_token(user)
        return Response({
            "message": "Login successful",
            "token": token
        }, status=status.HTTP_200_OK)
    if user and user.password and not user.is_active:
        return Response({
            "message": "account deactivated"
        }, status=status.HTTP_401_UNAUTHORIZED)
    return Response({
        "message": "Wrong credentials"
    }, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def register_for_course(request, lid, cid):
    """Register learner to a course"""

    user = get_user_from_request(request)
    # if token not passed or not valid
    if not user:
        response_data = {
            "message": "Not authenticated",
        }
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
    
    # Only a learn can register for course
    if not isinstance(user, Learner):
        response_data = {
            "message": "Not allowed",
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)
    
    try:
        learner = Learner.objects.get(pk=lid)
    except Learner.DoesNotExist:
        response_data = {
            "Message": "User not found"
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    
    try:
        course = Course.objects.get(pk=cid)
    except Course.DoesNotExist:
        response_data = {
            "Message": "Course not found"
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    
    learner.courses.add(course)

    response = {
        'message': 'Register successfully'
    }
    return Response(response)


@api_view(['GET'])
def get_learners_courses(request):
    """Get courses of a learner"""

    user = get_user_from_request(request)
    # if token not passed or not valid
    if not user:
        response_data = {
            "message": "Not authenticated",
        }
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
    
    # Only a learn can register for course
    if not isinstance(user, Learner):
        response_data = {
            "message": "Not allowed",
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)
    try:
        learner = Learner.objects.get(pk=user.id)
    except Learner.DoesNotExist:
        response_data = {
            "Message": "User not found"
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    courses = learner.courses.all()
    keyword = request.query_params.get('keyword', None)
    course_id = request.query_params.get('id', None)

    if keyword is not None:
        courses = courses.filter(course_name__icontains=keyword) | courses.filter(description__icontains=keyword)
    if course_id is not None:
        courses = courses.filter(id=course_id)
        
    paginator = Paginator(courses, request.query_params.get('page_size', 10)) # Default page size is 10
    page = paginator.get_page(request.query_params.get('page', 1)) # Default page is 1

    serializer = CourseSerializer(page, many=True)
    return Response({
        'message': 'Courses fetched',
        'count': paginator.count,
        'page_size': paginator.per_page,
        'page': page.number,
        'data': serializer.data
    }, status=status.HTTP_200_OK)
