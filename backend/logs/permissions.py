from rest_framework.permissions import BasePermission

class IsAdminAndHasAPIKey(BasePermission):
      def has_permission(self, request, view):
            return request.user and request.user.is_staff and request.auth is not None