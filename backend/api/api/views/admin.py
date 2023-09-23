""" All the views related to admin"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.contrib.auth.hashers import check_password, make_password

from ..models.admin import Admin
from ..serializers.admin import AdminSerializer, AdminUpdateSerializer
from ..utils.jwt_utils import generate_token, get_user_from_request

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
    if user and check_password(password, user.password) and user.is_active:
        token = generate_token(user)
        return Response({
            'message': 'Successfull login',
            'token': token,
        })
    if user and check_password(password, user.password) and not user.is_active:
        return Response({
            'Message': 'account desactivated',
        }, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'Message': 'Wrong credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'POST'])
def admin_list(request):
    """Get the list of admins or post an admin"""
    
    # commented as of now so we can create our first admins
    """
    user = get_user_from_request(request)
    # if token not passed or not valid
    if not user:
        response_data = {
            "message": "Not authenticated",
        }
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        
    # If user not an admin, only admins can get the list of admins or create an admin
    if not isinstance(user, Admin):
        response_data = {
            "message": "Not allowed",
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN) 
    """


    if request.method == 'GET':
        user = get_user_from_request(request)
        # if token not passed or not valid
        if not user:
            response_data = {
                "message": "Not authenticated",
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        # If user not an admin, only admins can get the list of admins or create an admin
        if not isinstance(user, Admin):
            response_data = {
                "message": "Not allowed",
            }
            return Response(response_data, status=status.HTTP_403_FORBIDDEN)
        # The code above is to be removed after uncommenting the lines above 
        
        admins = Admin.objects.all()
        first_name = request.query_params.get('firstName')
        last_name = request.query_params.get('lastName')
        email = request.query_params.get('email')
        phone_number = request.query_params.get('phoneNumber')
        is_active = request.query_params.get('isActive')
        admin_id = request.query_params.get('id')

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

        if admin_id is not None:
            admins = admins.filter(id=admin_id)

        paginator = Paginator(admins, request.query_params.get('page_size', 10)) # Default page size is 10
        page = paginator.get_page(request.query_params.get('page', 1)) # Default page is 1

        serializer = AdminSerializer(page, many=True)
        return Response({
            'message': 'admins fetched successfully',
            'count': paginator.count,
            'page_size': paginator.per_page,
            'page': page.number,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Admin created',
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def admin_detail(request, id):
    """ Get an admin details, update an admin and delete an admin"""


    user = get_user_from_request(request)
    # if token not passed or not valid
    if not user:
        response_data = {
            "message": "Not authenticated",
        }
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
    
    # Only an admin cant get, update or delete an admin
    if not isinstance(user, Admin):
        response_data = {
            "message": "Not allowed",
        }
        return Response(response_data, status=status.HTTP_403_FORBIDDEN)

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
        password = request.data.get('password')
        if password is not None:
            request.data['password'] = make_password(password)
        serializer = AdminUpdateSerializer(admin, data = request.data)
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
