# Generated by Django 4.2.9 on 2024-01-16 09:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0018_improve_crontab_helptext'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('operator_code', models.CharField(max_length=10)),
                ('tag', models.CharField(max_length=255)),
                ('timezone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('launch_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('message_text', models.TextField(max_length=500)),
                ('client_filter_operator_code', models.CharField(blank=True, max_length=10, null=True)),
                ('client_filter_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('end_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskNewsletterAssociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.newsletter')),
                ('periodic_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.periodictask')),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('count_sent_messages', models.IntegerField(default=0)),
                ('count_success_sent_messages', models.IntegerField(default=0)),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.newsletter')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('send_status', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.newsletter')),
            ],
        ),
    ]
