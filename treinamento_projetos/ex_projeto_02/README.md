```markdown
# 🛒 Projeto Simulado 2 — Pedido e Cliente (Associação entre Classes)

Este projeto é um simulado de nível avançado projetado para praticar conceitos profundos de **Programação Orientada a Objetos (POO)** em Python. O foco central é a **Associação de Classes**, o encapsulamento rigoroso, o tratamento de exceções em fluxos cruzados e a manipulação de arquivos de dados (CSV).

---

## 🎯 Objetivo do Projeto

Você recebeu a estrutura de um sistema de e-commerce composto por duas entidades principais: **`Cliente`** e **`Pedido`**. No mundo real, um pedido não flutua sozinho no banco de dados; ele pertence obrigatoriamente a um cliente específico. 

Sua missão é implementar as validações de consistência no nascimento dos objetos, garantir o vínculo correto entre eles usando herança/associação e criar algoritmos de filtros cruzados complexos que passem nas regras de negócio da diretoria.

---

## 📂 Estrutura de Arquivos

```text
projeto_pedidos/
├── data/
│   ├── clientes.csv
│   └── pedidos.csv
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cliente.py
│   │   └── pedido.py
│   └── repositories/
│       ├── __init__.py
│       └── ecom_repository.py
└── README.md