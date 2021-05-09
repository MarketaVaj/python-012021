# Generated by Django 3.2 on 2021-05-09 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0003_vypujcka'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vypujcka',
            old_name='CenaVypujcky',
            new_name='cenaVypujcky',
        ),
        migrations.RenameField(
            model_name='vypujcka',
            old_name='KonecVypujcky',
            new_name='konecVypujcky',
        ),
        migrations.RenameField(
            model_name='vypujcka',
            old_name='ZacatekVypujcky',
            new_name='zacatekVypujcky',
        ),
        migrations.RenameField(
            model_name='zakaznik',
            old_name='CisloRidicskehoPRukazu',
            new_name='cisloRidicskehoPRukazu',
        ),
        migrations.RenameField(
            model_name='zakaznik',
            old_name='Jmeno',
            new_name='jmeno',
        ),
        migrations.RenameField(
            model_name='zakaznik',
            old_name='Prijmeni',
            new_name='prijmeni',
        ),
        migrations.AddField(
            model_name='vypujcka',
            name='auto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.auto'),
        ),
        migrations.AddField(
            model_name='zakaznik',
            name='vypujcka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.vypujcka'),
        ),
    ]
