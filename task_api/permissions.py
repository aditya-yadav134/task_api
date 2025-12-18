from rest_framework import permissions

# Defining custom permissions
class IsAdminOrOwner(permissions.BasePermission):
  
  def has_object_permission(self, request, view, obj):
    
    if request.user.is_staff:
      return True
    else:
      return obj.owner == request.user 