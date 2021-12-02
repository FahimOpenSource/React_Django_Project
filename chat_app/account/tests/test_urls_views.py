from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from account.models import Account
import json

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

class SignUpViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('signup')
        self.account_1 = {
            'username':'Foo',
            'password': 'admin',
            'first_name': 'foo',
            'last_name': 'bar'
        }
        self.account_2 = {
            'username':'Bar',
            'password': 'admin',
            'first_name': 'bar',
            'last_name': 'foo'
        }

    
    def test_signup(self):

        url = self.url
        account = self.account_1

        data = json.dumps(account)
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().username, account['username'])
        self.assertTrue(is_json(response.content))
        content = json.loads(response.content)
        self.assertEqual(set(content.keys()),set(['username','first_name','last_name','id','last_seen_time','last_seen_date']))

    def test_signup_errors(self):

        url = self.url
        Account.objects.create(**self.account_1)
        account_data = self.account_1

        data = json.dumps(account_data)
        response = self.client.post(url, data, content_type='application/json')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content.keys(),{'username'})

        self.account_2['first_name'] = '12345678910'
        account_data = self.account_2

        data = json.dumps(account_data)
        response = self.client.post(url, data, content_type='application/json')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(content.keys(),{'first_name'})

    def test_accounts_list_view(self):

        url = self.url
        data_1 = json.dumps(self.account_1)
        response_1 = self.client.post(url, data_1, content_type='application/json')
        content_1 = json.loads(response_1.content)
        data_2 = json.dumps(self.account_2)
        response_2 = self.client.post(url, data_2, content_type='application/json')
        content_2 = json.loads(response_2.content)
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)

        response = self.client.get(url)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content,[content_1,content_2])
        
class AccountViewTest(APITestCase):

    def setUp(self):

        self.account_info = {
            'username':'Foo',
            'password': 'admin',
            'first_name': 'foo',
            'last_name': 'bar'
        }

        self.account = Account.objects.create(**self.account_info)

        self.url = reverse('account', kwargs={'pk': self.account.pk})

    def test_get(self):

        url = self.url
        response = self.client.get(url)
        content = json.loads(response.content)
        self.assertEqual(content['id'], self.account.pk)
        self.assertEqual(set(content.keys()),set(['username','first_name','last_name','id','last_seen_time','last_seen_date']))

    def test_errors(self):

        url = reverse('account', kwargs={'pk': 2})
        response = self.client.get(url)
        content = json.loads(response.content)
        self.assertEqual(content['detail'], 'Not found.')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_put(self):

        url = self.url

        self.account_info['username'] = 'Bar'
        self.account_info['last_name'] = 'foobar'

        data = json.dumps(self.account_info)
        
        response = self.client.put(url, data, content_type='application/json')
        content = json.loads(response.content)
        self.assertEqual(content['id'], self.account.pk)
        self.assertEqual(content['username'],self.account_info['username'])
        self.assertEqual(content['first_name'],self.account_info['first_name'])
        self.assertEqual(content['last_name'],self.account_info['last_name'])
    
    def test_delete(self):
        url = self.url

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Account.objects.filter(pk=self.account.pk)),0)
