# Generated by Django 3.2.8 on 2022-08-17 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quitance', '0016_auto_20220721_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='EcritureBrouillard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('POSTE_COMPTABLE', models.CharField(blank=True, max_length=100, null=True)),
                ('annee_budgetaire', models.CharField(blank=True, max_length=100, null=True)),
                ('JOURNAL', models.CharField(blank=True, max_length=100, null=True)),
                ('AUXILIAIRE', models.CharField(blank=True, max_length=100, null=True)),
                ('COMPTE', models.CharField(blank=True, max_length=100, null=True)),
                ('NUM_PIECE', models.CharField(blank=True, max_length=100, null=True)),
                ('CODE_PIECE', models.CharField(blank=True, max_length=100, null=True)),
                ('ORDONNATEUR', models.CharField(blank=True, max_length=100, null=True)),
                ('SENS_ECRITURE', models.CharField(blank=True, max_length=100, null=True)),
                ('MONTANT_ECRITURE', models.CharField(blank=True, max_length=100, null=True)),
                ('ECRITURE_LIBELLE', models.CharField(blank=True, max_length=100, null=True)),
                ('DATE_ECRITURE', models.CharField(blank=True, max_length=100, null=True)),
                ('ORIGINE', models.CharField(blank=True, max_length=100, null=True)),
                ('ORIGINE_KEY', models.CharField(blank=True, max_length=100, null=True)),
                ('DATE_CREATION', models.CharField(blank=True, max_length=100, null=True)),
                ('UTILISATEUR_CREATION', models.CharField(blank=True, max_length=100, null=True)),
                ('DATE_MODIFICATION', models.CharField(blank=True, max_length=100, null=True)),
                ('UTILISATEUR_MODIFICATION', models.CharField(blank=True, max_length=100, null=True)),
                ('num_ecriture', models.CharField(blank=True, max_length=100, null=True)),
                ('num_fiche', models.CharField(blank=True, max_length=100, null=True)),
                ('expediteur', models.CharField(blank=True, max_length=100, null=True)),
                ('destinataire', models.CharField(blank=True, max_length=100, null=True)),
                ('lien_ecriture', models.CharField(blank=True, max_length=100, null=True)),
                ('date_echeance', models.CharField(blank=True, max_length=100, null=True)),
                ('who_done', models.CharField(blank=True, max_length=100, null=True)),
                ('when_done', models.CharField(blank=True, max_length=100, null=True)),
                ('statut_ecriture', models.CharField(blank=True, max_length=100, null=True)),
                ('cloture', models.CharField(blank=True, max_length=100, null=True)),
                ('devise', models.CharField(blank=True, max_length=100, null=True)),
                ('montant_debit', models.CharField(blank=True, max_length=100, null=True)),
                ('montant_credit', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('model_line', models.CharField(blank=True, max_length=100, null=True)),
                ('comptable', models.CharField(blank=True, max_length=100, null=True)),
                ('SPECIFICATION_SECONDAIRE', models.CharField(blank=True, max_length=100, null=True)),
                ('SPECIFICATION_PRINCIPALE', models.CharField(blank=True, max_length=100, null=True)),
                ('REFERENCE_2', models.CharField(blank=True, max_length=100, null=True)),
                ('observations', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='quitance',
            name='numero_dr',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Numero Declaration recette'),
        ),
    ]