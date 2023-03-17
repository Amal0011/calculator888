from django.shortcuts import render
from django.views.generic import View

from django import forms

class OperationForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField() 


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class LoginForm2(forms.Form):
    first_name = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()
    phno = forms.CharField()


# Create your views here.

class AdditionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):
        print("value inside post", request.POST)
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        res=n1+n2
        print(res)
        return render(request,"add.html",{"result":res})
    
    
class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1-n2
        # print('yes')
        return render(request,"sub.html",{"result":res})
    
class AmstrongView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"amstrong.html")
    
    def post(self,request,*args,**kwargs):
        num=request.POST.get("num")

        ln = len(num)
        sum=0
        num=int(num)
        original=num
        while(num!=0): 
            digit=num%10
            sum=sum+(digit**ln)
            num=num // 10
        result=sum==original
        return render(request,"amstrong.html",{"res":result})
    
class EvenNumbersView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"even.html")
    
    def post(self,request,*args,**kwargs):
        start=request.POST.get("num11")
        stop=request.POST.get("num22")
        start=int(start)
        stop=int(stop)
        evens=[i for i in range(start, stop) if i % 2 == 0]
            
        return render(request,"even.html",{"result":evens})

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

   
class HealthView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"health.html")
        
    def post(self,request,*args,**kwargs):
        tummysize=request.POST.get("tummysize")
        buttocksize=request.POST.get("buttocksize")
        gender=request.POST.get("gender")

        value=int(tummysize) / int(buttocksize)
        value = round(value,2)
        print(value)
        context = {"gender":"", "healthrisk":"", "bodyshape":"","bmi":value}


        if(gender == 'female'):
            if(value <= 0.80):
                context["gender"]="woman"
                context["healthrisk"]="low"
                context["bodyshape"]="pear"
            elif(value <= 0.85 and value >= 0.81):
                context["gender"]="woman"
                context["healthrisk"]="moderate"
                context["bodyshape"]="avocado"
            else:
                context["gender"]="woman"
                context["healthrisk"]="high"
                context["bodyshape"]="apple"

        if(gender == 'male'):
            if(value <= 0.95):
                context["gender"]="male"
                context["healthrisk"]="low"
                context["bodyshape"]="pear"
            elif(value >= 0.96 and value <= 1.0 ):
                context["gender"]="male"
                context["healthrisk"]="moderate"
                context["bodyshape"]="avocado"
            else:
                context["gender"]="male"
                context["healthrisk"]="high"
                context["bodyshape"]="apple"
        print(tummysize,buttocksize,gender)
        print(value)
        return render(request,"health.html",context)
        
class TempView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"degreetofarenheit.html")
        
    def post(self,request,*args,**kwargs):
        degree=request.POST.get("degree")
        farenheit = (int(degree)*9/5) + 32

        return render(request,"degreetofarenheit.html",{"result":farenheit})
    
class ExponentView(View):
    def get(self,request,*args,**kwargs):
        form=OperationForm()
        return render(request,"exponent.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=OperationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1**n2
        return render(request,"exponent.html",{"result":result,"form":form})
    
    

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(request,"login.html",{"form":form})
    
class Login2View(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm2()
        return render(request,"loginform2.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
       form=LoginForm2(request.POST)

       if form.is_valid():
           print(form.cleaned_data)
           
       else:
            print("invalid")


       return render(request,"loginform2.html")
    

      
