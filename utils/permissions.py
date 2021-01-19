from rest_framework import permissions

from account.apps import AccountConfig as UserConf


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.type == UserConf.USER_ADMIN)
