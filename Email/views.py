from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Email_Information
from pymysql import *
from django.http import HttpResponse


class Email_View(TemplateView):
    template_name = 'Email_Temp.html'

    # def get(self, request):
    #     form = Email_Form()
    #     return render(request, self.template_name, {'form':form})

    def email_send(request):
            email_objects = Email_Information(request.POST)
            if request.method == "POST":
                 #if email_objects.is_valid():
                   NAME = request.POST.get("name")
                   TECHNOLOGY = request.POST.get("technology")
                   PASSPORT_NUMBER = request.POST.get("passport_no")
                   ISSUED_DATE = request.POST.get("issue_dt")
                   EXPIRY_DATE = request.POST.get("expiry_dt")
                   SALARY_ACCOUNT = request.POST.get("account_dtl")
                   PRE_ORG_NAME = request.POST.get("pre_org_name")
                   TOT_EXP_YEARS = request.POST.get("tot_exp_years")
                   TOT_EXP_MONTHS = request.POST.get("tot_exp_months")
                   REL_EXP_YEARS = request.POST.get("rel_exp_years")
                   REL_EXP_MONTHS = request.POST.get("rel_exp_months")
                   PERSONAL_EMAIL = request.POST.get("email_address")
                   BLOOD_GRP = request.POST.get("blood_group")
                   FAMILY_MEM = request.POST.get("family_member")
                   MEM_NAME = request.POST.get("member_name")
                   MEM_CON_NO = request.POST.get("member_no")
                   CURR_ADDRESS = request.POST.get("current_address")
                   PER_ADDRESS = request.POST.get("permanent_address")
                   MARITAL_STS = request.POST.get("status")

                   #print(NAME,TECHNOLOGY,PASSPORT_NUMBER,ISSUED_DATE,EXPIRY_DATE,SALARY_ACCOUNT,PRE_ORG_NAME,TOT_EXP_YEARS,TOT_EXP_MONTHS,REL_EXP_YEARS,REL_EXP_MONTHS,PERSONAL_EMAIL,BLOOD_GRP,FAMILY_MEM,MEM_NAME,MEM_CON_NO,CURR_ADDRESS,PER_ADDRESS,MARITAL_STS)
                   email_objects = Email_Information(NAME=NAME,TECHNOLOGY=TECHNOLOGY,PASSPORT_NUMBER=PASSPORT_NUMBER,ISSUED_DATE=ISSUED_DATE,EXPIRY_DATE=EXPIRY_DATE,SALARY_ACCOUNT=SALARY_ACCOUNT,PRE_ORG_NAME=PRE_ORG_NAME,TOT_EXP_YEARS=TOT_EXP_YEARS,TOT_EXP_MONTHS=TOT_EXP_MONTHS,REL_EXP_YEARS=REL_EXP_YEARS,REL_EXP_MONTHS=REL_EXP_MONTHS,PERSONAL_EMAIL  =PERSONAL_EMAIL,BLOOD_GRP=BLOOD_GRP,FAMILY_MEM=FAMILY_MEM,MEM_NAME=MEM_NAME,MEM_CON_NO=MEM_CON_NO,CURR_ADDRESS=CURR_ADDRESS,PER_ADDRESS=PER_ADDRESS,MARITAL_STS=MARITAL_STS,)
                   # conn = connect(host='localhost', user='root', password='root', db='django_projects')
                   email_objects.save()
            # return render(request, 'Email_Temp.html')
            return render(request, 'Email_Temp.html', {'form':email_objects})


    def Show_Details(request):
        post = Email_Information.objects.all()
        return render(request, "Show.html", {'Email_Information': post})


    def Home_View(request):
         return render(request, "Home.html")


    def About_View(request):
         return HttpResponse("about form in process")

