from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from .models import Products
from django.contrib.auth.models import User

class ProductsAPITestCase(APITestCase):
    def setUp(self):
        # Criar um usuário para autenticar
        self.user = User.objects.create_user(username='admintester', password='admintester')

        # Gerar um token JWT para o usuário
        self.token = AccessToken.for_user(self.user)

    def test_create_product(self):
        # Criar um cliente de teste
        client = APIClient()

        # Configurar as credenciais para autenticação (exemplo com token JWT)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Teste para criar um novo produto e verificar se retorna o status HTTP 201 Created
        data = {'name': 'Test Product', 'description': 'This is a test product.', 'price': '10.00'}
        response = client.post('/products/', data, format='json')

        # Verificar se a requisição foi bem-sucedida (status HTTP 201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificar se o produto foi criado no banco de dados
        self.assertTrue(Products.objects.filter(name='Test Product').exists())


    def test_empty_product_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    
    def test_create_single_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        data = {'name': 'New Product', 'description': 'A new product', 'price': '99.99'}
        response = self.client.post('/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Product')
        self.assertEqual(response.data['description'], 'A new product')
        self.assertEqual(float(response.data['price']), 99.99)


    def test_update_product(self):
        product = Products.objects.create(name='Initial Product', description='Initial description', price='50.00')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Dados para atualizar o produto
        data = {'name': 'Updated Product', 'description': 'Updated description', 'price': '75.00'}

        # Enviar requisição PUT para atualizar o produto
        response = self.client.put(f'/products/update/{product.id}/', data, format='json')

        # Verificar se a requisição foi bem-sucedida (status HTTP 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se o produto foi atualizado no banco de dados
        product.refresh_from_db()
        self.assertEqual(product.name, 'Updated Product')
        self.assertEqual(product.description, 'Updated description')
        self.assertEqual(float(product.price), 75.00)

    def test_delete_product(self):
        product = Products.objects.create(name='Product to Delete', description='To be deleted', price='100.00')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Enviar requisição DELETE para excluir o produto
        response = self.client.delete(f'/products/delete/{product.id}/')

        # Verificar se a requisição foi bem-sucedida (status HTTP 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se o produto foi removido do banco de dados
        with self.assertRaises(Products.DoesNotExist):
            Products.objects.get(id=product.id)

    def test_retrieve_product(self):
        product = Products.objects.create(name='Test Product', description='Test description', price='25.00')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Enviar requisição GET para obter os detalhes do produto
        response = self.client.get(f'/products/{product.id}/')

        # Verificar se a requisição foi bem-sucedida (status HTTP 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se os detalhes do produto retornados são corretos
        self.assertEqual(response.data['name'], 'Test Product')
        self.assertEqual(response.data['description'], 'Test description')
        self.assertEqual(float(response.data['price']), 25.00)