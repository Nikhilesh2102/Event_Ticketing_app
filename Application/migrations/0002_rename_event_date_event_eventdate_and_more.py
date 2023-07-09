# Generated by Django 4.2.2 on 2023-07-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Event_Date',
            new_name='EventDate',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='Event_Description',
            new_name='EventDescription',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='Event_Name',
            new_name='EventName',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='Event_Time',
            new_name='EventTime',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='Event_Venue',
            new_name='EventVenue',
        ),
        migrations.RemoveField(
            model_name='event',
            name='Event_AvailableTickets',
        ),
        migrations.AddField(
            model_name='event',
            name='EventAvailableTickets',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
    ]