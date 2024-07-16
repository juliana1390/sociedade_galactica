from django.shortcuts import render
from django.views.decorators.http import require_POST
from app.models import *
from app.utils import *

# SCIENTIST FUNCTIONS ==================================================================

# create star ----------------------------------------------------------
@require_POST
def view_create_star(request):
    id_estrela = request.POST.get('id_estrela')
    nome = request.POST.get('nome')
    classificacao = request.POST.get('classificacao')
    massa = request.POST.get('massa')
    x = request.POST.get('x')
    y = request.POST.get('y')
    z = request.POST.get('z')
     
    print('entrou na funcao')
    if massa is None or massa.strip() == '':
        return render(request, 'app/error_page.html', {'mensagem': "Massa não pode estar vazia."})
    if x is None or x.strip() == '':
        return render(request, 'app/error_page.html', {'mensagem': "Coordenada x não pode estar vazia."})
    if y is None or y.strip() == '':
        return render(request, 'app/error_page.html', {'mensagem': "Coordenada y não pode estar vazia."})
    if z is None or z.strip() == '':
        return render(request, 'app/error_page.html', {'mensagem': "Coordenada z não pode estar vazia."})

    try:
        massa = float(massa)
        x = float(x)
        y = float(y)
        z = float(z)

        create_star(id_estrela, nome, classificacao, massa, x, y, z)
        mensagem = f"Estrela '{id_estrela}' criada com sucesso!"
        return render(request, 'app/success_page.html', {'mensagem': mensagem})
    
    except ValueError as ve:
        mensagem_e = f"Erro na criação da estrela '{id_estrela}': {str(ve)}"
        return render(request, 'app/error_page.html', {'mensagem': mensagem_e})
    
    except Exception as e:
        mensagem_e = f"Erro na criação da estrela '{id_estrela}': {str(e)}"
        return render(request, 'app/error_page.html', {'mensagem': mensagem_e})

# read star data ----------------------------------------------------------
@require_POST
def view_read_star_data(request):
    id_estrela = request.POST.get('estrela')

    try:
        result = read_star_data(id_estrela)
        return render(request, 'app/star_report.html', {'result': result})
    
    except Exception as e:
        mensagem_e = f"Erro: {str(e)}"
        return render(request, 'app/error_page.html', {'mensagem': mensagem_e})


# update star ----------------------------------------------------------
def view_update_star(request):
    id_estrela = request.POST.get('id_estrela')
    nome = request.POST.get('nome')
    classificacao = request.POST.get('classificacao')
    massa = request.POST.get('massa')
    x = request.POST.get('x')
    y = request.POST.get('y')
    z = request.POST.get('z')
   
    if massa is None or massa.strip() == '':
        return render(request, 'app/error_page.html', {'mensagem': "Massa não pode estar vazia."})
    if x is None or x.strip() == '':
        return render(request, 'app/error_page.html', {'mensagem': "Coordenada x não pode estar vazia."})
    if y is None or y.strip() == '':
        return render(request, 'app/error_page.html', {'mensagem': "Coordenada y não pode estar vazia."})
    if z is None or z.strip() == '':
        return render(request, 'app/error_page.html', {'mensagem': "Coordenada z não pode estar vazia."})

    try:
       
        massa = float(massa)
        x = float(x)
        y = float(y)
        z = float(z)

        update_star(id_estrela, nome, classificacao, massa, x, y, z)
        mensagem = f"Estrela '{id_estrela}' atualizada com sucesso!"
        return render(request, 'app/success_page.html', {'mensagem': mensagem})
    
    except ValueError as ve:
       
        mensagem_e = f"Erro na atualização da estrela '{id_estrela}': {str(ve)}"
        return render(request, 'app/error_page.html', {'mensagem': mensagem_e})
    
    except Exception as e:
       
        mensagem_e = f"Erro na criação da estrela '{id_estrela}': {str(e)}"
        return render(request, 'app/error_page.html', {'mensagem': mensagem_e})

# delete star ----------------------------------------------------------
@require_POST
def view_delete_star(request):
    id_estrela = request.POST.get('estrela')

    try:
        delete_star(id_estrela)
        mensagem = f"Estrela '{id_estrela}' excluída!"
        return render(request, 'app/success_page.html', {'mensagem': mensagem})
    
    except Exception as e:
        mensagem_e = f"Erro: {str(e)}"
        return render(request, 'app/error_page.html', {'mensagem': mensagem_e})