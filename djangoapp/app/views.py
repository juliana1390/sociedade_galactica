from django.shortcuts import render
from django.views.decorators.http import require_POST
from app.models import *
from app.models import Users, Lider, Nacao, Especie

def index(request):
    return render(
        request,
        'app/index.html'
    )


def login(request):
    return render(
        request,
        'app/login_page.html'
    )

@require_POST
def login_check(request):
    cpi = request.POST.get('cpi')
    password = request.POST.get('password')
    print(cpi)
    # print(password)

    # print('antes do try')
    try:
        print('entrou no try')
        # Buscar usuário pelo cpi (id_lider)
        user = Users.objects.get(id_lider=cpi)
        print(user)

        if user.password == password:
            lider = user.id_lider
            
            # Armazenar o cpi na sessão
            request.session['cpi'] = cpi
            request.session['user_id'] = user.user_id
            
            # Verificar se o líder é também líder de facção
            is_lider_faccao = Faccao.objects.filter(lider=lider).exists()
            
            # Redirecionar com base no cargo e se é líder de facção
            cargo = lider.cargo.strip()
            
            if cargo == 'COMANDANTE':
                if is_lider_faccao:
                    return render(request, 'app/comandante_lider_faccao.html')
                else:
                    return render(request, 'app/comandante.html')
            elif cargo == 'OFICIAL':
                if is_lider_faccao:
                    return render(request, 'app/oficial_lider_faccao.html')
                else:
                    return render(request, 'app/oficial.html')
            elif cargo == 'CIENTISTA':
                if is_lider_faccao:
                    return render(request, 'app/cientista_lider_faccao.html')
                else:
                    return render(request, 'app/cientista.html')
            else:
                mensagem = "Erro ao fazer login: Página não encontrada."
                return render(request, 'app/error_page.html', {'mensagem': mensagem})
        else:
            mensagem = "Erro ao fazer login: Senha incorreta."
            return render(request, 'app/error_page.html', {'mensagem': mensagem})
    
    except Users.DoesNotExist:
        print('falhou')
        mensagem = "Erro ao fazer login: Usuário não encontrado."
        return render(request, 'app/error_page.html', {'mensagem': mensagem})
