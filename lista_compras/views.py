from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Item
from .forms import ItemForm # Importe o formulário que acabamos de criar

@login_required # Bloqueia acesso se não estiver logado
def mostrar_lista(request):
    # Lógica para salvar os dados (POST)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False) # Pausa o salvamento
            item.usuario = request.user    # Define o dono do item
            item.save()                    # Agora salva de verdade
            return redirect('lista')       # Redireciona para a página principal
    # Lógica para mostrar a página (GET)
    else:
        form = ItemForm() # Cria um formulário vazio

    itens = Item.objects.filter(usuario=request.user).order_by('comprado', 'nome')
    
    contexto = {
        'itens': itens,
        'form': form
    }
    return render(request, 'lista_compras/index.html', contexto)

@login_required
def editar_item(request, pk):
    item = get_object_or_404(Item, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        # Aqui está a mágica: passamos 'instance=item' para o formulário
        # Isso diz ao Django para ATUALIZAR este item, e não criar um novo.
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        # Preenche o formulário com os dados atuais do item
        form = ItemForm(instance=item)
    
    return render(request, 'lista_compras/editar.html', {'form': form})

@login_required
def deletar_item(request, pk):
    item = get_object_or_404(Item, pk=pk, usuario=request.user)
    item.delete()
    return redirect('lista')

@login_required
def alternar_status(request, pk):
    item = get_object_or_404(Item, pk=pk, usuario=request.user)
    # Inverte o valor booleano: se é True vira False, se é False vira True
    item.comprado = not item.comprado 
    item.save()
    return redirect('lista')

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})