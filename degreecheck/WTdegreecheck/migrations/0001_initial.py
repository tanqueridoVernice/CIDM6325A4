# Generated by Django 3.1 on 2023-10-08 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='College name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_ID', models.CharField(help_text='ex. CIDM 6325', max_length=20)),
                ('c_name', models.CharField(help_text='e-commerce and web development', max_length=150)),
                ('hours', models.IntegerField(default=3, help_text='number of credit hours')),
            ],
        ),
        migrations.CreateModel(
            name='Coursetype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Core', 'Core'), ('Major', 'Major')], default=0, max_length=20)),
                ('Core_category', models.CharField(help_text='010,020, ...', max_length=10)),
                ('Component_area', models.CharField(help_text='Mathematics, Major, ...', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Degree Name', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Department name', max_length=100)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.college')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(help_text='Spring,Fall,Summer I, Summer II', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('studentID', models.CharField(max_length=15)),
                ('coursestaken', models.ManyToManyField(to='WTdegreecheck.Course')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.degree')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.department')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(help_text='Major name', max_length=100)),
                ('college', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.college')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.degree')),
                ('dept', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.department')),
            ],
        ),
        migrations.CreateModel(
            name='Degreecheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(to='WTdegreecheck.Course')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.major')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.department'),
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='WTdegreecheck.coursetype'),
        ),
    ]
