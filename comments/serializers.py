from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comments

class CommentsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comments
        fields = [
            'id', 'owner', 'post', 'is_owner', 'profile_id',
            'profile_image', 'created_at',
            'updated_at', 'content', 'created_at', 'updated_at'
        ]

class CommentsDetailSerializer(CommentsSerializer):
    post = serializers.ReadOnlyField(source='post.id')