# 🚀 Taller de Programación - Clase GitHub

Repositorio educativo diseñado para la práctica de control de versiones con **Git y GitHub**, colaboración mediante **Pull Requests**, y desarrollo de una API REST con **FastAPI**.

---

## 📁 Estructura del Proyecto

```text
clase-github/
├── .github/
│   └── pull_request_template.md  # Plantilla para la creación de Pull Requests
├── API/
│   ├── app.py                    # Servidor FastAPI principal
│   ├── ejemplo.py                # Funciones de ejemplo en Python
│   └── requirements.txt          # Dependencias de la API
├── js/
│   └── index.js                  # Script de prueba en JavaScript
├── solucionAndrea.py             # Soluciones individuales de los participantes
├── solucionJosue.py
├── solucionGerman.py
├── solucionRamiro.py
└── README.md                     # Documentación del proyecto
```

---

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/) *(opcional, para scripts JS)*

---

## ⚙️ Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/LizAndrea/clase-github.git
cd clase-github
```

### 2. Ejecutar la API REST (FastAPI)

1. **Instalar dependencias necesarias**:
   ```bash
   pip install -r API/requirements.txt
   ```

2. **Iniciar el servidor local**:
   ```bash
   uvicorn API.app:app --reload
   ```

3. **Acceder a los endpoints y documentación**:
   - 🌐 API Base: `http://127.0.0.1:8000`
   - 📖 Documentación Swagger UI: `http://127.0.0.1:8000/docs`
   - 📖 Documentación ReDoc: `http://127.0.0.1:8000/redoc`

**Endpoints disponibles**:
- `GET /familia`: Retorna lista de integrantes de ejemplo.
- `GET /taller`: Retorna lista de temas aprendidos en el taller.

---

### 3. Ejecutar Scripts de Ejercicios

Puedes ejecutar los scripts individuales de Python mediante la terminal:

```bash
python API/ejemplo.py
python solucionAndrea.py
```

---

## 🤝 Flujo de Trabajo y Colaboración

En este taller practicamos el flujo estándar de Git/GitHub:

1. **Crear una rama para tu característica o solución**:
   ```bash
   git checkout -b feature/mi-solucion
   ```
2. **Realizar commits estructurados**:
   ```bash
   git add .
   git commit -m "feat: agrega solucion para el ejercicio X"
   ```
3. **Enviar los cambios a la rama remota**:
   ```bash
   git push origin feature/mi-solucion
   ```
4. **Abrir un Pull Request (PR)** en GitHub utilizando la plantilla oficial `.github/pull_request_template.md`.

---

## 📄 Licencia

Este proyecto tiene fines educativos para el **Taller de Programación**.

