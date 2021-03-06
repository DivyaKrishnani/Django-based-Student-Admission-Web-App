# Generated by Django 2.1 on 2018-10-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20181028_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='appform1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('aadhar_number', models.IntegerField()),
                ('category', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=7)),
                ('boe', models.CharField(max_length=7)),
                ('year', models.CharField(max_length=4)),
                ('result', models.CharField(max_length=10)),
                ('roll', models.IntegerField()),
                ('mothna', models.CharField(max_length=20)),
                ('mothc', models.CharField(max_length=20)),
                ('motho', models.CharField(max_length=20)),
                ('fathna', models.CharField(max_length=20)),
                ('fathc', models.CharField(max_length=20)),
                ('fatho', models.CharField(max_length=20)),
                ('ques', models.CharField(max_length=3)),
                ('add1', models.CharField(max_length=20)),
                ('add2', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('padd1', models.CharField(max_length=20)),
                ('padd2', models.CharField(max_length=20)),
                ('pcountry', models.CharField(max_length=20)),
                ('pstate', models.CharField(max_length=20)),
                ('pcity', models.CharField(max_length=20)),
                ('ppincode', models.IntegerField()),
                ('bank', models.CharField(max_length=20)),
                ('accn', models.CharField(max_length=20)),
                ('accno', models.IntegerField()),
                ('ifs', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
                ('sign', models.ImageField(upload_to='')),
                ('mark', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='appform',
        ),
    ]
