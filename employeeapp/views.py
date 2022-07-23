# Create your views here.
import base64

from django.http import HttpResponse
from django.shortcuts import render, redirect
from employeeapp.models import Employee


def loginhome(request):
    return render(request, "login.html")


def employeehome(request):
    employee = Employee.objects.all()

    datalist = []
    if employee:
        for i in employee:
            data = {
                "emp_id": i.emp_id,
                "name": i.name,
                "password": i.password,
                "email": i.email,
                "phone": i.phone,
                "address": i.address,
                "image": base64.b64encode(i.image).decode()

            }
            datalist.append(data)
    else:
        pass

    return render(request, "ViewEmployee.html", {'data': datalist})


def addpage(request):
    return render(request, "AddingEmployee.html")


def login(request):
    if request.method == 'POST':
        print("helloo")
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == "admin@gmail.com" and password == "admin123":

            return redirect('/employeehome')
        else:
            if Employee.objects.filter(email=email, password=password):
                return redirect('/employeehome')
            else:
                return HttpResponse(
                    "<script>alert('Invaild username and password!');window.location.href='/';</script>")


def newpostpage(request):
    return render(request, "newpostpage.html")


def addingemployee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        image = request.FILES['image']

        if Employee.objects.all():
            emp = Employee.objects.latest('id')

            emp_series = "EMP-"
            emp_id = 1 + int(emp.id)
            Employee.objects.create(emp_id=str(emp_series) + str(emp_id),
                                    name=name,
                                    email=email,
                                    password=password,
                                    phone=phone, image=image.read(),
                                    address=address)

            return redirect('/employeehome')
        else:
            Employee.objects.create(emp_id="EMP-0",
                                    name=name,
                                    email=email,
                                    password=password,
                                    phone=phone, image=image.read(),
                                    address=address)
            return redirect('/employeehome')
