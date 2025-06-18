
# Documentação do Projeto: Sistema Distribuído de Gerenciamento de Cargas e Frotas

**Desenvolvido por: Pedro Neves**

---

## Visão Geral

Este projeto implementa uma aplicação distribuída para gerenciamento de cargas e frotas de caminhões, abordando os conceitos fundamentais de sistemas distribuídos, como comunicação entre processos, tolerância a falhas, escalabilidade e persistência de dados.

A arquitetura adotada foi pensada para ser simples, funcional e clara para fins acadêmicos, utilizando tecnologias acessíveis e bem documentadas.

---

## Funcionalidades

- Cadastro e listagem de motoristas e caminhões
- Registro e roteirização de entregas
- Comunicação assíncrona entre serviços via fila de mensagens
- Armazenamento de dados em banco de dados distribuído (MongoDB)
- Monitoramento dos serviços com Prometheus

---

## Estrutura de Serviços

- **service-a**: Responsável pelo cadastro e recuperação de dados de motoristas e caminhões.
- **service-b**: Responsável pela criação e envio de dados de entregas para a fila RabbitMQ.
- **messaging**: Consumidor da fila que processa entregas enviadas.
- **mongo**: Banco de dados utilizado para persistência.
- **rabbitmq**: Sistema de mensageria que conecta os serviços.
- **prometheus**: Sistema de monitoramento de métricas.

---

## Instruções de Uso

### Pré-requisitos

- Docker e Docker Compose instalados

### Como executar o projeto

1. Clone ou extraia o conteúdo do projeto
2. Acesse o diretório raiz do projeto no terminal
3. Execute o comando:

```bash
docker-compose up --build
```

4. Acesse os serviços:

| Serviço               | Endereço                                    |
|-----------------------|---------------------------------------------|
| Cadastro API          | http://localhost:8001/docs                  |
| Entregas API          | http://localhost:8002/docs                  |
| RabbitMQ (admin)      | http://localhost:15672 (guest / guest)     |
| Prometheus            | http://localhost:9090                      |

5. Para parar os serviços:

```bash
docker-compose down
```

---

## Justificativa das Escolhas de Arquitetura

### Linguagem e Frameworks

- **Python + FastAPI**: Escolhido por ser leve, simples e com excelente suporte para APIs REST, além de fornecer documentação automática via Swagger.

### Banco de Dados

- **MongoDB**: Banco NoSQL ideal para protótipos rápidos com persistência flexível de dados, além de ser naturalmente distribuído.

### Mensageria

- **RabbitMQ**: Sistema de mensagens robusto, fácil de integrar com Python e ideal para simular comunicação assíncrona entre serviços.

### Monitoramento

- **Prometheus**: Amplamente utilizado em sistemas distribuídos, coleta métricas e facilita a visualização e análise do comportamento dos serviços.

### Contêineres

- **Docker Compose**: Permite orquestrar todos os serviços com um único comando, facilitando testes e demonstrações.

---

## Considerações Finais

Este projeto cobre todos os requisitos mínimos exigidos pela avaliação de Sistemas Distribuídos, implementando com clareza e funcionalidade os conceitos esperados. A estrutura modular também permite fácil expansão futura, como adição de autenticação, replicação ou interface web.

