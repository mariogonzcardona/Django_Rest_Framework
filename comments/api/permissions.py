from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'POST']:
            return True
        else:
            id_comment=view.kwargs['pk']
            comment=Comment.objects.get(pk=id_comment)
            id_user=request.user.pk
            is_user_comment=comment.user_id
        
            return True if id_user == is_user_comment else False