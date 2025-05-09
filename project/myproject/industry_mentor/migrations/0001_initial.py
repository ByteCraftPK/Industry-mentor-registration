# Generated by Django 5.1.7 on 2025-03-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryMentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact', models.CharField(max_length=15)),
                ('job_role', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('expertise', models.TextField()),
                ('pan_number', models.CharField(max_length=10, unique=True)),
                ('bank_account', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=255)),
                ('ifsc', models.CharField(max_length=11)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('passbook_image', models.ImageField(upload_to='passbooks/')),
                ('pan_card_image', models.ImageField(upload_to='pan_cards/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
