
STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'),
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'),
		('SE','SE'), ('SP','SP'), ('TO','TO'),    
    )

TYPE = [
    ('Compra', 'Compra'),
    ('Venda', 'Venda'),
    ('Outros', 'Outros')
]

   
STATUS_CHOICES = [
    ('Pendente', 'Pendente'),
    ('Aguardando', 'Aguardando'),
    ('Entregue', 'Entregue'),
    ('Cancelado', 'Cancelado'),
]

PGTO_CHOICES = [
    ("Pix", "Pix"),
    ("Cartão", "Cartão"),
    ("Dinheiro", "Dinheiro"),
    ("Cheque", "Cheque"),
]
