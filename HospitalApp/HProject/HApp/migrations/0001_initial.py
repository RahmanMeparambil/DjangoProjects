# Generated by Django 4.2.3 on 2023-07-27 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=200, null=True)),
                ('Name', models.CharField(max_length=200, null=True)),
                ('From_email', models.EmailField(max_length=254, null=True)),
                ('To_email', models.EmailField(max_length=254, null=True)),
                ('Message_content', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Specialization_name', models.CharField(max_length=200, null=True)),
                ('Description', models.TextField(null=True)),
                ('Icon', models.TextField(null=True)),
                ('Image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('Start_time', models.TimeField(null=True)),
                ('End_time', models.TimeField(null=True)),
                ('Is_available', models.BooleanField(default=True)),
                ('Doctor_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HApp.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('User_category', models.CharField(max_length=200, null=True)),
                ('Old_password', models.CharField(max_length=200, null=True)),
                ('New_password', models.CharField(max_length=200, null=True)),
                ('Req_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='Specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HApp.specialization'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Appointment_date', models.DateField(null=True)),
                ('Patient_name', models.CharField(max_length=200, null=True)),
                ('Patient_email', models.EmailField(max_length=200, null=True)),
                ('Specialization', models.CharField(max_length=200, null=True)),
                ('Start_time', models.TimeField(null=True)),
                ('End_time', models.TimeField(null=True)),
                ('Status', models.BooleanField(default=False)),
                ('Doctor_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HApp.doctor')),
            ],
        ),
    ]
