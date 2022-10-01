from django.test import TestCase

from ..models import Conta

# automatizar testes
# import doctest

# def function(x):
#     return x**2

# doctest.testmod()



# class ContaTestCase(TestCase):
    
#     def test_conta_novo_cadastro(self):
#         self.assertEqual(1,21)

#     def test_teste(self):
#         self.assertEqual(21,21)


class ContaTestCase(TestCase):
    # executa sempre antes de iniciar o teste
    def setUp(self):
        Conta.objects.create(
            nome='Caixa',
            agencia=1234,
            conta=212121,
            saldo=10,
            tel_contato='(31) 6541-2541',
            logradouro='Rua um',
            numero=1,
            complemento=2,
            cep='35.000-000',
            estado='MG',
            cidade='Ibiá'
        )
    
    def test_cadastro_conta(self):
        teste_cadastro = Conta.objects.get(nome='Caixa')
        self.assertEquals(teste_cadastro.__str__(), 'Caixa')
        print(
            'Nome', teste_cadastro.nome,'\n'
            'agencia', teste_cadastro.agencia,'\n'
            'conta', teste_cadastro.conta,'\n'
            'saldo', teste_cadastro.saldo,'\n'
            'tel_contato', teste_cadastro.tel_contato,'\n'
            'logradouro', teste_cadastro.logradouro,'\n'
            'numero', teste_cadastro.numero,'\n'
            'complemento', teste_cadastro.complemento,'\n'
            'cep', teste_cadastro.cep,'\n'
            'estado', teste_cadastro.estado,'\n'
            'cidade', teste_cadastro.cidade
        )

# para rodar o teste somente sa aplicação
# py manage.py test conta

    