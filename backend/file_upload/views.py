from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializer import FileUploadSerializer, SingleFileUploadSerializer
from .models import FileData
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


class FileUploadCreateRead(ViewSet):
   
   

    def get_file(self, request):
        response = {"success": False, 'data': []}
        status_code = status.HTTP_400_BAD_REQUEST
        data = list(FileData.objects.filter().values())
        if len(data) > 0:
            response.update({'data': data, 'success': True})
            response.update({'message': 'data received from db '})
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    def get_specific_file(self, request, pk):
        response = {"success": False,
                    "message": '!!! Ops something went wrong '}
        status_code = status.HTTP_400_BAD_REQUEST
        get_file = list(FileData.objects.filter(id=pk).values())
        if get_file:
            response = {"success": True,
                        "message": "The data is available in this file.",
                        'data': get_file}
            status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
    
    def create_single_file(self,request):
        serializer = SingleFileUploadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if True:
                response = {"success": True,
                            "message": "The file data has been created.",
                            }
                status_code = status.HTTP_206_PARTIAL_CONTENT
        else:
            response = {"success": False,
                        "errors": serializer.errors}
            status_code = status.HTTP_406_NOT_ACCEPTABLE
        return Response(response, status=status_code)
            

    def create_file(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            uuids = serializer.validated_data.get('uuid')
            file_name = serializer.validated_data.get('file_name')
            imagess = serializer.validated_data.get('images')
            print(imagess)
            images_list = []
            for image, uuid in zip(imagess, uuids):
                images_list.append(
                    FileData(uuid=uuid, file_name=file_name, images=image))

            if images_list:
                FileData.objects.bulk_create(images_list)
            # serializer.save()
            
            get_data = list(FileData.objects.all().values())
            if get_data:
                response = {"success": True,
                            "message": "The file data has been created.",
                            "data": get_data
                            }
                status_code = status.HTTP_201_CREATED
        else:
            response = {"success": False,
                        "errors": serializer.errors}
            status_code = status.HTTP_406_NOT_ACCEPTABLE
        return Response(response, status=status_code)

    def edit_file(self, request, pk):
        response = {"success": False,
                    "message": '!!! Ops something went wrong '}
        status_code = status.HTTP_400_BAD_REQUEST
        get_file = FileData.objects.get(id=pk)
        serializer = SingleFileUploadSerializer(
            get_file, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # profile_obj = list(serializer.data)
            # pk = profile_obj['id']
            # get_data = list(FileData.objects.filter(id=pk).values())

            if True:
                response = {"success": True,
                            "message": "The file data has been updated.",
                            }
                status_code = status.HTTP_206_PARTIAL_CONTENT
        else:
            response = {"success": False,
                        "errors": serializer.errors}
            status_code = status.HTTP_406_NOT_ACCEPTABLE
        return Response(response, status=status_code)

    def delete_file(self, request, uuid):
        response = {"success": False,
                    "message": '!!! Ops something went wrong '}
        status_code = status.HTTP_400_BAD_REQUEST
        get_file = FileData.objects.filter(uuid=uuid)
        print(get_file)
        data_deleted = get_file.delete()
        if data_deleted:
            response.update({'success': True})
            response.update({'message': 'file deleted successfully'})
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
