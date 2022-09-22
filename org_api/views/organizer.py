from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models.functions import Lower
from django.db.models import Q


from org_api.models import Organizer
from org_api.serializers import OrganizerSerializer


class OrganizerView(ViewSet):
    """Organizer Me Organizer User view"""

    def list(self, request):
        """handle GET request for a list of users, sorted in ascending order by name.
        """
        # all users
        users = Organizer.objects.all().order_by(Lower("user__username"))
        # logged in user
        org = Organizer.objects.get(user=request.auth.user)

        for user in users:
            user.approved = org in user.app_user.all()

        search = self.request.query_params.get('search', None)
        if search is not None:
            users = Organizer.objects.filter(
                Q(user__username__contains=search) |
                Q(user__first_name__contains=search) |
                Q(user__last_name__contains=search)
            )

        serializer = OrganizerSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """handle GET request for a single user
        """

        try:
            user = Organizer.objects.get(user=request.auth.user)
            serializer = OrganizerSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Organizer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['GET'], detail=False )
    def friends(self, request):
        """handle GET request for a list of users.
        """
        # all users
        users = Organizer.objects.all()
        # logged in user
        org = Organizer.objects.get(user=request.auth.user)
        
        for user in users:
            user.approved = org in user.approved_users.all()

        serializer = OrganizerSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def approve(self, request, pk):
        """POST request for the user to approve a user from viewing their profile"""
        # logged in user
        owner = Organizer.objects.get(user=request.auth.user)
        # user in url
        family_user = Organizer.objects.get(pk=pk)

        owner.approved_users.add(family_user)
        return Response({'message': 'User added'}, status=status.HTTP_201_CREATED)

    @action(methods=['DELETE'], detail=True)
    def remove(self, request, pk):
        """"DELETE request for the user remove a user from viewing their profile """

        owner = Organizer.objects.get(user=request.auth.user)
        family_user = Organizer.objects.get(pk=pk)

        owner.approved_users.remove(family_user)

        return Response({'message': 'User removed'}, status=status.HTTP_204_NO_CONTENT)
