# Generated by Django 4.2.7 on 2023-11-22 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0005_rename_printers_in_service_printers_in_servicemodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Printers_in_service_commentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(default='', max_length=100, verbose_name='Краткое описание')),
                ('comment', models.TextField(default='', verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('printers_in_service', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='printers.printers_in_servicemodel', verbose_name='Принтер (учет)')),
            ],
            options={
                'verbose_name': 'Принтеры (учет)_Комментарий',
                'verbose_name_plural': '(3) Принтеры (учет)_Комментарии',
                'ordering': ['created'],
                'get_latest_by': 'updated',
                'indexes': [models.Index(fields=['created'], name='printers_pr_created_af574f_idx')],
            },
        ),
    ]
