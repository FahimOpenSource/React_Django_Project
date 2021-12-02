from django.test import TestCase
from account.serializers import AccountSerializer
from account.serializers import Account

class AccountSerializerTest(TestCase):

    def setUp(self):

        self.user_info = {
            'username':'Foo',
            'password': 'admin',
            'first_name': 'foo',
            'last_name': 'bar'
        }

        self.serializer_data = {
            'username':'Bar',
            'password': 'admin',
            'first_name': 'bar',
            'last_name': 'foo'
        }

        self.account = Account.objects.create(**self.user_info)
        self.serializer = AccountSerializer(instance=self.account)

    def test_for_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),set(['username','first_name','last_name','id','last_seen_time','last_seen_date']))

    def test_for_errors(self):

        serializer = AccountSerializer(data=self.user_info)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors),set(['username']))

        self.serializer_data['first_name'] = '12345678910'
        serializer = AccountSerializer(data=self.serializer_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors),set(['first_name']))
        


    def test_create_account(self):
        
        serializer = AccountSerializer(data=self.serializer_data)
        if serializer.is_valid():
            data = serializer.save()

            account = Account.objects.get(username = str(data))
            self.assertEqual(data, account)

            account = {
                'username':serializer.data['username'],
                'password': 'admin',
                'first_name': serializer.data['first_name'],
                'last_name':serializer.data['last_name']
            }

            self.assertEqual(account, self.serializer_data)

    def test_update_account(self):

        serializer = self.serializer
        init_account = self.account
        init_data = serializer.data
        serializer_data = self.serializer_data
        
            
        serializer = AccountSerializer(instance=init_account, data=serializer_data)
        if serializer.is_valid():
            serializer.save()
            updated_data = serializer.data
           
            accounts = Account.objects.all()
            self.assertEqual(len(accounts), 1)
            self.assertEqual(serializer_data['username'], updated_data['username'])
            self.assertNotEqual(updated_data, init_data) #
            self.assertEqual(updated_data['id'], init_data['id'])
            self.assertNotEqual(updated_data['username'], init_data['username'])
            self.assertNotEqual(updated_data['first_name'], init_data['first_name'])
            self.assertNotEqual(updated_data['last_name'], init_data['last_name'])