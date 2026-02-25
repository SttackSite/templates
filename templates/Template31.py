import streamlit as st

def render():
    # --- SISTEMA DE DESIGN EPIMINDS ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;700;800&display=swap');

        :root {
            --epi-bg: #fdfbff;
            --epi-purple: #6c5ce7;
            --epi-peach: #ff8a71;
            --epi-text: #1f1f39;
            --epi-glass: rgba(255, 255, 255, 0.7);
        }

        .stApp { 
            background-color: var(--epi-bg); 
            color: var(--epi-text);
            background-image: 
                radial-gradient(at 0% 0%, rgba(108, 92, 231, 0.05) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(255, 138, 113, 0.05) 0px, transparent 50%);
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { 
            font-family: 'Plus Jakarta Sans', sans-serif; 
        }

        /* --- HERO SECTION --- */
        .epi-hero {
            padding: 140px 10% 80px 10%;
            text-align: center;
        }

        .epi-h1 {
            font-size: clamp(40px, 6vw, 82px);
            font-weight: 800;
            line-height: 1.1;
            letter-spacing: -0.03em;
            margin-bottom: 30px;
            color: var(--epi-text);
        }

        .epi-h1 span {
            background: linear-gradient(90deg, var(--epi-purple), var(--epi-peach));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* --- BOTÃO ROUNDED (SOFT TECH) --- */
        div.stButton > button {
            background: var(--epi-purple) !important;
            color: white !important;
            border: none !important;
            padding: 16px 42px !important;
            font-weight: 700 !important;
            border-radius: 100px !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            font-size: 16px !important;
            box-shadow: 0 10px 25px rgba(108, 92, 231, 0.2) !important;
        }

        div.stButton > button:hover {
            transform: scale(1.05) translateY(-5px) !important;
            box-shadow: 0 15px 35px rgba(108, 92, 231, 0.4) !important;
        }

        /* --- CARDS COM GLASSMORPHISM --- */
        .epi-card {
            background: var(--epi-glass);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.4);
            border-radius: 32px;
            padding: 40px;
            height: 100%;
            box-shadow: 0 20px 40px rgba(0,0,0,0.02);
            transition: 0.3s;
        }

        .epi-card:hover {
            transform: translateY(-10px);
            background: white;
            box-shadow: 0 30px 60px rgba(108, 92, 231, 0.1);
        }

        .epi-icon {
            width: 60px;
            height: 60px;
            background: rgba(108, 92, 231, 0.1);
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin-bottom: 25px;
        }

        /* --- NAV --- */
        .epi-nav {
            padding: 25px 10%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            background: rgba(253, 251, 255, 0.8);
            backdrop-filter: blur(10px);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div class="epi-nav">
        <div style="font-weight: 800; font-size: 24px; color: var(--epi-purple);">epiminds<span style="color:var(--epi-peach);">.</span></div>
        <div style="display: flex; gap: 35px; font-size: 14px; font-weight: 600; color: #555;">
            <span>Soluções</span>
            <span>Metodologia</span>
            <span>Neurociência</span>
            <span style="color: var(--epi-purple);">Entrar</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO ---
    st.markdown('<div class="epi-hero">', unsafe_allow_html=True)
    st.markdown("""
        <h1 class="epi-h1">
            Conectando a mente ao <br><span>desempenho humano.</span>
        </h1>
        <p style="font-size: 20px; color: #666; max-width: 700px; margin: 0 auto 40px auto; line-height: 1.6;">
            A Epiminds utiliza inteligência artificial e neurotecnologia para transformar a saúde mental e a produtividade de equipes globais.
        </p>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 0.8, 1])
    with c2:
        st.button("INICIAR DIAGNÓSTICO")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FEATURES SECTION ---
    st.markdown('<div style="padding: 60px 10% 120px 10%;">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3, gap="large")

    def render_epi_card(col, icon, title, desc):
        with col:
            st.markdown(f"""
            <div class="epi-card">
                <div class="epi-icon">{icon}</div>
                <h3 style="font-size: 22px; font-weight: 700; margin-bottom: 15px;">{title}</h3>
                <p style="color: #666; font-size: 15px; line-height: 1.7;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    render_epi_card(col1, "🧠", "Análise Neural", "Acompanhamento em tempo real dos biomarcadores de estresse e foco da sua equipe.")
    render_epi_card(col2, "⚡", "Biofeedback", "Intervenções personalizadas baseadas em algoritmos de neurociência comportamental.")
    render_epi_card(col3, "📊", "Insights de IA", "Dashboards preditivos que identificam sinais de burnout antes que eles aconteçam.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 100px 10%; background: #1f1f39; color: white; border-radius: 60px 60px 0 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 40px;">
            <div>
                <h2 style="font-size: 32px; font-weight: 800; margin-bottom: 10px;">Vamos evoluir juntos?</h2>
                <p style="opacity: 0.6;">Tecnologia com propósito para mentes brilhantes.</p>
            </div>
            <div style="display: flex; gap: 30px;">
                <div style="text-align: right;">
                    <p style="font-weight: 700;">CONTATO</p>
                    <p style="opacity: 0.6;">contato@epiminds.com.br</p>
                </div>
            </div>
        </div>
        <div style="margin-top: 80px; padding-top: 40px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 12px; opacity: 0.4;">
            © 2026 EPIMINDS NEUROTECH BRASIL. TODOS OS DIREITOS RESERVADOS.
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Epiminds | Neurotecnologia")
    render()
