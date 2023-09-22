"""All the views related to Course model"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

from api.utils.jwt_utils import get_user_from_request

from ..models.course import Course
from ..models.admin import Admin
from ..models.course_material import CourseMaterial
from ..serializers.course import CourseSerializer, CourseUpdateSerializer
from ..serializers.course_material import CourseMaterialSerializer, CourseMaterialUpdateSerializer


@api_view(['GET', 'POST'])
def course_list(request):
    """Create a course or get the list of courses with filters and pagination"""

    if request.method == 'GET':
        courses = Course.objects.all()

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
    
    if request.method == 'POST':
        user = get_user_from_request(request)
        # if token not passed or not valid
        if not user:
            response_data = {
                "message": "Not authenticated",
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        
        # Only admin can create a course
        if isinstance(user, Admin) and user.id != id:
            response_data = {
                "message": "Not allowed",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)
        
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message':'Course created successfully',
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'message':'Something went wrong',
            'error': serializer.errors,
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, id):
    """ Get a course details, update an course or delete a course"""

    try:
        course = Course.objects.get(pk=id)
    except Course.DoesNotExist:
        response_data = {
            "message": "Course not found"
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        response = {
            'message': 'Course material fetched',
            'data': serializer.data
        }
        return Response(response)
    
    elif request.method == 'PUT':
        user = get_user_from_request(request)
        # if token not passed or not valid
        if not user:
            response_data = {
                "message": "Not authenticated",
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        
        # Only admin can update a course
        if isinstance(user, Admin) and user.id != id:
            response_data = {
                "message": "Not allowed",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)
        
        serializer = CourseUpdateSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
            'message': "Course updated",
            'data': serializer.data
            }
            return Response(response_data)
        response = {
        'message':'Something went wrong',
        'error': serializer.errors,
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user = get_user_from_request(request)
        # if token not passed or not valid
        if not user:
            response_data = {
                "message": "Not authenticated",
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        
        # Only admin can delete a course
        if isinstance(user, Admin) and user.id != id:
            response_data = {
                "message": "Not allowed",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)
        course.delete()
        response_data = {
            "message": "Course deleted successfully"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def course_material_list(request, id):
    """Add a course material to a course or get the list of courses material with filters and pagination"""

    course = None
    try:
        course = Course.objects.get(pk=id)
    except Course.DoesNotExist:
        response_data = {
            "message": "Course not found"
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        materials = course.course_materials.all()

        title = request.query_params.get('title')
        author = request.query_params.get('author')
        source = request.query_params.get('source')
        material_id = request.query_params.get('id')

        if title is not None:
            materials = materials.filter(title__icontains=title)
        if author is not None:
            materials = materials.filter(author__icontains=author)
        if source is not None:
            materials = materials.filter(source__icontains=source)
        if material_id is not None:
            materials = materials.filter(pk=material_id)
       
        paginator = Paginator(materials, request.query_params.get('page_size', 10)) # Default page size is 10
        page = paginator.get_page(request.query_params.get('page', 1)) # Default page is 1

        serializer = CourseMaterialSerializer(page, many=True)
        return Response({
            'count': paginator.count,
            'page_size': paginator.per_page,
            'page': page.number,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        user = get_user_from_request(request)
        # if token not passed or not valid
        if not user:
            response_data = {
                "message": "Not authenticated",
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        
        # Only admin can add a course material
        if isinstance(user, Admin) and user.id != id:
            response_data = {
                "message": "Not allowed",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)
        
        serializer = CourseMaterialSerializer(data=request.data)
        request.data['course'] = id
        if serializer.is_valid():        
            serializer.save()
            response = {
                'message': 'Course material added successfully',
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'message':'Something went wrong',
            'error': serializer.errors,
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
def course_material_detail(request, cid, cmid):
    """ Get a course_material details, update an course or delete a course_material"""

    user = get_user_from_request(request)
    # if token not passed or not valid only logged in users can access course materials
    if not user:
        response_data = {
            "message": "Not authenticated",
        }
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        course_material = CourseMaterial.objects.get(pk=cmid)
    except CourseMaterial.DoesNotExist:
        response_data = {
            "message": "Course material not found"
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseMaterialSerializer(course_material)
        response = {
            'message': 'Course material fetched',
            'data': serializer.data
        }
        return Response(response)
    
    elif request.method == 'PUT':        
        # Only admin can update a course material
        if isinstance(user, Admin) and user.id != id:
            response_data = {
                "message": "Not allowed",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)
        
        serializer = CourseMaterialUpdateSerializer(course_material, data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            'message': "Course material updated",
            'data': serializer.data
            }
            return Response(response)
        response = {
            'message':'Something went wrong',
            'error': serializer.errors,
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':

        # Only admin can delete a course material
        if isinstance(user, Admin) and user.id != id:
            response_data = {
                "message": "Not allowed",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)
        
        course_material.delete()
        response = {
            "message": "Course material deleted successfully"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)