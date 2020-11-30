# Generated by Django 3.1.3 on 2020-11-30 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcard', '0003_auto_20201130_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageinfo',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='imageinfo',
            name='sign',
        ),
        migrations.AlterField(
            model_name='imageinfo',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='imageinfo',
            name='fname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='imageinfo',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='imageinfo',
            name='pan',
            field=models.BigIntegerField(null=True),
        ),
    ]
