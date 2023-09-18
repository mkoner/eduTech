""" All the views related to admin"""

from django.http import JsonResponse
from rest_framework import status
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.learner import Learner
from ..serializers.learner import LearnerSerializer, LearnerUpdateSerializer

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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
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
        serializer = LearnerUpdateSerializer(learner, data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Details updated successfully",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        learner.delete()
        response_data = {
            "message": "User deleted successfully"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)