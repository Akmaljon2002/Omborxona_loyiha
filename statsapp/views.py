from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views import View
from .models import *

from asosiy.models import Mahsulot, Client, Ombor



class StatsView(View):
    def get(self, request):
        soz = request.GET.get('soz')
        if soz is not None:
            stats = Stats.objects.filter(client__ombor__user=request.user, mahsulot__nom__contains=soz)|\
                    Stats.objects.filter(client__ombor__user=request.user, client__ism__contains=soz)|\
                    Stats.objects.filter(client__ombor__user=request.user, mahsulot__brend__contains=soz)
        else:
            stats = Stats.objects.filter(client__ombor__user=request.user)
        data = {
            'stats':stats,
            'mahsulotlar':Mahsulot.objects.filter(ombor__user=request.user),
            'clientlar':Client.objects.filter(ombor__user=request.user)
        }
        return render(request, 'stats.html', data)
    def post(self, request):
        if request.user.is_authenticated:
            farq = int(request.POST.get('summa')) - int(request.POST.get('tolandi'))
            nasiya = Client.objects.get(id=request.POST.get('client')).qarz + farq
            if farq > 0:
                qoldi = farq
            else:
                qoldi = 0

            Stats.objects.create(
            mahsulot = Mahsulot.objects.get(id=request.POST.get('mahsulot')),
            client = Client.objects.get(id=request.POST.get('client')),
            sana = request.POST.get('sana'),
            miqdor = request.POST.get('miqdor'),
            olchov = request.POST.get('olchov'),
            summa = request.POST.get('summa'),
            tolandi = request.POST.get('tolandi'),
            qoldi = qoldi
            )
            # nasiya = Client.objects.get(id=request.POST.get('client')).qarz + int(request.POST.get('qoldi'))
            Client.objects.filter(id=request.POST.get('client')).update(
                qarz = nasiya
            )

        return redirect("/stats/")

# 1
class StatsDeleteView(View):
    def get(self, request, pk):
        pr = Stats.objects.get(id=pk)
        if pr.client.ombor == Ombor.objects.get(user=request.user):
            pr.delete()
        return redirect("/stats/")

class StatsEditView(View):
    def get(self, request, pk):
        pr = Stats.objects.get(id=pk)
        if pr.client.ombor == Ombor.objects.get(user=request.user):
            return render(request, 'stats_update.html', {"stats":pr})
        return redirect("/stats/")
    def post(self, request, pk):
        farq = int(request.POST.get('summa')) - int(request.POST.get('tolandi'))
        nasiya = Stats.objects.get(id=pk).client.qarz + farq
        if farq > 0:
            qoldi = farq
        else:
            qoldi = 0
        Stats.objects.filter(id=pk).update(
            miqdor = request.POST.get('miqdor'),
            summa = request.POST.get('summa'),
            tolandi = request.POST.get('tolandi'),
            qoldi = qoldi
        )
        return redirect("/stats/")