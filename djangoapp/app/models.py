from django.db import models

# Create your models here.
class Federacao(models.Model):
    nome = models.CharField(max_length=15, primary_key=True)
    data_fund = models.DateField()

    def __str__(self):
        return self.nome

class Nacao(models.Model):
    nome = models.CharField(max_length=15, primary_key=True)
    qtd_planetas = models.IntegerField()
    federacao = models.ForeignKey(Federacao, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

class Planeta(models.Model):
    id_astro = models.CharField(max_length=15, primary_key=True)
    massa = models.DecimalField(max_digits=10, decimal_places=2)
    raio = models.DecimalField(max_digits=10, decimal_places=2)
    classificacao = models.CharField(max_length=63, blank=True, null=True)

    def __str__(self):
        return self.id_astro

class Especie(models.Model):
    nome = models.CharField(max_length=15, primary_key=True)
    planeta_or = models.ForeignKey(Planeta, on_delete=models.CASCADE)
    inteligente = models.CharField(max_length=1, choices=[('V', 'Verdadeiro'), ('F', 'Falso')])

    def __str__(self):
        return self.nome

class Lider(models.Model):
    cpi = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=15, blank=True, null=True)
    cargo = models.CharField(max_length=10, choices=[('COMANDANTE', 'Comandante'), ('OFICIAL', 'Oficial'), ('CIENTISTA', 'Cientista')])
    nacao = models.ForeignKey(Nacao, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Faccao(models.Model):
    nome = models.CharField(max_length=15, primary_key=True)
    lider = models.OneToOneField(Lider, on_delete=models.CASCADE)
    ideologia = models.CharField(max_length=15, choices=[('PROGRESSISTA', 'Progressista'), ('TOTALITARIA', 'Totalitaria'), ('TRADICIONALISTA', 'Tradicionalista')])
    qtd_nacoes = models.IntegerField()

    def __str__(self):
        return self.nome

class NacaoFaccao(models.Model):
    nacao = models.ForeignKey(Nacao, on_delete=models.CASCADE)
    faccao = models.ForeignKey(Faccao, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nacao', 'faccao')

class Estrela(models.Model):
    id_estrela = models.CharField(max_length=31, primary_key=True)
    nome = models.CharField(max_length=31, blank=True, null=True)
    classificacao = models.CharField(max_length=31, blank=True, null=True)
    massa = models.DecimalField(max_digits=10, decimal_places=2)
    x = models.DecimalField(max_digits=10, decimal_places=2)
    y = models.DecimalField(max_digits=10, decimal_places=2)
    z = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('x', 'y', 'z')

    def __str__(self):
        return self.nome

class Comunidade(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    nome = models.CharField(max_length=15)
    qtd_habitantes = models.IntegerField()

    class Meta:
        unique_together = ('especie', 'nome')

    def __str__(self):
        return self.nome

class Participa(models.Model):
    faccao = models.ForeignKey(Faccao, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    comunidade = models.CharField(max_length=15)

    class Meta:
        unique_together = ('faccao', 'especie', 'comunidade')

class Habitacao(models.Model):
    planeta = models.ForeignKey(Planeta, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    comunidade = models.CharField(max_length=15)
    data_ini = models.DateField()
    data_fim = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('planeta', 'especie', 'comunidade', 'data_ini')

class Dominancia(models.Model):
    planeta = models.ForeignKey(Planeta, on_delete=models.CASCADE)
    nacao = models.ForeignKey(Nacao, on_delete=models.CASCADE)
    data_ini = models.DateField()
    data_fim = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('nacao', 'planeta', 'data_ini')

class Sistema(models.Model):
    estrela = models.OneToOneField(Estrela, on_delete=models.CASCADE)
    nome = models.CharField(max_length=31)

    def __str__(self):
        return self.nome

class OrbitaEstrela(models.Model):
    orbitante = models.ForeignKey(Estrela, related_name='orbitante', on_delete=models.CASCADE)
    orbitada = models.ForeignKey(Estrela, related_name='orbitada', on_delete=models.CASCADE)
    dist_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dist_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    periodo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('orbitante', 'orbitada')

class OrbitaPlaneta(models.Model):
    planeta = models.ForeignKey(Planeta, on_delete=models.CASCADE)
    estrela = models.ForeignKey(Estrela, on_delete=models.CASCADE)
    dist_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dist_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    periodo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('planeta', 'estrela')        
    
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=32)
    id_lider = models.OneToOneField(Lider, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)

class LogTable(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user_id} - {self.data_hora}"        