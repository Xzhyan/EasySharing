# EasySharing*Free* - _Internal Sharing and Storage_

> Sistema de compartilhamento e armazenamento de arquivos diversos com interface web para ser usado especificamente em redes internas e domesticas.

---

![Descrição da imagem](bin/imgs/easysharing.png)

---

## Sumário

- [Informações](#informações)
- [Atualizações](#atualizações)
- [Licença](#licença)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Creditos](#creditos)

---

## Informações

EasySharing é uma evolução do projeto FileBrowserDjango de mesmo conceito. Ser um sistema web simples e leve para ser usado em redes internas de pequenas ou grandes empresas, redes domesticas ou qualquer outro tipo de ambiente de trabalho onde a conexão com rede externa não é necessaria.
O projeto ainda esta em desenvolvimento e inicialmente sua primeira versão vai ser gratuitas e simples. Uma nova versão mais robusta, dinamica e completa sera desenvolvida para fins comerciais.

---

## Atualizações

Várias mudanças durante o desenvolvimento porém ainda se constitui em uma versão inicial.

---

## Licença

A ferramenta pode ser utilizada livremente por qualquer pessoa, só peço que me avisem para que eu possa ter controle sobre o projeto. O código pode ser utilizado como base para estudos, mas não deve ser modificado e utilizado comercialmente sem autorização. O projeto é gratuito e não OpenSource.

---

## Instalação

1. Baixe do site ofcial o Python e instale em sua máquina.

2. Clone o repositório do github.

```bash
git clone https://github.com/Xzhyan/EasySharing.git
```

3. Acesse a pasta raiz.

```bash
cd EasySharing
```

4. Crie um ambiente virtual python

```bash
py -m venv .venv
```

5. Ative o ambiente virtual (Windows)

```bash
.venv\Scripts\activate
```

6. Instale o Django.

```bash
pip install Django
```

7. Faça as migrations do sistema.

```bash
py manage.py migrate
```

8. Inicie o sistema localmente.

```bash
py manage.py runserver
```

---

## Configuração

### Criar um usuário Adminitrador (Super Usuário)

```bash
py manage.py createsuperuser
```

### Configurar os Hosts autorizados

Altere o arquivo 'settings.py' dentro da pasta core do projeto: 'mysite\settings.py'.

```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.3.33']
```

---

## Uso

---

## Creditos
