from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django import forms
from django.views.generic import TemplateView

from core.models import Usuario


class HomeView(View):
    def get(self, request, **kwargs):
        user = self.request.session.get('username')
        context = {'username': user}
        return render(self.request, "index.html", context)

class LoginView(View):
    def get(self, request, **kwargs):
        return render(self.request, "login.html")
    def post(self, request, **kwargs):
        email = self.request.POST.get('email')
        senha = self.request.POST.get('password')
        usuario = Usuario.objects.filter(email=email, senha=senha)
        is_valido = usuario.exists()
        user = authenticate(request, username=email, password=senha)
        if is_valido and user:
            login(request, user)
            request.session['username'] = usuario.username
            return JsonResponse({'success': True})
        return JsonResponse({'error': 'Usuario ou senha invalido!'}, status=500)

class CadastroView(View):
    def get(self, request, **kwargs):
        return render(self.request, "register.html")
    def post(self, request, **kwargs):
        email = self.request.POST.get('email')
        senha = self.request.POST.get('password')
        username = self.request.POST.get('username')
        if Usuario.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Usuario ou senha invalido!'}, status=500)
        userDjango = User.objects.create_user(username, email, senha)
        login(request, userDjango)
        usuarioNovo = Usuario()
        usuarioNovo.username = username
        usuarioNovo.senha = senha
        usuarioNovo.email = email
        request.session['username'] = username
        usuarioNovo.save()
        if not userDjango and not usuarioNovo:
            return JsonResponse({'error': 'Erro ao cadastrar usuário!'})
        return JsonResponse({'success': True})
