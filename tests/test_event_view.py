from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.db.models.functions import Lower

from org_api.models import Event, Organizer
from org_api.serializers import EventSerializer


class EventTest(APITestCase):

    # fixtures to run to build the database
    fixtures = ['users', 'tokens', 'organizers',
                'events']

    def setUp(self):
        self.organizer = Organizer.objects.first()
        token = Token.objects.get(user=self.organizer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_event(self):
        """ Test the create event method
        - Test fails with current setup.  Test is failing due to readable time and date
        properties.  Test passes when the serializer is changed.
        """
        url = "/events"

        event = {
            "title": "Park",
            "date": "2022-09-27",
            "time": "18:30:00",
            "org": 1
        }

        response = self.client.post(url, event, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        new_event = Event.objects.last()

        expected = EventSerializer(new_event)
        self.assertEqual(expected.data, response.data)

    def test_get_event(self):
        """Testing the get single event method"""

        event = Event.objects.first()

        url = f'/events/{event.id}'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        expected = EventSerializer(event)
        self.assertEqual(expected.data, response.data)

    def test_list_events(self):
        """Testing the get all event method"""

        url = '/events'

        response = self.client.get(url)

        all_events = Event.objects.all().order_by(Lower('date'))
        expected = EventSerializer(all_events, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)

    def test_update_event(self):
        """test update event method"""

        event = Event.objects.first()
        url = f'/events/{event.id}'

        updated_event = {
            "title": f'{event.title} updated',
            "date": event.date,
            "time": event.time
        }

        response = self.client.put(url, updated_event, format='json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        event.refresh_from_db()
        self.assertEqual(updated_event['title'], event.title)

    def test_delete_event(self):
        """Testing the delete event method"""

        event = Event.objects.first()

        url = f'/events/{event.id}'
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
