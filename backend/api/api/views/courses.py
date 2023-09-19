"""All the views related to Course model"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

from ..models.course import Course
from ..models.course_material import CourseMaterial
from ..serializers.course import CourseSerializer
from ..serializers.course_material import CourseMaterialSerializer


@api_view(['GET', 'POST'])
def course_list(request):
    """Create a course or get the list of courses with filters and pagination"""
    print('Called course view')

    if request.method == 'GET':
        courses = Course.objects.all()
        print(request.method)

        keyword = request.query_params.get('keyword', None)

        if keyword is not None:
            courses = courses.filter(course_name__icontains=keyword) | courses.filter(description__icontains=keyword)
        
        paginator = Paginator(courses, request.query_params.get('page_size', 10)) # Default page size is 10
        page = paginator.get_page(request.query_params.get('page', 1)) # Default page is 1

        serializer = CourseSerializer(page, many=True)
        return Response({
            'count': paginator.count,
            'page_size': paginator.per_page,
            'page': page.number,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        print('Called post course')
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

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
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
            'message': "Course updated",
            'data': serializer.data
        }
            return Response(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        course.delete()
        response_data = {
            "message": "Course deleted successfully"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def course_material_list(request, id):
    """Add a course material to a course or get the list of courses material with filters and pagination"""

    print('called course_material_list')
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

        if title is not None:
            materials = materials.filter(name__icontains=title)
        if author is not None:
            materials = materials.filter(name__icontains=author)
        if source is not None:
            materials = materials.filter(name__icontains=source)
       
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
        print('called post')
        serializer = CourseMaterialSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print('valid')
            serializer.validated_data['course'] = course
            serializer.save()
            response = {
                'message': 'Course material added successfully',
                'data': serializer.data,
            }
            print(serializer.data)
            return Response(response, status=status.HTTP_201_CREATED)
        

