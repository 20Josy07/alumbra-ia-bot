# 🤖 AlumbraIA - Bot de Apoyo Emocional

**AlumbraIA** es un bot de Telegram diseñado para ayudarte a detectar señales de **abuso psicológico** en tus conversaciones. Utiliza inteligencia artificial para analizar textos y brindar orientación emocional básica, recomendaciones de autocuidado, y consejos de prevención. Está orientado a promover el bienestar y la conciencia sobre relaciones dañinas.

![Logo](https://telegra.ph/file/7e2f7a8b2d52c61bf5ced.jpg)

---

## 🚀 Funcionalidades principales

- `/start` – Mensaje de bienvenida e introducción al bot.
- `/help` – Muestra todos los comandos disponibles.
- `/info` – Información sobre el proyecto y su propósito.
- `/analizar` – Envía una conversación para que sea analizada.
- `/resultados` – Muestra el análisis más reciente realizado.
- `/consejos` – Consejos útiles para tu bienestar emocional.
- `/feedback` – Enlace a una encuesta para ayudarnos a mejorar.

---

## 🔧 Requisitos del proyecto

- Python 3.8+
- Librerías:
  - `python-telegram-bot`
  - `re`, `time`, `importlib`, `typing`
- Acceso al token del bot de Telegram
- (Opcional) Configuración de webhook con certificado SSL si se usa en modo producción

---

## 🛠 Estructura del proyecto

HunterAlpha/
│
├── init.py
├── main.py # Archivo principal que inicia el bot
├── config.py # Contiene configuraciones (TOKEN, OWNER_ID, etc.)
├── modules/ # Módulos adicionales con comandos
│ ├── analizar.py
│ ├── consejos.py
│ ├── extras.py
│ └── ...

yaml
Copiar
Editar

---

## 🧠 ¿Cómo funciona el análisis?

El bot recibe una conversación como entrada (texto plano) y aplica filtros lingüísticos y patrones de comportamiento para detectar posibles señales como:

- Manipulación emocional
- Chantaje psicológico
- Gaslighting
- Control excesivo o posesivo

> ⚠️ *Este bot no reemplaza la ayuda profesional. Siempre recomendamos buscar orientación de psicólogos o terapeutas si te sientes en riesgo.*

---

## 💬 Enlaces útiles

- 🌐 Sitio oficial: [alumbraia.com](http://alumbraia.com)
- 💡 Canal de soporte: [@HelpBot_J01](https://t.me/HelpBot_J01)
- 💌 Contáctanos: [@Josyam01](https://t.me/Josyam01)

---

## ❤️ Apóyanos

¿Te gusta este proyecto? Puedes ayudarnos a crecer con una donación:

[![PayPal](https://img.shields.io/badge/Paypal-Donar-blue)](https://www.paypal.me/)

---

## 🧾 Licencia

Este proyecto está licenciado bajo los términos de la **Licencia MIT**.

---

## 🙏 Créditos

Desarrollado con 💜 por el equipo de **AlumbraIA**.  
Gracias a todas las personas que han contribuido con ideas, pruebas y soporte técnico.