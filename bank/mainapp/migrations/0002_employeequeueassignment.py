# Generated by Django 4.2.6 on 2023-10-30 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeQueueAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('serving', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.employee')),
                ('queue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.queue')),
            ],
        ),
    ]
