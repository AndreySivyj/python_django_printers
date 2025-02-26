# Generated by Django 4.2.7 on 2023-11-30 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0017_alter_printed_pagesmodel_printers_in_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printers_in_servicemodel',
            name='printers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='printers_fk', to='printers.printersmodel', verbose_name='Модель принтера'),
        ),
        migrations.AlterField(
            model_name='printers_in_servicemodel',
            name='status_printer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_printer_fk', to='printers.statusprintersmodel', verbose_name='Статус'),
        ),
    ]
