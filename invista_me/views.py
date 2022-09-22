from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required

# criamos a função com a HttpResponse:
# def pagina_inicial(request):
# 	return HttpResponse('Hola Mundo!')

def contato(request):
    return HttpResponse('Para dúvidas envie um email para app@gmail.com')

def minha_historia(request):
	pessoa = {
		'nome': 'Jeff',
		'idade': 28,
		'hobby': 'Games'
	}
	return render(request, 'investimentos/minha_historia.html', pessoa)    

# def novo_investimento(request):
# 	return render(request, 'investimentos/novo_investimento.html')

# def investimento_registrado(request):
# 	investimento = {
# 		'tipo_investimento': request.POST.get('TipoInvestimento') # pega dado desse elemento que é um input
# 	}
# 	return render(request, 'investimentos/investimento_registrado.html', investimento) # passo investimento para a página com o render


def investimentos(request):
	dados = {
		'dados':Investimento.objects.all() # vai trazer todos os objetos da tabela
	}
	return render(request, 'investimentos/investimentos.html', context=dados )

def detalhe(request, id_investimento):
	dados = {
		'dados':Investimento.objects.get(pk=id_investimento)
	}
	return render(request,'investimentos/detalhe.html', dados)


@login_required
def criar(request):
	if request.method == 'POST':
		investimento_form = InvestimentoForm(request.POST)
		if investimento_form.is_valid():
			investimento_form.save()
		return redirect('investimentos')
	else:
		investimento_form = InvestimentoForm()
		formulario = {
			'formulario': investimento_form
		}
		return render(request, 'investimentos/novo_investimento.html', context=formulario)

@login_required
def editar(request, id_investimento):
	investimento = Investimento.objects.get(pk=id_investimento)
	# novo_investimento/1 -> GET
	if request.method == 'GET':
		formulario = InvestimentoForm(instance=investimento)
		return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
	# caso requisição seja POST
	else:
		formulario = InvestimentoForm(request.POST, instance=investimento)
		if formulario.is_valid():
			formulario.save()
		return redirect('investimentos')

@login_required
def excluir(request, id_investimento):
	investimento = Investimento.objects.get(pk=id_investimento)
	if request.method == 'POST':
		investimento.delete()
		return redirect('investimentos')
	return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})