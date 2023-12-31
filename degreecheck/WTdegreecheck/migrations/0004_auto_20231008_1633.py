# Generated by Django 3.1 on 2023-10-08 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WTdegreecheck', '0003_remove_course_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='major',
            old_name='course',
            new_name='course_req',
        ),
        migrations.RemoveField(
            model_name='course',
            name='type',
        ),
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_ID', models.CharField(help_text='ex. ENGL 1301', max_length=20)),
                ('c_name', models.CharField(help_text='Introduction to Academic Writing and Argumentation', max_length=150)),
                ('hours', models.IntegerField(default=3, help_text='number of credit hours')),
                ('type', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.coursetype')),
            ],
        ),
        migrations.AddField(
            model_name='major',
            name='core',
            field=models.ManyToManyField(to='WTdegreecheck.Core'),
        ),
    ]
