# Flask Form CRUD

## Visão Geral
Este repositório contém uma aplicação web **Flask** desenvolvida como atividade de faculdade para demonstrar um fluxo completo de **Criar, Ler, Atualizar e Deletar (CRUD)** de um formulário simples. O projeto ilustra os conceitos fundamentais de rotas Flask, e renderização de templates com **Jinja2**.

## Funcionalidades
- **Criar** – Submissão de um novo registro através de um formulário HTML.
- **Ler** – Listagem de todos os registros na página inicial.
- **Atualizar** – Edição de um registro existente com campos pré‑preenchidos.
- **Deletar** – Remoção de um registro com tela de confirmação.
- Validação no servidor e flash messages para feedback ao usuário.

## Estrutura do Projeto
```
Flask_Form_CRUD/
│
├─ templates/
│   ├─ index.html          # Layout do site (Bootstrap CDN incluído)
├─ app.py                 # Ponto de entrada – configuração do Flask, rotas e DB
├─ requirements.txt       # Dependências Python
└─ README.md              # Este documento
```

## Começando
### Pré‑requisitos
- Python 3.9+ (testado na versão 3.11)
- `virtualenv` (recomendado) ou outra ferramenta de ambiente virtual

### Instalação
1. **Clonar o repositório**
   ```bash
   git clone https://github.com/joseantonioalmeida/FORMULARIO-CRUD-FLASK
   cd FLASK_FORM_CRUD
   ```
2. **Criar e ativar um ambiente virtual**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. **Instalar as dependências**
   ```bash
   pip install -r requirements.txt
   ```

### Executando a Aplicação
```bash
python app.py
```
O servidor será iniciado em `http://127.0.0.1:5000/`. Abra esse endereço no navegador para usar a interface CRUD.

## Uso
- **Criar**: Clique em *Adicionar Novo* na página inicial, preencha o formulário e envie.
- **Ler**: A página inicial lista automaticamente todos os registros com opções *Editar* e *Deletar*.
- **Atualizar**: Clique em *Editar* ao lado de um registro, altere os campos e salve.
- **Deletar**: Clique em *Deletar* ao lado de um registro, confirme a ação e o item será removido.

## Testes
O projeto não inclui testes automatizados, mas é possível validar manualmente:
1. Adicione alguns registros.
2. Edite alguns deles.
3. Delete alguns registros.
4. Atualize a página inicial para confirmar que a lista reflete as alterações.

## Dependências
- **Flask** – Framework web
- **Bootstrap 5** – Estilização UI (via CDN em `base.html`)

Todas as dependências estão listadas em **requirements.txt**.

## Licença
Este projeto é disponibilizado para fins educacionais. Você pode usar, modificar e distribuir sob os termos da Licença MIT.

---
*Criado por:* **José Antonio de Almeida Silva** – Análise e Desenvolvimento de Sistemas, **UNINASSAU João Pessoa** – 2026
