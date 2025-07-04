# Generated by Django 5.2 on 2025-06-13 18:01

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(db_column='userId', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.TextField(blank=True, db_column='firstName', null=True)),
                ('last_name', models.TextField(blank=True, db_column='lastName', null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.TextField(blank=True, null=True, unique=True)),
                ('employee', models.BooleanField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(db_column='createdAt', default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(db_column='updatedAt', default=django.utils.timezone.now)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], default='User', max_length=20)),
                ('location', models.JSONField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.UUIDField(db_column='jobId', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
                ('start_date', models.DateTimeField(db_column='startDate')),
                ('end_date', models.DateTimeField(blank=True, db_column='endDate', null=True)),
                ('salary', models.FloatField(blank=True, null=True)),
                ('higher_salary', models.FloatField(blank=True, db_column='higherSalary', null=True)),
                ('description', models.TextField()),
                ('requirements', models.TextField(blank=True, null=True)),
                ('posted_date', models.DateTimeField(db_column='postedDate')),
                ('start_age', models.IntegerField(blank=True, db_column='startage', null=True)),
                ('end_age', models.IntegerField(blank=True, db_column='endage', null=True)),
                ('gender', models.BooleanField(blank=True, null=True)),
                ('location', models.JSONField(blank=True, null=True)),
                ('job_type', models.CharField(blank=True, choices=[('FULL_TIME', 'Full Time'), ('PART_TIME', 'Part Time'), ('CONTRACT', 'Contract'), ('TEMPORARY', 'Temporary'), ('INTERNSHIP', 'Internship')], db_column='jobType', null=True)),
                ('location_name', models.TextField(blank=True, db_column='locationName', null=True)),
                ('company', models.TextField(blank=True, null=True)),
                ('duration', models.TextField(blank=True, choices=[('Less than 1 month', 'Less Than 1 Month'), ('1-3 months', 'One To Three Months'), ('3-6 months', 'Three To Six Months'), ('6-12 months', 'Six To Twelve Months'), ('1+ year', 'One Plus Year'), ('Ongoing', 'Ongoing')], null=True)),
                ('pay_type', models.CharField(blank=True, choices=[('Hourly', 'Hourly'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Project-based', 'Project Based'), ('Negotiable', 'Negotiable')], db_column='payType', null=True)),
                ('employer_id', models.ForeignKey(db_column='employerId', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Job',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('application_id', models.UUIDField(db_column='applicationId', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('accept', models.IntegerField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('employee_review', models.TextField(blank=True, db_column='employeeReview', null=True)),
                ('employer_review', models.TextField(blank=True, db_column='employerReview', null=True)),
                ('employee_id', models.ForeignKey(db_column='employeeId', on_delete=django.db.models.deletion.DO_NOTHING, related_name='applications_as_employee', to=settings.AUTH_USER_MODEL)),
                ('employer_id', models.ForeignKey(db_column='employerId', on_delete=django.db.models.deletion.DO_NOTHING, related_name='appications_as_employer', to=settings.AUTH_USER_MODEL)),
                ('job_id', models.ForeignKey(db_column='jobId', on_delete=django.db.models.deletion.DO_NOTHING, to='applications.job')),
            ],
            options={
                'db_table': 'Application',
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['email'], name='User_email_ffa2e0_idx'),
        ),
        migrations.AddIndex(
            model_name='job',
            index=models.Index(fields=['job_type'], name='Job_jobType_cb943a_idx'),
        ),
        migrations.AddIndex(
            model_name='job',
            index=models.Index(fields=['location_name'], name='Job_locatio_dcc49a_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='job',
            unique_together={('name', 'employer_id', 'start_date')},
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together={('job_id', 'employee_id')},
        ),
    ]
