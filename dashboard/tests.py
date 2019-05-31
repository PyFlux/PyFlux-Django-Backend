from django.test import TestCase
from dashboard.models import Users
from django.test import Client

class UsersCase(TestCase):
    def setUp(self):
        self.url = '/dashboard/users/'
        self.client = Client()
        self.user1 = Users.objects.create_user('suhail', 'suhailvs@gmail.com', 'mypassword')
        self.user2 = Users.objects.create_user('ajani', 'suhailvs1@gmail.com', 'mypassword')
        self.user3 = Users.objects.create_user('jinto', 'suhailvs2@gmail.com', 'mypassword')
        
        response = self.client.post('/api-token-auth/', {'username': 'suhail', 'password': 'mypassword'})
        self.assertIn('token',response.data)
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + response.data['token']

    def test_users_can_add(self):
        """users can access users"""        
        self.client.login(username='suhail',password='mypassword')

        # get token for login
        response = self.client.post('/api-token-auth/', {'username': 'suhail', 'password': 'mypassword'})
        self.assertEqual(response.status_code, 200)
        # check token in response
        self.assertIn('token',response.data)
        self.assertIn('username',response.data)

    def test_add_user(self):        
        self.client.login(username='suhail',password='mypassword')

        # create a user throug rest api url(/dashboard/users)
        response = self.client.post(self.url , {
            'username': 'someuser', 
            'password': 'mypassword',  
            'first_name':'someone',  
            'email':'someone@gmail.com',
            })

        # test status created
        self.assertEqual(response.status_code, 201)

        self.client.logout()

        # get token of new user
        response = self.client.post('/api-token-auth/', {'username': 'someuser', 'password': 'mypassword'})
        self.assertIn('token',response.data)
        
        response = self.client.get(self.url,**{'HTTP_AUTHORIZATION':'Token %s'%response.data['token']})
        self.assertEqual(response.status_code, 200)
        # print(response.data)

    """
    def test_partial_update(self):
        response = self.client.get(self.url)
        # print (response.data[0]['username'])
        user_id = response.data[0]['id']
        print (user_id)
        print (response.data[0]['first_name'])
        # user_name = response.data[0]['username']

        # make a partial update: change first_name(on put request i get 415)        
        response = self.client.patch('%s%d/'%(self.url,user_id),{'username': 'someuser', 'password': 'mypassword','first_name':'suh'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('%s%d/'%(self.url,user_id))
        print (response.data)
        self.assertEqual(response.data['first_name'], 'suh')
    """