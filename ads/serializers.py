from rest_framework import serializers

from ads.models import Location, User, Ad, Category


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for locations in self._locations:
            obj, _ = locations.objects.get_or_create(name=locations)
            user.locations.add(obj)
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "role"]


class UserDetailSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ["password"]


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"
