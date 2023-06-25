# Atividade Sistemas Distribuídos 04

## Requisitos para iniciar 🛠

- python3 == 3.8.10
- pip == 20.0.2
- virtualenv == 20.21.0

## 1. Instalando dependências do projeto na máquina de desenvolvimento

### Cria um ambiente virtual chamado "atv_sd_04_venv"

```bash
python -m virtualenv atv_sd_04_venv
```

### Ativa o ambiente virtual criado acima

```bash
source atv_sd_04_venv/bin/activate
```

### Instala as bibliotecas externas do projeto

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

## 2. Inicia os containers Docker para desenvolvimento

```bash
docker-compose up -d --build
```

----------
Released in 2023. This project is under the MIT license.

By [Victor B. Fiamoncini](https://github.com/Victor-Fiamoncini) ☕
