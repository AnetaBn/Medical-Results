# Generated by Django 4.1.3 on 2023-01-20 19:27

from django.db import migrations, models
import django.db.models.deletion
import legacy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('doctor_name', models.CharField(blank=True, max_length=50, null=True)),
                ('specialization', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'doctor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('patient_pesel', models.CharField(blank=True, max_length=50, null=True)),
                ('patient_name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('study_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hospital', models.CharField(blank=True, max_length=64, null=True)),
                ('study_date', models.DateField(blank=True, null=True)),
                ('study_time', models.CharField(blank=True, max_length=64, null=True)),
                ('modality', models.CharField(blank=True, max_length=10, null=True)),
                ('note', models.CharField(blank=True, max_length=500, null=True)),
                ('pathfile', models.CharField(blank=True, db_column='pathFile', max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=legacy.models.get_filename)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='legacy.doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='legacy.patient')),
            ],
            options={
                'db_table': 'study',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ChangesHistory',
            fields=[
                ('his_change_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('his_study_id', models.IntegerField(blank=True, null=True)),
                ('his_hospital', models.CharField(blank=True, max_length=64, null=True)),
                ('his_study_date', models.DateField(blank=True, null=True)),
                ('his_study_time', models.CharField(blank=True, max_length=64, null=True)),
                ('his_modality', models.CharField(blank=True, max_length=10, null=True)),
                ('his_note', models.CharField(blank=True, max_length=500, null=True)),
                ('his_pathfile', models.CharField(blank=True, db_column='pathFile', max_length=100, null=True)),
                ('his_image', models.ImageField(blank=True, null=True, upload_to=legacy.models.get_filename)),
                ('his_change_date', models.DateTimeField(auto_now=True, verbose_name='date_published')),
                ('his_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='legacy.doctor')),
                ('his_patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='legacy.patient')),
            ],
            options={
                'db_table': 'changesHistory',
                'managed': True,
            },
        ),
    ]
