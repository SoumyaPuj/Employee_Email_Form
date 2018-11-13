from django.db import models


class Email_Information(models.Model):
    NAME            = models.CharField(max_length=50)
    TECHNOLOGY      = models.TextField()
    PASSPORT_NUMBER = models.CharField(max_length=50)
    ISSUED_DATE     = models.DateField()
    EXPIRY_DATE     = models.DateField()
    SALARY_ACCOUNT  = models.IntegerField()
    PRE_ORG_NAME    = models.CharField(max_length=150)
    TOT_EXP_YEARS   = models.IntegerField()
    TOT_EXP_MONTHS  = models.IntegerField()
    REL_EXP_YEARS   = models.IntegerField()
    REL_EXP_MONTHS  = models.IntegerField()
    PERSONAL_EMAIL  = models.EmailField()
    BLOOD_GRP       = models.CharField(max_length=50)
    FAMILY_MEM      = models.CharField(max_length=50)
    MEM_NAME        = models.CharField(max_length=50)
    MEM_CON_NO      = models.CharField(max_length=15)
    CURR_ADDRESS    = models.TextField()
    PER_ADDRESS     = models.TextField()
    MARITAL_STS     = models.CharField(max_length=50)

    class Meta:
        db_table = "Email_Information"