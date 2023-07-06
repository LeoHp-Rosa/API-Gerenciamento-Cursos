# Generated by Django 4.0.7 on 2023-07-06 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='students',
            field=models.ManyToManyField(related_name='student', to='users.student'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='users.instructor'),
        ),
    ]
