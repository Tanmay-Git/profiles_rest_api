from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """to update own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is tryong to update his profile only"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id