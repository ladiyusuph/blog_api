from rest_framework import serializers
from .models import BlogPost, Tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"


class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = "__all__"

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        blogpost = BlogPost.objects.create(**validated_data)

        for tag_data in tags_data:
            # Get or create the tag
            tag, created = Tags.objects.get_or_create(name=tag_data["name"])
            blogpost.tags.add(tag)

        return blogpost

    def update(self, instance, validated_data):
        tags_data = validated_data.pop("tags")
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()

        # Clear existing tags and set new ones
        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tags.objects.get_or_create(name=tag_data["name"])
            instance.tags.add(tag)

        return instance
