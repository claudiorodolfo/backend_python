from django.shortcuts import render


def home(request):
    """Tela inicial: usuário escolhe manipular categorias ou produtos."""
    return render(request, 'home.html')
