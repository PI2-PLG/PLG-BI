<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/18190061/65366176-f592ff00-dbf6-11e9-9b7a-8cc5c6d85ddc.png">
</p>

# Projeto Lobo-Guará - Business Intelligence
### Sistema de monitoramento de queimadas feito por alunos da Universidade de Brasília.

Este repositório é o responsável pelo microsserviço relacionado a Business Intelligence

## Requisitos
Para executar o sistema é necessário possuir o **docker** e o **docker-compose** instalados em seu ambiente. Você pode verificar como instalar estas ferramentas nos links a seguir:

* [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [docker-compose](https://docs.docker.com/compose/install/)

## Como utilizar?

Tendo o docker e o docker-compose instalados em seu ambiente execute os passos a seguir:

```

$ docker-compose -f docker-compose.yml build

```

A imagem docker será então construída. Execute o comando a seguir para rodar o sistema:

```

$ docker-compose -f docker-compose.yml up

```

Com o processo tendo funcionado perfeitamente, será possível acessar a interface da API em:

* https:\\\\localhost:8000

## Populando o Banco de Dados

Com o sistema funcionando execute a seguinte linha:  

```

sudo docker-compose exec -T web python manage.py shell < ./scripts/module-seed.py

```

Caso tudo ocorra normalmente o banco será populado com Modulos e seus dados.

## Exemplos de Requisições

* Exemplo pra criar um módulo:

```

curl -d '{"module":{"name":"modulo2"}}' -H "Content-Type: application/json" -X POST http://localhost:8003/new-module/

```

* Exemplo para criar um conjunto de dados de um módulo:

```

curl -d '{"module":{"name":"Modulo-FGA-D"},"module_data":{"latitude":"12.12","longitude":"12.12","temperature":"12.12","humidity":"12.12","pressure":"12.12","ppm":"123"}}' -H "Content-Type: application/json" -X POST http://localhost:8003/new-module-data/

```

* Exemplo para a coleta da lista de módulos e suas respectivas posições:

```

curl -X GET http://localhost:8003/all-modules-list/

```

* Exemplo de requisição de todos os dados de um módulo

```
curl -d '{"module":{"name":"Modulo-FGA-A"}}' -H "Content-Type: application/json" -X GET http://localhost:8003/all-module-data/

```

* Exemplo para a coleta de todos os módulos e seus conjuntos de dados:

```

curl -X GET http://localhost:8003/all-data/

```

