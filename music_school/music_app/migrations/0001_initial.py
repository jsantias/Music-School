# Generated by Django 2.0.2 on 2018-04-27 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_name', models.CharField(max_length=250)),
                ('instrument_category', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instrument', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('room', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('skill_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=12)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=18)),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.teacher'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.user'),
        ),
        migrations.AddField(
            model_name='bookings',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.schedule'),
        ),
        migrations.AddField(
            model_name='bookings',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.user'),
        ),
        migrations.AddField(
            model_name='bookings',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.teacher'),
        ),
    ]
