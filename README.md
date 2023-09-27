# One:One API 💬

A API **One:One** nasceu como uma plataforma de agendamentos de mentorias entre colaboradores e psicólogos, para que juntos possam encaminhar metas em reuniões one-on-one.


Para esse projeto de MVP da Sprint 3 do curso de Pós-graduação em Desenvolvimento Full Stack da PUC-Rio, foi desenvolvido serviços para a área do(a) gestor(a) do contrato de mentorias, possibilidando que ele(a) possa cadastrar mentores e suas disponibilidades, designar mentorandos e decidir o formato das reuniões.

👀 **Não esqueça de baixar e rodar a aplicação web**! Acesse o [One:One App](https://github.com/brennofacasi/one-one-app).

## Primeiros passos 🚀

Primeiro, clone o projeto:
```bash
git clone https://github.com/brennofacasi/one-one-api
```

Renomeie o arquivo ```env.example``` para ```.env```. Não é necessário editar a variável, a não ser que seja uma API diferente da [DummyJSON](https://dummyjson.com/).

```env
USERS_API='https://dummyjson.com/users?limit=15&select=firstName,lastName,email,company'
```

> A One:One utiliza a base de usuários do **DummyJSON** para representar os dados de mentorandos. A aplicação obtém resultados através de uma chamada GET e retorna os dados formatados para serem utilizados internamente.

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

```bash
$ docker build -t one-one-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```bash
$ docker run -p 3050:5000 one-one-api
```

Abra o endereço [http://localhost:3050](http://localhost:3050) para acessar a documentação da API em Swagger.