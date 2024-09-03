from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.form import *


def admin_log(request):
    if request.method=='POST':
        form=AdminLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('UserName')
            password=form.cleaned_data.get('Password')
            res = Login.objects.filter(UserName=username, Password=password)
            if res.exists():
                log=Login.objects.get(UserName=username, Password=password)
                request.session['lid'] = log.id
                if log.Type == "user":
                    return HttpResponse('''<script>alert('Login Successfully');window.location="/myapp/user_home/"</script>''')
                elif log.Type == 'admin':
                  return HttpResponse('''<script>alert('Login Successfully');window.location="/myapp/admin_home/"</script>''')

            else:
                return HttpResponse('''<script>alert('Incorrect Password');</script>''')


    else:
     form=AdminLoginForm()
     return render(request,'login_index.html',{'form':form})

def company(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')
    if request.method=='POST':
        form=CompanyProfile(request.POST,request.FILES)
        if form.is_valid():
            photo=form.cleaned_data['Photo']
            x=FileSystemStorage()
            date=datetime.now().strftime('%y%m%d=%H%M%S')+".jpeg"
            fn=x.save(date,photo)

            comp=Company(
                CompanyName=form.cleaned_data['CompanyName'],
                Address=form.cleaned_data['Address'],
                PhoneNumber=form.cleaned_data['PhoneNumber'],
                Email=form.cleaned_data['Email'],
                Website=form.cleaned_data['Website'],
                SocialMedia=form.cleaned_data['SocialMedia'],
                AboutUs=form.cleaned_data['AboutUs'],
                ServiceOffered=form.cleaned_data['SeviceOffered'],
                Logo=x.url(date),
            )
            comp.save()
            return HttpResponse('ok')
        else:
            return HttpResponse("Error")
    else:
        c1=CompanyProfile()
        return render(request,'company.html',{'form':c1})
def admin_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')
    return render(request,'admin_index_home.html')

def view_company(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    cc=Company.objects.all()
    print(cc)
    return render(request,'view_company.html',{'company':cc})


def services(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    if request.method=='POST':
        form=Service_form(request.POST)
        if form.is_valid():
            ser=Services(
                Service =form.cleaned_data['Service'],
                Description=form.cleaned_data['Description'],
                Price=form.cleaned_data['Price'],
                LOGIN=Login.objects.get(id=request.session['lid']),
            )
            ser.save()
            return HttpResponse('''<script>alert('Add Successfully');window.location="/myapp/admin_home/"</script>''')
        else:
            return HttpResponse('error')
    else:
        s1=Service_form()
        return render(request,'service.html',{'form':s1})


def view_service(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    vv=Services.objects.all()
    return render(request,'view_services.html',{"service":vv})

def edit_service(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    ed=Services.objects.get(id=id)
    return render(request,'edit_service.html',{"service":ed})
def view_edview(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    service=request.POST['S1']
    description=request.POST['D1']
    price=request.POST['P1']
    id=request.POST['id']

    obj=Services.objects.get(id=id)
    obj.Service=service
    obj.Description=description
    obj.Price=price
    obj.save()
    return HttpResponse('''<script>alert('Edit Successfully');window.location="/myapp/view_service/"</script>''')

def delete(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    Services.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('Delete Successfully');window.location="/myapp/view_service/"</script>''')


def manage_gallery(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    if request.method=='POST':
        form=Gallery_form(request.POST,request.FILES)
        if form.is_valid():
                Image=form.cleaned_data['Images']
                x=FileSystemStorage()
                data=datetime.now().strftime('%y%m%d=%H%M%S')+'.jpeg'
                fn=x.save(data,Image)


                gal=Gallery(
                    Image=x.url(data),
                    Description=form.cleaned_data['Description']

                )
                gal.save()
                return HttpResponse('''<script>alert('Upload Successfully');window.location="/myapp/manage_gallery/"</script>''')
        else:
            return HttpResponse('error')

    else:
        G1=Gallery_form()
        return render(request,'Gallery.html',{"form":G1})


def view_gallery(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    gallery_items=Gallery.objects.all()
    return render(request,'view_gallery.html',{"gallery_items":gallery_items})


def edit_gallery(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    gal=Gallery.objects.get(id=id)
    return render(request,'Edit_gallery.html',{'gallery':gal})

def view_galEdit(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    des=request.POST['des1']
    id=request.POST['id']
    obj=Gallery.objects.get(id=id)
    if 'img1' in request.FILES:
        pht = request.FILES['img1']
        ph = FileSystemStorage()
        date = datetime.now().strftime("%y%m%d-%H%M%S") + ".jpeg"
        ph.save(date, pht)
        path = ph.url(date)
        print("hii")


        obj.Image=path
        obj.Description=des
        obj.save()

    else:

        obj.Description=des
        obj.save()

    return HttpResponse('''<script>alert('Edit Successfully');window.location="/myapp/view_gallery/"</script>''')


def gal_delete(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    Gallery.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('Delete Successfully');window.location="/myapp/view_gallery/"</script>''')



def Register1(request):
    if request.method=='POST':
        form=User_Register(request.POST)
        if form.is_valid():
            lobj=Login(
                UserName=form.cleaned_data['Email'],
                Password=form.cleaned_data['Password'],
                Type="user"
            )
            lobj.save()
            user=Register(
                name=form.cleaned_data['Name'],
                password=form.cleaned_data['Password'],
                email=form.cleaned_data['Email'],
                place=form.cleaned_data['Place'],
                phone=form.cleaned_data['Phone'],
                LOGIN=lobj,
            )
            user.save()
            return HttpResponse('''<script>alert('Register Successfully');window.location="/myapp/admin_log/"</script>''')
        else:
            return HttpResponse('error')
    else:
        R1=User_Register()
        return render(request,'register_index.html',{'form':R1})



def user_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    return render(request,'user_home_index.html')

def view_prof(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    pp = Register.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'view_prof.html',{'data':pp})


def edit_prf(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=Register.objects.get(id=id)
    return render(request,'edit_prof.html',{"prof":aa})


def vw_prf_ed(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    name=request.POST['n1']
    password=request.POST['p1']
    email=request.POST['e1']
    place=request.POST['ph1']
    phone=request.POST['pl']
    id=request.POST['id']

    obj=Register.objects.get(id=id)
    obj.name=name
    obj.password=password
    obj.email=email
    obj.place=place
    obj.phone=phone
    obj.save()
    return HttpResponse('''<script>alert('Edit Successfully');window.location="/myapp/view_prof/"</script>''')



def admn_vw_usr(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=Register.objects.all()
    return render(request,'admn_vw_usr.html',{'aa':aa})


def explore_ser(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=Services.objects.all()
    return render(request,'explore_services.html',{"services":aa})



def request(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=Services.objects.get(id=id)
    bb=Register.objects.get(LOGIN_id=request.session['lid'])
    obj=Request()
    obj.REGISTER_id=bb.id
    obj.SERVICES_id=aa.id
    obj.Status="pending"
    obj.Date=datetime.now().date()
    obj.save()
    return HttpResponse('''<script>alert('Request submitted Successfully');window.location="/myapp/explore_ser/"</script>''')

def admn_vw_request(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=Request.objects.filter(Status='pending')
    return render(request,'vw_request.html',{'data':aa})


def approve(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=Request.objects.filter(id=id).update(Status='Approve')
    return HttpResponse('''<script>alert('Request Approved Successfully');window.location="/myapp/admn_vw_request/"</script>''')


def Reject(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    bb=Request.objects.filter(id=id).update(Status='Reject')
    return HttpResponse('''<script>alert('Request Rejected Successfully');window.location="/myapp/admn_vw_request/"</script>''')


def ad_viw_apprvd_reqst(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=Request.objects.filter(Status='Approve')
    print(aa)
    return render(request,'amn_vw_aprvs.html',{'approved_requests':aa})

def usr_vw_aprv_sts(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    bb=Request.objects.filter(Status='Approve',REGISTER__LOGIN_id=request.session['lid'])
    return render(request, 'user_vw_apprvs.html', {'approved_requests': bb})

def usr_vw_rjct_sts(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    cc=Request.objects.filter(Status='Reject',REGISTER__LOGIN_id=request.session['lid'])
    return render(request, 'user_vw_rejcts.html', {'approved_requests': cc})


def comp(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    return render(request,'compalint.html')

def compost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    com = request.POST['c1']


    obj=Complaint()
    obj.complaint=com
    obj.Reply='pending'
    obj.Status='pending'
    obj.Date = datetime.now().today()
    obj.REGISTER=Register.objects.get(LOGIN__id=request.session['lid'])
    obj.save()

    return HttpResponse(
        '''<script>alert('send complaint Successfully');window.location="/myapp/user_home/"</script>''')




def vw_comp(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=Complaint.objects.all()
    return render(request,'view complaint.html',{'data':aa})


def sendReply(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    return render(request,'snd_reply.html',{"id":id})


def sndReplypost(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    vr=request.POST['r1']
    id=request.POST['srid']
    res=Complaint.objects.filter(id=id).update(Reply=vr,Status="Replayed")
    return HttpResponse('''<script>alert('Reply Successfull');window.location='/myapp/vw_comp/'</script>''')


def reply(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    res=Complaint.objects.filter(REGISTER__LOGIN_id=request.session['lid'])
    return render(request,'view_reply.html',{"data":res})

def chng_pass(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    return render(request,'chng_pass.html')
def chngepass(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    current=request.POST['pas1']
    nwpass=request.POST['npas1']
    cnfmpass=request.POST['cpas1']
    lid=request.session['lid']
    res=Login.objects.filter(id=lid,Password=current)
    if res.exists():
        if nwpass==cnfmpass:
            up=Login.objects.filter(id=lid,Password=current).update(Password=nwpass)
            return HttpResponse('''<script>alert('password changed Successfully');window.location="/myapp/admin_log/"</script>''')
        else:
            return HttpResponse("invalid")

    else:
        return HttpResponse("Fields Cannot Be Empty")


def usr_pass(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    return render(request,'user_chng_pass.html')
def us_chngepass(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    current=request.POST['pas1']
    nwpass=request.POST['npas1']
    cnfmpass=request.POST['cpas1']
    lid=request.session['lid']
    res=Login.objects.filter(id=lid,Password=current)
    if res.exists():
        if nwpass==cnfmpass:
            up=Login.objects.filter(id=lid,Password=current).update(Password=nwpass)
            return HttpResponse('''<script>alert('password changed Successfully');window.location="/myapp/admin_log/"</script>''')
        else:
            return HttpResponse("invalid")

    else:
        return HttpResponse("ok")




def payment1(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=Services.objects.get(id=id)
    bb=Register.objects.get(LOGIN_id=request.session['lid'])
    obj=payment()
    obj.REGISTER_id=bb.id
    obj.SERVICES_id=aa.id
    obj.Date=datetime.now().date()
    obj.price=aa.Price
    obj.save()
    return HttpResponse('''<script>alert('Payment Done Successfully');window.location="/myapp/usr_vw_aprv_sts/"</script>''')

def admn_vw_pymnt(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("PLEASE LOGIN ");window.location="/myapp/admin_log/"</script>''')

    aa=payment.objects.all()
    return render(request,'admn_vw_pymnt.html',{'data':aa})



def land(request):
    return render(request,'landing_index.html')


def emilchnge(request):
    aj=request.POST['Email']
    obj=Register.objects.filter(email=aj).exists()
    return JsonResponse({'status':obj})

def phnchnge(request):
    aj=request.POST['Phone']
    obj=Register.objects.filter(phone=aj).exists()
    return JsonResponse({'status':obj})


def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert("LOGOUT SUCCESSFULL");window.location="/myapp/admin_log/"</script>''')

