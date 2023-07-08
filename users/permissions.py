from rest_framework.permissions import BasePermission


class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and user.is_instructor:
            return True
