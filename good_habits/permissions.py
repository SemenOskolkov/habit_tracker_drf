from rest_framework.permissions import BasePermission


class OwnerPerms(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.owner.pk:
            return True
        return False
