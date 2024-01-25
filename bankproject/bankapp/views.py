from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Products, Branch



def home(request):
    products = Products.objects.all()
    districts = Branch.objects.values_list('district', flat=True).distinct()
    context = {'product_list': products, 'districts': districts}
    return render(request, 'home.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('bank:details')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if not all([username, first_name, last_name, email, password, cpassword]):
            messages.error(request, "All fields are required")
            return redirect('bank:register')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('bank:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('bank:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect('bank:login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('bank:register')

    return render(request, "register.html")






def logout_view(request):
    logout(request)
    return redirect('bank:home')







def details(request):
    if request.method == 'POST':

        messages.success(request, 'Application accepted')
        return redirect('bank:welcome')

    districts = Branch.objects.values('district').distinct()

    return render(request, 'details.html', {'districts': districts})


def welcome(request):
    user = auth.authenticate(request)
    if user is not None and user.is_authenticated:
        auth.login(request, user)
        return redirect('bank:details')
    return render(request, 'welcome.html')


class DistrictsView(View):
    def get(self, request, *args, **kwargs):
        districts = Branch.objects.values('district').distinct()
        return JsonResponse(list(districts), safe=False)

class BranchesView(View):
    def get(self, request, *args, **kwargs):
        district = request.GET.get('district', None)
        if district:
            branches = Branch.objects.filter(district=district).values('name')
            return JsonResponse(list(branches), safe=False)
        return JsonResponse([], safe=False)


def about(request,products_id):
    products=Products.objects.get(id=products_id)
    return render(request,"about.html",{'products':products})


