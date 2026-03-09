# 🛒 E-commerce API - Django REST Framework

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-green.svg)
![Django REST Framework](https://img.shields.io/badge/DRF-3.15+-red.svg)

## 🚀 Sobre o Projeto

Uma API RESTful robusta para gerenciamento de e-commerce, focada em segurança financeira, integridade de dados e regras de negócio complexas. Este projeto vai além de um simples CRUD, implementando lógicas avançadas de transações e controle de estoque dinâmico.

## ✨ Principais Funcionalidades & Arquitetura

* **Controle de Estoque Atômico:** Validação de disponibilidade de produtos e baixa de estoque utilizando `transaction.atomic()` do Django, garantindo a regra do "Tudo ou Nada" (Rollback automático em caso de falhas).
* **Segurança contra Injeção de Dados:** Uso de `read_only_fields` em Serializers customizados para ignorar tentativas de manipulação de preços pelo client-side.
* **Cálculos no Backend:** Utilização de `@property` nos Models para cálculo em tempo real de subtotais e totais de pedidos.
* **Integração de API Externa:** Consumo da API do ViaCEP para preenchimento e validação automática de endereços de clientes.
* **Autenticação e Permissões:** Proteção de rotas sensíveis utilizando Token Authentication nativo do DRF, garantindo que apenas usuários logados acessem e criem pedidos.
* **Performance e Otimização:** Implementação de Filtros dinâmicos via Query Parameters e Paginação de resultados para evitar sobrecarga do servidor.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Django
* **API Toolkit:** Django REST Framework (DRF)
* **Banco de Dados:** SQLite (Pronto para PostgreSQL)
* **Requisições Externas:** Biblioteca `requests`

## ⚙️ Como rodar o projeto localmente

Siga os passos abaixo para clonar e testar a API na sua máquina:

```bash
# 1. Clone este repositório
git clone [https://github.com/felipebzc2002/e-commerce_api.git](https://github.com/felipebzc2002/e-commerce_api.git)

# 2. Entre na pasta do projeto
cd e-commerce_api

# 3. Crie e ative o ambiente virtual (Windows)
python -m venv venv
venv\Scripts\activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Crie as tabelas no banco de dados
python manage.py migrate

# 6. Crie um superusuário para acessar o painel Admin e gerar Tokens
python manage.py createsuperuser

# 7. Rode o servidor local
python manage.py runserver