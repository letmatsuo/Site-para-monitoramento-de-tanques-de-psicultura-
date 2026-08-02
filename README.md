# 🐟 Sistema para Monitoramento de Tanques de Piscicultura

Sistema web desenvolvido para o monitoramento em tempo real dos parâmetros da água em tanques de piscicultura, auxiliando produtores na tomada de decisões e contribuindo para a saúde e o bem-estar dos peixes.

---

## 📖 Sobre o projeto

O projeto tem como objetivo facilitar o acompanhamento das condições da água por meio de uma plataforma web intuitiva, permitindo a visualização de informações coletadas por sensores instalados nos tanques.

Os dados são enviados por um microcontrolador e armazenados em um banco de dados, sendo apresentados ao usuário em uma interface organizada e de fácil interpretação.

Os parâmetros monitorados incluem:

- 🌡️ Temperatura da água
- 💧 pH
- 🫧 Oxigênio dissolvido
- 🌫️ Turbidez
- ⚗️ Amônia

Além da visualização em tempo real, o sistema pode emitir alertas quando algum parâmetro estiver fora dos níveis recomendados.

---

## 🚀 Tecnologias utilizadas

### Backend

- Python
- Django

### Frontend

- HTML5
- CSS3
- JavaScript

### Banco de dados

- MySQL (desenvolvimento)

### Hardware

- ESP32
- Sensores de monitoramento da qualidade da água

### Ferramentas

- Git
- GitHub
- Visual Studio Code

---

## ✨ Funcionalidades

- Monitoramento em tempo real dos sensores
- Interface web responsiva
- Exibição dos parâmetros da água
- Organização por páginas para cada sensor
- Atualização contínua das informações
- Sistema preparado para emissão de alertas

---

## 📂 Estrutura do projeto

```
Projeto/
│
├── monitoramento/
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Como executar
## Vale ressaltar que o projeto não pode ser executado de forma independende, visto que precisa ser conectado a um hardware e a um outro código de um ESP32.


### Clone o repositório

```bash
git clone https://github.com/letmatsuo/Site-para-monitoramento-de-tanques-de-psicultura-.git
```

### Entre na pasta

```bash
cd Site-para-monitoramento-de-tanques-de-psicultura-
```

### Crie um ambiente virtual

```bash
python -m venv venv
```

### Ative o ambiente virtual

Windows

```bash
venv\Scripts\activate
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

### Execute as migrações

```bash
python manage.py migrate
```

### Inicie o servidor

```bash
python manage.py runserver
```

## 🎯 Objetivos

- Automatizar o monitoramento da qualidade da água.
- Facilitar a visualização dos dados coletados.
- Auxiliar na prevenção de problemas na criação de peixes.
- Aplicar conhecimentos em desenvolvimento Full Stack e Internet das Coisas (IoT).

---

## 📸 Demonstração

Em breve serão adicionadas imagens da interface e demonstrações do sistema.

---

## 👩‍💻 Desenvolvedores

**Camila Vitória Faria, Giovana Souza Vilela Desidério, Letícia Tomomi Matsuo e Matheus Barbosa Ribeiro**

GitHub: https://github.com/letmatsuo

---

## 🏆 Projeto acadêmico

Este sistema foi desenvolvido como projeto acadêmico para aplicação de conceitos de:

- Desenvolvimento Web
- Python
- Django
- Internet das Coisas (IoT)
- Automação

---

## 📄 Licença

Projeto desenvolvido para fins acadêmicos e de aprendizagem.
