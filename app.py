"""
╔══════════════════════════════════════════════════════════════════╗
║            360 TRAINING TRACKER — Jersson Pro  v3.0             ║
║   Recomposición Corporal · Fútbol · 5K · Memoria Semanal        ║
╚══════════════════════════════════════════════════════════════════╝
Instalar: pip install streamlit pandas plotly
Ejecutar:  streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import date, timedelta
import os
import plotly.express as px
import random
# ─────────────────────────────────────────────
#  CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="360 Training Tracker",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  ESTILOS GLOBALES (Mobile-First)
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Space+Mono:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Syne', sans-serif; }
.stApp { background: #0a0f0a; color: #e8f5e8; }
[data-testid="stSidebar"] { background: #111811 !important; border-right: 1px solid rgba(57,255,74,0.1); }
[data-testid="stSidebar"] * { color: #8aad8a !important; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color: #39ff4a !important; }
h1 { color: #39ff4a !important; font-weight: 800 !important; }
h2 { color: #e8f5e8 !important; font-weight: 700 !important; }
h3 { color: #8aad8a !important; font-weight: 600 !important; }
.card { background: #141f14; border: 1px solid rgba(57,255,74,0.1); border-radius: 16px; padding: 16px 20px; margin-bottom: 12px; }
.card-accent { background: rgba(57,255,74,0.06); border: 1px solid rgba(57,255,74,0.2); border-radius: 16px; padding: 16px 20px; margin-bottom: 12px; }
.card-week { background: #111811; border: 1px solid rgba(57,255,74,0.12); border-radius: 14px; padding: 14px 16px; margin-bottom: 8px; transition: all 0.2s; }
.card-week:hover { border-color: rgba(57,255,74,0.3); }
.card-week-active { background: rgba(57,255,74,0.06); border: 1px solid rgba(57,255,74,0.35) !important; border-radius: 14px; padding: 14px 16px; margin-bottom: 8px; }
.stat-val { font-size: 32px; font-weight: 800; color: #39ff4a; font-family: 'Space Mono', monospace; line-height: 1; }
.stat-label { font-size: 11px; color: #4d6b4d; font-family: 'Space Mono', monospace; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 4px; }
.tag { display: inline-block; font-size: 10px; padding: 3px 10px; border-radius: 20px; font-family: 'Space Mono', monospace; font-weight: 700; margin-right: 4px; }
.tag-green { background: rgba(57,255,74,0.12); color: #39ff4a; }
.tag-warn  { background: rgba(255,170,34,0.12); color: #ffaa22; }
.tag-red   { background: rgba(255,68,68,0.12);  color: #ff4444; }
.tag-blue  { background: rgba(57,100,255,0.12); color: #7b9fff; }
.tag-gray  { background: rgba(100,100,100,0.15); color: #888; }
.rec-card { display: flex; gap: 12px; align-items: flex-start; background: #1a271a; border: 1px solid rgba(57,255,74,0.08); border-radius: 12px; padding: 12px 14px; margin-bottom: 8px; }
.week-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(57,255,74,0.1); border: 1px solid rgba(57,255,74,0.25); border-radius: 20px; padding: 4px 12px; font-size: 12px; font-family: 'Space Mono', monospace; color: #39ff4a; font-weight: 700; }
.week-badge-gray { display: inline-flex; align-items: center; gap: 6px; background: rgba(100,100,100,0.1); border: 1px solid rgba(100,100,100,0.2); border-radius: 20px; padding: 4px 12px; font-size: 12px; font-family: 'Space Mono', monospace; color: #666; font-weight: 700; }
.delta-pos { color: #39ff4a; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; }
.delta-neg { color: #ff4444; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; }
.delta-neu { color: #8aad8a; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 13px; }
.stButton > button { background: #39ff4a !important; color: #0a0f0a !important; font-weight: 700 !important; border: none !important; border-radius: 12px !important; font-family: 'Syne', sans-serif !important; width: 100%; }
.stButton > button:hover { opacity: 0.9 !important; }
.stTextInput input, .stNumberInput input, .stDateInput input, .stSelectbox select { background: #1a271a !important; border: 1px solid rgba(57,255,74,0.15) !important; color: #e8f5e8 !important; border-radius: 10px !important; }
.streamlit-expanderHeader { background: #141f14 !important; border: 1px solid rgba(57,255,74,0.1) !important; border-radius: 12px !important; color: #e8f5e8 !important; font-weight: 700 !important; }
.stProgress > div > div { background: #39ff4a !important; }
.stTabs [data-baseweb="tab-list"] { background: #111811; border-radius: 12px; }
.stTabs [data-baseweb="tab"] { color: #4d6b4d !important; font-family: 'Syne', sans-serif; font-weight: 600; }
.stTabs [aria-selected="true"] { color: #39ff4a !important; border-bottom: 2px solid #39ff4a !important; }
hr { border-color: rgba(57,255,74,0.1) !important; }
footer { display: none !important; }
#MainMenu { display: none !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  PERSISTENCIA CSV — ESTRUCTURA SEMANAL
# ─────────────────────────────────────────────
SESSIONS_FILE = "sessions.csv"   # columnas: semana, dia_num, completed, fecha
WEIGHT_FILE   = "weight_log.csv" # columnas: semana, fecha, peso
RACE_FILE     = "race_log.csv"   # columnas: semana, fecha, tiempo_min
NOTES_FILE    = "weekly_notes.csv" # columnas: semana, fecha_inicio, nota, objetivo

def get_week_number():
    """Devuelve el número de semana ISO del año actual."""
    return date.today().isocalendar()[1]

def get_week_start(offset=0):
    """Fecha del lunes de la semana actual (o de una semana anterior con offset negativo)."""
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    return monday + timedelta(weeks=offset)

def week_label(semana_num):
    """Convierte número de semana ISO a etiqueta legible."""
    # Encontrar el lunes de esa semana en el año actual
    try:
        d = date.fromisocalendar(date.today().year, semana_num, 1)
        return f"Semana {semana_num}  ({d.strftime('%d %b')} – {(d + timedelta(days=4)).strftime('%d %b')})"
    except:
        return f"Semana {semana_num}"

# ── Sessions ──
def load_sessions():
    if os.path.exists(SESSIONS_FILE):
        df = pd.read_csv(SESSIONS_FILE)
        if "semana" not in df.columns:
            df["semana"] = get_week_number()
        return df
    return pd.DataFrame(columns=["semana", "dia_num", "completed", "fecha"])

def save_sessions(df):
    df.to_csv(SESSIONS_FILE, index=False)

# ── Weight ──
def load_weight():
    if os.path.exists(WEIGHT_FILE):
        df = pd.read_csv(WEIGHT_FILE, parse_dates=["fecha"])
        if "semana" not in df.columns:
            df["semana"] = get_week_number()
        return df
    return pd.DataFrame(columns=["semana", "fecha", "peso"])

def save_weight(df):
    df.to_csv(WEIGHT_FILE, index=False)

# ── Races ──
def load_races():
    if os.path.exists(RACE_FILE):
        df = pd.read_csv(RACE_FILE, parse_dates=["fecha"])
        if "semana" not in df.columns:
            df["semana"] = get_week_number()
        return df
    return pd.DataFrame(columns=["semana", "fecha", "tiempo_min"])

def save_races(df):
    df.to_csv(RACE_FILE, index=False)

# ── Notes ──
def load_notes():
    if os.path.exists(NOTES_FILE):
        return pd.read_csv(NOTES_FILE)
    return pd.DataFrame(columns=["semana", "fecha_inicio", "nota", "objetivo"])

def save_notes(df):
    df.to_csv(NOTES_FILE, index=False)


# ─────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────
if "sessions_df" not in st.session_state:
    st.session_state.sessions_df = load_sessions()
if "weight_df" not in st.session_state:
    st.session_state.weight_df = load_weight()
if "race_df" not in st.session_state:
    st.session_state.race_df = load_races()
if "notes_df" not in st.session_state:
    st.session_state.notes_df = load_notes()
if "semana_vista" not in st.session_state:
    st.session_state.semana_vista = get_week_number()


# ─────────────────────────────────────────────
#  HELPERS SEMANA
# ─────────────────────────────────────────────
def sessions_de_semana(semana):
    df = st.session_state.sessions_df
    if df.empty:
        return pd.DataFrame(columns=["semana", "dia_num", "completed", "fecha"])
    return df[df["semana"] == semana]

def completadas_semana(semana):
    df = sessions_de_semana(semana)
    if df.empty:
        return 0
    return int(df["completed"].sum())

def peso_semana(semana):
    df = st.session_state.weight_df
    if df.empty:
        return None
    s = df[df["semana"] == semana]
    return s.sort_values("fecha").iloc[-1]["peso"] if not s.empty else None

def mejor_5k_semana(semana):
    df = st.session_state.race_df
    if df.empty:
        return None
    s = df[df["semana"] == semana]
    return s["tiempo_min"].min() if not s.empty else None

def fmt_tiempo(t):
    if t is None:
        return "—"
    m, s = int(t), int((t % 1) * 60)
    return f"{m}:{s:02d}"

def semanas_con_datos():
    """Retorna lista de semanas que tienen algún dato, ordenadas desc."""
    semanas = set()
    for df in [st.session_state.sessions_df, st.session_state.weight_df, st.session_state.race_df]:
        if not df.empty and "semana" in df.columns:
            semanas.update(df["semana"].unique().tolist())
    semanas.add(get_week_number())
    return sorted(semanas, reverse=True)


# ─────────────────────────────────────────────
#  DATOS DEL PLAN
# ─────────────────────────────────────────────
PLAN = {
    "Día 1 — Impacto Medio 🏋️": {
        "tag": "tag-warn", "tag_text": "Impacto Medio",
        "descripcion": "Tren inferior explosivo y resistencia aeróbica base para el 5k.",
        "fuerza": [
            {"nombre": "Sentadilla Búlgara", "series": "4×8/pierna", "icon": "🦵",
             "tecnica": "Pie trasero en banco. Baja hasta que la rodilla trasera casi toque el suelo. Torso erguido.",
             "tips": "💡 Reduce asimetría de fuerza, clave en futbolistas.",
             "musculos": ["Cuádriceps", "Glúteos", "Estabilizadores"]},
            {"nombre": "Peso Muerto Rumano", "series": "3×10", "icon": "🔒",
             "tecnica": "Bisagra de cadera pura. Baja deslizando la barra por las piernas hasta sentir el estiramiento máximo.",
             "tips": "💡 Esencial para prevenir lesiones de isquiotibiales.",
             "musculos": ["Isquiotibiales", "Glúteos", "Espalda baja"]},
            {"nombre": "Prensa pies altos", "series": "3×12", "icon": "⬆️",
             "tecnica": "Pies en parte alta de la plataforma. Mayor activación de glúteos y femorales.",
             "tips": "💡 Pies altos = femorales/glúteos. Pies bajos = cuádriceps.",
             "musculos": ["Cuádriceps", "Glúteos", "Femorales"]},
        ],
        "cardio": {"tipo": "Cardio Tempo 5k", "icon": "🏃",
                   "descripcion": "20 min en cinta a ritmo tempo. Desarrolla el umbral anaeróbico.",
                   "parametros": "Ritmo: 5:30–6:00 min/km · FC: 80–85% FCM · Inclinación: 1%"},
    },
    "Día 2 — Cero Impacto 🚣": {
        "tag": "tag-blue", "tag_text": "Cero Impacto",
        "descripcion": "Tren superior y cardio sin carga articular.",
        "fuerza": [
            {"nombre": "Press Inclinado Mancuernas", "series": "4×8-10", "icon": "💪",
             "tecnica": "Banco 30-45°. Codos a 45°. Contrae el pecho en la cima.",
             "tips": "💡 Trabaja pecho superior sin estrés en el hombro anterior.",
             "musculos": ["Pecho superior", "Hombro anterior", "Tríceps"]},
            {"nombre": "Remo Polea Baja", "series": "4×10", "icon": "🔗",
             "tecnica": "Agarre neutro. Codos al cuerpo. Aprieta omóplatos 1 seg al final.",
             "tips": "💡 No uses el impulso del torso. Pausa final maximiza contracción.",
             "musculos": ["Dorsal", "Romboides", "Bíceps"]},
        ],
        "cardio": {"tipo": "HIIT Remo / Bici Asalto", "icon": "⚡",
                   "descripcion": "10 series en remo o bici de asalto. Máxima intensidad.",
                   "parametros": "10 × (30s sprint 100% + 30s descanso completo)"},
    },
    "Día 3 — Prevención y Core 🛡️": {
        "tag": "tag-green", "tag_text": "Prevención",
        "descripcion": "Blindar articulaciones y fortalecer cadena posterior.",
        "fuerza": [
            {"nombre": "Paseo del Granjero", "series": "4×30m", "icon": "🧑‍🌾",
             "tecnica": "Mancuernas pesadas. Hombros atrás, core activo, pasos cortos.",
             "tips": "💡 Desarrolla agarre, core lateral y estabilidad global.",
             "musculos": ["Core", "Trapecios", "Antebrazo"]},
            {"nombre": "Curl Nórdico (Nordic Curl)", "series": "4×5", "icon": "🛡️",
             "tecnica": "De rodillas, pies fijos. Baja resistiendo con isquiotibiales. Usa manos al final.",
             "tips": "💡 Reduce riesgo de lesión isquiotibial hasta un 51%.",
             "musculos": ["Isquiotibiales", "Glúteos"]},
            {"nombre": "Box Jumps (bajada con paso)", "series": "3×5", "icon": "📦",
             "tecnica": "Salto explosivo al cajón. Baja SIEMPRE caminando, nunca saltando.",
             "tips": "💡 La bajada saltando genera 3-4× el impacto de la subida.",
             "musculos": ["Piernas", "Potencia", "SNC"]},
        ],
        "cardio": None,
    },
    "Día 4 — Impacto Alto 🔥": {
        "tag": "tag-red", "tag_text": "Impacto Alto",
        "descripcion": "Potencia de cadera e intervalos específicos 5k.",
        "fuerza": [
            {"nombre": "Hip Thrust", "series": "4×10", "icon": "🍑",
             "tecnica": "Espalda en banco, barra con pad. Empuja caderas al techo. Aprieta glúteos 1 seg.",
             "tips": "💡 Potencia directamente la aceleración en el fútbol.",
             "musculos": ["Glúteos", "Isquiotibiales", "Core"]},
            {"nombre": "Kettlebell Swings", "series": "4×12", "icon": "🔔",
             "tecnica": "Bisagra de cadera explosiva, no sentadilla. La KB sube por la cadera, no los brazos.",
             "tips": "💡 Patrón motor idéntico al sprint. Esencial para el fútbol.",
             "musculos": ["Glúteos", "Femorales", "Core", "Potencia"]},
        ],
        "cardio": {"tipo": "Intervalos específicos 5k", "icon": "🏅",
                   "descripcion": "El entrenamiento más específico para mejorar el 5k.",
                   "parametros": "5 × (3 min a ritmo 5k + 1.5 min trote suave)"},
    },
    "Día 5 — RSA Alto 🚀": {
        "tag": "tag-red", "tag_text": "RSA Máximo",
        "descripcion": "Repeated Sprint Ability — clave para el fútbol de alto nivel.",
        "fuerza": [
            {"nombre": "Press Militar", "series": "4×8", "icon": "🏋️",
             "tecnica": "De pie. Barra desde clavícula hasta arriba de la cabeza. Core apretado.",
             "tips": "💡 Estabilidad de hombro esencial para duelos aéreos.",
             "musculos": ["Hombros", "Tríceps", "Core superior"]},
            {"nombre": "Empuje de Trineo (Sled Push)", "series": "3 rondas", "icon": "🛷",
             "tecnica": "Posición inclinada, pasos explosivos. Sin trineo: sprint con banda de resistencia.",
             "tips": "💡 Patrón motor idéntico al sprint. El ejercicio más transferible al fútbol.",
             "musculos": ["Cuádriceps", "Glúteos", "SNC"]},
        ],
        "cardio": {"tipo": "HIIT RSA en cinta", "icon": "🚀",
                   "descripcion": "El protocolo más exigente. 15s de máximo absoluto.",
                   "parametros": "Cinta 4% inclinación · 8 × (15s sprint MÁXIMO + 45s descanso)"},
    },
}

NUTRICION_RECS = [
    ("💧", "Hidratación", "35ml/kg mínimo. El rendimiento baja 5% con solo 2% de deshidratación."),
    ("😴", "Sueño anabólico", "8h mínimo. La GH se libera en sueño profundo. Sin sueño, sin recomposición."),
    ("🌿", "Papaya post-entreno", "150g + 8 semillas masticadas. La papaína mejora absorción de proteínas y reduce inflamación."),
    ("🥩", "Proteína alta", "1.8–2.2g/kg/día. Para 75kg = 135–165g. Distribuye en 4–5 tomas."),
]


# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚡ 360 Training")
    st.markdown("**Tracker  v3.0**")
    st.markdown("---")

    semana_actual = get_week_number()
    st.markdown(f"<div style='font-size:11px;color:#4d6b4d;font-family:Space Mono'>HOY: {date.today().strftime('%d %b %Y').upper()}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:11px;color:#39ff4a;font-family:Space Mono;font-weight:700'>📅 SEMANA {semana_actual}</div>", unsafe_allow_html=True)
    st.markdown("")

    seccion = st.radio("Navegar", [
        "🏠 Dashboard",
        "🏋️ Plan de Entrenamiento",
        "📅 Historial Semanal",
        "🥗 Nutrición 360",
        "📊 Métricas y Progreso",
        "🏃‍♂️ Analítica 5K",
        "👨‍🍳 Chef AI",
        "🛠️ Constructor de Rutinas"
    ], label_visibility="collapsed")

    st.markdown("---")

    # Mini resumen semana actual
    comp = completadas_semana(semana_actual)
    st.markdown(f"<div class='stat-label'>Semana {semana_actual} — Sesiones</div>", unsafe_allow_html=True)
    st.progress(min(comp / 5, 1.0))
    st.markdown(f"<div style='font-size:13px;color:#39ff4a;font-family:Space Mono;font-weight:700'>{comp}/5 completadas</div>", unsafe_allow_html=True)
    st.markdown("")

    peso_act = peso_semana(semana_actual)
    if peso_act:
        st.markdown(f"<div class='stat-label'>Peso actual</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:18px;font-weight:800;color:#e8f5e8'>{peso_act:.1f} kg</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<div style='font-size:10px;color:#4d6b4d;font-family:Space Mono'>Jersson Pro · v3.0</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  ══ DASHBOARD ══
# ─────────────────────────────────────────────
if seccion == "🏠 Dashboard":
    semana_actual = get_week_number()
    st.markdown("# ⚡ 360 Training Tracker")
    st.markdown(f"<div style='color:#4d6b4d;font-family:Space Mono;font-size:12px;margin-bottom:20px'>SEMANA {semana_actual} · {date.today().strftime('%d %B %Y').upper()}</div>", unsafe_allow_html=True)

    # Stats top
    comp = completadas_semana(semana_actual)
    peso_hoy = peso_semana(semana_actual)
    mejor_5k = mejor_5k_semana(semana_actual)

    # Comparación con semana anterior
    comp_prev   = completadas_semana(semana_actual - 1)
    peso_prev   = peso_semana(semana_actual - 1)
    mejor_prev  = mejor_5k_semana(semana_actual - 1)

    col1, col2, col3 = st.columns(3)
    with col1:
        delta_comp = comp - comp_prev if comp_prev is not None else 0
        st.markdown(f"""<div class='card'>
            <div class='stat-label'>Sesiones S{semana_actual}</div>
            <div class='stat-val'>{comp}/5</div>
            <div class='{"delta-pos" if delta_comp >= 0 else "delta-neg"}'>{delta_comp:+d} vs sem. ant.</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        peso_str = f"{peso_hoy:.1f}" if peso_hoy else "—"
        if peso_hoy and peso_prev:
            dp = peso_hoy - peso_prev
            delta_peso_html = f"<div class='{'delta-pos' if dp <= 0 else 'delta-neg'}'>{dp:+.1f} kg vs sem. ant.</div>"
        else:
            delta_peso_html = "<div class='delta-neu'>Sin dato anterior</div>"
        st.markdown(f"""<div class='card'>
            <div class='stat-label'>Peso (kg)</div>
            <div class='stat-val'>{peso_str}</div>
            {delta_peso_html}
        </div>""", unsafe_allow_html=True)
    with col3:
        t_str = fmt_tiempo(mejor_5k)
        if mejor_5k and mejor_prev:
            dt = mejor_prev - mejor_5k
            delta_5k_html = f"<div class='{'delta-pos' if dt >= 0 else 'delta-neg'}'>{'-' if dt >= 0 else '+'}{abs(dt):.1f} min vs sem. ant.</div>"
        else:
            delta_5k_html = "<div class='delta-neu'>Sin dato anterior</div>"
        st.markdown(f"""<div class='card'>
            <div class='stat-label'>Mejor 5k</div>
            <div class='stat-val' style='font-size:24px'>{t_str}</div>
            {delta_5k_html}
        </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Progreso días de la semana
    st.markdown("### 📅 Semana actual")
    dias_plan = list(PLAN.keys())
    cols = st.columns(5)
    sessions_df = st.session_state.sessions_df
    for i, (col, dia) in enumerate(zip(cols, dias_plan)):
        dia_num = f"Día {i+1}"
        s_week = sessions_df[(sessions_df["semana"] == semana_actual) & (sessions_df["dia_num"] == dia_num)] if not sessions_df.empty else pd.DataFrame()
        done = not s_week.empty and bool(s_week["completed"].values[0])
        with col:
            if done:
                st.markdown(f"<div style='text-align:center;background:rgba(57,255,74,0.15);border:1px solid #39ff4a;border-radius:12px;padding:10px 4px'><div style='font-size:18px'>✅</div><div style='font-size:10px;color:#39ff4a;font-family:Space Mono;font-weight:700'>D{i+1}</div></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align:center;background:#141f14;border:1px solid rgba(57,255,74,0.1);border-radius:12px;padding:10px 4px'><div style='font-size:18px'>⭕</div><div style='font-size:10px;color:#4d6b4d;font-family:Space Mono'>D{i+1}</div></div>", unsafe_allow_html=True)

    st.markdown("")
    st.progress(min(comp / 5, 1.0))
    st.markdown(f"<div style='font-size:12px;color:#8aad8a;font-family:Space Mono'>{comp} de 5 sesiones · {int(comp/5*100)}% completado</div>", unsafe_allow_html=True)

    st.markdown("---")

    # Entrenamiento de hoy
    dia_semana = date.today().weekday()
    if dia_semana < 5:
        hoy_plan = dias_plan[dia_semana]
        hoy_data = PLAN[hoy_plan]
        st.markdown("### 🎯 Entrenamiento de hoy")
        st.markdown(f"""<div class='card-accent'>
            <div style='font-size:11px;font-family:Space Mono;color:#4d6b4d;margin-bottom:6px'>DÍA {dia_semana+1} DE 5</div>
            <div style='font-size:18px;font-weight:800;color:#e8f5e8'>{hoy_plan}</div>
            <div style='font-size:13px;color:#8aad8a;margin-top:6px'>{hoy_data["descripcion"]}</div>
            <div style='margin-top:10px'><span class='tag {hoy_data["tag"]}'>{hoy_data["tag_text"]}</span><span class='tag tag-green'>{len(hoy_data["fuerza"])} ejercicios</span></div>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown("### 🏖️ Fin de semana — Descanso activo")
        st.markdown("""<div class='card'><div style='font-size:13px;color:#8aad8a'>Caminata 30–45 min, movilidad, yoga o natación. El descanso es donde el cuerpo se adapta.</div></div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💡 Recomendaciones de hoy")
    for icon, titulo, desc in NUTRICION_RECS:
        st.markdown(f"""<div class='rec-card'>
            <div style='font-size:22px'>{icon}</div>
            <div><div style='font-size:13px;font-weight:700;color:#e8f5e8'>{titulo}</div>
            <div style='font-size:11px;color:#4d6b4d;font-family:Space Mono;margin-top:3px;line-height:1.5'>{desc}</div></div>
        </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  ══ PLAN DE ENTRENAMIENTO ══
# ─────────────────────────────────────────────
elif seccion == "🏋️ Plan de Entrenamiento":
    semana_actual = get_week_number()
    st.markdown("# 🏋️ Plan de Entrenamiento")
    st.markdown(f"<div style='color:#4d6b4d;font-family:Space Mono;font-size:12px;margin-bottom:20px'>SEMANA {semana_actual} · 5 DÍAS</div>", unsafe_allow_html=True)

    dia_sel = st.selectbox("Selecciona el día:", list(PLAN.keys()), label_visibility="collapsed")
    idx_dia = list(PLAN.keys()).index(dia_sel)
    data = PLAN[dia_sel]
    dia_num = f"Día {idx_dia + 1}"

    st.markdown(f"""<div class='card-accent'>
        <div style='font-size:11px;font-family:Space Mono;color:#4d6b4d;margin-bottom:4px'>{dia_num.upper()} · SEMANA {semana_actual}</div>
        <div style='font-size:20px;font-weight:800'>{dia_sel}</div>
        <div style='font-size:13px;color:#8aad8a;margin-top:6px'>{data["descripcion"]}</div>
        <div style='margin-top:10px'><span class='tag {data["tag"]}'>{data["tag_text"]}</span></div>
    </div>""", unsafe_allow_html=True)

    st.markdown("### 💪 Bloque de Fuerza")
    for ex in data["fuerza"]:
        with st.expander(f"{ex['icon']}  {ex['nombre']}  ·  {ex['series']}"):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"<div style='font-size:13px;color:#8aad8a;line-height:1.6'>{ex['tecnica']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='font-size:13px;color:#39ff4a;margin-top:8px'>{ex['tips']}</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div class='stat-label'>Músculos</div>", unsafe_allow_html=True)
                for m in ex["musculos"]:
                    st.markdown(f"<span class='tag tag-green'>{m}</span>", unsafe_allow_html=True)
                st.markdown(f"<div class='stat-label' style='margin-top:10px'>Series</div><div style='font-size:18px;font-weight:800;color:#39ff4a;font-family:Space Mono'>{ex['series']}</div>", unsafe_allow_html=True)
            st.markdown(f"""<div style='background:#1a271a;border:1px dashed rgba(57,255,74,0.15);border-radius:10px;padding:14px;text-align:center;margin-top:10px'>
                <div style='font-size:10px;color:#4d6b4d;font-family:Space Mono'>TÉCNICA VISUAL — {ex["nombre"]}</div>
                <img src='https://via.placeholder.com/400x160/141f14/39ff4a?text={ex["nombre"].replace(" ", "+")}' style='width:100%;border-radius:8px;margin-top:8px;opacity:0.4'/>
            </div>""", unsafe_allow_html=True)

    if data["cardio"]:
        st.markdown("---")
        c = data["cardio"]
        st.markdown(f"### {c['icon']} Bloque de Cardio — {c['tipo']}")
        st.markdown(f"""<div class='card'>
            <div style='font-size:13px;color:#8aad8a;line-height:1.6;margin-bottom:10px'>{c["descripcion"]}</div>
            <div style='background:#0a0f0a;border-radius:10px;padding:10px 14px'>
                <div style='font-size:11px;font-family:Space Mono;color:#39ff4a'>{c["parametros"]}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ✅ Completar sesión")
    sessions_df = st.session_state.sessions_df
    s_filtrada = sessions_df[(sessions_df["semana"] == semana_actual) & (sessions_df["dia_num"] == dia_num)] if not sessions_df.empty else pd.DataFrame()
    ya_done = not s_filtrada.empty and bool(s_filtrada["completed"].values[0])

    if ya_done:
        st.markdown(f"<div style='background:rgba(57,255,74,0.1);border:1px solid rgba(57,255,74,0.3);border-radius:12px;padding:12px 16px;font-weight:700;color:#39ff4a'>✅ {dia_num} completado — Semana {semana_actual}</div>", unsafe_allow_html=True)
    else:
        if st.button(f"🏁 Completar {dia_num} — Semana {semana_actual}"):
            nueva = pd.DataFrame([{"semana": semana_actual, "dia_num": dia_num, "completed": True, "fecha": str(date.today())}])
            st.session_state.sessions_df = pd.concat([sessions_df, nueva], ignore_index=True)
            save_sessions(st.session_state.sessions_df)
            st.balloons()
            st.toast(f"🔥 ¡{dia_num} completado! Semana {semana_actual}", icon="💪")
            st.rerun()


# ─────────────────────────────────────────────
#  ══ HISTORIAL SEMANAL ══
# ─────────────────────────────────────────────
elif seccion == "📅 Historial Semanal":
    semana_actual = get_week_number()
    st.markdown("# 📅 Historial Semanal")
    st.markdown("<div style='color:#4d6b4d;font-family:Space Mono;font-size:12px;margin-bottom:20px'>TODAS LAS SEMANAS · EVOLUCIÓN COMPLETA</div>", unsafe_allow_html=True)

    semanas = semanas_con_datos()

    # Resumen visual de todas las semanas
    st.markdown("### 🗓️ Resumen por semana")
    for sem in semanas:
        comp = completadas_semana(sem)
        peso = peso_semana(sem)
        t5k  = mejor_5k_semana(sem)
        es_actual = sem == semana_actual

        # nota de la semana
        notes_df = st.session_state.notes_df
        nota_row = notes_df[notes_df["semana"] == sem] if not notes_df.empty else pd.DataFrame()
        nota_txt = nota_row.iloc[0]["nota"] if not nota_row.empty else ""

        badge = f"<span class='week-badge'>📅 Semana {sem} {'· ACTUAL' if es_actual else ''}</span>"
        card_class = "card-week-active" if es_actual else "card-week"

        dias_html = ""
        for d in range(1, 6):
            dn = f"Día {d}"
            s_df = st.session_state.sessions_df
            done = (not s_df.empty and
                    not s_df[(s_df["semana"] == sem) & (s_df["dia_num"] == dn)].empty and
                    bool(s_df[(s_df["semana"] == sem) & (s_df["dia_num"] == dn)]["completed"].values[0]))
            dias_html += f"<span style='font-size:16px'>{'✅' if done else '⭕'}</span>"

        peso_html = f"{peso:.1f} kg" if peso else "—"
        t5k_html  = fmt_tiempo(t5k)

        st.markdown(f"""<div class='{card_class}'>
            <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:10px'>
                {badge}
                <div style='font-size:11px;color:#4d6b4d;font-family:Space Mono'>{comp}/5 sesiones</div>
            </div>
            <div style='display:flex;gap:6px;margin-bottom:10px'>{dias_html}</div>
            <div style='display:flex;gap:16px'>
                <div><div class='stat-label'>Peso</div><div style='font-size:15px;font-weight:700;color:#e8f5e8'>{peso_html}</div></div>
                <div><div class='stat-label'>Mejor 5k</div><div style='font-size:15px;font-weight:700;color:#e8f5e8'>{t5k_html}</div></div>
                <div><div class='stat-label'>Completado</div><div style='font-size:15px;font-weight:700;color:#39ff4a'>{int(comp/5*100)}%</div></div>
            </div>
            {f'<div style="margin-top:10px;font-size:12px;color:#8aad8a;font-family:Space Mono;border-top:1px solid rgba(57,255,74,0.08);padding-top:8px">📝 {nota_txt}</div>' if nota_txt else ''}
        </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Agregar nota a una semana
    st.markdown("### 📝 Añadir nota a una semana")
    with st.form("form_nota"):
        sem_opciones = [f"Semana {s}{' (actual)' if s == semana_actual else ''}" for s in semanas]
        sem_elegida = st.selectbox("Semana:", sem_opciones)
        sem_num = int(sem_elegida.split(" ")[1])
        objetivo = st.selectbox("Tipo de nota:", ["📋 Nota general", "🎯 Objetivo logrado", "⚠️ Dificultad encontrada", "💡 Aprendizaje"])
        nota_input = st.text_area("Escribe tu nota:", placeholder="Ej: Aumenté peso en sentadilla búlgara. Me costó el día 4 por poco sueño...")
        if st.form_submit_button("💾 Guardar nota"):
            if nota_input.strip():
                notes_df = st.session_state.notes_df
                # Actualizar si ya existe
                if not notes_df.empty and sem_num in notes_df["semana"].values:
                    st.session_state.notes_df.loc[notes_df["semana"] == sem_num, "nota"] = nota_input.strip()
                    st.session_state.notes_df.loc[notes_df["semana"] == sem_num, "objetivo"] = objetivo
                else:
                    nueva = pd.DataFrame([{"semana": sem_num, "fecha_inicio": str(get_week_start(sem_num - semana_actual)), "nota": nota_input.strip(), "objetivo": objetivo}])
                    st.session_state.notes_df = pd.concat([notes_df, nueva], ignore_index=True)
                save_notes(st.session_state.notes_df)
                st.toast("Nota guardada ✓", icon="📝")
                st.rerun()

    st.markdown("---")

    # Gráfica de consistencia semanal (sesiones por semana)
    st.markdown("### 📈 Consistencia semanal")
    if len(semanas) >= 2:
        data_chart = pd.DataFrame([{
            "Semana": f"S{s}",
            "Sesiones": completadas_semana(s),
            "Peso": peso_semana(s) or 0,
        } for s in sorted(semanas)])

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=data_chart["Semana"],
            y=data_chart["Sesiones"],
            marker_color=["#39ff4a" if s == semana_actual else "#2dcc3a" for s in sorted(semanas)],
            name="Sesiones completadas",
        ))
        fig.add_hline(y=5, line_dash="dot", line_color="rgba(57,255,74,0.3)", annotation_text="Meta: 5")
        fig.update_layout(
            paper_bgcolor="#0a0f0a", plot_bgcolor="#0a0f0a",
            font=dict(color="#8aad8a", family="Space Mono"),
            xaxis=dict(gridcolor="rgba(57,255,74,0.06)"),
            yaxis=dict(gridcolor="rgba(57,255,74,0.06)", range=[0, 6]),
            margin=dict(l=0, r=0, t=10, b=0), height=220,
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Completa al menos 2 semanas para ver la gráfica de consistencia.")


# ─────────────────────────────────────────────
#  ══ NUTRICIÓN 360 ══
# ─────────────────────────────────────────────
elif seccion == "🥗 Nutrición 360":
    st.markdown("# 🥗 Nutrición 360")
    st.markdown("<div style='color:#4d6b4d;font-family:Space Mono;font-size:12px;margin-bottom:20px'>RECOMPOSICIÓN CORPORAL · PROTOCOLO COMPLETO</div>", unsafe_allow_html=True)

    macros = [
        ("🔥", "Déficit calórico ligero", "250–400 kcal/día", "Un déficit moderado permite la recomposición: perder grasa sin sacrificar músculo. Más déficit = más pérdida muscular. Paciencia."),
        ("🥩", "Proteína alta", "1.8–2.2 g/kg", "Prioridad absoluta. Para 75kg = 135–165g/día. Distribuye en 4–5 tomas. El músculo se construye en este rango incluso en déficit."),
        ("🍚", "Carbos — timing", "Pre y post entreno", "Arroz integral, camote, avena, plátano. Mayor concentración alrededor del entreno. Reduce por la noche."),
        ("🥑", "Grasas saludables", "25–30% calorías", "Omega-3 reduce inflamación post-HIIT. Aguacate y frutos secos. Evita grasas trans."),
    ]
    st.markdown("### 🎯 Los 4 pilares")
    for icon, titulo, valor, desc in macros:
        st.markdown(f"""<div class='card'>
            <div style='display:flex;align-items:center;gap:12px;margin-bottom:8px'>
                <div style='font-size:26px'>{icon}</div>
                <div>
                    <div style='font-size:14px;font-weight:700'>{titulo}</div>
                    <div style='font-size:16px;font-weight:800;color:#39ff4a;font-family:Space Mono'>{valor}</div>
                </div>
            </div>
            <div style='font-size:12px;color:#8aad8a;line-height:1.6'>{desc}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🌿 Protocolo Papaya — Arma secreta post-entreno")
    beneficios = [
        "Mejora la absorción de proteínas post-entrenamiento hasta un 30%",
        "Reduce la inflamación intestinal causada por el HIIT intenso",
        "Mejora la salud del microbioma, clave en la recuperación muscular",
        "Efecto antioxidante que combate el estrés oxidativo del entrenamiento",
        "Las semillas: antiparasitario natural y limpieza del tracto digestivo",
    ]
    st.markdown(f"""<div style='background:linear-gradient(135deg,rgba(57,255,74,0.08),rgba(57,255,74,0.02));border:1px solid rgba(57,255,74,0.25);border-radius:16px;padding:20px;margin-bottom:12px'>
        <div style='font-size:18px;font-weight:800;margin-bottom:10px'>🌿 PAPAYA + SEMILLAS</div>
        <div style='font-size:13px;color:#8aad8a;line-height:1.6;margin-bottom:10px'>La papaya contiene <b style='color:#39ff4a'>PAPAÍNA</b>, una enzima proteolítica que descompone proteínas con mayor eficiencia. Las semillas tienen <b style='color:#39ff4a'>CARPASINA e ISOTIOCIANATOS</b>: antiinflamatorios y mejoradores del microbioma.</div>
        {''.join([f"<div style='display:flex;gap:8px;margin-bottom:5px'><span style='color:#39ff4a;flex-shrink:0'>→</span><span style='font-size:12px;color:#8aad8a'>{b}</span></div>" for b in beneficios])}
        <div style='background:#0a0f0a;border-radius:10px;padding:10px 14px;margin-top:12px'>
            <div style='font-size:11px;font-family:Space Mono;color:#39ff4a'>DOSIS: 150–200g de papaya madura + 8–10 semillas masticadas · dentro de los 30 min post-entreno</div>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🍽️ Plan de comidas — Ejemplo 75kg")
    comidas = [
        ("07:00", "Desayuno", "Avena 80g + 4 claras + 1 huevo + banana", "480 kcal · 38g P"),
        ("10:30", "Pre-entreno", "Arroz integral 100g + pechuga 150g + brócoli", "490 kcal · 45g P"),
        ("13:30", "Post-entreno", "🌿 Papaya 150g + semillas + Whey 30g", "280 kcal · 28g P"),
        ("16:00", "Almuerzo", "Salmón 180g + camote 150g + ensalada", "460 kcal · 42g P"),
        ("19:30", "Cena", "Pechuga 180g + vegetales + aguacate 1/4", "380 kcal · 40g P"),
    ]
    for hora, nombre, desc, macros_txt in comidas:
        st.markdown(f"""<div style='display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-bottom:1px solid rgba(57,255,74,0.06)'>
            <div style='background:rgba(57,255,74,0.1);color:#39ff4a;font-size:10px;font-family:Space Mono;font-weight:700;padding:3px 8px;border-radius:6px;flex-shrink:0;margin-top:2px'>{hora}</div>
            <div style='flex:1'><div style='font-size:13px;font-weight:700'>{nombre}</div><div style='font-size:11px;color:#4d6b4d;font-family:Space Mono;margin-top:2px'>{desc}</div></div>
            <div style='font-size:11px;color:#39ff4a;font-family:Space Mono;text-align:right;flex-shrink:0'>{macros_txt}</div>
        </div>""", unsafe_allow_html=True)
    st.markdown("<div style='text-align:right;margin-top:8px;font-size:12px;font-family:Space Mono;color:#39ff4a;font-weight:700'>TOTAL: ~2.090 kcal · ~193g proteína</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  ══ MÉTRICAS Y PROGRESO ══
# ─────────────────────────────────────────────
elif seccion == "📊 Métricas y Progreso":
    semana_actual = get_week_number()
    st.markdown("# 📊 Métricas y Progreso")
    st.markdown("<div style='color:#4d6b4d;font-family:Space Mono;font-size:12px;margin-bottom:20px'>EVOLUCIÓN COMPLETA · SEMANA A SEMANA</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["⚖️ Peso corporal", "🏃 Tiempos 5k", "✅ Sesiones"])

    # ── TAB 1: Peso ──
    with tab1:
        st.markdown("### ⚖️ Registrar peso")
        with st.form("form_peso"):
            col1, col2, col3 = st.columns(3)
            with col1:
                fecha_peso = st.date_input("Fecha", value=date.today())
            with col2:
                nuevo_peso = st.number_input("Peso (kg)", min_value=40.0, max_value=150.0, value=75.0, step=0.1)
            with col3:
                sem_peso = st.number_input("Semana #", min_value=1, max_value=52, value=semana_actual, step=1)
            if st.form_submit_button("💾 Guardar"):
                nueva = pd.DataFrame([{"semana": int(sem_peso), "fecha": str(fecha_peso), "peso": nuevo_peso}])
                st.session_state.weight_df = pd.concat([st.session_state.weight_df, nueva], ignore_index=True)
                save_weight(st.session_state.weight_df)
                st.toast(f"✓ Peso registrado: {nuevo_peso} kg — Semana {int(sem_peso)}", icon="⚖️")
                st.rerun()

        weight_df = st.session_state.weight_df
        if not weight_df.empty:
            ws = weight_df.sort_values(["semana","fecha"])
            peso_inicial = ws.iloc[0]["peso"]
            peso_actual  = ws.iloc[-1]["peso"]
            delta = peso_actual - peso_inicial

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Peso inicial", f"{peso_inicial:.1f} kg")
            with col2: st.metric("Peso actual",  f"{peso_actual:.1f} kg",  delta=f"{delta:+.1f} kg")
            with col3: st.metric("Semanas registradas", ws["semana"].nunique())

            # Gráfica por semana (promedio semanal)
            sem_avg = ws.groupby("semana")["peso"].mean().reset_index()
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=sem_avg["semana"].astype(str).apply(lambda x: f"S{x}"),
                y=sem_avg["peso"],
                mode="lines+markers",
                line=dict(color="#39ff4a", width=2),
                marker=dict(color="#39ff4a", size=8),
                fill="tozeroy", fillcolor="rgba(57,255,74,0.04)",
                name="Peso promedio",
            ))
            fig.update_layout(
                paper_bgcolor="#0a0f0a", plot_bgcolor="#0a0f0a",
                font=dict(color="#8aad8a", family="Space Mono"),
                xaxis=dict(gridcolor="rgba(57,255,74,0.06)", title="Semana"),
                yaxis=dict(gridcolor="rgba(57,255,74,0.06)", title="Peso (kg)"),
                margin=dict(l=0,r=0,t=10,b=0), height=250,
            )
            st.plotly_chart(fig, use_container_width=True)

            # Tabla completa
            st.markdown("**Historial completo**")
            tabla = ws[["semana","fecha","peso"]].rename(columns={"semana":"Semana","fecha":"Fecha","peso":"Peso (kg)"})
            st.dataframe(tabla, use_container_width=True, hide_index=True)
        else:
            st.info("Registra tu primer peso para ver la evolución.")

    # ── TAB 2: 5k ──
    with tab2:
        st.markdown("### 🏃 Registrar tiempo 5k")
        with st.form("form_race"):
            col1, col2, col3, col4 = st.columns(4)
            with col1: fecha_r = st.date_input("Fecha", value=date.today(), key="rd")
            with col2: sem_r   = st.number_input("Semana #", min_value=1, max_value=52, value=semana_actual, step=1)
            with col3: minutos = st.number_input("Min", min_value=10, max_value=60, value=30, step=1)
            with col4: segs    = st.number_input("Seg", min_value=0,  max_value=59, value=0,  step=1)
            if st.form_submit_button("🏁 Guardar"):
                tiempo = minutos + segs / 60
                race_df = st.session_state.race_df
                es_record = race_df.empty or tiempo < race_df["tiempo_min"].min()
                nueva = pd.DataFrame([{"semana": int(sem_r), "fecha": str(fecha_r), "tiempo_min": tiempo}])
                st.session_state.race_df = pd.concat([race_df, nueva], ignore_index=True)
                save_races(st.session_state.race_df)
                if es_record:
                    st.balloons()
                    st.toast(f"🏆 ¡NUEVO RÉCORD! {minutos}:{segs:02d}", icon="🏆")
                else:
                    st.toast(f"✓ {minutos}:{segs:02d} — Semana {int(sem_r)}", icon="🏃")
                st.rerun()

        race_df = st.session_state.race_df
        if not race_df.empty:
            rs = race_df.sort_values(["semana","fecha"])
            mejor   = rs["tiempo_min"].min()
            ultimo  = rs.iloc[-1]["tiempo_min"]
            mejora  = rs.iloc[0]["tiempo_min"] - mejor

            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Mejor tiempo",  fmt_tiempo(mejor))
            with col2: st.metric("Último tiempo", fmt_tiempo(ultimo))
            with col3: st.metric("Mejora total",  f"{mejora:.1f} min")

            # Gráfica: mejor tiempo por semana
            sem_best = rs.groupby("semana")["tiempo_min"].min().reset_index()
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=sem_best["semana"].astype(str).apply(lambda x: f"S{x}"),
                y=sem_best["tiempo_min"],
                mode="lines+markers",
                line=dict(color="#ffaa22", width=2),
                marker=dict(color="#ffaa22", size=8),
                fill="tozeroy", fillcolor="rgba(255,170,34,0.04)",
                name="Mejor 5k",
            ))
            fig2.update_layout(
                paper_bgcolor="#0a0f0a", plot_bgcolor="#0a0f0a",
                font=dict(color="#8aad8a", family="Space Mono"),
                xaxis=dict(gridcolor="rgba(57,255,74,0.06)", title="Semana"),
                yaxis=dict(gridcolor="rgba(57,255,74,0.06)", title="Tiempo (min)", autorange="reversed"),
                margin=dict(l=0,r=0,t=10,b=0), height=250,
            )
            st.plotly_chart(fig2, use_container_width=True)

            st.markdown("**Historial completo**")
            tabla2 = rs.copy()
            tabla2["Tiempo"] = tabla2["tiempo_min"].apply(fmt_tiempo)
            st.dataframe(tabla2[["semana","fecha","Tiempo"]].rename(columns={"semana":"Semana","fecha":"Fecha"}), use_container_width=True, hide_index=True)
        else:
            st.info("Registra tu primer tiempo en 5k para ver la evolución.")

    # ── TAB 3: Sesiones ──
    with tab3:
        st.markdown("### ✅ Control de sesiones")
        sessions_df = st.session_state.sessions_df

        # Selector de semana para marcar
        semanas_disponibles = semanas_con_datos()
        sem_labels = [f"Semana {s}{' (actual)' if s == semana_actual else ''}" for s in semanas_disponibles]
        sem_sel_label = st.selectbox("Gestionar semana:", sem_labels)
        sem_sel = int(sem_sel_label.split(" ")[1])

        st.markdown(f"<div style='font-size:11px;font-family:Space Mono;color:#4d6b4d;margin-bottom:10px'>{week_label(sem_sel).upper()}</div>", unsafe_allow_html=True)

        for i, dia in enumerate(list(PLAN.keys())):
            dia_num = f"Día {i+1}"
            s_f = sessions_df[(sessions_df["semana"] == sem_sel) & (sessions_df["dia_num"] == dia_num)] if not sessions_df.empty else pd.DataFrame()
            done = not s_f.empty and bool(s_f["completed"].values[0])
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"<div style='padding:8px 0;font-size:13px'>{'✅' if done else '⭕'} &nbsp; <b>{dia_num}</b> — {dia.split('—')[1].strip().split('�')[0].strip()}</div>", unsafe_allow_html=True)
            with col2:
                if not done:
                    if st.button("✓", key=f"ses_{sem_sel}_{i}"):
                        nueva = pd.DataFrame([{"semana": sem_sel, "dia_num": dia_num, "completed": True, "fecha": str(date.today())}])
                        st.session_state.sessions_df = pd.concat([sessions_df, nueva], ignore_index=True)
                        save_sessions(st.session_state.sessions_df)
                        st.balloons()
                        st.toast(f"💪 {dia_num} completado — Semana {sem_sel}", icon="🔥")
                        st.rerun()

        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Nueva semana"):
                # La nueva semana es simplemente la actual; los datos se crean al completar días
                st.toast(f"Trabajando en Semana {semana_actual}. ¡A entrenar!", icon="📅")
        with col2:
            if st.button("🔄 Limpiar semana seleccionada"):
                st.session_state.sessions_df = sessions_df[sessions_df["semana"] != sem_sel] if not sessions_df.empty else sessions_df
                save_sessions(st.session_state.sessions_df)
                st.toast(f"Semana {sem_sel} reiniciada.", icon="🔄")
                st.rerun()

# ─────────────────────────────────────────────
#  ══ ANALÍTICA 5K ══
# ─────────────────────────────────────────────
elif seccion == "🏃‍♂️ Analítica 5K":
    st.markdown("# 🏃‍♂️ Analítica Avanzada de Carrera")
    st.markdown("<div style='color:#4d6b4d;font-family:Space Mono;font-size:12px;margin-bottom:20px'>CRUCE DE DATOS AERÓBICOS · GESTIÓN DE CARGAS</div>", unsafe_allow_html=True)

    # 1. FORMULARIO DE INGRESO DE DATOS
    with st.expander("➕ Registrar Nueva Carrera", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            fecha_carrera = st.date_input("Fecha de la sesión", date.today())
            distancia_km = st.number_input("Distancia (km)", min_value=0.0, step=0.1, value=5.0)
            tiempo_min = st.number_input("Tiempo Total (minutos)", min_value=0.0, step=1.0, value=25.0)
        with col2:
            inclinacion = st.number_input("Inclinación Promedio (%)", min_value=0.0, step=0.5, value=1.0)
            rpe = st.slider("Esfuerzo Percibido (RPE 1-10)", min_value=1, max_value=10, value=7,
                            help="1 = Paseo suave, 10 = Máximo esfuerzo (Fallo)")
        
        if st.button("💾 Guardar Registro Analítico"):
            if distancia_km > 0 and tiempo_min > 0:
                # --- MOTOR LÓGICO DE CÁLCULOS ---
                ritmo_decimal = tiempo_min / distancia_km
                minutos = int(ritmo_decimal)
                segundos = int((ritmo_decimal - minutos) * 60)
                ritmo_str = f"{minutos}:{segundos:02d}"
                
                velocidad_kmh = round((distancia_km / tiempo_min) * 60, 2)
                
                # Carga Externa (1% pendiente suma 10% de carga)
                factor_inclinacion = 1 + (inclinacion / 10)
                carga_entrenamiento = round(tiempo_min * rpe * factor_inclinacion, 1)

                nuevo_registro = pd.DataFrame([{
                    "Fecha": fecha_carrera,
                    "Distancia (km)": distancia_km,
                    "Tiempo (min)": tiempo_min,
                    "Ritmo (min/km)": ritmo_str,
                    "Ritmo Decimal": ritmo_decimal,
                    "Velocidad (km/h)": velocidad_kmh,
                    "Inclinación (%)": inclinacion,
                    "RPE": rpe,
                    "Carga Externa": carga_entrenamiento
                }])
                
                if 'df_carreras' not in st.session_state:
                    st.session_state.df_carreras = pd.DataFrame()
                
                st.session_state.df_carreras = pd.concat([st.session_state.df_carreras, nuevo_registro], ignore_index=True)
                st.success(f"¡Cálculo Exitoso! Ritmo: {ritmo_str} min/km | Velocidad: {velocidad_kmh} km/h | Carga: {carga_entrenamiento}")

    # 2. VISUALIZACIÓN Y DASHBOARD
    if 'df_carreras' in st.session_state and not st.session_state.df_carreras.empty:
        df = st.session_state.df_carreras.sort_values(by="Fecha")
        
        st.markdown("---")
        st.subheader("📊 Gráfica Multivariable")
        st.markdown("<div style='font-size:13px;color:#8aad8a;margin-bottom:15px'><b>Guía:</b> Eje Y (Velocidad) | Tamaño de burbuja (Carga) | Color (Esfuerzo RPE)</div>", unsafe_allow_html=True)
        
        fig = px.scatter(
            df, 
            x="Fecha", 
            y="Velocidad (km/h)", 
            size="Carga Externa", 
            color="RPE",
            hover_data=["Distancia (km)", "Ritmo (min/km)", "Inclinación (%)"],
            color_continuous_scale="RdYlGn_r",
        )
        
        fig.update_layout(
            template="plotly_dark", 
            plot_bgcolor="rgba(0,0,0,0)", 
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=10, r=10, t=20, b=10)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("<div class='stat-label'>Datos en crudo</div>", unsafe_allow_html=True)
        st.dataframe(df.drop(columns=["Ritmo Decimal"]), use_container_width=True)
# ─────────────────────────────────────────────
#  ══ CHEF AI (GENERADOR DE RECETAS) ══
# ─────────────────────────────────────────────
elif seccion == "👨‍🍳 Chef AI":
    import random
    st.markdown("# 👨‍🍳 Tu Chef Deportivo")
    st.markdown("<div style='color:#4d6b4d;font-family:Space Mono;font-size:12px;margin-bottom:20px'>INTELIGENCIA NUTRICIONAL · OPTIMIZACIÓN DE MACROS</div>", unsafe_allow_html=True)

    st.subheader("¿Qué tienes en la despensa/nevera?")
    
    col1, col2 = st.columns(2)
    with col1:
        fuente_proteina = st.multiselect(
            "🥩 Fuentes de Proteína",
            ["Pechuga de Pollo", "Huevos", "Atún", "Carne de res magra", "Pescado blanco", "Proteína en polvo (Whey)"]
        )
    with col2:
        fuente_carbo = st.multiselect(
            "🍚 Carbohidratos (Energía)",
            ["Arroz integral", "Avena", "Papa cocida", "Pasta", "Pan integral", "Tortillas de maíz"]
        )
    
    vegetales_extras = st.text_input("🥦 Vegetales y otros extras (Escribe separados por coma. Ej: espinaca, cebolla, tomate, aguacate):")
    
    if st.button("🍳 Generar Menú de Recomposición"):
        if not fuente_proteina:
            st.warning("⚠️ Necesitas seleccionar al menos una fuente de proteína para construir músculo.")
        else:
            with st.spinner("Diseñando tu comida..."):
                # --- MOTOR LÓGICO CON VARIABILIDAD ---
                protes_str = ", ".join(fuente_proteina).lower()
                veggies = vegetales_extras if vegetales_extras else 'un mix de vegetales frescos'
                carbos = fuente_carbo[0].lower() if fuente_carbo else 'una buena ensalada'
                
                # Opciones para Huevos
                if "huevos" in protes_str:
                    opciones = [
                        f"**Omelette de Poder:** Bate los huevos (3 claras x 1 yema). Hazlo en sartén de teflón y rellena con {veggies}. Acompaña con {carbos}.",
                        f"**Revuelto Anabólico:** Saltea primero {veggies}. Cuando doren, echa los huevos encima y revuelve. Sírvelo sobre {carbos}.",
                        f"**Tortilla Fit (Estilo Español):** Mezcla los huevos con {veggies} y un poco de {carbos} directamente en el bowl, luego a la sartén tapada a fuego lento."
                    ]
                    receta = f"### 🍳 {random.choice(opciones)}\n"
                
                # Opciones para Pollo / Carne
                elif "pechuga de pollo" in protes_str or "carne de res magra" in protes_str:
                    opciones = [
                        f"**Bowl de Campeones:** Corta el {fuente_proteina[0].lower()} en dados. Ásalo a la plancha. Arma un bowl con base de {carbos}, la carne y corona con {veggies}.",
                        f"**Fajitas Desarmadas:** Corta la carne en tiras finas. Saltea a fuego muy alto junto con {veggies} y especias (pimentón, comino). Acompaña con {carbos}.",
                        f"**Guiso Express Limpio:** Dora el {fuente_proteina[0].lower()}, agrega {veggies} picados chiquitos, un chorrito de agua y tapa para que se cocine al vapor. Sírvelo junto a {carbos}."
                    ]
                    receta = f"### 🍛 {random.choice(opciones)}\n"
                
                else:
                    receta = f"### 🍲 Salteado Proteico\n**Instrucciones:** Cocina tu {fuente_proteina[0].lower()} a la plancha. Sirve con una guarnición de {veggies} al vapor y {carbos}."
                
                # Integración del Hack Digestivo
                receta += "\n---\n"
                receta += "💡 **Estrategia de Asimilación:** Para asegurar que tu cuerpo absorba hasta el último gramo de esta proteína sin generar inflamación abdominal, incluye una porción de **papaya fresca**. Triturar algunas de sus semillas junto con la fruta aportará una carga altísima de enzimas digestivas, manteniendo tu microbiota sana y lista para soportar el estrés de las sesiones de HIIT."
                
                st.success("¡Menú estructurado con éxito!")
                st.markdown("<div style='background-color:#111811; padding:20px; border-radius:10px; border:1px solid #27ae60;'>", unsafe_allow_html=True)
                st.markdown(receta)
                st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  ══ CONSTRUCTOR DE RUTINAS (SESSION BUILDER) ══
# ─────────────────────────────────────────────
# ─────────────────────────────────────────────
#  ══ CONSTRUCTOR DE RUTINAS (SESSION BUILDER) ══
# ─────────────────────────────────────────────
elif seccion == "🛠️ Constructor de Rutinas":
    import plotly.graph_objects as go
    
    st.markdown("# 🛠️ Constructor Dinámico")
    st.markdown("<div style='color:#4d6b4d;font-family:Space Mono;font-size:12px;margin-bottom:20px'>INTELIGENCIA BIOMECÁNICA · SELECCIÓN POR PATRONES</div>", unsafe_allow_html=True)

    # 1. BASE DE DATOS ESTRUCTURADA
    ejercicios_db = {
        "Empuje (Pecho/Hombros)": ["Press de Banca", "Press Inclinado Mancuernas", "Press Militar", "Flexiones (Push-ups)", "Fondos en paralelas", "Extensión de Tríceps"],
        "Tirón (Espalda/Bíceps)": ["Dominadas", "Remo con barra", "Remo en polea baja", "Face Pull", "Curl de Bíceps", "Pull-over"],
        "Dominante Rodilla (Cuádriceps)": ["Sentadilla Búlgara", "Prensa de piernas", "Sentadilla Frontal", "Zancadas", "Extensión de Cuádriceps", "Sentadilla Goblet"],
        "Dominante Cadera (Isquios/Glúteo)": ["Peso Muerto Rumano", "Hip Thrust", "Curl Nórdico", "Kettlebell Swing", "Curl de Isquios en máquina"],
        "Core y Estabilidad": ["Paseo del Granjero", "Plancha Abdominal", "Press Pallof", "Rueda Abdominal", "Rotación en Polea", "Woodchoppers"],
        "Pliometría y RSA": ["Saltos al Cajón", "Saltos Laterales", "Sprints en Cinta", "Empuje de Trineo", "Lanzamiento Balón Medicinal"]
    }

    st.subheader("1. Diseña tu rutina por zonas")
    st.markdown("Abre las categorías y selecciona tus ejercicios de hoy:")

    seleccionados = []

    # 2. INTERFAZ DE COLUMNAS DIVIDIDAS (Mejor UX en PC y Móvil)
    col_a, col_b = st.columns(2)

    with col_a:
        with st.expander("🔵 Empuje (Pecho/Hombros/Tríceps)", expanded=True):
            sel_empuje = st.multiselect("Ejercicios:", ejercicios_db["Empuje (Pecho/Hombros)"], key="emp", label_visibility="collapsed")
            seleccionados.extend([(e, "Empuje (Pecho/Hombros)") for e in sel_empuje])
            
        with st.expander("🔴 Dominante Rodilla (Cuádriceps)", expanded=True):
            sel_rodilla = st.multiselect("Ejercicios:", ejercicios_db["Dominante Rodilla (Cuádriceps)"], key="rod", label_visibility="collapsed")
            seleccionados.extend([(e, "Dominante Rodilla (Cuádriceps)") for e in sel_rodilla])
            
        with st.expander("🛡️ Core y Estabilidad"):
            sel_core = st.multiselect("Ejercicios:", ejercicios_db["Core y Estabilidad"], key="cor", label_visibility="collapsed")
            seleccionados.extend([(e, "Core y Estabilidad") for e in sel_core])

    with col_b:
        with st.expander("🟢 Tirón (Espalda/Bíceps)", expanded=True):
            sel_tiron = st.multiselect("Ejercicios:", ejercicios_db["Tirón (Espalda/Bíceps)"], key="tir", label_visibility="collapsed")
            seleccionados.extend([(e, "Tirón (Espalda/Bíceps)") for e in sel_tiron])
            
        with st.expander("🟠 Dominante Cadera (Isquios/Glúteo)", expanded=True):
            sel_cadera = st.multiselect("Ejercicios:", ejercicios_db["Dominante Cadera (Isquios/Glúteo)"], key="cad", label_visibility="collapsed")
            seleccionados.extend([(e, "Dominante Cadera (Isquios/Glúteo)") for e in sel_cadera])
            
        with st.expander("⚡ Pliometría y Cardio"):
            sel_plio = st.multiselect("Ejercicios:", ejercicios_db["Pliometría y RSA"], key="pli", label_visibility="collapsed")
            seleccionados.extend([(e, "Pliometría y RSA") for e in sel_plio])

    # 3. MOTOR DE ANÁLISIS Y GRAFICACIÓN RADAR
    if seleccionados:
        st.markdown("---")
        st.subheader("2. Análisis de Carga Biomecánica")
        
        # Lógica de conteo optimizada
        conteo = {cat: 0 for cat in ejercicios_db.keys()}
        for ej, cat in seleccionados:
            conteo[cat] += 1

        categorias = list(conteo.keys())
        valores = list(conteo.values())

        # Configuración del Gráfico de Radar (Polar)
        categorias_radar = categorias + [categorias[0]] # Cerrar el polígono
        valores_radar = valores + [valores[0]]

        fig = go.Figure(data=go.Scatterpolar(
            r=valores_radar,
            theta=[c.split(" ")[0] for c in categorias_radar], # Nombres cortos en el gráfico
            fill='toself',
            line_color='#e74c3c',
            fillcolor='rgba(231, 76, 60, 0.4)',
            marker=dict(size=8)
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, max(valores) + 1 if max(valores) > 0 else 4], tickfont=dict(color="#888")),
                angularaxis=dict(tickfont=dict(size=12, color="#e8f5e8"))
            ),
            showlegend=False,
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=50, r=50, t=20, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)

        # 4. SISTEMA DE ALERTAS INTELIGENTES
        volumen_total = len(seleccionados)
        max_cat_valor = max(valores)
        
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.metric("Volumen Total", f"{volumen_total} ejercicios")
        with col_res2:
            st.metric("Patrón Dominante", categorias[valores.index(max_cat_valor)].split(" ")[0])

        if max_cat_valor >= 4:
            st.error("⚠️ Alerta de Sobrecarga: Tienes demasiados ejercicios del mismo grupo muscular. Balancea la rutina.")
        elif valores[2] > 0 and valores[3] == 0:
            st.warning("⚠️ Descompensación: Has incluido trabajo de Cuádriceps pero nada de Isquios/Glúteo. ¡Agrega un Peso Muerto para proteger tu rodilla!")
        elif volumen_total > 8:
            st.warning("⚠️ Alto Volumen: Más de 8 ejercicios puede generar demasiada fatiga central para una sola sesión.")
        else:
            st.success("✅ Sesión biomecánicamente balanceada. ¡Guarda tu celular y a levantar!")
