import streamlit as st

def render():
    # --- CSS CORRIGIDO (SEM ERRO NO BOTÃO) ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

        :root {
            --futuros-purple: #6c42f5;
            --futuros-gradient: linear-gradient(135deg, #6c42f5 0%, #3a1c91 100%);
            --futuros-bg: #fdfdff;
            --futuros-dark: #14141d;
        }

        .stApp { background-color: var(--futuros-bg); color: var(--futuros-dark); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }

        /* --- CORREÇÃO DO BOTÃO (ANTI-GHOSTING) --- */
        div.stButton > button {
            background: var(--futuros-gradient) !important;
            color: white !important;
            border: none !important;
            padding: 16px 40px !important;
            font-weight: 600 !important;
            border-radius: 100px !important;
            box-shadow: 0 10px 25px rgba(108, 66, 245, 0.3) !important;
            transition: all 0.3s ease !important;
            display: inline-flex !important;
            outline: none !important;
        }

        div.stButton > button:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 15px 35px rgba(108, 66, 245, 0.5) !important;
            color: white !important;
        }

        div.stButton > button:active {
            transform: translateY(0px) !important;
        }

        /* Hero Section */
        .hero-futuros {
            padding: 120px 10% 160px 10%;
            background: radial-gradient(circle at top right, rgba(108, 66, 245, 0.08), transparent);
            text-align: center;
        }

        .hero-h1 { 
            font-size: clamp(40px, 6vw, 72px); 
            background: var(--futuros-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
            font-weight: 800;
        }

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

        /* Cards Glassmorphism */
        .futuros-card {
            background: white;
            border: 1px solid rgba(0,0,0,0.05);
            border-radius: 32px;
            padding: 40px;
            height: 100%;
            transition: 0.4s;
            box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        }

        .futuros-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 30px 60px rgba(108, 66, 245, 0.1);
        }

        .curve {
            height: 100px;
            background: white;
            border-radius: 100% 100% 0 0;
            margin-top: -100px;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- HERO ---
    st.markdown("""
    <div class="hero-futuros">
        <div class="pill">TRANSFORMANDO O AMANHÃ</div>
        <h1 class="hero-h1">A educação que desenha<br>novos horizontes.</h1>
        <p style="font-size: 18px; color: #667; max-width: 800px; margin: 0 auto 40px auto; line-height: 1.6;">
            Conectamos pessoas, tecnologias e novas mentalidades para criar o futuro que queremos viver hoje.
        </p>
    """, unsafe_allow_html=True)
    
    # Centralizando o botão corrigido
    col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 1, 1])
    with col_btn_2:
        st.button("CONHEÇA NOSSOS PROGRAMAS", use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('<div class="curve"></div>', unsafe_allow_html=True)

    # --- GRID ---
    st.markdown('<div style="padding: 100px 10%; background: white;">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3, gap="large")

    def render_card(col, title, label, color):
        with col:
            st.markdown(f"""
            <div class="futuros-card">
                <div style="width: 40px; height: 40px; background: {color}; border-radius: 12px; margin-bottom: 20px; opacity: 0.2;"></div>
                <p style="text-transform: uppercase; font-size: 10px; font-weight: 800; letter-spacing: 2px; color: #99a;">{label}</p>
                <h3 style="font-size: 24px; margin: 10px 0;">{title}</h3>
                <p style="color: #778; font-size: 14px;">Inovação aplicada ao desenvolvimento humano e tecnológico.</p>
            </div>
            """, unsafe_allow_html=True)

    render_card(c1, "Futuros Jovens", "IMPACTO SOCIAL", "#6c42f5")
    render_card(c2, "Futuros Líderes", "CORPORATIVO", "#3a1c91")
    render_card(c3, "Futuros Tech", "TECNOLOGIA", "#00d4ff")
    st.markdown('</div>', unsafe_allow_html=True)

# Execução direta
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    render()
