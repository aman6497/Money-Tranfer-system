# Generated by Django 5.0.6 on 2024-05-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MESSAGES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=100)),
                ('To', models.CharField(max_length=100)),
                ('Message', models.TextField()),
                ('Date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sender', models.CharField(max_length=100)),
                ('Reciever', models.CharField(max_length=100)),
                ('Amount', models.IntegerField()),
                ('Date_time', models.DateTimeField()),
                ('Remarks', models.TextField()),
                ('Reference_Number', models.CharField(max_length=20)),
                ('Payment_Status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=100)),
                ('Query', models.TextField()),
                ('Date_time', models.DateTimeField()),
                ('Query_Status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Aadhar', models.CharField(max_length=12)),
                ('Mobile', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=255)),
                ('Date_Of_Birth', models.DateField()),
                ('Account_Number', models.CharField(max_length=20)),
                ('IFSC', models.CharField(max_length=12)),
                ('Bank_Name', models.CharField(max_length=100)),
                ('User_ID', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('MPIN', models.CharField(max_length=6)),
                ('Status', models.CharField(max_length=20)),
                ('Balance', models.IntegerField()),
                ('Unique_Key', models.CharField(default='qwertyuiopasd', max_length=13)),
                ('Active_Status', models.BooleanField(default=False)),
            ],
        ),
    ]
