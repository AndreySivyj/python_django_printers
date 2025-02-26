# Generated by Django 4.2.7 on 2023-11-22 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0002_cartridgesmodel_print_serversmodel_type_oidmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='printersmodel',
            name='printed_pages_all_oid',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='printed_pages_all_oid', to='printers.snmp_oidmodel', verbose_name='Распечатано страниц (всего) OID'),
        ),
        migrations.AddField(
            model_name='printersmodel',
            name='sn_oid',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sn_oid', to='printers.snmp_oidmodel', verbose_name='S/N OID'),
        ),
        migrations.CreateModel(
            name='Printers_in_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(db_index=True, max_length=50, verbose_name='S/N')),
                ('name_on_print_server', models.CharField(max_length=100, null=True, verbose_name='Имя на Print-server')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP-address')),
                ('location', models.CharField(max_length=100, verbose_name='Локация/Кабинет')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('archived', models.BooleanField(default=False)),
                ('print_server', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='printers.print_serversmodel', verbose_name='print-server')),
                ('printers', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='printers.printersmodel', verbose_name='Модель принтера')),
                ('status_printer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='printers.statusprintersmodel', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Принтер (учет)',
                'verbose_name_plural': '(3) Принтеры (учет)',
                'ordering': ['print_server', 'location', 'printers'],
                'indexes': [models.Index(fields=['serial_number', 'printers'], name='printers_pr_serial__46998d_idx')],
            },
        ),
    ]
