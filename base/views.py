from django.shortcuts import render

from joblib import load

from .models import PredictedResult, ReferralMessage, resultMail, ContactMessage

# Create your views here.


def home(request):
    return render(request, 'base/index.html')


# Importing the ML model for prediction.
model = load('./savedModels/G3model.joblib')

# Predictor views here.


def predictor(request):
    if request.method == 'POST':
        age = request.POST['age']
        gender = request.POST['gender']
        county = request.POST['county']
        maritalStatus = request.POST['maritalStatus']
        coupleDiscordant = request.POST['coupleDiscordant']
        SexWithWoman = request.POST['SexWithWoman']
        SexWithMan = request.POST['SexWithMan']
        condom_use = request.POST['condom_use']
        sw = request.POST['sw']
        pwid = request.POST['pwid']
        testedBefore = request.POST['testedBefore']
        presumedTB = request.POST['presumedTB']
        treatmentTB = request.POST['treatmentTB']
        sti = request.POST['sti']
        rapevictim = request.POST['rapevictim']
        HIVPrEP = request.POST['HIVPrEP']

        y_pred = model.predict(
            [[age, gender, maritalStatus, coupleDiscordant, sw, pwid, testedBefore, presumedTB, treatmentTB]])

        if y_pred <= 0.009:
            y_pred = 'LOW'

        elif y_pred > 0.01 or y_pred <= 0.2:
            y_pred = 'MODERATE'

        elif y_pred > 0.21 or y_pred <= 0.6:
            y_pred = 'HIGH'
        else:
            y_pred = 'HIGH RISK and SHOULD TEST NOW'

        # y_pred = result_out

        userresult = PredictedResult.objects.create(age=age,
                                                    gender=gender,
                                                    county=county,
                                                    maritalStatus=maritalStatus,
                                                    coupleDiscordant=coupleDiscordant,
                                                    SexWithWoman=SexWithWoman,
                                                    SexWithMan=SexWithMan,
                                                    condom_use=condom_use,
                                                    sw=sw,
                                                    pwid=pwid,
                                                    testedBefore=testedBefore,
                                                    presumedTB=presumedTB,
                                                    treatmentTB=treatmentTB,
                                                    sti=sti,
                                                    rapevictim=rapevictim,
                                                    HIVPrEP=HIVPrEP,
                                                    y_pred=y_pred)

        userresult.save()

        return render(request, 'base/result.html', {'result': y_pred})
    return render(request, 'base/survey.html')


def about(request):
    return render(request, 'base/about.html')


def welcome(request):
    return render(request, 'base/welcome.html')


def survey(request):
    return render(request, 'base/survey.html')


def vctPage(request):
    return render(request, 'base/vct.html')
