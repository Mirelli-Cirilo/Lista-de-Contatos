from django.shortcuts import render, redirect
from .models import Contato

# Create your views here.

def index(request):
    contatos = Contato.objects.all()

    search = request.GET.get('search-area')

    if search:
        contatos = Contato.objects.filter(nome_completo__icontains=search)
    else:
        contatos = Contato.objects.all() 
        search = ''   
        

    
    return render(request, 'index.html', {'contatos': contatos, 'search':search})

def newContact(request):
    if request.method == 'POST':

        new_contact = Contato(
            nome_completo = request.POST['nome_completo'],
            relação = request.POST['relação'],
            email = request.POST['email'],
            numero = request.POST['numero'],
            endereco = request.POST['endereco'],
            )
        new_contact.save()
        return redirect('/')

    return render(request, 'new.html')

def editContact(request, pk):
    contato = Contato.objects.get(id=pk)

    if request.method == 'POST':
        contato.nome_completo = request.POST['nome_completo']
        contato.relação = request.POST['relação']
        contato.email = request.POST['email']
        contato.numero = request.POST['numero']
        contato.endereco = request.POST['endereco']
        contato.save()

        return redirect('/detalhes/'+str(contato.id))
    return render(request, 'edit.html', {'contato': contato})




def detailsContact(request, pk):
    contato = Contato.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contato':contato})


def deleteContact(request, pk):
    contato = Contato.objects.get(id=pk)

    if request.method == 'POST':
        contato.delete()
        return redirect('/')



    context = {'contato': contato}
    return render(request, 'delete.html', context)