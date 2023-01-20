from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy as _

from .forms import EditUserForm, SignupAgentForm
from .models import User


@user_passes_test(lambda u: u.is_superuser)
def users_list(request):
    object = User.objects.all()
    context = {
        'object': object,
    }
    return render(request, 'user/users_list.html', context)


@login_required
def user_update(request, pk):
    obj = get_object_or_404(User, pk=pk)
    form = EditUserForm(instance=obj)

    if request.method == 'POST':
        form = EditUserForm(request.POST or None, instance=obj)

        if form.is_valid():
            obj = form.save(commit=True)
            messages.success(request, 'Dados alterados com sucesso!!!')
            return redirect('user:users_list')
        else:
            return render(request, 'user/user_update.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'user/user_update.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def agent_signup(request):
    if request.method == "POST":
        form = SignupAgentForm(request.POST)
        if form.is_valid():
            agent = form.save(commit=False)
            user = request.user
            agent.company_id = user.company_id
            agent.option = '2'
            agent = form.save()
            messages.success(request, 'Agente cadastrado com sucesso!!!')
            return redirect('company:company_agents_list')

    form = SignupAgentForm()
    template_name = "account/signup_agent.html"
    context = {
        "form": form
    }
    return render(request, template_name, context)
