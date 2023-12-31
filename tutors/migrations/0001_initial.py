# Generated by Django 4.2.5 on 2023-10-30 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('research_fields', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('biography', models.TextField()),
                ('birth_date', models.DateField()),
                ('position', models.CharField(max_length=255)),
                ('academic_degree', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='scientists/')),
                ('research_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research_fields.researchfield')),
            ],
        ),
    ]
