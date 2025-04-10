
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Pagina

class PaginaModelTest(TestCase):
    def setUp(self):
        # Criando um usuário para testar
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_pagina(self):
        # Testando a criação de uma página
        pagina = Pagina.objects.create(
            titulo="Test Page",
            subtitulo="This is a test page",
            conteudo="This is the content of the test page.",
            autor=self.user
        )
        self.assertEqual(pagina.titulo, "Test Page")
        self.assertEqual(pagina.subtitulo, "This is a test page")
        self.assertEqual(pagina.conteudo, "This is the content of the test page.")

class PaginaViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_pagina_list_view(self):
        # Testando a view de listagem de páginas
        response = self.client.get(reverse('blog:lista_paginas'))  # Altere 'blog:lista_paginas' para o nome correto da sua URL
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nenhuma página encontrada')  # Mensagem que você exibe quando não há páginas

    def test_pagina_create_view(self):
        # Testando a criação de uma página através da view
        response = self.client.post(reverse('blog:criar_pagina'), {
            'titulo': 'Test Page',
            'subtitulo': 'Test Subtitle',
            'conteudo': 'Test Content',
            'autor': self.user.id
        })
        self.assertEqual(response.status_code, 302)  # Status code de redirecionamento após criar
        self.assertTrue(Pagina.objects.filter(titulo='Test Page').exists())

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_user_profile_update(self):
        # Testando a atualização de perfil do usuário
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('blog:atualizar_perfil'), {
            'first_name': 'NewFirstName',
            'last_name': 'NewLastName',
            'email': 'newemail@example.com',
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'NewFirstName')
        self.assertEqual(self.user.last_name, 'NewLastName')
        self.assertEqual(self.user.email, 'newemail@example.com')

class LoginTest(TestCase):
    def test_login_view(self):
        # Testando o login
        user = User.objects.create_user(username='testuser', password='12345')
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)  # Redireciona após login

    def test_logout_view(self):
        # Testando o logout
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redireciona após logout
