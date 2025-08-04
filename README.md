
# 🐶🐱 VisionNet18 - Classificador de Animais com ResNet18 e Transfer Learning

Este projeto aplica **Transfer Learning** com a arquitetura **ResNet18 pré-treinada** para classificar imagens de **gatos**, **cães** e **animais selvagens**, utilizando um subconjunto cuidadosamente preparado do dataset [Animal Faces (AFHQ)](https://www.kaggle.com/datasets/andrewmvd/animal-faces).

---

## 📁 Estrutura do Projeto
---
```bash
.
├── .venv/                     # Ambiente virtual (ignorado no Git)
├── data/
│   └── processed/
│       └── Animais/
│           ├── train/        # Imagens de treino organizadas por classe
│           └── val/          # Imagens de validação organizadas por classe
├── notebook/
│   └── explore.ipynb         # Notebook com todo o pipeline de treinamento
├── src/
│   └── prepare_dataset.py    # Script para baixar e preparar o dataset
└── README.md
```
---

## 🔍 Objetivo

Classificar imagens em três categorias:
- 🐶 Cachorro (`dog`)
- 🐱 Gato (`cat`)
- 🐯 Animal selvagem (`wild`)

Utilizando uma abordagem de **Transfer learning** com a **ResNet18**, conseguimos reduzir o tempo de treinamento e aproveitar o conhecimento aprendido previamente além disso foram utilizados algumas técnicas de data augmentation para ajudar o modelo a aprender as variações das imagens e fazer com que para o treinamento do modelo fossem ainda mais imagens.

---

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/visionnet18.git
cd visionnet18
````

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Prepare o dataset

Certifique-se de ter uma conta no [Kaggle](https://www.kaggle.com/) e estar autenticado localmente. Então execute:

```bash
python prepare_dataset.py
```

> Isso fará o download do dataset "Animal Faces", criará um subconjunto balanceado e o organizará na pasta `data/processed/Animais`.

### 5. Execute o notebook

Abra `explore.ipynb` e execute as células para:

* Carregar dados com `ImageFolder`
* Aplicar data augmentation com `torchvision.transforms`
* Treinar a ResNet18
* Avaliar os resultados

---

## 🧠 Tecnologias Usadas

* Python 3.8+
* PyTorch
* torchvision
* kagglehub
* scikit-learn
* matplotlib

---

## 📊 Resultados (Exemplo)

> Após 10 épocas de treinamento:

* Acurácia de Validação: **98.67%**

(Os resultados podem variar conforme o número de imagens e ajustes no fine-tuning.)

---

## 📂 Dataset Original

📦 [Animal Faces Dataset (AFHQ)](https://www.kaggle.com/datasets/andrewmvd/animal-faces)
Contém imagens de alta qualidade e bem distribuídas entre classes.

---

## 📸 Previsões do Modelo

Abaixo, alguns exemplos de previsões feitas pelo modelo VisionNet18:

### 🐶 Exemplo 1: Cachorro detectado com alta confiança
![Previsão 2](https://i.imgur.com/knSEorY.png)

### 🐱 Exemplo 2: Gato corretamente classificado
![Previsão 1](https://i.imgur.com/vfqLGrB.png)

### 🐯 Exemplo 3: Animal selvagem identificado
![Previsão 3](https://i.imgur.com/xVv8Z8n.png)

---

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

## ✍️ Autor

Desenvolvido por [Geronimo Morais / LinkedIn](https://www.linkedin.com/in/geronimoneto/)


