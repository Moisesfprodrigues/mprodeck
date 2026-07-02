# MPRO Deck App

Aplicação desktop em Python baseada em Tkinter que simula um Stream Deck simples, com 8 botões configuráveis que podem reproduzir sons, mostrar imagens e executar ações via atalhos de teclado.

## Funcionalidades

- 8 botões personalizáveis (grid 4x2)
- Reprodução de ficheiros `.mp3` por botão
- Suporte a imagens `.png` por botão
- Títulos configuráveis via ficheiros `.txt`
- Atalhos de teclado (1–8) com ativação/desativação
- Feedback visual ao pressionar botão
- Interface gráfica em Tkinter

## Estrutura do projeto

```
MPRO_Deck_App/
├─ main.py
└─ assets/
   ├─ audio/
   │  ├─ sample1.mp3
   │  └─ ...
   ├─ img/
   │  ├─ img1.png
   │  └─ ...
   └─ text/
      ├─ label1.txt
      └─ ...
```

## Requisitos

```bash
pip install pygame pillow keyboard
```

## Como executar

```bash
python main.py
```

## Funcionamento

Cada botão:

- Reproduz áudio `assets/audio/sampleX.mp3`
- Mostra imagem `assets/img/imgX.png`
- Usa texto `assets/text/labelX.txt` (se existir)

## Atalhos

Teclas `1`–`8` ativam os botões correspondentes quando os atalhos estão ligados.

## Compilação para EXE

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
pyinstaller --onefile --noconsole --add-data "assets;assets" main.py
```

## Autor

Moisés Rodrigues — 2026
