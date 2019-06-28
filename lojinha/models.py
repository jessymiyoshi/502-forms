from django.db import models

# Create your models here.

class Bolo(models.Model):
    sabores_opcoes = [
        ('ch','Chocolate'),
        ('ce','Cenoura'),
        ('se','Sensação'),
        ('pr','Prestigio'),
        ('nh','Ninho'),
        ('cr', 'Churros'),
        ('ba', 'Banana')
    ]

    recheios_opcoes = [
        ('br', 'Brigadeiro'),
        ('bj', 'Beijinho'),
        ('dl', 'Doce de Leite'),
        ('fv', 'Frutas Vermelhas'),
        ('nu', 'Nutella'),
        ('ni', 'Ninho'),
        ('fr', 'Frutas')
    ]

    coberturas_opcoes = [
        ('gr', 'Granulado'),
        ('ct', 'Chantilly'),
        ('mr', 'Morango'),
        ('sm', 'Sem Cobertura'),
        ('br', 'Brigadeiro')
    ]

    sabor = models.CharField(max_length=2, choices=sabores_opcoes)
    recheio = models.CharField(max_length=2, choices=recheios_opcoes)
    cobertura = models.CharField(max_length=2, choices=coberturas_opcoes, default='sm')
    peso = models.DecimalField(decimal_places=2, max_digits=3, default=1.00)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    pagamento_opcoes = [
        ('av', 'Pagamento à vista'),
        ('p2', 'Parcelado em 2 vezes'),
        ('p3', 'Parcelado em 3 vezes')
    ]

    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2, choices=pagamento_opcoes, default= 'av')

    
    
