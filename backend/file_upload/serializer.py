from .models import FileData
from rest_framework import serializers

class FileUploadSerializer(serializers.ModelSerializer):
    # uuid =serializers.ListField()
    # images = serializers.ListField()
    # def to_internal_value(self, data):
    #     try:
    #         if data["images"] == 'Empty':
    #             data["images"] = None
    #         return super(FileUploadSerializer, self).to_internal_value(data)
    #     except:
    #         pass
    class Meta :
        model = FileData
        fields  = '__all__'
        
        
class SingleFileUploadSerializer(serializers.ModelSerializer):
    class Meta :
        model = FileData
        fields  = '__all__'
    
# class MultipleImageSerializer(serializers.Serializer):
#     images = serializers.ListField(child = FileUploadSerializer())
   
    
