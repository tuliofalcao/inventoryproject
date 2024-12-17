# UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO
## LICENCIATURA EM COMPUTAÇÃO - 2024.2

Professora: Rozelma França
Aluno: Túlio Falcão

Projeto de Inventário para a disciplina ESTÁGIO SUPERVISIONADO OBRIGATÓRIO II, a partir do canal do Kenbro Tech (https://www.youtube.com/@KenBroTech) em seu tutorial de Django.

## Para rodar o projeto

1) Você vai precisar ter o python 3.11, ou superior, instalado em sua máquina. Também precisar ter instalado o git. E precisará instalar o gerenciador de projetos python POETRY. Para instalar o Poetry, pode-se instalá-lo usan1do o pipx:

https://pipx-pypa-io.translate.goog/stable/installation/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc

2) Depois do pipx instalado, rode o seguinte comando:

pipx install poetry

3) clone o projeto para sua máquina:

https://github.com/tuliofalcao/inventoryproject.git

4) Vá até a pasta do projeto:

cd inventoryproject

5) Acione o ambiente virtual do Poetry:

poetry shell

6) baixe e instale as dependências do projeto:

poetry update

7) para rodar o projeto no navegador (http://127.0.0.1:8000/), entre na pasta "inventory" e depois rode o comando:

cd inventory 
python manage.py runserver

