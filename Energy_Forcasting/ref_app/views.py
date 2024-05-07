import json
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from ref_app.fo_gru import predictfn
from ref_app.models import *


def login_post(request):
    uname=request.POST['textfield7']
    passw=request.POST['textfield8']
    try:
        ob=login_table.objects.get(username=uname,password=passw)
        if ob.type=='admin':

            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert("Welcome.....");window.location="/admin_home"</script>''')
        elif ob.type=='supervisor':

            request.session['lid']=ob.id
            return HttpResponse('''<script>alert("Welcome.....");window.location="/suphome"</script>''')
        else:
          return HttpResponse('''<script>alert("invalid user");window.location="/"</script>''')
    except:
        return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')

def login(request):
    return render(request,"index.html")


def logout(request):
    return render(request,"index.html")

####################################################Admin############################################################

def admin_home(request):
    return render(request,"adminindex.html")

def addsup(request):
    return render(request,"Admin/addsup.html")

def addsuppost(request):
  try:
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    gender=request.POST['radio']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    email=request.POST['textfield9']
    qualification=request.POST['textfield12']
    dob=request.POST['textfield8']
    joindate=request.POST['textfield11']
    pin=request.POST['textfield6']
    phone=request.POST['textfield7']
    photo=request.FILES['file']
    proof=request.FILES['file1']
    uname=request.POST['textfield1']
    passw=request.POST['textfield10']
    fs = FileSystemStorage()
    fsave = fs.save(photo.name, photo)
    fsave1 = fs.save(proof.name, proof)

    vv=login_table.objects.filter(username__icontains=uname,password__icontains=passw)
    if len(vv)>0:
        return HttpResponse('''<script>alert("Duplicate entry...registration Failed....Retry ");window.location="/mngsupervsr#about"</script>''')
    else:
        ob=login_table()
        ob.username=uname
        ob.password=passw
        ob.type='supervisor'
        ob.save()

        ob1=supervisor_table()
        ob1.LOGIN=ob
        ob1.fname=fname
        ob1.lname=lname
        ob1.gender=gender
        ob1.place=place
        ob1.post=post
        ob1.dob=dob
        ob1.joindate=joindate
        ob1.pin=pin
        ob1.phone=phone
        ob1.email=email
        ob1.qualification=qualification
        ob1.photo=fsave
        ob1.proof=fsave1
        ob1.save()
        return HttpResponse('''<script>alert("Added ");window.location="/mngsupervsr#about"</script>''')
  except:
      return HttpResponse('''<script>alert("Duplicate entry ");window.location="/mngsupervsr#about"</script>''')


def assignsup(request):
    ob=supervisor_table.objects.all()
    ob1=resources_table.objects.all()
    return render(request,"Admin/assignsup.html",{'v':ob,'v1':ob1})

def assignworktosup(request):
    ob=assignworksup_table.objects.all()
    return render(request,"Admin/assignworktosup.html",{'value':ob})


def assigningworktosup(request):
    supervisor=request.POST['select']
    works=request.POST['textfield']
    details=request.POST['textfield2']
    resources=request.POST['select2']
    obb=assignworksup_table.objects.filter(work__iexact=works)
    if len(obb)==0:
        ob=assignworksup_table()
        ob.SUPERVISOR=supervisor_table.objects.get(id=supervisor)
        ob.RESOURCE=resources_table.objects.get(id=resources)
        ob.details=details
        ob.status='Pending'
        ob.work=works
        ob.updated_date = datetime.datetime.today()
        ob.date=datetime.datetime.today()
        ob.save()
        return HttpResponse('''<script>alert("Assigned ");window.location="/assignworks#about"</script>''')
    else:
        return HttpResponse('''<script>alert('Work Already Assigned');window.location='/assignworks'</script>''')


def editassignworkstosup(request,id):
    request.session['ed'] = id
    assignwrk=assignworksup_table.objects.get(id=id)
    ob = supervisor_table.objects.all()
    ob1 = resources_table.objects.all()
    return render(request, "Admin/editworkstosup.html", {'v': ob, 'v1': ob1,"work":assignwrk})

def editassignworkstosuppost(request):
    SUPERVISOR=request.POST['select']
    RESOURCE=request.POST['select2']
    work=request.POST['textfield']
    details=request.POST['textfield2']

    ob1 = assignworksup_table.objects.get(id=request.session['ed'])
    ob1.SUPERVISOR_id=SUPERVISOR
    ob1.RESOURCE_id=RESOURCE
    ob1.work=work
    ob1.details=details
    ob1.save()
    return HttpResponse('''<script>alert("Updated ");window.location="/assignworks#about"</script>''')

def deleteassignworkstosup(request,id):
    ob=assignworksup_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location="/assignworks#about"</script>''')

def editsupervsr(request,id):
    request.session['ed']=id
    ob=supervisor_table.objects.get(id=id)
    return render(request,"Admin/editsupervsr.html",{"val":ob,'date':str(ob.dob),'date2':str(ob.joindate)})

def deletesup(request,id):
    ob=login_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location="/mngsupervsr#about"</script>''')

def searchsup(request):
    search=request.POST['textfield']
    ob=supervisor_table.objects.filter(fname__istartswith=search)
    return render(request, "Admin/mngsupervsr.html", {"val": ob})

def editsuppost(request):
   if "file" in request.FILES and 'file1' in request.FILES:
       fname = request.POST['textfield']
       lname = request.POST['textfield2']
       gender = request.POST['radio']
       place = request.POST['textfield4']
       post = request.POST['textfield5']
       email = request.POST['textfield9']
       dob = request.POST['textfield8']
       pin = request.POST['textfield6']
       phone = request.POST['textfield7']
       photo = request.FILES['file']
       qualification = request.POST['textfield12']
       joindate = request.POST['textfield11']
       proof = request.FILES['file1']
       fs = FileSystemStorage()
       fsave = fs.save(photo.name, photo)
       fsave1 = fs.save(proof.name, proof)

       ob1 = supervisor_table.objects.get(id=request.session['ed'])
       ob1.fname = fname
       ob1.lname = lname
       ob1.gender = gender
       ob1.place = place
       ob1.post = post
       ob1.dob = dob
       ob1.joindate = joindate
       ob1.qualification = qualification
       ob1.pin = pin
       ob1.phone = phone
       ob1.email = email
       ob1.photo = fsave
       ob1.proof = fsave1
       ob1.save()
       return HttpResponse('''<script>alert("Updated ");window.location="/mngsupervsr#about"</script>''')
   elif 'file1' in request.FILES:
       fname = request.POST['textfield']
       lname = request.POST['textfield2']
       gender = request.POST['radio']
       place = request.POST['textfield4']
       post = request.POST['textfield5']
       email = request.POST['textfield9']
       dob = request.POST['textfield8']
       pin = request.POST['textfield6']
       phone = request.POST['textfield7']
       qualification = request.POST['textfield12']
       joindate = request.POST['textfield11']
       proof = request.FILES['file1']
       fs = FileSystemStorage()
       fsave1 = fs.save(proof.name, proof)

       ob1 = supervisor_table.objects.get(id=request.session['ed'])
       ob1.fname = fname
       ob1.lname = lname
       ob1.gender = gender
       ob1.place = place
       ob1.post = post
       ob1.dob = dob
       ob1.joindate = joindate
       ob1.qualification = qualification
       ob1.pin = pin
       ob1.phone = phone
       ob1.email = email
       ob1.proof = fsave1
       ob1.save()
       return HttpResponse('''<script>alert("Updated ");window.location="/mngsupervsr#about"</script>''')

   elif "file" in request.FILES:
       fname = request.POST['textfield']
       lname = request.POST['textfield2']
       gender = request.POST['radio']
       place = request.POST['textfield4']
       post = request.POST['textfield5']
       email = request.POST['textfield9']
       dob = request.POST['textfield8']
       pin = request.POST['textfield6']
       phone = request.POST['textfield7']
       photo = request.FILES['file']
       qualification = request.POST['textfield12']
       joindate = request.POST['textfield11']
       fs = FileSystemStorage()
       fsave = fs.save(photo.name, photo)

       ob1 = supervisor_table.objects.get(id=request.session['ed'])
       ob1.fname = fname
       ob1.lname = lname
       ob1.gender = gender
       ob1.place = place
       ob1.post = post
       ob1.dob = dob
       ob1.joindate = joindate
       ob1.qualification = qualification
       ob1.pin = pin
       ob1.phone = phone
       ob1.email = email
       ob1.photo = fsave
       ob1.save()
       return HttpResponse('''<script>alert("Updated ");window.location="/mngsupervsr#about"</script>''')
   else:
       fname = request.POST['textfield']
       lname = request.POST['textfield2']
       gender = request.POST['radio']
       place = request.POST['textfield4']
       post = request.POST['textfield5']
       email = request.POST['textfield9']
       dob = request.POST['textfield8']
       joindate = request.POST['textfield11']
       pin = request.POST['textfield6']
       phone = request.POST['textfield7']
       qualification = request.POST['textfield12']



       ob1 = supervisor_table.objects.get(id=request.session['ed'])
       ob1.fname = fname
       ob1.lname = lname
       ob1.gender = gender
       ob1.place = place
       ob1.post = post
       ob1.dob = dob
       ob1.pin = pin
       ob1.joindate = joindate
       ob1.qualification = qualification
       ob1.phone = phone
       ob1.email = email
       ob1.save()
       return HttpResponse('''<script>alert("Updated ");window.location="/mngsupervsr#about"</script>''')


def editworkstosup(request):
    return render(request,"Admin/editworkstosup.html")

def mngsupervsr(request):
    ob=supervisor_table.objects.all().order_by('-id')
    return render(request,"Admin/mngsupervsr.html",{"val":ob})

def assignworks(request):
    ob=assignworksup_table.objects.all().order_by('-id')
    return render(request,"Admin/assignworktosup.html",{'value':ob})


def Verifyworker(request):
    ob=worker_table.objects.all().order_by('-id')
    return render(request,"Admin/Verifyworker.html",{"val":ob})

def acceptworker(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='Worker'
    ob.save()
    return HttpResponse('''<script>alert("Accepted ");window.location="/Verifyworker#about"</script>''')

def rejectworker(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='Rejected'
    ob.save()
    return HttpResponse('''<script>alert("Rejected ");window.location="/Verifyworker#about"</script>''')


def verifyworkersearch(request):
    fname = request.POST['textfield']
    ob = worker_table.objects.filter(fname__istartswith=fname)
    return render(request, "Admin/Verifyworker.html", {'val': ob, 'n': fname})

def viewcomplandsendreply(request):
    # ob = complaint_table.objects.filter(LOGIN__type="supervisor")
    ob = complaint_table.objects.all().order_by('-id')
    print(request.session['lid'])
    return render(request,"Admin/viewcomplandsendreply.html",{'val':ob})


def viewcomplandsendreply_search(request):
    fname=request.POST['textfield']
    ob=complaint_table.objects.filter(LOGIN__username__istartswith=fname)
    return render(request, "Admin/viewcomplandsendreply.html",{'val': ob})




def adminsendreply(request,id):
    request.session['comid'] = id
    ob=complaint_table.objects.get(id=id)
    return render(request, "Admin/adminsendreply.html",{"val":ob})


def adminsendreply_post(request):
    rep=request.POST['textfield']
    ob = complaint_table.objects.get(id=request.session['comid'])
    ob.reply = rep
    ob.save()
    return HttpResponse('''<script>alert("Sended ");window.location="/viewcomplandsendreply#about"</script>''')




def viewfeedbck(request):
    ob=feedback_table.objects.all().order_by('-id')
    return render(request,"Admin/viewfeedbck.html",{"val":ob})


def viewfeedback_search(request):
    workername=request.POST['textfield']
    ob=feedback_table.objects.filter(WORKER__fname__istartswith=workername)
    return render(request, "Admin/viewfeedbck.html",{"val":ob})


def viewresources(request):
    ob=resources_table.objects.all().order_by('-id')
    return render(request,"Admin/viewresources.html",{"val":ob})

def viewresourcessearch(request):
    product_type = request.POST['textfield']
    ob = resources_table.objects.filter(product_type__istartswith=product_type)
    return render(request, "Admin/viewresources.html", {'val': ob, 'n': product_type})


def viewworkstatus(request):
    return render(request,"Admin/viewworkstatus.html")

######################supervisor#######################################################################################

def addresourc(request):
    return render(request,"Supervisor/addresourc.html")


def editres(request,id):
    ob=resources_table.objects.get(id=id)
    request.session['oid']=ob.id
    return render(request,"Supervisor/editresourc.html",{'val':ob})


def deleteres(request,id):
    ob=resources_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location="/mngresources#about"</script>''')


def addres(request):
    type=request.POST['select']
    name=request.POST['textfield2']
    mn=request.POST['textfield3']
    mnn=request.POST['textfield4']
    det=request.POST['textfield5']
    photo=request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(photo.name,photo)

    ob=resources_table()
    ob.photo=fsave
    ob.product_name=name
    ob.product_type=type
    ob.manufacturer=mn
    ob.model_number=mnn
    ob.details=det
    ob.date=datetime.datetime.now()
    ob.SUPERVISOR=supervisor_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added ");window.location="/mngresources#about"</script>''')





def edittaddres(request):
    try:
        type=request.POST['textfield']
        name=request.POST['textfield2']
        mn=request.POST['textfield3']
        mnn=request.POST['textfield4']
        det=request.POST['textfield5']
        photo=request.FILES['file']
        fs=FileSystemStorage()
        fsave=fs.save(photo.name,photo)

        ob=resources_table.objects.get(id= request.session['oid'])
        ob.photo=fsave
        ob.product_name=name
        ob.product_type=type
        ob.manufacturer=mn
        ob.model_number=mnn
        ob.details=det
        ob.date=datetime.datetime.now()
        ob.save()
        return HttpResponse('''<script>alert("Updated ");window.location="/mngresources#about"</script>''')
    except:
        type = request.POST['textfield']
        name = request.POST['textfield2']
        mn = request.POST['textfield3']
        mnn = request.POST['textfield4']
        det = request.POST['textfield5']

        ob = resources_table.objects.get(id= request.session['oid'])
        ob.product_name = name
        ob.product_type = type
        ob.manufacturer = mn
        ob.model_number = mnn
        ob.details = det
        ob.date = datetime.datetime.now()
        ob.save()
        return HttpResponse('''<script>alert("Updated ");window.location="/mngresources#about"</script>''')


def suphome(request):
    return render(request,"supervsrindex.html")



def assignworkstoworker(request,assinid):
    request.session['assinid']=assinid
    ob=worker_table.objects.all()
    return render(request, "Supervisor/assignworks.html",{'worker':ob})
import datetime
def assignworkstoworker_post(request):
    workerid=request.POST["select"]
    work=request.POST["textfield"]
    deta=request.POST["textfield2"]
    obb=assignworkworker_table.objects.filter(work__iexact=work)
    if len(obb)==0:
        ob=assignworkworker_table()
        ob.ASSIGNWORK_id=request.session['assinid']
        ob.WORKER_id=workerid
        ob.details=deta
        ob.work=work
        ob.date=datetime.datetime.now()
        ob.status="pending"
        ob.updated_date=datetime.datetime.today()
        ob.save()
        # return supviewandassignwork(request)
        # return redirect('/supviewandassignwork')
        return HttpResponse('''<script>alert('Success');window.location='/supviewandassignwork'</script>''')
    else:
        return HttpResponse('''<script>alert('Work Already Assigned');window.location='/supviewandassignwork'</script>''')



def viewassignedworkstoworker(request,id):
    ob=assignworkworker_table.objects.filter(ASSIGNWORK__id=id).order_by('-id')
    return render(request, "Supervisor/viewassignedwork.html",{'val':ob})


def viewassignedworkstoworker_search(request):
    workername=request.POST['textfield']
    ob=assignworkworker_table.objects.filter(WORKER__fname__istartswith=workername)
    return render(request,"Supervisor/viewassignedwork.html",{"val":ob})


def viewsup_updatestatus(request,id):
    request.session['nihal']=id
    ob=assignworksup_table.objects.get(id=id)
    return render(request,"Supervisor/updatestatus.html",{"val":ob})

def updatedstatus(request):
    a=request.POST['select']
    ob=assignworksup_table.objects.get(id= request.session['nihal'])
    ob.status=a
    ob.save()
    return HttpResponse('''<script>alert("Updated ");window.location="/supviewandassignwork#about"</script>''')


def supviewandassignwork(request):
    # request.session['assinid']=assinid
    ob=assignworksup_table.objects.filter(SUPERVISOR__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request, "Supervisor/supviewandassignwork.html",{'value':ob})

def supviewandassignworksearch(request):
    search=request.POST['textfield']
    ob=assignworksup_table.objects.filter(RESOURCE__product_type__istartswith=search,SUPERVISOR__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request,"Supervisor/supviewandassignwork.html",{'value':ob})




# def supviewassignworkupdtstatus(request):
#     status=request.POST['select']
#     ob=assignworksup_table.objects.get()




def editresourc(request):
    return render(request,"Supervisor/editresourc.html")

def mngresources(request):
    ob =resources_table.objects.filter(SUPERVISOR__LOGIN_id=request.session["lid"]).order_by('-id')
    return render(request,"Supervisor/mngresources.html",{'val':ob})


def mngresources_search(request):
    search=request.POST['textfield']
    ob=resources_table.objects.filter(product_type__istartswith=search,SUPERVISOR=request.session["lid"])
    return render(request,"Supervisor/mngresources.html",{'val':ob,'search':search})



def sendcomplaint(request):
    ob=complaint_table.objects.all()
    return render(request,"Supervisor/sendcomplaint.html",{'val':ob})



def sendcomplaint_post(request):
    com=request.POST["textfield"]
    ob=complaint_table()
    ob.complaint=com
    ob.reply="pending"
    ob.date=datetime.datetime.now()
    ob.LOGIN_id=request.session["lid"]

    ob.save()
    return HttpResponse('''<script>alert("Sended ");window.location="/sendcoomplaintandviewreply#about"</script>''')


def sendcoomplaintandviewreply(request):
    ob = complaint_table.objects.all().order_by('-id')
    print(request.session['lid'])
    return render(request,"Supervisor/sendcoomplaintandviewreply.html", {'val': ob})
##########3###                    ################# #############################
def viewworkercomplaintandsendreply(request):
    ob=tosuprvsrcomplaint_table.objects.filter(SUPERVISOR__LOGIN_id=request.session['lid']).order_by('-id')
    print(request.session['lid'])
    return render(request, "Supervisor/viewworkercomplaintandsendreply.html", {'val': ob})


def viewworkercomplaintandsendreply_search(request):
    workername = request.POST['textfield']
    ob = tosuprvsrcomplaint_table.objects.filter(WORKEER__fname__istartswith=workername)
    return render(request, "Supervisor/viewworkercomplaintandsendreply.html", {"val": ob})


def sendreply(request,id):
    request.session["scid"]=id
    ob=tosuprvsrcomplaint_table.objects.get(id=id)
    return render(request,"Supervisor/sendreply.html",{"val":ob})

def sendreply_post(request):
    rep = request.POST["textfield"]
    ob = tosuprvsrcomplaint_table.objects.get(id=request.session["scid"])
    ob.reply = rep
    ob.date = datetime.datetime.now()
    ob.LOGIN_id = request.session["lid"]
    ob.save()
    return HttpResponse('''<script>alert("Sended ");window.location="/viewworkercomplaintandsendreply#about"</script>''')

def viewptr_slr(request):
    return render(request,"Supervisor/slr_prmtrs.html")

def viewptr_wnd(request):
    return render(request,"Supervisor/wnd_prmtrs.html")
############ ##########################################################################33
def sendreplyfordoubt(request):
    return render(request,"Supervisor/sendreplyfordoubt.html")

def updateworkstatus(request):
    return render(request,"Supervisor/updateworkstatus.html")

def viewcomplaintandsendreply(request):
    return render(request, "Supervisor/viewworkercomplaintandsendreply.html")

def viewdoubtandsendreply(request):
    return render(request,"Supervisor/viewdoubtandsendreply.html")

def forecasting(request):
    return render(request,"Supervisor/forecasting.html")

def forecasting_post(request):
    datatype=request.POST['select']
    days=request.POST['textfield']
    if datatype=="solar":
        from ref_app.sample_solar import solar
        res= solar(days)
        print(res,"======================")
        solr=[]
        count=[]
        c=0
        for i in res:

            c=c+1
            print(i[0])
            solr.append(i[0])

            if c==int(days):
                break
        for i2 in range(0,100):
            count.append(i2)


        return render(request, 'Supervisor/graph.html', {'v': res, 'c': solr, 's': count,"type":datatype})
        # return render(request, "Supervisor/forecasting.html",{"img":""})
    elif datatype=="wind":
        from ref_app.sample_wind import wind
        res = wind(days)
        print(res, "======================")
        solr = []
        count = []
        c = 0
        for i in res:
            # count.append(c)
            c = c + 1
            print(i[0])
            solr.append(i[0])
            if c==int(days):
                break
        for i2 in range(0, 100):
            count.append(i2)

        return render(request, 'Supervisor/graph.html', {'v': res, 'c': solr, 's': count,"type":datatype})



        return HttpResponse('''<script>alert("Sended ");window.location="/forecasting#about"</script>''')

#############################Admin chat
def chatwithuser(request):
    ob =supervisor_table.objects.all()
    print(ob,"KKKKKKKKKKKKKKKKKK")
    return render(request, "Admin/fur_chat.html", {'val':ob})
#______________________-cha
def chatview(request):
    ob = supervisor_table.objects.all()
    d=[]
    for i in ob:
        r={"name":i.fname,'photo':str(i.photo.url),'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)

def coun_msg(request,id):
    ob1=chat_table.objects.filter(fromid__id=id,toid__id=request.session['lid'])
    ob2=chat_table.objects.filter(fromid__id=request.session['lid'],toid__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.fromid.id,"msg":i.message,"date":i.date,"chat_id":i.id})
    obu=supervisor_table.objects.get(LOGIN__id=id)
    return JsonResponse({"data":res,"name":obu.fname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})

def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=chat_table()
    ob.fromid=login_table.objects.get(id=request.session['lid'])
    ob.toid=login_table.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.save()
    return JsonResponse({"task":"ok"})
    # refresh messages chatlist

#############################supervisor chat
def chatwithworker(request):
    return render(request, "Supervisor/fur_chat2.html")

def chatview2(request):
    ob = worker_table.objects.all()
    d = []
    for i in ob:
        r = {"name": i.fname, 'photo': str(i.photo.url), 'email': i.email, 'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)
    # ob = login_table.objects.get(id=1)
    # d=[]
    # r={"name":"Admin",'photo':'/media/admin2.png','email':0,'loginid':ob.id}
    # d.append(r)
    # return JsonResponse(d, safe=False)

def coun_msg2(request,id):
    print(id)
    print(id)
    print(id)
    print(id)
    ob1=chat_table.objects.filter(fromid__id=id,toid__id=request.session['lid'])
    ob2=chat_table.objects.filter(fromid__id=request.session['lid'],toid__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id": i.fromid.id, "msg": i.message, "date": i.date, "chat_id": i.id})

    obu = worker_table.objects.get(LOGIN_id=id)
    return JsonResponse({"data": res, "name": obu.fname, "photo": obu.photo.url, "user_lid": obu.LOGIN.id})

#------------------------------------------------------------------------------------------------------------#

def chatwithuser1(request):
    # ob =supervisor_table.objects.all()
    # print(ob,"KKKKKKKKKKKKKKKKKK")
    return render(request, "Supervisor/fur_chat.html", {'val':0})


def chatview1(request):
    ob = login_table.objects.get(id=1)
    d=[]
    r={"name":"Admin",'photo':'/media/admin2.png','email':0,'loginid':ob.id}
    d.append(r)
    return JsonResponse(d, safe=False)

def coun_msg1(request,id):
    ob1=chat_table.objects.filter(fromid__id=id,toid__id=request.session['lid'])
    ob2=chat_table.objects.filter(fromid__id=request.session['lid'],toid__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.fromid.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=login_table.objects.get(id=id)
    print("&&&&&&&&&&&", res)

    return JsonResponse({"data":res,"name":"Admin","photo":"/media/admin2.png","user_lid":obu.id})




def coun_insert_chat1(request,msg,id):
    print("===",msg,1)
    ob=chat_table()
    ob.fromid=login_table.objects.get(id=request.session['lid'])
    ob.toid=login_table.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.save()
    return JsonResponse({"task":"ok"})


####android login###########3

def login_code(request):
    username = request.POST['uname']
    password = request.POST['pass']
    print(username,password)
    try:
        users = login_table.objects.get(username=username, password=password,type="Worker")
        ob=worker_table.objects.get(LOGIN__id=users.id)
        if users is None:
            data = {"task": "invalid"}

        else:
            data = {"task": "valid", "id": users.id,"name":ob.fname,"image":ob.photo.url}
            r = json.dumps(data)
            return HttpResponse(r)
    except Exception as t:

        print(t)
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


def registration(request):
    fname = request.POST['Firstname']
    lname = request.POST['Lastname']
    gender = request.POST['Gender']
    place = request.POST['Place']
    post = request.POST['Post']
    email = request.POST['Email']
    dob = request.POST['Dob']
    pin = request.POST['Pin']
    phone = request.POST['Phone']
    photo = request.FILES['Photo']
    fs=FileSystemStorage()
    fp=fs.save(photo.name,photo)

    username = request.POST['Username']
    password = request.POST['Password']

    ob=login_table.objects.filter(Q(username__icontains=username)|Q(password__icontains=password))

    if len(ob)>0:
        data = {"task": "no"}
        r = json.dumps(data)
        return HttpResponse(r)
    else:

        lob = login_table()
        lob.username = username
        lob.password = password
        lob.type = 'pending'
        lob.save()

        user_obj = worker_table()
        user_obj.fname = fname
        user_obj.lname = lname
        user_obj.gender = gender
        user_obj.place = place
        user_obj.post = post
        user_obj.email = email
        user_obj.dob = dob
        user_obj.pin = pin
        user_obj.phone = phone
        user_obj.photo = fp

        user_obj.LOGIN = lob
        user_obj.save()
        data = {"task": "Success"}
        r = json.dumps(data)
        return HttpResponse(r)

###########Android Servers####################################################################

def viewassignedwork_worker(request):
    lid=request.POST['lid']
    ob=assignworkworker_table.objects.filter(WORKER__LOGIN__id=lid).order_by('-id')
    d=[]
    for i in ob:

        data={"work":i.work,"photo":i.ASSIGNWORK.RESOURCE.photo.url,"det":i.details,"res":i.ASSIGNWORK.RESOURCE.product_type+" "+i.ASSIGNWORK.RESOURCE.product_type,"date":str(i.date),"status":i.status,"Workid":i.id}
        d.append(data)
    r=json.dumps(d)
    return HttpResponse(r)

def updatestatusandroid(request):
    wid=request.POST['wid']
    stts=request.POST['stts']
    ob=assignworkworker_table.objects.get(id=wid)
    ob.status=stts
    ob.save()
    data = {"task": "Success"}
    r = json.dumps(data)
    return HttpResponse(r)

def send_complaints(request):
    lid=request.POST['lid']
    comp=request.POST['comp']
    ob=complaint_table()
    ob.complaint=comp
    ob.date=datetime.datetime.today()
    ob.reply ="pending"
    ob.LOGIN = login_table.objects.get(id=lid)
    ob.save()
    data = {"task": "Success"}
    r = json.dumps(data)
    return HttpResponse(r)


def viewcomplaint(request):
    lid=request.POST['lid']
    ob=complaint_table.objects.filter(LOGIN__id=lid).order_by('-id')
    d=[]
    for i in ob:
        data={"complaint":i.complaint,"date":str(i.date),"reply":i.reply}
        d.append(data)
    r=json.dumps(d)
    print("&&&&&&&&&&&&&", r)
    return HttpResponse(r)


def send_sup_complaints(request):
    lid=request.POST['lid']
    comp=request.POST['comp']
    supervisor=request.POST['Sup_id']
    ob=tosuprvsrcomplaint_table()
    ob.complaint=comp
    ob.SUPERVISOR=supervisor_table.objects.get(id=supervisor)
    ob.date=datetime.datetime.today()
    ob.reply ="pending"
    ob.WORKEER = worker_table.objects.get(LOGIN__id=lid)
    ob.save()
    data = {"task": "Success"}
    r = json.dumps(data)
    return HttpResponse(r)


def view_sup_complaint(request):
    lid=request.POST['lid']
    ob=tosuprvsrcomplaint_table.objects.filter(WORKEER__LOGIN_id=lid).order_by('-id')
    d=[]
    for i in ob:
        data={"complaint":i.complaint,"date":str(i.date),"reply":i.reply, "supervisor":i.SUPERVISOR.fname+""+i.SUPERVISOR.lname}
        d.append(data)
    r=json.dumps(d)
    print("&&&&&&&&&&&&&", r)
    return HttpResponse(r)


def viewsupervisor(request):

    ob=supervisor_table.objects.all().order_by('-id')
    d=[]
    for i in ob:
        data={"supervisor":i.fname+" "+i.lname,"supervisor_id":i.id}
        d.append(data)
    r=json.dumps(d)
    print("&&&&", r)
    return HttpResponse(r)

###################   ANDROID CHAT    ##################################################################

def viewsupervisorchat(request):

    ob=supervisor_table.objects.all().order_by('-id')
    d=[]
    for i in ob:
        data={"supervisor":i.fname+" "+i.lname,"supervisor_id":i.LOGIN.id,"photo":str(i.photo.url)}
        d.append(data)
    r=json.dumps(d)
    print("&&&&", r)
    return HttpResponse(r)

def view_message2(request):
    print("&&&&&&&&&&&&&&&", request.POST)
    fromid = request.POST['fid']
    toid = request.POST['toid']
    mid = request.POST['lastmsgid']

    ob1 = chat_table.objects.filter(fromid__id=fromid, toid__id=toid, id__gt=mid)
    ob2 = chat_table.objects.filter(fromid__id=toid, toid__id=fromid, id__gt=mid)
    ob = ob1.union(ob2)
    ob = ob.order_by("id")
    data = []
    for i in ob:
        r = {"msgid": i.id, "date": str(i.date), "message": i.message, "fromid": i.fromid.id}
        data.append(r)
    print("############", data)
    if len(data) > 0:
        return JsonResponse({"status": "ok", "res1": data})
    else:
        return JsonResponse({"status": "na"})


def in_message2(request):
    print("&&&&&&&&&innnnnnnnnnnnnn&&&&&&", request.POST)

    fromid = request.POST['fid']
    toid = request.POST['toid']
    message = request.POST['msg']
    chat_obj = chat_table()
    chat_obj.fromid = login_table.objects.get(id=fromid)
    chat_obj.toid = login_table.objects.get(id=toid)
    chat_obj.message = message
    chat_obj.date = datetime.datetime.now().today()
    chat_obj.save()
    data = {"status": "send"}
    r = json.dumps(data)
    return HttpResponse(r)

#################################################################################################3#

def send_fbk(request):
    lid=request.POST['lid']
    res=request.POST['res']
    fbk=request.POST['fbk']
    ob=feedback_table()
    ob.date=datetime.datetime.today()
    ob.WORKER=worker_table.objects.get(LOGIN__id=lid)
    ob.RESOURCE=resources_table.objects.get(id=res)
    ob.feedback=fbk
    ob.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)

def resrs(request):
    ob = resources_table.objects.all()
    d = []
    for i in ob:
        data = {"reso": i.product_type+"-"+i.product_name, "rid": str(i.id)}
        d.append(data)
    r = json.dumps(d)
    print("&&&&&&&&&&&&&", r)
    return HttpResponse(r)
