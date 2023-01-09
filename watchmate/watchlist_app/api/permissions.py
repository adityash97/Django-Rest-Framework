from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        admin = super().has_permission(request, view)
        return bool(request.method == 'GET' or admin)

class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.review_user == request.user