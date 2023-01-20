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

STATUS_PARCELA_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),    
)


PGTO_CHOICES = (
    ("Boleto", "Boleto"),
    ("Cheque", "Cheque"),
    ("C/Entrega", "C/Entrega"),
    ("Pix", "Pix"),
    ("Cartão", "Cartão"),
    ("Dinheiro", "Dinheiro"),
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

TAXAS_CHOICES = (
    ('0.00', '0.00'),
    ('0.01', '0.01'),
    ('0.02', '0.02'),
    ('0.03', '0.03'),
    ('0.04', '0.04'),
    ('0.05', '0.05'),
    ('0.06', '0.06'),
    ('0.07', '0.07'),
    ('0.08', '0.08'),
    ('0.09', '0.09'),
    ('0.10', '0.10'),
    ('0.11', '0.11'),
    ('0.12', '0.12'),
    ('0.13', '0.13'),
    ('0.14', '0.14'),
    ('0.15', '0.15'),
    ('0.16', '0.16'),
    ('0.17', '0.17'),
    ('0.18', '0.18'),
    ('0.19', '0.19'),
    ('0.20', '0.20'),    
)

PARCELAS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),        
)