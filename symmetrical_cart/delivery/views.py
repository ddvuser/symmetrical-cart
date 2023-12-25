from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

@login_required()
def delivery_index(request):
    if not request.user.is_employee:
        return redirect('index')
    context = {
    }
    return render(request, "delivery_index.html", context=context)

