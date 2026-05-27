# ⚡ 360 Training Tracker — Jersson Pro

App web en Streamlit para recomposición corporal, fútbol y preparación de 5k.

---

## 🚀 Instalación y ejecución

### Opción A — Local (Mac/PC)

```bash
# 1. Instalar Python si no lo tienes (python.org)

# 2. Instalar dependencias
pip install streamlit pandas plotly

# 3. Ejecutar la app
streamlit run app.py
```

La app abre automáticamente en tu navegador en `http://localhost:8501`

---

### Opción B — Streamlit Cloud (gratis, acceso desde celular)

1. Sube `app.py` y `requirements.txt` a un repositorio de GitHub
2. Ve a **share.streamlit.io** e inicia sesión con GitHub
3. Clic en **New app** → selecciona tu repo → `app.py`
4. Clic en **Deploy** — en 2 minutos tienes tu URL pública
5. Ábrela desde cualquier celular

---

## 📁 Archivos generados por la app

La app crea automáticamente estos archivos CSV en la misma carpeta:

| Archivo | Contenido |
|---|---|
| `sessions.csv` | Sesiones de entrenamiento completadas |
| `weight_log.csv` | Historial de peso corporal |
| `race_log.csv` | Tiempos en la carrera de 5k |

---

## 🏋️ Secciones de la app

- **Dashboard** — Resumen semanal, stats, entrenamiento del día
- **Plan de Entrenamiento** — Los 5 días con ejercicios detallados
- **Nutrición 360** — Macros, protocolo papaya, suplementación
- **Métricas** — Gráficas de peso y 5k, control de sesiones

---

## 📱 Cómo usar desde el celular

Después de hacer el deploy en Streamlit Cloud:

- **iPhone**: Safari → compartir → "Agregar a inicio"  
- **Android**: Chrome → menú ⋮ → "Añadir a pantalla de inicio"

---

## 🔧 Actualizar la app

Cualquier cambio que hagas en `app.py` y subas a GitHub se refleja automáticamente en Streamlit Cloud.
