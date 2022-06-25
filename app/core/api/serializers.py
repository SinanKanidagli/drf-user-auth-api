from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "password",
            "is_staff",
            "is_active",
            "is_superuser",
            "date_joined",
        )
        read_only_fields = (
            "id",
            "is_staff",
            "is_active",
            "is_superuser",
            "date_joined",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = get_user_model()(
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
