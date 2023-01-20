# SISTEMA DE TURISMO

## Escopo
O Desenvolvimento de um sistema de cadastro e login de forma que os usuários possam cadastrar usuário, email e senha, bem como dados da sua empresa. Conterá com diversas funcionalidades como alteração dos seus dados, recuperação e alteração de senha.
O acesso administrador conta, ainda, com lista de todos os usuários e empresas cadastrados e tem acesso para editar os dados e deixar inativo os usuários. 
O projeto está utilizando o framework Django 4.0 e a linguagem de programação Python 3.9.5.

# Estrutura

* models
    - user - campos tabela usuários:
		* id, password, last_login, is_superuser, username, first_name, last_name,is_staff, is_active, date_joined, email, option;

	- company - campos tabela empresas:
		* id, company_name, document_number, document_imag, street,  number, complement, postal_code, city, state, user_id;
	
	- contact - campos tabela contatos:
		* id, cel_phone, user_id;

	- socialmedia - campos tabela redes sociais:
		* id, social_media, user_id;

# Funcionalidades

* cadastro:
	- na tela de cadastro o usuário tem as opções entre Agência ou Fornecedor para selecionar, campos para inserção do nome de usuario, email, senha, confirmar senha, botão para salvar o cadastro e link que direciona para a tela de login;
	- na tela de completar cadastro tem os campos para inserção da razão social, cnpj, logradouro, número, complemento, cidade, estado, CEP, botão para fazer upload de uma imagem e botão para salvar o cadastro;
	- concluído o cadastro, o usuário será automaticamente logado.

* login:
	- na tela de login tem os campos usuário/email, senha, botão acessar, link para recuperar a senha e link que direciona para a tela de cadastro;

* configurações:
	- Usarname/Email - o usuário poderá editar os campos Usuário e Email;
	- Empresa - o usuário poderá editar os campos Razão social, CNPJ, Logradouro, Número complemento, Cidade, Estado, CEP e fazer upload de uma imagem.

* administrador:
	- no sidebar, a opção GESTÃO/Usuários/Listar abre a tela que lista todos os usuários. Possui um seletor de entradas por páginas, campo de pesquisa, um paginador e ícone com opção de editar dados do usuário;
	- na tela editar cadastro, há a opção Usuário Ativo, para ativar/inativar o usuario;
	- no sidebar, a opção GESTÃO/Empresas/Listar abre a tela que lista todas empresas. Possui um seletor de entradas por páginas, campo de pesquisa, um paginador e ícone com opção de editar dados da empresa. 
	
	-> Estas opções estão disponíveis apenas para usuário administrador.

* logout:
	- o usuário optar por clicar no botão 'sair' para confirmar logout.

## Instruções de nstalação

### Instalar e atualizar pip

```
pip install
python.exe -m pip install --upgrade pip
```


### Criar e acessar pasta do projeto

```
mkdir tourproject
cd tourproject
```


### Criar ambiente virtual

```
py -m venv venv_tourproject
```


### Ativar ambiente virtual

```
- Windows -
venv_tourproject/scripts/activate.bat

- Linux -
venv_tourproject\bin\activate
```


### Clonar o projeto

```
git clone https://github.com/carlosalbertoprojetos/tourproject.git
```


### Acessar a pasta do projeto

```
cd tourproject

```

### Instalar dependências

```
pip install -r requirements.txt
```


### Aplicar migrações

```
python manage.py migrate
```


### Criar super usuário

```
python manage.py createsuperuser
```

obs.: o email será utilizado como username para login


### Rodar o projeto

```
python manage.py runserver
```
