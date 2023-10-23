from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def home(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type')

        expense = Expense(name=text, amount=amount,
                          expense_type=expense_type, user=request.user)
        expense.save()

        if expense_type == "Positive":
            profile.balance = (profile.balance or 0) + float(amount)
        else:
            profile.expenses = (profile.expenses or 0) + float(amount)
            profile.balance = (profile.balance or 0) - float(amount)

        profile.save()
        return redirect('/')

    context = {'profile': profile, "expenses": expenses}
    return render(request, 'home.html', context)
