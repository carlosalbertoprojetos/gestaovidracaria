
STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'),
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'),
		('SE','SE'), ('SP','SP'), ('TO','TO'),    
    )

TYPE = [
    ('Compra', 'compra'),
    ('Venda', 'venda'),
    ('Outros', 'outros')
]

   
STATUS_CHOICES = [
    ('Pendente', 'pendente'),
    ('Aguardando', 'aguardando'),
    ('Entregue', 'entregue'),
    ('Cancelado', 'cancelado'),
]

PGTO_CHOICES = [
    ("Pix", "pix"),
    ("Cartão", "cartão"),
    ("Dinheiro", "dinheiro"),
]
