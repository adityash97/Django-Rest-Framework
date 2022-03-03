from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission,SAFE_METHODS


class PostUserWritePermission(BasePermission):  # Custom Permission (Object level permission)
    # Over Riding method
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user 
            """
            Returning False if author is not matching to user i.e No Write(delete or update ) permision
            Returning True if author is same as user . i.e with Write(delete or update ) Permision
            """



class PostList(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUser]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # View level permission.Edited in admin pannel(created group)
    queryset = Post.postobject.all() # postobject is custom model manager
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
