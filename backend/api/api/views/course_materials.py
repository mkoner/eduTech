"""All the views related to Course_material model"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

from ..models.course import Course
from ..models.course_material import CourseMaterial
from ..serializers.course import CourseSerializer
from ..serializers.course_material import CourseMaterialSerializer, CourseMaterialUpdateSerializer

@api_view(['POST', 'GET'])
def create_course_material(request):
    ''' 
    This route creates a new course material 
    and returns list of course material
    '''
    if request.method == 'POST':
        serializer = CourseMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Course material uploaded successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        try:
            queryset = CourseMaterial.objects.all()
            title = request.query_params.get('title', None)
            author = request.query_params.get('author', None)
            source = request.query_params.get('source', None)
            id = request.query_params.get('id', None)

            if title:
                queryset = queryset.filter(title__icontains=title)

            if author:
                queryset = queryset.filter(author__icontains=author)

            if source:
                queryset = queryset.filter(source__icontains=source)
            
            if id:
                queryset = queryset.filter(id__icontains=id)

            if not queryset:
                return Response({
                    "message": "No data found"
                }, status=status.HTTP_404_NOT_FOUND)

            paginator = Paginator(queryset, request.query_params.get('page_size', 10)) # Default page size is 10
            page = paginator.get_page(request.query_params.get('page', 1)) # Default page is 1
        
            serializer = CourseMaterialSerializer(page, many=True)
            return Response({
                'count': paginator.count,
                'page_size': paginator.per_page,
                'page': page.number,
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(f'An error occurred: {e}')
            return Response({
                "error": "An error occured"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def get_course_material(request, id):
    ''' Get, Updates and delete a course material'''
    try:
        course_material = CourseMaterial.objects.get(pk=id)
    except CourseMaterial.DoesNotExist:
        response_date = {
            "error": "No course material found",
            "status_code": "404"
        }
        return Response(response_date, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CourseMaterialSerializer(course_material)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CourseMaterialUpdateSerializer(course_material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_date = {
                "message": "Course material updated successfully",
                "data": serializer.data
            }
            return Response(response_date, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        course_material.delete()
        response_data = {
            "message": "course material deleted successfully"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)