# Generated by Django 2.0.1 on 2018-04-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180131_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionquestion',
            name='position',
            field=models.CharField(default='none', max_length=50),
        ),
    ]