# Generated by Django 2.1.1 on 2018-09-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlorders', '0005_auto_20180925_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqlordersexectasks',
            name='is_ghost',
            field=models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='是否启用ghost改表'),
        ),
    ]