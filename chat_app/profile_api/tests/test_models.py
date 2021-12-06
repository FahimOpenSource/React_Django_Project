from django.core.exceptions import ValidationError
from django.test import TestCase
from account.models import Account
from profile_api.models import Friend
from profile_api.models import FriendRequest

class FriendRequestModelTest(TestCase):
    def setUp(self):
        self.account_info_1 = {
            'username':'Foo',
            'password': 'admin',
            'first_name': 'foo',
            'last_name': 'bar'
        }
        self.account_info_2 = {
            'username':'Bar',
            'password': 'admin',
            'first_name': 'bar',
            'last_name': 'foo'
        }

        self.account_1 = Account.objects.create(**self.account_info_1)
        self.account_2 = Account.objects.create(**self.account_info_2)

        self.request_info = {
            'sent_by':self.account_1,
            'sent_to':self.account_2,
            'approved':False,
            'declined':False
        }

    def test_request_create(self):

        request = FriendRequest.objects.create(**self.request_info)

        self.assertTrue(request)
        self.assertEqual(request.sent_by, self.account_1)
        self.assertEqual(request.sent_to, self.account_2)

    def test_request_update(self):

        # create request
        request = FriendRequest(**self.request_info)
        request.save()

        request.sent_by = self.account_2
        request.sent_to = self.account_1

        request.save(update_fields=['sent_to','sent_by'])

        self.assertTrue(request)
        self.assertNotEqual(request.sent_by, self.account_1)
        self.assertNotEqual(request.sent_to, self.account_2)

    def test_sent_to_and_sent_by_validation(self):

        #declined and aproved

        self.request_info['sent_to'] = self.account_1

        request = FriendRequest(**self.request_info)
        try:
            request.full_clean()
        except ValidationError as e:
            self.assertTrue(e.message_dict)
            self.assertEqual(set(e.message_dict.keys()), set(['sent_to','sent_by']))
    
    def test_declined_approved_validation(self):
        self.request_info['declined'] = True
        self.request_info['approved'] = True

        request = FriendRequest(**self.request_info)
        try:
            request.full_clean()
        except ValidationError as e:
            self.assertTrue(e.message_dict)
            self.assertEqual(set(e.message_dict.keys()), set(['declined','approved']))

class FriendModelTest(TestCase):
    
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
        self.friend_request = FriendRequest.objects.create(
            sent_by=self.account_1,
            sent_to=self.account_2,
            approved=True,
            declined=False
        )
        self.friend = Friend(
            account=self.account_1,
            friend_account=self.account_2,
            approved_request=self.friend_request,
        )

    def test_create(self):
        self.friend.save()
        friend = self.friend

        self.assertTrue(friend)
        self.assertEqual(friend.account, self.account_1)
        self.assertEqual(friend.friend_account, self.account_2)
        self.assertEqual(friend.approved_request, self.friend_request)

    def test_update(self):
        self.friend.save()
        self.friend.account = self.account_2
        self.friend.friend_account = self.account_1
        self.friend.chat = True
        self.friend.save()
        friend = self.friend

        self.assertNotEqual(friend.account, self.account_1)
        self.assertNotEqual(friend.friend_account, self.account_2)
        self.assertTrue(friend.chat)
        
    def test_errors(self):
                
        self.friend.account = self.account_2
        try:
            self.friend.full_clean()
        except ValidationError as e:
            self.assertTrue(e.message_dict)
            self.assertEqual(set(e.message_dict.keys()), set(['friend account']))
        
        
