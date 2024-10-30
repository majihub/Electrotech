from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Cart, Payment, Products, customers, favourites
# Create your views here.
def home(request):
    if 'id' in request.session:
        session_id=request.session['id']
        user=customers.objects.get(id=session_id)
        return render(request,"home.html",{'user':user,'sessionid':session_id})
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['password']
        user=customers.objects.filter(Email=email,Password=pwd)
        if user:
            getuser=customers.objects.get(Email=email)
            request.session['id']=getuser.id
            print(getuser.id)
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,'login.html')
def logout(request):
    del request.session['id']
    return redirect('/')
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        pwd=request.POST['password']
        cpass=request.POST['cpassword']
        ph=request.POST['mobile']
        country=request.POST['country']
        district=request.POST['district']
        address=request.POST['address']
        emailexists=customers.objects.filter(Email=email)
        if emailexists:
            messages.error(request,"Email ID already registered")
        elif pwd!=cpass:
            messages.error(request,"Password does not match")
        else:
            customers.objects.create(UserName=name,Email=email,Password=pwd,Mobile=ph,Country=country,District=district,Address=address)
            return redirect('login')
    return render(request,'register.html')
def products(request):
    if 'id' in request.session:
        session_id=request.session['id']
        user=customers.objects.get(id=session_id)
        return render(request,"products.html",{'user':user,'sessionid':session_id})
    return render(request,"products.html")
def shoppingitems(request,productitem):
    if 'id' in request.session:
        session_id=request.session['id']
        user=customers.objects.get(id=session_id)
        product=Products.objects.filter(ProductType=productitem)
        return render(request,"shoppingproducts.html",{'product':product,'producttype':productitem,'user':user,'sessionid':session_id})
    else:
        product=Products.objects.filter(ProductType=productitem)
        return render(request,"shoppingproducts.html",{'product':product,'producttype':productitem})
def add_to_cart(request,id):
    if 'id' in request.session:
        session_id=request.session['id']
        user=customers.objects.get(id=session_id)
        product=Products.objects.get(id=id)
        cartitemexists=Cart.objects.filter(ProductID=product)
        if cartitemexists:
            item=Cart.objects.get(ProductID=product)
            item.Quantity+=1
            item.save()
        else:
            Cart.objects.create(ProductID=product,UserID=user,Price=product.Price)
        return redirect('products')
    else:
        return redirect('login')
def mycart(request):
    if 'id' in request.session:
        session_id=request.session['id']
        user=customers.objects.get(id=session_id)
        cart=Cart.objects.filter(UserID=user)
        product=[]
        result=0
        for i in cart:
            cartitem=Cart.objects.get(id=i.id)  
            cartitem.Price=cartitem.ProductID.Price*cartitem.Quantity
            cartitem.save()
            result=result+cartitem.Price
        print(result)
        return render(request,'mycart.html',{'cart':cart,'result':result,'product':product,'sessionid':session_id,'user':user})
    else:
        return redirect('login')
def payment(request):
    if 'id' in request.session:
        session_id=request.session['id']
        user=customers.objects.get(id=session_id)
        cart=Cart.objects.filter(UserID=user)
        result=0
        for i in cart:  
            result=result+i.Price
        if request.method=='POST':
            cardnum=request.POST['cardnumber']
            expiry=request.POST['expirydate']
            cvv=request.POST['cvv']
            Payment.objects.create(CardNumber=cardnum,cvv=cvv,expiry=expiry,PaidUser=user.UserName)
            item=Cart.objects.filter(UserID=user)
            for i in item:
                i.delete()
            messages.success(request,"Your payment successfull")
        return render(request,"payment.html",{'result':result,'user':user,'sessionid':session_id})
    return render(request,"payment.html")
def delete_cart_item(request,id):
    item=Cart.objects.get(id=id)
    item.delete()
    return redirect('mycart')
def update_cart(request,id,op):
    item=Cart.objects.get(id=id)
    if op=='plus':
        item.Quantity+=1
        item.save()
        return redirect('mycart')
    elif op=='minus':
        if item.Quantity>1:
            item.Quantity-=1
            item.save()
            return redirect('mycart')
        else:
            item.delete()
            return redirect('mycart')
def add_to_fav(request,id):
    if 'id' in request.session:
        session_id=request.session['id']
        user=customers.objects.get(id=session_id)
        product=Products.objects.get(id=id)
        itemexists=favourites.objects.filter(ProductID=product)
        if itemexists:
            messages.error(request,"Already added to favourites")
            return redirect('products')
        else:
            favourites.objects.create(ProductID=product,UserID=user)
            return redirect('products')
def my_favourites(request):
    if 'id' in request.session:
        session_id=request.session['id']
        user=customers.objects.get(id=session_id)
        fav=favourites.objects.filter(UserID=user)
        return render(request,"favourites.html",{'fav':fav,'session_id':session_id,'user':user})
def delete_item(request,id):
    item=favourites.objects.get(id=id)
    item.delete()
    return redirect('favourites')
def clear(request):
    if 'id' in request.session:
        session_id=request.session['id']
        user=customers.objects.get(id=session_id)
        fav=favourites.objects.filter(UserID=user)
        for i in fav:
            i.delete()
        return redirect('favourites')