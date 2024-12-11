# Generated by Django 5.1.2 on 2024-12-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0006_inventario_status_alter_inventario_actadevolucion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentas',
            name='cuenta',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cuentas',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cuentas',
            name='plataforma',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cuentas_admin',
            name='correo',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cuentas_admin',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cuentas_admin',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cuentas_ope',
            name='correo',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cuentas_ope',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='cuentas_ope',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='direccionamiento',
            name='ip',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='dominios',
            name='dominio',
            field=models.CharField(max_length=50, null=True, verbose_name='DOMINION'),
        ),
        migrations.AlterField(
            model_name='dominios',
            name='enlace',
            field=models.URLField(max_length=60, null=True, verbose_name='ENLACE'),
        ),
        migrations.AlterField(
            model_name='dominios',
            name='password',
            field=models.CharField(max_length=30, null=True, verbose_name='PASSWORD'),
        ),
        migrations.AlterField(
            model_name='dominios',
            name='usuario',
            field=models.CharField(max_length=30, null=True, verbose_name='USUARIO'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='actadevolucion',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='actaentregado',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='anydesk',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='area',
            field=models.CharField(choices=[('Bodega', 'Bodega'), ('Contabilidad', 'Contabilidad'), ('Control y Gestion', 'Gestion y Gestion'), ('Desarrollo', 'Desarrollo'), ('Gerencia', 'Gerencia'), ('Inspector de Equipos', 'Inspector de Equipos'), ('Maquinarias', 'Maquinarias'), ('Operaciones', 'Operaciones'), ('Prevencion de Riesgo', 'Prevencion de Riesgo'), ('Recursos Humanos', 'Recursos Humanos'), ('Relacionadas', 'Relacionadas'), ('Tesoreria', 'Tesoreria'), ('Ventas', 'Ventas')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='cargo',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ddrx',
            field=models.CharField(default=0, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='empresa',
            field=models.CharField(choices=[('GBYC', 'GBYC'), ('BYCT', 'BYCT'), ('BULL', 'BULL'), ('IVIC', 'IVIC'), ('FEMM', 'FEMM'), ('KCBS', 'KCBS')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='gbram',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ghzcpu',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='macethernet',
            field=models.CharField(default=0, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='macwifi',
            field=models.CharField(default=0, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='marca',
            field=models.CharField(choices=[('HP', 'HP'), ('Lenovo', 'Lenovo'), ('Asus', 'Asus')], default=0, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='marcacpu',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='mhzram',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='modelo',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='modelocpu',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='nombre_pc',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='nserie',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='os',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='password',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='responsable',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='rustdesk',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='status',
            field=models.CharField(choices=[('Asignado', 'Asignado'), ('Dipsonible', 'Disponible')], default='Asignado', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='tipo',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='usuario',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='nubecorporativa',
            name='cuenta',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nubecorporativa',
            name='departamentos',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nubecorporativa',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='planes',
            name='company',
            field=models.CharField(choices=[('WOM', 'WOM'), ('ENTEL', 'ENTEL'), ('MOVISTAR', 'MOVISTAR')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='planes',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='planes',
            name='numero',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sesionremota',
            name='colaborador',
            field=models.CharField(default='DISPONIBLE', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sesionremota',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sesionremota',
            name='password',
            field=models.CharField(choices=[('abod', 'abodByC#887-1'), ('acon', 'aconByC#887-1'), ('adirector', 'adirByC#887-1'), ('amm', 'amaqByC#887-1'), ('apoer', 'aopeByC#887-1'), ('arem', 'aremByC#887-1'), ('arhh', 'arrhByC#887-1'), ('ater', 'atesByC#887-1'), ('aventas', 'avenByC#887-1'), ('bod', 'bodeByC#887-1'), ('cobranza', 'cobrByC#887-1'), ('cont', 'contByC#887-1'), ('ctrl', 'ctrlByC#887-1'), ('fin', 'finaByC#887-1'), ('ger', 'gereByC#887-1'), ('iformat', 'infoByC#887-1'), ('provedores', 'provByC#887-1'), ('reclut', 'reclByC#887-1'), ('relacionadas', 'relaByC#887-1'), ('remu', 'remuByC#887-1'), ('rrhh', 'rrhhByC#887-1'), ('tesor', 'tesoByC#887-1'), ('ventas', 'ventByC#887-1')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sesionremota',
            name='usuario',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
