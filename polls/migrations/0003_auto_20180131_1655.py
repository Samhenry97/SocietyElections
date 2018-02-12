# Generated by Django 2.0.1 on 2018-01-31 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20171230_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidatechoice',
            old_name='candidate_id',
            new_name='candidate',
        ),
        migrations.AlterField(
            model_name='candidatechoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.PositionQuestion'),
        ),
    ]