from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='login')
@user_passes_test(is_manager)
def manager_main(request):
    return render(request, 'manager.html')