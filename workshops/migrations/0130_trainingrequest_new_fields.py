# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-02-11 18:30
from __future__ import unicode_literals

from datetime import datetime

from django.db import migrations, models

from workshops.models import Person


def set_data_privacy_agreement(apps, schema_editor):
    """Set data privacy agreement to TRUE for every request created after
    2016-11-10, ie. the day this agreement was incorporated into AMY"""
    TrainingRequest = apps.get_model('workshops', 'TrainingRequest')
    cutoff_date = datetime(2016, 11, 11)
    TrainingRequest.objects.filter(created_at__gte=cutoff_date).update(
        data_privacy_agreement=True
    )


def set_other_agreements(apps, schema_editor):
    """All training requests required 3 agreements from the start, so
    we need to set them to TRUE."""
    TrainingRequest = apps.get_model('workshops', 'TrainingRequest')
    TrainingRequest.objects.update(
        code_of_conduct_agreement=True,
        training_completion_agreement=True,
        workshop_teaching_agreement=True,
    )


def set_underrepresented(apps, schema_editor):
    """All training requests required 3 agreements from the start, so
    we need to set them to TRUE."""
    TrainingRequest = apps.get_model('workshops', 'TrainingRequest')
    for request in TrainingRequest.objects.all():
        if request.gender == Person.FEMALE:
            request.underrepresented = "Woman"
            request.save()
        elif request.gender == Person.OTHER:
            request.underrepresented = request.gender_other or "other"
            request.save()


def set_previous_training(apps, schema_editor):
    """Prepare previous_training for removal of one option ('days')."""
    TrainingRequest = apps.get_model('workshops', 'TrainingRequest')
    TrainingRequest.objects.filter(previous_training='days').update(
        previous_training='workshops'
    )


def set_teaching_frequency_expectation(apps, schema_editor):
    """Prepare teaching_frequency_expectation for removal of one option
    ('often')."""
    TrainingRequest = apps.get_model('workshops', 'TrainingRequest')
    TrainingRequest.objects.filter(teaching_frequency_expectation='often').update(
        teaching_frequency_expectation='other',
        teaching_frequency_expectation_other='Often (primary occupation)'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0129_trainingrequest_texts_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingrequest',
            name='code_of_conduct_agreement',
            field=models.BooleanField(default=False, verbose_name='I agree to abide by The Carpentries\' Code of Conduct. The Code of Conduct can be found at <a href="http://software-carpentry.org/conduct/">http://software-carpentry.org/conduct/</a> and <a href="http://datacarpentry.org/code-of-conduct/">http://datacarpentry.org/code-of-conduct/</a>.'),
        ),
        migrations.AddField(
            model_name='trainingrequest',
            name='data_privacy_agreement',
            field=models.BooleanField(default=False, verbose_name='I have read and agree to <a href="https://software-carpentry.org/privacy/", target="_blank">the Software Carpentry Foundation\'s data privacy policy</a>.'),
        ),
        migrations.AddField(
            model_name='trainingrequest',
            name='nonprofit_teaching_experience',
            field=models.CharField(blank=True, help_text="Provide details or leave blank if this doesn't apply to you.", max_length=255, null=True, verbose_name='I have been an active contributor to other volunteer or non-profit groups with significant teaching or training components.'),
        ),
        migrations.AddField(
            model_name='trainingrequest',
            name='training_completion_agreement',
            field=models.BooleanField(default=False, verbose_name='I agree to complete this training within three months of the training course. The completion steps are described at <a href="http://carpentries.github.io/instructor-training/checkout/">http://carpentries.github.io/instructor-training/checkout/</a> and take a total of approximately 8-10 hours.'),
        ),
        migrations.AddField(
            model_name='trainingrequest',
            name='underrepresented',
            field=models.CharField(blank=True, help_text="Provide details or leave blank if this doesn't apply to you.", max_length=255, null=True, verbose_name='I self-identify as a member of a group that is under-represented in research and/or computing, e.g., women, ethnic minorities, LGBTQ, etc.'),
        ),
        migrations.AddField(
            model_name='trainingrequest',
            name='underresourced',
            field=models.BooleanField(default=False, help_text='The Carpentries strive to make workshops accessible to as many people as possible, in as wide a variety of situations as possible.', verbose_name='This is a small, remote, or under-resourced institution'),
        ),
        migrations.AddField(
            model_name='trainingrequest',
            name='workshop_teaching_agreement',
            field=models.BooleanField(default=False, verbose_name='I agree to teach a Carpentry workshop within 12 months of this Training Course.'),
        ),
        migrations.RunPython(set_data_privacy_agreement),
        migrations.RunPython(set_other_agreements),
        migrations.RunPython(set_underrepresented),
        migrations.RunPython(set_previous_training),
        migrations.RunPython(set_teaching_frequency_expectation),
    ]
