# Generated by Django 2.1.2 on 2018-10-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0006_auto_20181024_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_design',
            name='MEM_CON_NO',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='email_design',
            name='REL_EXP_MONTHS',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='email_design',
            name='REL_EXP_YEARS',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='email_design',
            name='TOT_EXP_MONTHS',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='email_design',
            name='TOT_EXP_YEARS',
            field=models.IntegerField(max_length=50),
        ),
    ]
