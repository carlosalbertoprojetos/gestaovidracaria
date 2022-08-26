from django.urls import reverse_lazy as _


STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'),
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'),
		('SE','SE'), ('SP','SP'), ('TO','TO'),    
    )

TYPE = (
    ('Compra', 'compra'),
    ('Venda', 'venda'),
    ('Outros', 'outros')
)
   
STATUS_CHOICES = (
    ('Pendente', 'pendente'),
    ('Aguardando', 'aguardando'),
    ('Entregue', 'entregue'),
    ('Cancelado', 'cancelado'),
)

PGTO_CHOICES = (
    ("Pix", "pix"),
    ("Cartão", "cartão"),
    ("Dinheiro", "dinheiro"),
)

SEXO_CHOICES = (
    ('M','M'), ('F','F'), ('OUTRO','OUTRO'), ('PREFIRO NÃO DIZER','PREFIRO NÃO DIZER'),
)

RACA_CHOICES = (
    ('BRANCA','BRANCA'), ('PRETA','PRETA'), ('PARDA','PARDA'), ('AMARELA','AMARELA'), ('INDÍGENA','INDÍGENA'),
)

# CONTA_OPERACAO_DEBITO = 'd'
# CONTA_OPERACAO_CREDITO = 'c'
CONTA_OPERACAO_CHOICES = (
    ('d', 'Debito'),
    ('c', 'Credito'),
)

# CONTA_STATUS_APAGAR = 'a'
# CONTA_STATUS_PAGO = 'p'
CONTA_STATUS_CHOICES = (
    ('a', 'A Pagar'),
    ('p', 'Pago'),
)
