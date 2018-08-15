# Generated by Django 2.0.2 on 2018-08-15 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mstats', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='webshellgrant',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='mysqlslowlog',
            index_together={('md5sum',)},
        ),
        migrations.AlterUniqueTogether(
            name='mysqlschemainfo',
            unique_together={('host', 'port', 'schema')},
        ),
        migrations.AddField(
            model_name='mysqlschemagrant',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mstats.MysqlSchemaInfo', to_field='schema_join'),
        ),
        migrations.AddField(
            model_name='mysqlschemagrant',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='deadlockrecord',
            unique_together={('server', 'ts', 'thread')},
        ),
        migrations.AlterUniqueTogether(
            name='webshellgrant',
            unique_together={('user', 'shell')},
        ),
        migrations.AlterUniqueTogether(
            name='mysqlschemagrant',
            unique_together={('user', 'schema')},
        ),
    ]