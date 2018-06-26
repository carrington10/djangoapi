from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
    """ serializer to map the model into json format """


    class Meta:
        """ map serializers fields with the model fields """
        model = Bucketlist
        fields = ('id','name','date_created','date_modified')
        read_only_fields = ('date_created','daye_modified')
        
