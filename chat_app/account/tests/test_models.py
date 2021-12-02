from django.test import TestCase
from account.models import Account,validate_string

class AccountModelTest(TestCase):

    def test_create_update_account(self):

        init_user_info = {
            'username':'Foo',
            'password': 'admin',
            'first_name': 'foo',
            'last_name': 'bar'
        }

        init_account = Account.objects.create(**init_user_info)

        account = Account.objects.get(pk=init_account.id)
        self.assertEqual(init_account, account)


        account.username = 'bar'
        account.password = 'root'

        account.save(update_fields=['username','password'])

        accounts = Account.objects.all()
        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0],account)
        self.assertEqual(init_account.id, account.id)
        self.assertNotEqual(init_account.username,account.username)
        self.assertFalse(account.check_password(init_user_info['password']))
        self.assertEqual(init_account.first_name,account.first_name)
        self.assertEqual(init_account.last_name,account.last_name)

    def test_account_password_hashing(self):

        user_info = {
            'username':'Foo',
            'password': 'admin',
            'first_name': 'foo',
            'last_name': 'bar'
        }

        account = Account.objects.create(**user_info)

        self.assertTrue(account.check_password(user_info['password']))
        self.assertNotEqual(account.password, user_info['password'])

    def test_string_constraints(self):

        user_info = {
            'username':' Foo ',
            'password': 'admin',
            'first_name': 'ba r  foo',
            'last_name': 'bar'
        }

        account = Account.objects.create(**user_info)

        self.assertEqual(account.username, 'Foo')
        self.assertNotEqual(account.username, user_info['username'])
        self.assertNotEqual(account.first_name, user_info['first_name'])
        self.assertEqual(account.first_name, 'ba r foo')
        self.assertEqual(account.last_name, user_info['last_name'])
    
    def test_string_validate_function(self):
        strings = ['  food  ', 'foo  bar ', 'fooh d  ', 'foobar']

        for string in strings[:2]:
            validated_string = validate_string(string)
            self.assertNotEqual(validated_string, string)

        validated_string = validate_string(strings[-1])
        self.assertEqual(validated_string,strings[-1])
        
    def test_str_representation(self):

        user_info = {
            'username':'Foo',
            'password': 'admin',
            'first_name': 'foo',
            'last_name': 'bar'
        }

        account = Account.objects.create(**user_info)

        self.assertEqual(user_info['username'],str(account))