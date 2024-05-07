from django.db import models

class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)



class worker_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dob=models.DateField()
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    photo=models.FileField()


class supervisor_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    dob = models.DateField()
    joindate = models.DateField()
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    photo = models.FileField()
    proof = models.FileField()


class resources_table(models.Model):
    SUPERVISOR=models.ForeignKey(supervisor_table, on_delete=models.CASCADE)
    date=models.DateField()
    product_type=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    manufacturer=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    model_number=models.CharField(max_length=100)
    photo=models.FileField()

class assignworksup_table(models.Model):
    SUPERVISOR=models.ForeignKey(supervisor_table, on_delete=models.CASCADE)
    RESOURCE=models.ForeignKey(resources_table, on_delete=models.CASCADE)
    work=models.CharField(max_length=300)
    details=models.CharField(max_length=200)
    status=models.CharField(max_length=100)
    date=models.DateField()
    updated_date = models.DateField()


class assignworkworker_table(models.Model):
    ASSIGNWORK=models.ForeignKey(assignworksup_table, on_delete=models.CASCADE)
    WORKER=models.ForeignKey(worker_table, on_delete=models.CASCADE)
    work=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date=models.DateField()
    updated_date=models.DateField()


class complaint_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=500)
    reply=models.CharField(max_length=500)
    date=models.DateField()


class tosuprvsrcomplaint_table(models.Model):
    SUPERVISOR = models.ForeignKey(supervisor_table, on_delete=models.CASCADE)
    WORKEER = models.ForeignKey(worker_table, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=500)
    reply=models.CharField(max_length=500)
    date=models.DateField()


class chat_table(models.Model):
    fromid=models.ForeignKey(login_table,on_delete=models.CASCADE,related_name='fromid')
    toid=models.ForeignKey(login_table,on_delete=models.CASCADE,related_name='toid')
    message=models.CharField(max_length=100)
    date=models.DateField()


class doubt_table(models.Model):
    WORKER=models.ForeignKey(worker_table, on_delete=models.CASCADE)
    doubt=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    date=models.DateField()

class feedback_table(models.Model):
    WORKER=models.ForeignKey(worker_table, on_delete=models.CASCADE)
    # SUPERVISOR=models.ForeignKey(supervisor_table, on_delete=models.CASCADE)
    RESOURCE=models.ForeignKey(resources_table, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=500)
    date=models.DateField()

class dailydetails_table(models.Model):
    date=models.DateField()
    unit=models.FloatField()







