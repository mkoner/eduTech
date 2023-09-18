""" All the views related to admin"""

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

from ..models.admin import Admin
from ..serializers.admin import AdminSerializer

@api_view(['POST'])
def admin_login(request):
    """Admin login"""

    email = request.data.get('email', None)
    password = request.data.get('password', None)
    user = None
    if not password or not email:
        return Response({'Message': 'email and password are required to login'}, 
                        status= status.HTTP_400_BAD_REQUEST)
    try:
        user = Admin.objects.get(email=email)
    except Admin.DoesNotExist:
        pass
    if user and user.password == password and user.is_active:
        return Response({
            'message': 'Successfull login',
            'user': user.id,
        })
    if user and user.password == password and not user.is_active:
        return Response({
            'Message': 'account desactivated',
        }, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'Message': 'Wrong credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'POST'])
def admin_list(request):
    """Get the list of admins or post an admin"""

    if request.method == 'GET':
        admins = Admin.objects.all()

        first_name = request.query_params.get('firstName')
        last_name = request.query_params.get('lastName')
        email = request.query_params.get('email')
        phone_number = request.query_params.get('phoneNumber')
        is_active = request.query_params.get('isActive')

        if first_name is not None:
            admins = admins.filter(first_name__icontains=first_name)

        if last_name is not None:
            admins = admins.filter(last_name__icontains=last_name)

        if email is not None:
            admins = admins.filter(email__icontains=email)

        if phone_number is not None:
            admins = admins.filter(phone_number__icontains=phone_number)

        if is_active is not None:
            admins = admins.filter(is_active=is_active)

        paginator = Paginator(admins, request.query_params.get('page_size', 10)) # Default page size is 10
        page = paginator.get_page(request.query_params.get('page', 1)) # Default page is 1

        serializer = AdminSerializer(page, many=True)
        return Response({
            'count': paginator.count,
            'page_size': paginator.per_page,
            'page': page.number,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def admin_detail(request, id):
    """ Get an admin details, update an admin and delete an admin"""

    try:
        admin = Admin.objects.get(pk=id)
    except Admin.DoesNotExist:
        response_data = {
            "message": "User not found"
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdminSerializer(admin)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AdminSerializer(admin, data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
            'message': "Admin updated",
            'data': serializer.data
        }
            return Response(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        admin.delete()
        response_data = {
            "message": "Admin deleted successfully"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
