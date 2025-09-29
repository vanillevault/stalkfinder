# 🕵️ stalkfinder.py

**OSINT Tool by Vanille**  
Búscalo. Encuéntralo. Analízalo. Todo desde la CLI.

>
> ## 🧠 ¿Qué es stalkfinder?

`stalkfinder.py` es una herramienta OSINT que busca la presencia digital de un **nombre de usuario** en múltiples plataformas sociales y web.  
Diseñada para ser rápida, minimalista y con una estética lowkey — estilo Vanille.

### 🛰️ Detecta presencia en:
- Instagram, Twitter, TikTok  
- GitHub, Reddit, Steam  
- Telegram, Pornhub, Spotify, Twitch  
- (Y puedes añadir más fácilmente)

- ## ⚙️ Instalación

```bash
git clone https://github.com/vanillevault/stalkfinder
cd stalkfinder
pip install -r requirements.txt

🚀 Uso rápido

python stalkfinder.py <username>

Opciones:

Flag	Descripción

--json	Guarda los resultados en <username>_stalk.json
--vanille	Activa respuestas con estilo Vanille IA


Ejemplo:

python stalkfinder.py dommage --json --vanille

🧪 Output CLI

>>> Buscando presencia para: dommage

┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Plataforma ┃ Estado       ┃ URL                                   ┃
┣━━━━━━━━━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ GitHub     ┃ Encontrado   ┃ https://github.com/dommage            ┃
┃ TikTok     ┃ No           ┃ https://www.tiktok.com/@dommage       ┃
┗━━━━━━━━━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

Con --vanille activado:

[VANILLE]: Usuario activo en GitHub → github.com/dommage

🧩 Plataformas incluidas

Edita el archivo platforms.json para añadir, quitar o personalizar plataformas.
Ejemplo de entrada:

{
  "name": "GitHub",
  "url": "https://github.com/{}"
}

📁 Estructura

stalkfinder/
├── stalkfinder.py       # Script principal
├── platforms.json       # Plataformas objetivo
├── requirements.txt     # Dependencias Python
└── README.md            # Este documento

🔐 Requisitos

Python 3.6 o superior

Módulos: requests, rich


Instalación de dependencias:

pip install -r requirements.txt


---

✍️ Autor

Coded by Vanille
Silk OSINT Lab — NodoSpectre Project
🔗 github.com/vanillevault


