import os
import random
import shutil
from sklearn.model_selection import train_test_split
import kagglehub

# 1. Baixar o dataset via kagglehub
print("⬇️ Baixando dataset do Kaggle...")
path = kagglehub.dataset_download("andrewmvd/animal-faces")  # Baixa e retorna o caminho local
print("✅ Dataset salvo em:", path)

# 2. Definir diretórios
orig_dir = os.path.join(path, "afhq")  # Dataset original (com subpastas train/val/test)
reduced_dir = os.path.abspath("./data/processed/Animais")  # Onde salvar o novo dataset reduzido

os.makedirs(reduced_dir, exist_ok=True)

# 3. Parâmetros de configuração
train_count = 50
val_count = 50
total_required = train_count + val_count
splits = ['train', 'val']
classes = ['cat', 'dog', 'wild']

# 4. Criar subconjunto do dataset
for class_name in classes:
    all_images = []

    # Coleta imagens tanto da pasta 'train' quanto da 'val'
    for split in splits:
        class_dir = os.path.join(orig_dir, split, class_name)
        if not os.path.isdir(class_dir):
            continue
        imgs = [f for f in os.listdir(class_dir) if f.lower().endswith('.jpg')]
        all_images += [os.path.join(class_dir, f) for f in imgs]

    if len(all_images) < total_required:
        print(f"❌ Classe '{class_name}' tem apenas {len(all_images)} imagens. Pulando...")
        continue

    # Seleciona aleatoriamente as imagens necessárias
    random.seed(42)
    selected = random.sample(all_images, total_required)

    # Divide em treino e validação
    train_imgs, val_imgs = train_test_split(
        selected, test_size=val_count, train_size=train_count, random_state=42
    )

    # Copiar imagens para nova estrutura
    for split_name, img_list in zip(['train', 'val'], [train_imgs, val_imgs]):
        dest_dir = os.path.join(reduced_dir, split_name, class_name)
        os.makedirs(dest_dir, exist_ok=True)

        for img_path in img_list:
            dst = os.path.join(dest_dir, os.path.basename(img_path))
            shutil.copyfile(img_path, dst)

# 5. Finalização
print("✅ Dataset reduzido e organizado salvo na pasta:", reduced_dir)
