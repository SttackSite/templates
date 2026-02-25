import streamlit as st

def render():
    # --- CSS INSTITUTO FUTUROS STYLE ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

        :root {
            --futuros-purple: #6c42f5;
            --futuros-gradient: linear-gradient(135deg, #6c42f5 0%, #3a1c91 100%);
            --futuros-bg: #fdfdff;
            --futuros-dark: #14141d;
        }

        .stApp {
            background-color: var(--futuros-bg);
            color: var(--futuros-dark);
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia */
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        h1, h2, h3 {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 800;
            letter-spacing: -1px;
        }

        /* Hero Section - Futurista */
        .hero-futuros {
            padding: 120px 10% 160px 10%;
            background: radial-gradient(circle at top right, rgba(108, 66, 245, 0.08), transparent),
                        radial-gradient(circle at bottom left, rgba(58, 28, 145, 0.05), transparent);
            text-align: center;
        }

        .hero-h1 { 
            font-size: clamp(40px, 6vw, 72px); 
            background: var(--futuros-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }

        /* Cards Glassmorphism */
        .futuros-card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 32px;
            padding: 40px;
            height: 100%;
            transition: 0.5s cubic-bezier(0.2, 1, 0.2, 1);
            box-shadow: 0 20px 40px rgba(0,0,0,0.03);
        }

        .futuros-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 40px 80px rgba(108, 66, 245, 0.15);
            background: white;
        }

        /* Pill Badges */
        .pill {
            background: rgba(108, 66, 245, 0.1);
            color: var(--futuros-purple);
            padding: 8px 20px;
            border-radius: 100px;
            font-size: 14px;
            font-weight: 600;
            display: inline-block;
            margin-bottom: 20px;
        }

        /* Botão Arredondado Moderno */
        div.stButton > button {
            background: var(--futuros-gradient);
            color: white;
            border: none;
            padding: 18px 45px;
            font-weight: 600;
            border-radius: 100px;
            transition: 0.3s;
            box-shadow: 0 10px 30px rgba(108, 66, 245, 0.3);
            width: auto;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 40px rgba(108, 66, 245, 0.5);
            color: white;
        }

        /* Divider Curve */
        .curve {
            position: relative;
            height: 100px;
            width: 100%;
            background: white;
            border-radius: 100% 100% 0 0;
            margin-top: -100px;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 25px 10%; display: flex; justify-content: space-between; align-items: center; background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); position: sticky; top:0; z-index:999;">
        <div style="font-weight: 800; font-size: 24px; color: var(--futuros-purple);">Instituto Futuros<span style="color:#3a1c91">_</span></div>
        <div style="display: flex; gap: 40px; font-weight: 600; font-size: 14px; color: var(--futuros-dark);">
            <span>Ecossistema</span>
            <span>Programas</span>
            <span>Manifesto</span>
            <span style="color: var(--futuros-purple);">Seja Parceiro</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 1 & 2. HERO SECTION ---
    st.markdown("""
    <div class="hero-futuros">
        <div class="pill">TRANSFORMANDO O AMANHÃ</div>
        <h1 class="hero-h1">A educação que desenha<br>novos horizontes.</h1>
        <p style="font-size: 20px; color: #667; max-width: 800px; margin: 0 auto 40px auto; line-height: 1.6;">
            Conectamos pessoas, tecnologias e novas mentalidades para criar o futuro que queremos viver hoje.
        </p>
    """, unsafe_allow_html=True)
    st.button("CONHEÇA NOSSOS PROGRAMAS")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('<div class="curve"></div>', unsafe_allow_html=True)

    # --- 3 & 4. PROGRAMAS (GRID GLASSMorphism) ---
    st.markdown('<div style="padding: 100px 10%; background: white;">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")

    def render_futuros_card(col, title, label, desc, color):
        with col:
            st.markdown(f"""
            <div class="futuros-card">
                <div style="width: 50px; height: 5px; background: {color}; border-radius: 10px; margin-bottom: 30px;"></div>
                <p style="text-transform: uppercase; font-size: 11px; font-weight: 800; letter-spacing: 2px; color: #99a;">{label}</p>
                <h3 style="font-size: 28px; margin: 15px 0;">{title}</h3>
                <p style="color: #667; line-height: 1.7; font-size: 15px; margin-bottom: 30px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    render_futuros_card(col1, "Futuros Jovens", "IMPACTO SOCIAL", "Desenvolvimento de competências digitais e socioemocionais para jovens em vulnerabilidade.", "#6c42f5")
    render_futuros_card(col2, "Futuros Líderes", "CORPORATIVO", "Treinamento especializado para gestores que buscam navegar na complexidade da nova economia.", "#3a1c91")
    render_futuros_card(col3, "Futuros Tech", "TECNOLOGIA", "Aceleração de talentos técnicos focada nas tecnologias mais demandadas pelo mercado global.", "#00d4ff")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. SEÇÃO DE IMPACTO (NÚMEROS) ---
    st.markdown("""
    <div style="background: var(--futuros-dark); color: white; padding: 100px 10%; border-radius: 80px 80px 0 0;">
        <div style="text-align: center; margin-bottom: 80px;">
            <h2 style="color: white; font-size: 42px;">Nosso Impacto em Números</h2>
        </div>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px;">
            <div style="text-align: center;">
                <h1 style="color: var(--futuros-purple); font-size: 64px;">+15k</h1>
                <p style="opacity: 0.6; font-weight: 600;">ALUNOS FORMADOS</p>
            </div>
            <div style="text-align: center;">
                <h1 style="color: var(--futuros-purple); font-size: 64px;">+200</h1>
                <p style="opacity: 0.6; font-weight: 600;">EMPRESAS PARCEIRAS</p>
            </div>
            <div style="text-align: center;">
                <h1 style="color: var(--futuros-purple); font-size: 64px;">92%</h1>
                <p style="opacity: 0.6; font-weight: 600;">TAXA DE EMPREGABILIDADE</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 6. CHAMADA FINAL ---
    st.markdown("""
    <div style="padding: 150px 10%; text-align: center; background: white;">
        <h2 style="font-size: 48px; margin-bottom: 30px;">Vamos construir o amanhã?</h2>
        <p style="color: #667; font-size: 18px; margin-bottom: 50px;">Junte-se ao nosso ecossistema de transformação.</p>
    """, unsafe_allow_html=True)
    st.button("QUERO SER PARCEIRO", key="final_cta")
    st.markdown("</div>", unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 60px 10%; border-top: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; font-size: 14px; color: #99a;">
        <div>© 2026 Instituto Futuros. Todos os direitos reservados.</div>
        <div style="display: flex; gap: 30px;">
            <span>Instagram</span>
            <span>LinkedIn</span>
            <span>YouTube</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Execução direta
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Instituto Futuros | Educação e Inovação")
    render()
