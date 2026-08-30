# Automação de Download de Relatórios

Automação desenvolvida em Python para acessar um site utilizando o navegador Chrome, realizar o login e efetuar o download dos relatórios disponíveis na página.

Após o download, os arquivos são armazenados no diretório configurado para a aplicação.

## Funcionalidades

- Acesso automatizado ao site
- Login automatizado
- Localização dos relatórios disponíveis
- Download automatizado dos relatórios
- Armazenamento dos arquivos em diretório configurável

## Tecnologias

- Python
- Google Chrome

As bibliotecas Python utilizadas devem ser consultadas na implementação atual do projeto.

## Requisitos

- Python instalado
- Google Chrome instalado
- Acesso ao site utilizado pela automação
- Credenciais necessárias para autenticação

## Como utilizar

Clone o repositório:

```bash
git clone https://github.com/bispobr/python-automacao-relatorio.git
cd python-automacao-relatorio
```

Configure o diretório onde os relatórios deverão ser armazenados de acordo com as configurações utilizadas pela aplicação.

Em seguida, execute:

```bash
python app.py
```

## Fluxo da automação

```text
Início
  │
  ▼
Acessar site
  │
  ▼
Realizar login
  │
  ▼
Localizar relatórios
  │
  ▼
Baixar arquivos
  │
  ▼
Salvar no diretório configurado
  │
  ▼
Fim
```

## Estrutura

O ponto de entrada da automação é o arquivo `app.py`.

A estrutura dos demais arquivos e diretórios deve ser consultada diretamente no projeto para identificar configurações e dependências específicas.

## Execução

Para executar a automação:

```bash
python app.py
```

Durante a execução, o navegador será utilizado para acessar o sistema, autenticar o usuário e realizar os downloads disponíveis.

## Status

Projeto de automação em Python para download de relatórios, desenvolvido com foco na automatização de tarefas repetitivas realizadas através do navegador.
