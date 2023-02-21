from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        user = authenticate(username = request.POST.get('l'),
                            password = request.POST.get('p'))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/bolim/")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class BolimlarView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')

# 3
class MahsulotlarView(View):
    def get(self, request):
        soz = request.GET.get('m_qidirish')
        if soz is None:
            mahsulot = Mahsulot.objects.filter(ombor__user=request.user)
        else:
            mahsulot = Mahsulot.objects.filter(ombor__user=request.user, nom__contains=soz)|\
                       Mahsulot.objects.filter(ombor__user=request.user, brend__contains=soz)|\
                       Mahsulot.objects.filter(ombor__user=request.user, kelgan_sana__contains=soz)
        data = {
            "mahsulotlar":mahsulot,
            'user':request.user
        }
        return render(request, 'products.html', data)
    def post(self, request):
        if request.user.is_authenticated:
            ombor = Ombor.objects.get(user=request.user)
            Mahsulot.objects.create(
                nom = request.POST.get('nom'),
                brend = request.POST.get('brend'),
                miqdor = request.POST.get('miqdor'),
                narx = request.POST.get('narx'),
                olchov = request.POST.get('olchov'),
                kelgan_sana = request.POST.get('k_sana'),
                ombor = ombor
            )
            return redirect("mahsulotlar")

# 4
class ClientlarView(View):
    def get(self, request):
        soz = request.GET.get('c_qidirish')
        if soz is None:
            client = Client.objects.filter(ombor__user=request.user)
        else:
            client = Client.objects.filter(ombor__user=request.user, ism__contains=soz)|\
                     Client.objects.filter(ombor__user=request.user, nom__contains=soz)|\
                     Client.objects.filter(ombor__user=request.user, manzil__contains=soz)|\
                     Client.objects.filter(ombor__user=request.user, tel__contains=soz)
        data = {
            'clientlar':client,
            'user':request.user
        }
        return render(request, 'clients.html', data)
    def post(self, request):
        if request.user.is_authenticated:
            ombor = Ombor.objects.get(user=request.user)
            Client.objects.create(
                nom = request.POST.get('nom'),
                manzil = request.POST.get('manzil'),
                ism = request.POST.get('ism'),
                tel = request.POST.get('tel'),
                qarz = request.POST.get('qarz'),
                ombor = ombor
            )
            return redirect("clients")

# 1
class ClientDeleteView(View):
    def get(self, request, pk):
        pr = Client.objects.get(id=pk)
        if pr.ombor == Ombor.objects.get(user=request.user):
            pr.delete()
        return redirect("clients")

# 2
class ClientEditView(View):
    def get(self, request, pk):
        pr = Client.objects.get(id=pk)
        if pr.ombor == Ombor.objects.get(user=request.user):
            return render(request, 'client_update.html', {'client':pr})
        return redirect("clients")
    def post(self, request, pk):
        Client.objects.filter(id=pk).update(
            nom = request.POST.get('nom'),
            ism = request.POST.get('ism'),
            tel = request.POST.get('tel'),
            manzil = request.POST.get('manzil'),
            qarz = request.POST.get('qarz')
        )
        return redirect("clients")

class MahsulotDeleteView(View):
    def get(self, request, pk):
        pr = Mahsulot.objects.get(id=pk)
        if pr.ombor == Ombor.objects.get(user=request.user):
            pr.delete()
        return redirect("mahsulotlar")

class MahsulotEditView(View):
    def get(self, request, pk):
        pr = Mahsulot.objects.get(id=pk)
        if pr.ombor == Ombor.objects.get(user=request.user):
            return render(request, 'product_update.html', {'product' : pr})
        return redirect("mahsulotlar")

    def post(self, request, pk):
        Mahsulot.objects.filter(id=pk).update(
            miqdor = request.POST.get('amount'),
            narx = request.POST.get('price'),
        )
        return redirect("mahsulotlar")