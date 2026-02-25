import streamlit as st

def render():
    # --- CSS FORZY STYLE ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');

        :root {
            --forzy-black: #000000;
            --forzy-gray: #f5f5f7;
            --forzy-text-secondary: #86868b;
            --forzy-accent: #0066cc;
        }

        .stApp {
            background-color: white;
            color: var(--forzy-black);
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* Tipografia Apple Style */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            letter-spacing: -0.022em;
        }

        h1 {
            font-weight: 700;
            font-size: clamp(40px, 8vw, 80px);
            line-height: 1.05;
            letter-spacing: -0.05em;
            color: var(--forzy-black);
        }

        h2 {
            font-weight: 700;
            font-size: clamp(32px, 5vw, 48px);
            letter-spacing: -0.04em;
        }

        /* Hero - O Impacto do Simples */
        .hero-forzy {
            padding: 120px 10% 80px 10%;
            text-align: center;
            background: white;
        }

        /* Card Elegante */
        .forzy-card {
            background: var(--forzy-gray);
            border-radius: 28px;
            padding: 50px;
            height: 100%;
            transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid transparent;
        }

        .forzy-card:hover {
            transform: scale(1.02);
        }

        /* Botão Minimalista Corrigido */
        div.stButton > button {
            background-color: var(--forzy-black) !important;
            color: white !important;
            border: none !important;
            padding: 12px 30px !important;
            font-weight: 600 !important;
            border-radius: 40px !important;
            transition: 0.3s !important;
            font-size: 16px !important;
            width: auto !important;
        }

        div.stButton > button:hover {
            background-color: #333 !important;
            transform: scale(1.05) !important;
        }

        /* Navbar Clean */
        .nav-forzy {
            padding: 20px 10%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255,255,255,0.8);
            backdrop-filter: blur(20px);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div class="nav-forzy">
        <div style="font-weight: 700; font-size: 22px; letter-spacing: -1px;">FORZY</div>
        <div style="display: flex; gap: 30px; font-size: 12px; font-weight: 500; color: var(--forzy-text-secondary);">
            <span>SOLUÇÕES</span>
            <span>METODOLOGIA</span>
            <span>SOBRE</span>
            <span style="color: var(--forzy-black); font-weight: 700;">CONTATO</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 1 & 2. HERO SECTION ---
    st.markdown("""
    <div class="hero-forzy">
        <p style="font-weight: 600; color: var(--forzy-text-secondary); margin-bottom: 20px; letter-spacing: 1px;">DESIGN & PERFORMANCE</p>
        <h1>Impulsione sua marca<br>com precisão digital.</h1>
        <p style="font-size: 24px; color: var(--forzy-text-secondary); max-width: 700px; margin: 30px auto 50px auto; line-height: 1.4;">
            Criamos experiências que conectam negócios ao futuro, unindo estética minimalista e tecnologia de alta conversão.
        </p>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 0.8, 1])
    with c2:
        st.button("VAMOS CONVERSAR")
    
    st.markdown("</div>", unsafe_allow_html=True)

    # --- 3 & 4. GRIDS DE SERVIÇOS ---
    st.markdown('<div style="padding: 40px 5% 100px 5%;">', unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2, gap="medium")

    with col_a:
        st.markdown("""
        <div class="forzy-card">
            <h2 style="margin-bottom: 20px;">Estratégia<br>Digital.</h2>
            <p style="color: var(--forzy-text-secondary); font-size: 18px; line-height: 1.6;">
                Planejamento focado em crescimento escalável e posicionamento de mercado.
            </p>
            <div style="margin-top: 100px; font-weight: 700; font-size: 14px;">EXPLORAR →</div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="forzy-card" style="background-color: var(--forzy-black); color: white;">
            <h2 style="margin-bottom: 20px; color: white;">Interface &<br>Experiência.</h2>
            <p style="color: #86868b; font-size: 18px; line-height: 1.6;">
                Design intuitivo que elimina fricções e encanta o usuário final.
            </p>
            <div style="margin-top: 100px; font-weight: 700; font-size: 14px; color: white;">VER PROJETOS →</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. SEÇÃO DE PROVA ---
    st.markdown("""
    <div style="padding: 100px 10%; text-align: center; background: var(--forzy-gray);">
        <h2 style="margin-bottom: 40px;">Feito para quem busca o extraordinário.</h2>
        <div style="display: flex; justify-content: space-around; opacity: 0.4; filter: grayscale(100%); flex-wrap: wrap; gap: 40px;">
            <h3>PARTNER</h3>
            <h3>STARTUP</h3>
            <h3>ENTERPRISE</h3>
            <h3>GLOBAL</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 80px 10%; background: white; border-top: 1px solid #eee;">
        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
            <div>
                <div style="font-weight: 700; font-size: 24px; margin-bottom: 20px;">FORZY.</div>
                <p style="color: var(--forzy-text-secondary); font-size: 14px;">São Paulo, Brasil</p>
            </div>
            <div style="text-align: right; color: var(--forzy-text-secondary); font-size: 12px;">
                © 2026 FORZY DIGITAL INTERFACE. ALL RIGHTS RESERVED.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Execução direta
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Forzy | Digital Interface")
    render()
