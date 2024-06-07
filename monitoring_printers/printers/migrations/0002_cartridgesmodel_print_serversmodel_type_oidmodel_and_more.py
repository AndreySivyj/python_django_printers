# Generated by Django 4.2.7 on 2023-11-20 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartridgesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Картридж')),
            ],
            options={
                'verbose_name': 'Модель картриджа',
                'verbose_name_plural': '(1) Модели картриджей',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Print_serversModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('print_server', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='print-server')),
            ],
            options={
                'verbose_name': 'print-server',
                'verbose_name_plural': '(1) print-servers',
                'ordering': ['print_server'],
            },
        ),
        migrations.CreateModel(
            name='Type_OIDModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, unique=True, verbose_name='Type_OID')),
            ],
            options={
                'verbose_name': 'Type_OID',
                'verbose_name_plural': '(1) Type_OID',
                'ordering': ['type'],
            },
        ),
        migrations.AlterModelOptions(
            name='statusprintersmodel',
            options={'ordering': ['id', 'status'], 'verbose_name': 'Статус', 'verbose_name_plural': '(1) Статусы'},
        ),
        migrations.CreateModel(
            name='SNMP_OIDModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.CharField(max_length=100, unique=True, verbose_name='OID')),
                ('type_OID', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='type_OID', to='printers.type_oidmodel', verbose_name='Type_OID')),
            ],
            options={
                'verbose_name': 'SNMP_OID',
                'verbose_name_plural': '(1) SNMP_OID',
                'ordering': ['type_OID', 'oid'],
            },
        ),
        migrations.CreateModel(
            name='PrintersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Модель принтера')),
                ('cartridges', models.ManyToManyField(blank=True, related_name='cartridges_printers', to='printers.cartridgesmodel', verbose_name='Модели картриджей')),
            ],
            options={
                'verbose_name': 'Модель принтера',
                'verbose_name_plural': '(1) Модели принтеров',
                'ordering': ['name'],
            },
        ),
    ]
