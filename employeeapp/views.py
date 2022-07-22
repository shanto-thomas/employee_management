import base64

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from employeeapp.models import Employee


def loginhome(request):
    # user = User.objects.all()
    return render(request, "login.html")
def employeehome(request):
    # user = User.objects.all()
    employee =Employee.objects.all()
    # print(employee)
    datalist=[]
    for i in employee:
        # print(i.text.decode('utf-8'))

        sample_string = i.text
        sample_string_bytes = sample_string.encode("ascii")

        base64_bytes = base64.b64encode(sample_string_bytes)
        # base64_string = base64_bytes.decode("ascii")

        print(base64_bytes)
        data={
            "emp_id" :i.emp_id,
            "name" :i.name,
            "password" :i.password,
            "email" :i.email,
            "phone" :i.phone,
            "address" :i.address,
            "image" :str(i.image),
            "text" :base64_bytes

        }
        datalist.append(data)
    # print(datalist)
    return render(request, "ViewEmployee.html",{'data': datalist})

def addpage(request):
    # user = User.objects.all()
    return render(request, "AddingEmployee.html")
def login(request):
    # user = User.objects.all()
    if request.method == 'POST':
        print("helloo")
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email=="admin@gmail.com" and password=="admin123":

            return redirect('/employeehome')
        else:
            if Employee.objects.filter(email=email, password=password):
                return redirect('/employeehome')
            else:
                return HttpResponse("<script>alert('Invaild username and password!');window.location.href='/';</script>")


def newpostpage(request):
    # user = User.objects.all()
    return render(request, "newpostpage.html")
def addpost(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        category = request.POST.get('category')
        tag = request.POST.get('tag')
        content = request.POST.get('content')
        print("grdgth",heading)
        return redirect('/newpostpage')

def addingemployee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        image = request.FILES['image']
        print(image)
        if Employee.objects.all():
            emp = Employee.objects.latest('id')
            # if inqry:
            emp_series = "EMP-"
            emp_id = 1 + int(emp.id)
            Employee.objects.create(emp_id=str(emp_series)+str(emp_id),
                                    name = name,
                                    email = email,
                                    password = password,
                                    phone = phone,image=image,text=image,
                                    address = address)

            return redirect('/employeehome')
        else:
            Employee.objects.create(emp_id="EMP-0",
                                    name=name,
                                    email=email,
                                    password=password,
                                    phone=phone, image=image, text=image,
                                    address=address)
