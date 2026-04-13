# ⚽ Cadastro de Jogador em Python

Projeto desenvolvido em Python com o objetivo de praticar **estruturas de dados**, **entrada de dados** e **manipulação de informações**.

---

## 📌 Descrição

Este projeto simula um sistema simples de cadastro de jogador de futebol, onde o usuário informa:

* Nome do jogador
* Quantidade de partidas jogadas
* Número de gols em cada partida

Ao final, o programa exibe um resumo completo com todas as informações organizadas.

---

## ⚙️ Funcionalidades

* ✔️ Cadastro de jogador
* ✔️ Registro de gols por partida
* ✔️ Cálculo automático do total de gols
* ✔️ Exibição organizada dos dados
* ✔️ Uso de dicionários e listas para armazenamento

---

## 🧠 Conceitos aplicados

* Dicionários (`dict`)
* Listas (`list`)
* Estruturas de repetição (`for`)
* Função `enumerate()`
* Função `sum()`
* Entrada de dados com `input()`
* Manipulação e exibição de dados

---

## ▶️ Como executar

1. Certifique-se de ter o Python instalado (versão 3.x)

2. Clone este repositório:

```bash
git clone https://github.com/Yurizin3333/Cadastro-Jogador
```

3. Acesse a pasta do projeto:

```bash
cd Cadastro-Jogador
```

4. Execute o arquivo:

```bash
python cadastro_jogador.py
```

---

## 💻 Exemplo de uso

```bash
Nome do jogador: Neymar
Quantas partidas jogadas?: 3
   Quantos gols na partida 0?: 2
   Quantos gols na partida 1?: 1
   Quantos gols na partida 2?: 0

==================================================
{'nome': 'Neymar', 'gols': [2, 1, 0], 'total': 3}
==================================================

O campo nome tem valor Neymar
O campo gols tem valor [2, 1, 0]
O campo total tem valor 3

==================================================
O jogador Neymar jogou 3 partidas!
   => Na partida 0, fez 2 gols.
   => Na partida 1, fez 1 gols.
   => Na partida 2, fez 0 gols.
Foi um total de 3 gols!
```

---

## 📁 Estrutura do projeto

```
Cadastro-Jogador/
│
├── cadastro_jogador.py
└── README.md
```

---

## 🚀 Melhorias futuras

* Adicionar tratamento de erros para entradas inválidas
* Permitir cadastro de múltiplos jogadores
* Salvar dados em arquivo (JSON ou banco de dados)
* Criar interface gráfica (GUI)

---

## 👨‍💻 Autor

**Yuri da Silva Ignacio**

* GitHub: https://github.com/Yurizin3333
* LinkedIn: https://www.linkedin.com/in/yuri-d-332701246/

---

## 📄 Licença

Este projeto é de uso livre para fins de estudo e aprendizado.
