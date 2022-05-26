from django.shortcuts import render,HttpResponse
from .models import Books,Teacher,Student


# Create your views here.
def index(request):
    return render(request,'index.html')

def allbooks(request):
    bks = Books.objects.all()
    context = {
        'bks': bks

    }
    print(context)
    return render(request, 'books.html', context)

def allteacher(request):
    tks = Teacher.objects.all()
    context = {
        'tks': tks

    }
    print(context)
    return render(request, 'allteacher.html', context)

def allstudent(request):
    sks = Student.objects.all()
    context = {
        'sks': sks

    }
    print(context)
    return render(request, 'allstudent.html', context)

def teach(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        dept = request.POST['dept']
        phone = int(request.POST['phone'])
        email = request.POST['email']

        tc = Teacher(fname=fname, lname=lname, dept=dept, phone=phone, email=email)
        tc.save()
        return HttpResponse('Teacher Added successfully')
    elif request.method == 'GET':
        return render(request, 'teacher_login.html')
    else:
        return HttpResponse('An Exception Occured')

def student(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        dept = request.POST['dept']
        phone = int(request.POST['phone'])
        email = request.POST['email']

        sc = Student(fname=fname, lname=lname, dept=dept, phone=phone, email=email)
        sc.save()
        return HttpResponse('Student Added successfully')
    elif request.method == 'GET':
        return render(request, 'student_login.html')
    else:
        return HttpResponse('An Exception Occured')

def filterbooks(request):
    if request.method == 'POST':
        name = request.POST['name']
        publication = request.POST['publication']
        author = request.POST['author']
        bks = Books.objects.all()
        if name:
            bks = bks.filter(bname__icontains=name)

        if publication:
            bks = bks.filter(publication__icontains=publication)
        if author:
            bks = bks.filter(author__icontains=author)
        context = {
            'bks': bks

        }
        return render(request, 'books.html', context)
    elif request.method == 'GET':
        return render(request, 'filter.html')
    else:
        return HttpResponse('An exception Occured')


def removebooks(request, bkid = 0):
    if bkid:
        try:
            bk_to_be_removed = Books.objects.get(id=bkid)
            bk_to_be_removed.delete()
            return HttpResponse('Book Removed Successfully')
        except:
            return HttpResponse('Please Enter a Valid Book')
    bks = Books.objects.all()
    context = {
        'bks': bks

    }
    return render(request,'remove.html', context)

def addbooks(request):
    if request.method == 'POST':
        bid= request.POST['bid']
        bname = request.POST['bname']
        author = request.POST['author']
        publication = request.POST['publication']
        price = int(request.POST['price'])

        new_bk = Books(bid=bid, bname= bname, author= author, publication= publication, price= price)
        new_bk.save()
        return HttpResponse('Book Added successfully')
    elif request.method=='GET':
        return  render(request,'addbooks.html')
    else:
        return HttpResponse('An Exception Occured')