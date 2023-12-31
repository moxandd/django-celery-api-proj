# Generated by Django 4.2.5 on 2023-10-02 15:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('mobile_code', models.CharField(max_length=3)),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('timezone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('send_status', models.BooleanField(default=False)),
                ('newsletter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.newsletter')),
                ('send_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
            ],
        ),
    ]
