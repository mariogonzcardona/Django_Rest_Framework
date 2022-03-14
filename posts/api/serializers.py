from rest_framework.serializers import ModelSerializer
from posts.models import Post
from user.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class PostSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    category=CategorySerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id','title','content','slug','image','created_at','published','user','category')