from django.shortcuts import render
from django.http import HttpResponse
from . models import Registration


# Create your views here.
def index(request):
    return render(request, 'hospitalApp/index.html')


def FormRegister(request):
    if request.method == "POST":
        patientName = request.POST.get('patientName', '')
        phoneNo = request.POST.get('phoneNo')
        docName = request.POST.get('docName', '')
        specialist = request.POST.get('specialist', '')
        day = request.POST.get('day', '')
        Time = request.POST.get('Time', '')
        AM_PM = request.POST.get('AM_PM', '')
        fees = request.POST.get('fees', '')
        token = request.POST.get('token', '')

        print(patientName, phoneNo, docName,
              specialist, day, Time, AM_PM, fees, token)

        form = Registration(patientName_db=patientName, phoneNo_db=phoneNo, doctorName=docName, specialist_db=specialist,
                            day_db=day, time_db=Time, AM_PM_db=AM_PM, fees_db=fees, tokenNo_db=token)
        form.save()

    return render(request, "hospitalApp/index.html")


def displayData(request):
    patientData = {}
    data = Registration.objects.all()
    patientData = {"patientData": data}

    if request.method == "POST":
        patientName = request.POST.get('patientName')
        # phoneNo = request.POST.get('phoneNo')
        AID = request.POST.get('AID')

        if patientName != '':
            '''
            patient_name = Registration.objects.filter(patientName_db = patientName)
            patientData = {"patientData": patient_name}
            '''

            try:
                patient_name = Registration.objects.filter(
                    patientName_db=patientName)

            except Registration.DoesNotExist:
                print("Patient Name Not Exist")
                # return render(request, "hospitalApp/displayData.html",patientData)

            else:
                patientData = {"patientData": patient_name}

        
        # elif phoneNo != '':
        #     try:
        #         ph = Registration.objects.get(phoneNo_db=phoneNo)

        #     except Registration.DoesNotExist:
        #         print("Not Exist")
        #         # return render(request, "hospitalApp/displayData.html",patientData,mess)

        #     else:
        #         info = Registration.objects.filter(patientName_db=ph)
        #         patientData = {"patientData": info}

        #     '''
        #     ph = Registration.objects.get(phoneNo_db = phoneNo)
        #     info = Registration.objects.filter(patientName_db = ph)
        #     patientData = {"patientData": info}
        #     '''
        

        elif AID != '':
            # print(type(AID))
            AID = int(AID)

            try:
                Registration.objects.get(aid_db=AID).delete()

            except Registration.DoesNotExist:
                print("Delete.")
                # return render(request, "hospitalApp/displayData.html",patientData)
        
    return render(request, "hospitalApp/displayData.html", patientData)


"""
def updateRecord(request):
    patientData = {} 
    
    if request.method == "POST":
        aid = request.POST.get('AID')
        print(aid)
        info = Registration.objects.get(aid_db=aid)
        print(type(info))
        info = Registration.objects.filter(patientName_db = info)
        patientData = {"patientData": info}
        print(patientData)

    return render(request, "hospitalApp/UpdateData.html", patientData)
"""


def updateRecord(request, id):
    info = Registration.objects.get(aid_db=id)

    if request.method == "POST":
        
        patientName = request.POST.get('patientName', '')
        phoneNo = request.POST.get('phoneNo')
        docName = request.POST.get('docName', '')
        specialist = request.POST.get('specialist', '')
        day = request.POST.get('day', '')
        Time = request.POST.get('Time', '')
        AM_PM = request.POST.get('AM_PM', '')
        fees = request.POST.get('fees', '')
        token = request.POST.get('token', '')

        form = Registration(aid_db=id, patientName_db=patientName, phoneNo_db=phoneNo, doctorName=docName, specialist_db=specialist,
                            day_db=day,time_db=Time, AM_PM_db=AM_PM, fees_db=fees, tokenNo_db=token)
        form.save()

    params = {"finalData": info}
    return render(request, "hospitalApp/edit.html", params)


def updateInfo(request):
    result = Registration.objects.all()
    params = {"results": result}
    return render(request, "hospitalApp/updateData.html", params)

def editData(request, id):
    edit_data = Registration.objects.get(aid_db=id)
    params = {"finalData": edit_data}
    return render(request, "hospitalApp/edit.html", params)
