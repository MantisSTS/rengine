# Generated by Django 3.1.6 on 2021-05-05 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0002_auto_20210502_0601'),
        ('startScan', '0010_vulnerabilityscan_http_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discovered_date', models.DateTimeField(null=True)),
                ('http_url', models.CharField(max_length=8000, null=True)),
                ('name', models.CharField(max_length=400)),
                ('severity', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('extracted_results', models.CharField(blank=True, max_length=1000, null=True)),
                ('template_used', models.CharField(max_length=100)),
                ('matcher_name', models.CharField(blank=True, max_length=400, null=True)),
                ('open_status', models.BooleanField(blank=True, default=True, null=True)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='targetApp.domain')),
                ('endpoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='startScan.endpoint')),
                ('scan_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startScan.scanhistory')),
            ],
        ),
        migrations.DeleteModel(
            name='VulnerabilityScan',
        ),
    ]
