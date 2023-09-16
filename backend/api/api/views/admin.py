""" All the views related to admin"""

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.admin import Admin
from ..serializers.admin import AdminSerializer

@api_view(['GET', 'POST'])
def admin_list(request):
    """Get the list of admins or post an admin"""

    if request.method == 'GET':
        admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return JsonResponse(serializer.data, safe=False )
    
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
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdminSerializer(admin)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AdminSerializer(admin, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
