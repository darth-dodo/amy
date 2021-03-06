# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-18 08:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0098_auto_20160617_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCSelfOrganizedEventRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('organization', models.CharField(max_length=255, verbose_name='University or organization affiliation')),
                ('instructor_status', models.CharField(blank=True, choices=[('', 'None'), ('incomplete', "Have gone through instructor training, but haven't yet completed checkout"), ('dc', 'Certified Data Carpentry instructor'), ('swc', 'Certified Software Carpentry instructor'), ('both', 'Certified Software and Data Carpentry instructor')], max_length=40, verbose_name='Your Software and Data Carpentry instructor status')),
                ('is_partner', models.CharField(blank=True, choices=[('y', 'Yes'), ('n', 'No'), ('u', 'Unsure'), ('', 'Other (enter below)')], max_length=1, verbose_name='Is your organization a Data Carpentry or Software Carpentry Partner')),
                ('is_partner_other', models.CharField(blank=True, default='', max_length=100, verbose_name='Other (is your organization a Partner?)')),
                ('location', models.CharField(help_text='City, Province or State', max_length=255, verbose_name='Location')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('associated_conference', models.CharField(blank=True, default='', help_text='If the workshop is to be associated with a conference or meeting, which one?', max_length=100, verbose_name='Associated conference')),
                ('dates', models.CharField(help_text='Preferably in YYYY-MM-DD to YYYY-MM-DD format', max_length=255, verbose_name='Planned workshop dates')),
                ('domains_other', models.CharField(blank=True, default='', help_text='If none of the fields above works for you.', max_length=255, verbose_name='Other domains for the workshop')),
                ('topics_other', models.CharField(blank=True, default='', help_text='If none of the fields above works for you.', max_length=255, verbose_name='Other topics to be taught')),
                ('payment', models.CharField(choices=[('per_participant', 'I will contribute $25/participant through registration fees'), ('invoice', 'I will contribute $500 via an invoice'), ('credit_card', 'I will contribute $500 via a credit card payment'), ('fee_waiver', 'I would like to request a fee waiver')], default='per_participant', help_text='Self-organized workshops for non-Partner organizations are $500 or $25/participant for a workshop licensing fee (<a href="http://www.datacarpentry.org/self-organized-workshops/">http://www.datacarpentry.org/self-organized-workshops/</a>). Fee waivers are available and generally granted upon request.', max_length=40, verbose_name='Payment choice')),
                ('fee_waiver_reason', models.CharField(blank=True, default='', max_length=255, verbose_name='Reason for requesting a fee waiver')),
                ('handle_registration', models.BooleanField(default=False, verbose_name='I confirm that I will handle registration for this workshop')),
                ('distribute_surveys', models.BooleanField(default=False, verbose_name='I confirm that I will distribute the Data Carpentry surveys to workshop participants')),
                ('follow_code_of_conduct', models.BooleanField(default=False, verbose_name='I confirm that I will follow the Data Carpentry Code of Conduct')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('attendee_academic_levels', models.ManyToManyField(help_text='If you know the academic level(s) of your attendees, indicate them here.', to='workshops.AcademicLevel', verbose_name="Attendees' academic level")),
                ('attendee_data_analysis_level', models.ManyToManyField(help_text="If you know, indicate learner's general level of data analysis experience", to='workshops.DataAnalysisLevel', verbose_name="Attendees' level of data analysis experience")),
                ('domains', models.ManyToManyField(help_text="Set of lessons you're going to teach", to='workshops.DCWorkshopDomain', verbose_name='Domain for the workshop')),
                ('topics', models.ManyToManyField(help_text='A Data Carpentry workshop must include a Data Carpentry lesson on data organization and the other modules in the same domain from the Data Carpentry curriculum (see <a href="http://www.datacarpentry.org/workshops/">http://www.datacarpentry.org/workshops/</a>). If you do want to include materials not in our curriculum, please note that below and we\'ll get in touch.', to='workshops.DCWorkshopTopic', verbose_name='Topics to be taught')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
