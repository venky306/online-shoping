from django.shortcuts import render
from .models import MerchantMdel
from django.core.mail import send_mail
from pro1 import settings as se
from django.views.generic import View
from django.core.serializers import serialize
from django.http import HttpResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import Merchentnewpassword, MerchantProduct

def home(request):
    us=request.POST.get('username')
    pw=request.POST.get('password')

    if us == "venky" and pw == "venky":
        return render(request,'home.html')
    else:
        return render(request,'show.html',{"error":"Invalid user"})


def mlogin(request):
    return render(request,'mlogin.html')


def mregister(request):
    try:
        result=MerchantMdel.objects.all()[::-1][0]
        indo=int(result.indo)+1
        return render(request,'mregister.html',{"data":indo})
    except IndexError:
        indo=1001000
        return render(request,'mregister.html',{"data":indo})


def esavereg(request):
    midno=request.POST.get('midno')
    mname=request.POST.get('mname')
    mcontact=request.POST.get('mcontact')
    memail=request.POST.get('memail')
    mpassword = str(int(midno) + len(mname))
    mpassword = mcontact[0] + mpassword + mcontact[-1]
    mpassword = memail[0] + mpassword[:int(len(mpassword) / 2)] + memail[5] + mpassword[int(len(mpassword) / 2):] + memail[4]
    MerchantMdel(indo=midno,name=mname,contact=mcontact,email=memail,password=mpassword).save()
    subject="your Merchent id is successfily register  "
    message='Hello user your user id :'+memail+' your password :'+mpassword
    send_mail(subject,message,se.EMAIL_HOST_USER,[memail])
    return render(request,'mlogin.html',{"message":'Your Merchent email' '-' +memail+' successfully Register'} )


def viewmr(request):
    viewmr=MerchantMdel.objects.all()
    return render(request,'viewmr.html',{'details':viewmr})


def adhome(request):
    return render(request,'adhome.html')

def delmt(request):
    viewmr = MerchantMdel.objects.all()
    return render(request, 'delmt.html', {'details': viewmr})



def deleteMerchant(request):
    delid = request.GET.get('merchdel')
    MerchantMdel.objects.filter(indo=delid).delete()
    return delmt(request)


def logout(request):
    return render(request,'show.html')


class Merchentpagelogin(View):
    def get(self,request,email,password):
        try:
            data=MerchantMdel.objects.get(email=email,password=password)
            dict={
                "indo":data.indo,
                "name":data.name,
                "contact":data.contact,
                "email":data.email,
                "password":data.password
            }

            json_data=json.dumps(dict)
            # json_data=serialize('json',[data])

            return HttpResponse(json_data,content_type='application/json',status=200)
        except MerchantMdel.DoesNotExist:
            check={'key':'invalid username and password'}
            json_data= json.dumps(check)
            return HttpResponse(json_data,content_type='application/json',status=500)

@method_decorator(csrf_exempt,name="dispatch")
class Change(View):
    def put(self,requst,email,password):
        try:
            newpassword=MerchantMdel.objects.get(email=email,password=password)
        except MerchantMdel.DoesNotExist :
            d1= "Given EMAIL and PASSWORD is Invalid"
            json_mp = json.dumps(d1)
            return HttpResponse(json_mp, content_type="application/json",status=500)
        else:
            old_password={'email':newpassword.email,'password':newpassword.password,'indo':newpassword.indo,'name':newpassword.name,'contact':newpassword.contact}
            data=requst.body
            newpass=json.loads(data)
            print(newpass)
            old_password.update(newpass)
            mp =Merchentnewpassword(old_password,instance=newpassword)
            print(mp)
            if mp.is_valid():
                mp.save()
                d1="NEW Password is Updated"
                json_mp = json.dumps(d1)
                return HttpResponse(json_mp, content_type="application/json",status=200)
            if mp.errors:
                json_mp = json.dumps(mp.errors)
                return HttpResponse(json_mp, content_type="application/json",status=500)

@method_decorator(csrf_exempt,name="dispatch")
class Productsave(View):
    def post(self,request):
        data=request.body # reading data from post( post method will send data in body)
        merproduct=json.loads(data)# the post will give data in bytes format
        pm=MerchantProduct(merproduct) # Writing data into Database using forms
        if pm.is_valid():
            pm.save()
            jd=json.dumps("products are saved")
            return HttpResponse(jd,content_type='application/json',status=200)
        if pm.errors:
            jd = json.dumps(pm.errors)
            return HttpResponse(jd, content_type="application/json",status=500)
