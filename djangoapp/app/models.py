from django.db import models

# Create your models here.

# TABELAS

class Comunidade(models.Model):
    especie = models.OneToOneField('Especie', models.DO_NOTHING, db_column='especie', primary_key=True)  # The composite primary key (especie, nome) found, that is not supported. The first column is selected.
    nome = models.CharField(max_length=15, unique=True)
    qtd_habitantes = models.FloatField()

    class Meta:
        managed = True
        db_table = 'comunidade'
        unique_together = (('especie', 'nome'),)

class Dominancia(models.Model):
    planeta = models.ForeignKey('Planeta', models.DO_NOTHING, db_column='planeta')
    nacao = models.OneToOneField('Nacao', models.DO_NOTHING, db_column='nacao', primary_key=True)  # The composite primary key (nacao, planeta, data_ini) found, that is not supported. The first column is selected.
    data_ini = models.DateField()
    data_fim = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dominancia'
        unique_together = (('nacao', 'planeta', 'data_ini'),)


class Especie(models.Model):
    nome = models.CharField(primary_key=True, max_length=15)
    planeta_or = models.ForeignKey('Planeta', models.DO_NOTHING, db_column='planeta_or', blank=True, null=True)
    inteligente = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'especie'


class Estrela(models.Model):
    id_estrela = models.CharField(primary_key=True, max_length=31)
    nome = models.CharField(max_length=31, blank=True, null=True)
    classificacao = models.CharField(max_length=31, blank=True, null=True)
    massa = models.FloatField(blank=True, null=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    class Meta:
        managed = True
        db_table = 'estrela'
        unique_together = (('x', 'y', 'z'),)


class Faccao(models.Model):
    nome = models.CharField(primary_key=True, max_length=15)
    lider = models.OneToOneField('Lider', models.DO_NOTHING, db_column='lider')
    ideologia = models.CharField(max_length=15, blank=True, null=True)
    qtd_nacoes = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'faccao'


class Federacao(models.Model):
    nome = models.CharField(primary_key=True, max_length=15)
    data_fund = models.DateField()

    class Meta:
        managed = True
        db_table = 'federacao'


class Habitacao(models.Model):
    planeta = models.OneToOneField('Planeta', models.DO_NOTHING, db_column='planeta', primary_key=True)  # The composite primary key (planeta, especie, comunidade, data_ini) found, that is not supported. The first column is selected.
    especie = models.ForeignKey(Comunidade, models.DO_NOTHING, db_column='especie')
    comunidade = models.ForeignKey(Comunidade, models.DO_NOTHING, db_column='comunidade', to_field='nome', related_name='habitacao_comunidade_set')
    data_ini = models.DateField()
    data_fim = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'habitacao'
        unique_together = (('planeta', 'especie', 'comunidade', 'data_ini'),)


class Lider(models.Model):
    cpi = models.CharField(primary_key=True, max_length=14)
    nome = models.CharField(max_length=15, blank=True, null=True)
    cargo = models.CharField(max_length=10)
    nacao = models.ForeignKey('Nacao', models.DO_NOTHING, db_column='nacao')
    especie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='especie')

    class Meta:
        managed = True
        db_table = 'lider'


class Nacao(models.Model):
    nome = models.CharField(primary_key=True, max_length=15)
    qtd_planetas = models.FloatField(blank=True, null=True)
    federacao = models.ForeignKey(Federacao, models.DO_NOTHING, db_column='federacao', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nacao'


class NacaoFaccao(models.Model):
    nacao = models.OneToOneField(Nacao, models.DO_NOTHING, db_column='nacao', primary_key=True)  # The composite primary key (nacao, faccao) found, that is not supported. The first column is selected.
    faccao = models.ForeignKey(Faccao, models.DO_NOTHING, db_column='faccao')

    class Meta:
        managed = True
        db_table = 'nacao_faccao'
        unique_together = (('nacao', 'faccao'),)


class OrbitaEstrela(models.Model):
    orbitante = models.OneToOneField(Estrela, models.DO_NOTHING, db_column='orbitante', primary_key=True)  # The composite primary key (orbitante, orbitada) found, that is not supported. The first column is selected.
    orbitada = models.ForeignKey(Estrela, models.DO_NOTHING, db_column='orbitada', related_name='orbitaestrela_orbitada_set')
    dist_min = models.FloatField(blank=True, null=True)
    dist_max = models.FloatField(blank=True, null=True)
    periodo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orbita_estrela'
        unique_together = (('orbitante', 'orbitada'),)


class OrbitaPlaneta(models.Model):
    planeta = models.OneToOneField('Planeta', models.DO_NOTHING, db_column='planeta', primary_key=True)  # The composite primary key (planeta, estrela) found, that is not supported. The first column is selected.
    estrela = models.ForeignKey(Estrela, models.DO_NOTHING, db_column='estrela')
    dist_min = models.FloatField(blank=True, null=True)
    dist_max = models.FloatField(blank=True, null=True)
    periodo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orbita_planeta'
        unique_together = (('planeta', 'estrela'),)


class Participa(models.Model):
    faccao = models.OneToOneField(Faccao, models.DO_NOTHING, db_column='faccao', primary_key=True)  # The composite primary key (faccao, especie, comunidade) found, that is not supported. The first column is selected.
    especie = models.ForeignKey(Comunidade, models.DO_NOTHING, db_column='especie')
    comunidade = models.ForeignKey(Comunidade, models.DO_NOTHING, db_column='comunidade', to_field='nome', related_name='participa_comunidade_set')

    class Meta:
        managed = True
        db_table = 'participa'
        unique_together = (('faccao', 'especie', 'comunidade'),)


class Planeta(models.Model):
    id_astro = models.CharField(primary_key=True, max_length=15)
    massa = models.FloatField(blank=True, null=True)
    raio = models.FloatField(blank=True, null=True)
    classificacao = models.CharField(max_length=63, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'planeta'


class Sistema(models.Model):
    estrela = models.OneToOneField(Estrela, models.DO_NOTHING, db_column='estrela', primary_key=True)
    nome = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sistema'


class Users(models.Model):
    user_id = models.FloatField(primary_key=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    id_lider = models.ForeignKey(Lider, models.DO_NOTHING, db_column='id_lider', blank=True, null=True)
    # id_lider = models.ForeignKey(Lider, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'users'

    # def __str__(self) -> str:
    #     return f"{self.user_id} | {self.id_lider}"


class LogTable(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'log_table'

    # def __str__(self):
    #     return f"{self.user_id} - {self.data_hora}"
    
# class Users(models.Model):
#     user_id = models.CharField(max_length=14)  # Assumindo que o CPF tem até 14 caracteres
#     password = models.CharField(max_length=50)
#     id_lider = models.ForeignKey(Lider, on_delete=models.CASCADE)

#     class Meta:
#         managed = True
#         db_table = 'users'

    # def __str__(self):
    #     return self.user_id