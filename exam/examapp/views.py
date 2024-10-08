from django.shortcuts import render,redirect
from examapp.models import Register,Trangection
# Create your views here.

def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        data=Register(
            name=name,
            email=email,
            password=password,
            amount1=0
        )
        data.save()
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        
        username=request.POST['username']
        password=request.POST['password']

        data=Register.objects.filter(name=username,
                                     password=password).first()
      

        if data:
            data_id=data.id
            # print(data_id)
            return redirect(f'/dashboard/{data_id}')
        else :
            return render(request,'error.html')
      
    return render(request,'login.html')


def dashboard(request,id):

    data=Register.objects.filter(id=id).get()
    

    data2=Trangection.objects.filter(userid=id)


    data3=Trangection.objects.filter(userid=id).values('amount')
    data3=[i['amount'] for i in data3]
    data3=sum(data3)


    contex={'user_id':id,'username':data,'transactions':data2,'blance':data3}
    return render(request,'dashboard.html',contex)


def transction(request,id):
    print('id',id)
    if request.method == 'POST':
        
        username=request.POST['username']
        amount=request.POST['amount']
        description=request.POST['description']

       
        data=Trangection(
            userid_id=id,
            user_name=username,
            amount=amount,
            description=description,
        )

        data.save()
        
        return redirect(f'/dashboard/{id}')
    return render(request,'transection.html')
    

def update(request,id):

    if request.method == 'POST':
        
        username=request.POST['username']
        amount=request.POST['amount']
        description=request.POST['description']

        data=Trangection.objects.filter(id=id).update(
            user_name=username, 
            amount=amount, 
            description=description
        )
        id=Trangection.objects.filter(id=id).values('userid')
        # print(id)
        id=id[0]['userid']
        # print(id)
        return redirect(f'/dashboard/{id}')
    show=Trangection.objects.filter(id=id).get()


    return render(request,'transection.html',{'updates':show})



def delete(request,id):

    user = Trangection.objects.filter(id=id).values('userid')
    user=[i['userid'] for i in user]
    user = user[0]
    print(user)
    Trangection.objects.filter(id=id).delete()
    
    
    return redirect(f'/dashboard/{user}')

