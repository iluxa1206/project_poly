# Generated by Django 4.2.5 on 2023-10-30 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('research_fields', '0001_initial'),
        ('tutors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('photo', models.ImageField(upload_to='articles/')),
                ('research_field_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research_fields.researchfield')),
                ('scientist_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutors.tutor')),
            ],
        ),
    ]
