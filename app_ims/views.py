from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *

# Create your views here.
from django.views import View
from django.http import HttpResponse
from .models import Product
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,'productinput.html')
class InserView(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        resp=HttpResponse("product inserted successfully")
        return resp

class DisplayView(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dic={"records":qs}
        return render(request,"display.html",con_dic)
class DeleteInputView(View):
    def get(self,request):
        return render(request,"deleteinput.html")
class DeleteView(View):
    def get(self,request):
        P_id=int(request.GET["t1"])
        prod=Product.objects.filter(pid=P_id)
        prod.delete()
        resp = HttpResponse("product deleted successfully")
        return resp
class UpdateInputView(View):
    def get(self,request):
        return render(request,"updateinput.html")
class UpdateView(View):
    def post(self,request):
        P_id=int(request.POST["t1"])
        p_name = request.POST["t2"]
        p_cost = float(request.POST["t3"])
        p_mfdt = request.POST["t4"]
        p_expdt = request.POST["t5"]
        prod=Product.objects.get(pid=P_id)
        prod.pname=p_name
        prod.pcost=p_cost
        prod.pmfdt=p_mfdt
        prod.pexpdt=p_expdt
        prod.save()
        resp = HttpResponse("product updated successfully")
        return resp

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if User.objects.filter(is_staff='True'):
                return render(request,'admin.html')
            else:
                return render(request,'home.html')
    context = {}
    return render(request, 'Login.html', context)

def registerPage(request):
    form = createuserform()
    cust_form = createcustomerform()
    if request.method == 'POST':
        form = createuserform(request.POST)
        cust_form = createcustomerform(request.POST)
        if form.is_valid() and cust_form.is_valid():
            user = form.save()
            customer = cust_form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('login')
    context = {
        'form': form,
        'cust_form': cust_form,
    }
    return render(request, 'register.html', context)

def Aboutus(request):
    return render(request, 'aboutus.html')

def Contactus(request):
    return render(request,'contactus.html')