from django.shortcuts import render,redirect
import requests
import json
from django.contrib import messages
from django.core.serializers import serialize

def showIndex(request):
    request.COOKIES["merchent_id"]
    return render(request,"index.html")

def changepassword(request):
    return render(request,'changepassword.html')

def logout(request):
    log=redirect('main')
    log.set_cookie('merchent_id',None)
    print(request.COOKIES['merchent_id'])
    return log


def mhome(request):
    return render(request,'mhome.html')

def merlogin(request):
    merchent_login=request.POST.get('merchentuser')
    merchent_password=request.POST.get('merchentpass')
    try:
        result=requests.get('http://192.168.43.161:8000/merchentpagelogin/'+merchent_login+'&'+merchent_password)
        if result.status_code==200:
            json_data=result.json()
            response=render(request,'merchentproduct.html',{'data':json_data})
            response.set_cookie("merchent_id",json_data.get('indo'))
            # print(json_data)
            # print(type(json_data))
            return response
        else:
            messages.error(request,'invalid username and password')
            return redirect('main')
    except requests.exceptions.ConnectionError:
        messages.error(request,'server not avaliable')
        return redirect('main')


def passwordchange(request):
    merchentemail=request.POST.get('merchentemail')
    merchentoldpass=request.POST.get('merchentoldpass')
    merchentnewpass=request.POST.get('merchentnewpass')
    merchentconformpass=request.POST.get('merchentconformpass')

    if merchentnewpass==merchentconformpass:
        di = {'password': merchentnewpass}
        json_data = json.dumps(di)  # convert dict data to json data using dumps
        try:
            res=requests.put('http://192.168.43.161:8000/change/'+merchentemail+'&'+merchentoldpass+'/',data=json_data)
            # messages.error(request,'Merchent Password Has Change')
        except requests.exceptions.ConnectionError:
            messages.error(request,'server Not Avaliable')
            return redirect('/changepassword/')
        else:
            if res.status_code==200:
                response=res.json()
                messages.success(request,response)
                return redirect('/changepassword/')
            else:
                # response = res.json()
                messages.error(request,"Invalid Username and Password")
                return redirect('/changepassword/')
    else:
        messages.error(request,'plz chech new and old password')
        return redirect('/changepassword/')


def productpage(request):
    merchent_id=request.COOKIES["merchent_id"]
    print(merchent_id)
    return render(request,'productpage.html',{'merchent_id':merchent_id})


def saveproduct(request):
    productno=request.POST.get('productno')
    productname=request.POST.get('productname')
    productprice=request.POST.get('productprice')
    productqty=request.POST.get('productqty')
    merchant_id=request.POST.get("pmerchentid")
    productdict={
        'product_no':productno,
        'product_name':productname,
        'product_price':productprice,
        'product_qty':productqty,
        'merchant_id':merchant_id
    }
    json_data=json.dumps(productdict)
    try:
        result=requests.post('http://192.168.43.161:8000/saveproduct/',data=json_data)
    except requests.exceptions.ConnectionError:
        messages.error(request,'server not avaliable')
        return redirect("mproductpage")
    else:
        if result.status_code==200:
            rj=result.json()
            messages.success(request,rj)
            return redirect("mproductpage")
        else:
            rj=result.json()
            messages.error(request,rj)
            return redirect("mproductpage")


