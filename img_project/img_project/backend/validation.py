from rest_framework import permissions


class IsSenior(permissions.BasePermission):
    message = 'Only 3rd yearites and 4th yearites are permitted.'

    def has_permission(self, request, view):
        return request.user.is_master

class CanViewMemberDetails(permissions.BasePermission):
    message = 'Sophomores and Freshers are not permitted to view details of 3y or later.'

    def has_object_permission(self, request, view, obj):
        return request.user.year > 2 or obj.year < 3