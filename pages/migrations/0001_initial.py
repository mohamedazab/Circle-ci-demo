# Generated by Django 2.2.3 on 2019-07-20 19:19

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('moisture_threshold', models.FloatField()),
                ('recommended_ph', models.FloatField()),
                ('recommended_temperature', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('password_salt', models.CharField(max_length=128)),
                ('field', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.Plant')),
            ],
        ),
    ]