# One:One API 💬

A API **One:One** nasceu como uma plataforma de agendamentos de mentorias entre colaboradores e psicólogos, para que pudessem encaminhar metas em reuniões one-on-one.


Para esse projeto de MVP, foi desenvolvido serviços para a área do(a) gestor(a) do contrato de mentorias, possibilidando que ele(a) possa cadastrar mentores e suas disponibilidades, designar mentorandos e decidir o formato das reuniões.

## Primeiros passos 🚀

Primeiro, clone o projeto:
```bash
git clone https://github.com/brennofacasi/one-one-api
```

Renomeie o arquivo ```env.example``` para ```.env```. Não é necessário editar a variável, a não ser que seja uma API diferente da [DummyJSON](https://dummyjson.com/) .

```env
USERS_API='https://dummyjson.com/users?limit=15&select=firstName,lastName,email,company'
```

Para rodar o projeto, crie um ambiente virtual (com [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)), ative-o e instale os pacotes necessários:

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
Para executar a aplicação, use o comando:

```bash
(env) flask run --host 0.0.0.0 --port 3050
```
Caso precise atualizar a cada atualização feita no código, utilize a flag `--reload` ao final do comando acima.

## Com Docker 🐳

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o ```Dockerfile``` e o ```requirements.txt``` no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t one-one-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:3050 one-one-api
```

Abra o endereço [http://localhost:3050](http://localhost:3050) para acessar a documentação da API em Swagger.