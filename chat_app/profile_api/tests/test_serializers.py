from django.test import TestCase
from account.models import Account
from profile_api.models import FriendRequest, Friend
from profile_api.serializers import FriendRequestSerializer

class FriendRequestSerializerTest(TestCase):
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
        self.serializer_data = {
            'sent_by':self.account_1.pk,
            'sent_to':self.account_2.pk,
            'approved':False,
            'declined':False
        }
        self.friend_request = FriendRequest(
            sent_by=self.account_1,
            sent_to=self.account_2,
            approved=False,
            declined=False
        )

    def test_create(self):
        serializer_data = self.serializer_data
        serializer = FriendRequestSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(serializer.data['id'], 1)
        self.assertEqual(serializer_data['sent_to'], serializer.data['sent_to'])
        self.assertEqual(serializer_data['sent_by'], serializer.data['sent_by'])
        self.assertEqual(len(FriendRequest.objects.all()), 1)

    def test_update(self):

        self.friend_request.save()
        self.serializer_data['sent_to'] = self.account_1.pk
        self.serializer_data['sent_by'] = self.account_2.pk
        self.serializer_data['approved'] = True

        serializer = FriendRequestSerializer(instance=self.friend_request ,data=self.serializer_data)

        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(serializer.validated_data['sent_to'], self.account_1)
        self.assertEqual(serializer.validated_data['sent_by'], self.account_2)
        self.assertEqual(instance.sent_by, self.account_1)
        self.assertEqual(instance.sent_to, self.account_2)
        self.assertEqual(instance.approved, self.serializer_data['approved'])        
        self.assertEqual(len(FriendRequest.objects.all()), 1)
        self.assertEqual(len(Friend.objects.all()), 2)

    def test_declined_approved_field_validation(self):

        self.serializer_data['approved'] = True
        self.serializer_data['declined'] = True
        serializer = FriendRequestSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()),set(['declined','approved']))
    
    def test_sent_to_and_sent_by_validation(self):

        self.serializer_data['sent_to'] = self.account_1.pk
        self.serializer_data['sent_by'] = self.account_1.pk
        serializer = FriendRequestSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()),set(['sent_to','sent_by']))

    def test_pending_validation(self):
        serializer_data = self.serializer_data
        serializer = FriendRequestSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        serializer_data = self.serializer_data
        serializer = FriendRequestSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()),set(['request']))
        

class FriendTest(TestCase):

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
        self.serializer_data = {
            'sent_by':self.account_1.pk,
            'sent_to':self.account_2.pk,
            'approved':False,
            'declined':False
        }
        self.friend_request = FriendRequest(
            sent_by=self.account_1,
            sent_to=self.account_2,
            approved=False,
            declined=False
        )
        self.friend_request.save()

    def test_update(self):

        self.serializer_data['approved'] = True

        serializer = FriendRequestSerializer(instance=self.friend_request ,data=self.serializer_data)

        self.assertTrue(serializer.is_valid())
        request = serializer.save() 
        self.assertEqual(len(Friend.objects.all()), 2)
        
        friends = Friend.objects.filter(approved_request=request)
        self.assertTrue(friends.exists())
        self.assertEqual(len(friends), 2)


