# Generated by Django 4.2.7 on 2023-11-30 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0015_alter_printed_pagesmodel_printers_in_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service_objectmodel',
            options={'ordering': ['service_object_name'], 'verbose_name': 'Объект_обслуживания', 'verbose_name_plural': '(2) Объекты_обслуживания'},
        ),
        migrations.AlterField(
            model_name='printers_in_servicemodel',
            name='name_on_print_server',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя на Print-server'),
        ),
        migrations.AlterField(
            model_name='printers_in_servicemodel',
            name='print_server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='print_server_fk', to='printers.print_serversmodel', verbose_name='print-server'),
        ),
        migrations.AlterField(
            model_name='printers_in_servicemodel',
            name='printers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='printers_fk', to='printers.printersmodel', verbose_name='Модель принтера'),
        ),
        migrations.AlterField(
            model_name='printers_in_servicemodel',
            name='service_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='printers.service_objectmodel', verbose_name='Объект_обслуживания'),
        ),
    ]
