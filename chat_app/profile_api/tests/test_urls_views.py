from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from account.models import Account
import json
from profile_api.models import FriendRequest, Friend

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

class ProfileViewTest(TestCase):
    def setUp(self):
        self.account_info = {
            'username':'Foo',
            'password': 'admin',
            'first_name': 'foo',
            'last_name': 'bar'
        }
        self.account = Account.objects.create(**self.account_info)
        self.url = reverse('profile', kwargs={'pk':self.account.pk})
    def test_get_profile(self):

        account = self.account
        url = self.url

        response = self.client.get(url, content_type='application/json')

        self.assertTrue(is_json(response.content))
        content = json.loads(response.content)
        self.assertEqual(set(content.keys()),{'last_name', 'date_joined', 'received', 'id', 'first_name', 'sent', 'friends', 'username', 'active'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SendFriendRequestViewTest(TestCase):
    def setUp(self):
        self.account_1 = Account.objects.create(
            username='Foo',
            password='admin',
            first_name= 'foo',
            last_name= 'bar'
        )
        self.account_2 = Account.objects.create(
            username='Bar',
            password='admin',
            first_name= 'bar',
            last_name= 'foo'
        )
        self.request_data = {
            'sent_by':self.account_1.pk,
            'sent_to':self.account_2.pk,
            'approved':False,
            'declined':False
        }

    def test_post_get_request(self):

        url = reverse('send_request')
        data = self.request_data

        response = self.client.post(url, data, content_type='application/json')
        content = json.loads(response.content)
        self.assertEqual(set(content.keys()), {'id','sent_by','sent_to','approved','declined','last_modified'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(content.keys()), {'id','sent_by','sent_to','approved','declined','last_modified'})

class FriendRequestViewTest(TestCase):

    def setUp(self):
        self.account_1 = Account.objects.create(
            username='Foo',
            password='admin',
            first_name= 'foo',
            last_name= 'bar'
        )
        self.account_2 = Account.objects.create(
            username='Bar',
            password='admin',
            first_name= 'bar',
            last_name= 'foo'
        )

        self.friend_request = FriendRequest(
            sent_by=self.account_1,
            sent_to=self.account_2,
            approved=False,
            declined=False
        )
        self.friend_request.save()
        self.url = reverse('view_request', kwargs={'pk':self.friend_request.id})

    def test_get_request(self):

        url = self.url
        response = self.client.get(url, content_type='application/json')
        content = json.loads(response.content)

        self.assertEqual(set(content.keys()), {'id','sent_by','sent_to','approved','declined','last_modified'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request(self):

        url = self.url
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class FriendViewTest(TestCase):

    def setUp(self):
        self.account_1 = Account.objects.create(
            username='Foo',
            password='admin',
            first_name= 'foo',
            last_name= 'bar'
        )
        self.account_2 = Account.objects.create(
            username='Bar',
            password='admin',
            first_name= 'bar',
            last_name= 'foo'
        )

        self.friend_request = FriendRequest(
            sent_by=self.account_1,
            sent_to=self.account_2,
            approved=False,
            declined=False
        )
        self.friend_request.save()
        self.url = reverse('view_request', kwargs={'pk':self.friend_request.id})

    def test_create_delete_friend_and_update_request(self):

        url = self.url
        data = {
            'sent_by':self.account_1.pk,
            'sent_to':self.account_2.pk,
            'approved':True,
            'declined':False
        }

        response = self.client.put(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Friend.objects.all()), 2)

        friends = Friend.objects.filter(approved_request=self.friend_request)
        self.assertTrue(friends.exists())

        url = reverse('view_request', kwargs={'pk':friends[0].pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Friend.objects.all()), 0)
        friends = Friend.objects.filter(approved_request=self.friend_request)
        self.assertFalse(friends.exists())