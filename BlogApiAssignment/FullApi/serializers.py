from rest_framework.serializers import ModelSerializer
from .models import Blog, User
from django.contrib.auth.models import User





class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

class BlogsSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["user"] = instance.user.all().values()
        return rep


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
