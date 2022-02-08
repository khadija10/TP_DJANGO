# Generated by Django 4.0.1 on 2022-01-27 18:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_magasin_produit_profilmagasin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='magasin',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='produit',
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
            field=models.DateTimeField(auto_now_add=True, default=1.0),
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
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='country',
            field=models.CharField(choices=[('BJ', 'BENIN'), ('BF', 'BURKINA FASO'), ('CI', "COTE D' IVOIRE"), ('SN', 'SENEGAL'), ('GN', 'GUINEE')], default='SN', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(default='/file/00.png', upload_to='PRODUCT_IMG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='magasin',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='product_magasin', to='polls.magasin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='price',
            field=models.DecimalField(decimal_places=2, default=django.utils.timezone.now, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profilmagasin',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilmagasin',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilmagasin',
            name='magasin',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='magasin_profil', to='polls.magasin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilmagasin',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilmagasin',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.CharField(choices=[('BJ', 'BENIN'), ('BF', 'BURKINA FASO'), ('CI', "COTE D' IVOIRE"), ('SN', 'SENEGAL'), ('GN', 'GUINEE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('MASCULIN', 'MASCULIN'), ('FEMININ', 'FEMININ')], max_length=10),
        ),
    ]