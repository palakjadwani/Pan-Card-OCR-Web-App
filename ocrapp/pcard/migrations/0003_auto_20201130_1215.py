# Generated by Django 3.1.3 on 2020-11-30 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcard', '0002_auto_20201128_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('pan', models.BigIntegerField()),
                ('sign', models.ImageField(upload_to='')),
                ('pic', models.ImageField(upload_to='')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcard.image')),
            ],
        ),
    ]
