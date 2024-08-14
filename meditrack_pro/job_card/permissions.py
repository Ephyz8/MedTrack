from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow administrators to edit or delete job cards.

    Read-only permissions are granted to any request, but write permissions 
    are only allowed to administrators (staff members).
    """

    def has_permission(self, request, view):
        """
        Return True if the request is a safe method (GET, HEAD, OPTIONS) or 
        if the user is a staff member (admin).
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
