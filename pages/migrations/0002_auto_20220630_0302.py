# Generated by Django 3.1.14 on 2022-06-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distritosadm',
            name='bairro',
            field=models.IntegerField(choices=[(1, 'Cidade Velha'), (2, 'Campina'), (3, 'Reduto'), (4, 'Umarizal'), (5, 'Telegrafo'), (6, 'Sacramenta'), (7, 'Pedreira'), (8, 'Marco'), (9, 'Souza'), (10, 'Marambaia'), (11, 'Canudos'), (12, 'Fatima'), (13, 'Sao Bras'), (14, 'Nazare'), (15, 'Batista Campos'), (16, 'Jurunas'), (17, 'Condor'), (18, 'Guama'), (19, 'Terra Firme'), (20, 'Cremacao'), (21, 'Val De Cans'), (22, 'Miramar'), (23, 'Pratinha'), (24, 'Tapana'), (25, 'Bengui'), (26, 'Maracangalha'), (27, 'Barreiro'), (28, 'Universitario'), (29, 'Curio Utinga'), (30, 'Aura'), (31, 'Castanheira'), (32, 'Aguas Lindas'), (33, 'Guanabara'), (34, 'Sao Clemente'), (35, 'Parque Guajara'), (36, 'Tenone'), (37, 'Aguas Negras'), (38, 'Maracacuera'), (39, 'Parque Verde'), (40, 'Cruzeiro'), (41, 'Ponta Grossa'), (42, 'Mangueirao'), (43, 'Cabanagem'), (44, 'Campina De Icoaraci'), (45, 'Paracuri'), (46, 'Agulha'), (47, 'Una'), (48, 'Coqueiro'), (49, 'Sao Jao De Outeiro'), (50, 'Itaiteua'), (51, 'Aguas Negra'), (52, 'Maracaja'), (53, 'Vila'), (54, 'Praia Grande'), (55, 'Farol'), (56, 'Mangueiras'), (57, 'Sao Francisco'), (58, 'Carananduba'), (59, 'Marahu'), (60, 'Paraiso'), (61, 'Baia Do Sol'), (62, 'Sucurijuquara'), (63, 'Caruara'), (64, 'Bonfim'), (65, 'Ariramba'), (66, 'Murubira'), (67, 'Porto Arthur'), (68, 'Natal Do Morumbira'), (69, 'Chapeu Virado'), (70, 'Aeroporto')], default=17),
        ),
        migrations.AlterField(
            model_name='distritosadm',
            name='distrito_saude',
            field=models.CharField(choices=[('DAMOS', 'Distrito Administrativos de Mosqueiro'), ('DAOUT', 'Distrito Administrativo de Outeiro'), ('DAICO', 'Distrito Administrativo de Icoaraci'), ('DABEN', 'Distrito Administrativo do Benguí'), ('DAENT', 'Distrito Administrativo do Entroncamento'), ('DASAC', 'Distrito Administrativo da Sacramenta'), ('DABEL', 'Distrito Administrativo de Belém'), ('DAGUA', 'Distrito Administrativo de Guamá')], default='DABEL', max_length=5, verbose_name='DA'),
        ),
    ]
