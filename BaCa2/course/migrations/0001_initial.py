# Generated by Django 4.1.3 on 2022-12-14 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True)),
                ('deadline_date', models.DateTimeField()),
                ('reveal_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_instance', models.IntegerField()),
                ('task_name', models.CharField(max_length=1023)),
                ('judging_mode', models.CharField(choices=[('L', 'Linear'), ('U', 'Unanimous')], default='L', max_length=1)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.round')),
            ],
        ),
        migrations.CreateModel(
            name='TestSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=255)),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=255)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.task')),
                ('task_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.testset')),
            ],
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('source_code', models.FilePathField()),
                ('user', models.IntegerField()),
                ('final_score', models.FloatField(default=-1)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.test')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PND', 'Pending'), ('OK', 'Test accepted'), ('ANS', 'Wrong answer'), ('RTE', 'Runtime error'), ('MEM', 'Memory exceeded'), ('TLE', 'Time limit exceeded'), ('CME', 'Compilation error'), ('EXT', 'Unknown extension'), ('INT', 'Internal error')], default='PND', max_length=3)),
                ('submit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.submit')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.test')),
            ],
        ),
    ]
