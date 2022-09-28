from rest_framework import permissions
from users.models import CustomUser

class ReadOnly (permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsSuperUser (permissions.IsAdminUser):
    def has_permission(self, request, view):
        return request.user.username == 'kelin'

class IsAuthorOrReadyOnly (permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated