# Generated by Django 4.0.1 on 2022-01-27 18:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_magasin_profile_product_remove_profilmagasin_magasin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(choices=[('BJ', 'BENIN'), ('BF', 'BURKINA FASO'), ('CI', "COTE D' IVOIRE"), ('SN', 'SENEGAL'), ('GN', 'GUINEE')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='PRODUCT_IMG')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfilMagasin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Magasin_profile',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterModelOptions(
            name='magasin',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='magasin',
            name='country',
            field=models.CharField(choices=[('BJ', 'BENIN'), ('BF', 'BURKINA FASO'), ('CI', "COTE D' IVOIRE"), ('SN', 'SENEGAL'), ('GN', 'GUINEE')], default='SN', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magasin',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magasin',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='magasin',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.CharField(choices=[('BJ', 'BENIN'), ('BF', 'BURKINA FASO'), ('CI', "COTE D' IVOIRE"), ('SN', 'SENEGAL'), ('GN', 'GUINEE')], default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('MASCULIN', 'MASCULIN'), ('FEMININ', 'FEMININ')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profilmagasin',
            name='magasin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='magasin_profil', to='polls.magasin'),
        ),
        migrations.AddField(
            model_name='produit',
            name='magasin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_magasin', to='polls.magasin'),
        ),
    ]
