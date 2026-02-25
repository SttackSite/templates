import streamlit as st

def render():
    # --- SISTEMA DE DESIGN GOOD SECRETS ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,500;1,300&family=Inter:wght@300;400;500&display=swap');

        :root {
            --gs-bg: #FDF9F3; /* Creme Suave */
            --gs-dark: #2D1B14; /* Marrom Chocolate */
            --gs-text: #4A3B33;
            --gs-accent: #E8D5C4;
        }

        .stApp { background-color: var(--gs-bg); color: var(--gs-dark); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        /* --- TYPOGRAPHY --- */
        .gs-serif { font-family: 'Cormorant Garamond', serif; }
        
        .gs-h1 {
            font-family: 'Cormorant Garamond', serif;
            font-size: clamp(40px, 7vw, 90px);
            font-weight: 300;
            line-height: 1;
            letter-spacing: -0.02em;
            margin-bottom: 30px;
        }

        .gs-label {
            font-size: 11px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: var(--gs-dark);
            margin-bottom: 20px;
            display: block;
        }

        /* --- NAV --- */
        .gs-nav {
            padding: 30px 6%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: transparent;
            position: absolute; width: 100%; top: 0; z-index: 100;
        }

        /* --- BUTTONS --- */
        div.stButton > button {
            background-color: var(--gs-dark) !important;
            color: white !important;
            border: none !important;
            padding: 14px 40px !important;
            border-radius: 100px !important;
            font-size: 14px !important;
            font-weight: 400 !important;
            transition: 0.3s !important;
        }

        div.stButton > button:hover {
            opacity: 0.85 !important;
            transform: scale(1.02);
        }

        /* --- SEÇÕES --- */
        .gs-section { padding: 120px 6%; }
        
        .gs-image-hero {
            width: 100%;
            height: 90vh;
            background-image: url('https://images.unsplash.com/photo-1515377067373-bc604084e6f6?w=1600');
            background-size: cover;
            background-position: center;
            border-radius: 4px;
        }

        .gs-card {
            background: white;
            padding: 40px;
            border-radius: 0px;
            text-align: center;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div class="gs-nav">
        <div style="font-weight: 500; font-size: 18px; letter-spacing: 4px;">GOOD SECRETS</div>
        <div style="display: flex; gap: 40px; font-size: 12px; font-weight: 400; text-transform: uppercase; letter-spacing: 1px;">
            <span>Suplementos</span>
            <span>Ritual</span>
            <span>Sobre</span>
            <span style="border-bottom: 1px solid var(--gs-dark)">Comprar</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown('<div class="gs-section" style="padding-top: 180px;">', unsafe_allow_html=True)
    col_h1, col_h2 = st.columns([1, 1], gap="large")
    with col_h1:
        st.markdown('<span class="gs-label">O SEGREDO DA LONGEVIDADE</span>', unsafe_allow_html=True)
        st.markdown('<h1 class="gs-h1">Nutrição consciente para <span style="font-style:italic">mentes modernas.</span></h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 18px; line-height: 1.6; margin-bottom: 40px; color: var(--gs-text);">Acreditamos que o bem-estar começa de dentro para fora. Criamos suplementos puros, potentes e elegantes para o seu ritual diário.</p>', unsafe_allow_html=True)
        st.button("VER COLEÇÃO")
    with col_h2:
        st.markdown('<div style="height: 500px; background-image: url(\'https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=800\'); background-size: cover; border-radius: 200px 200px 0 0;"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SEÇÃO DE PRODUTOS (PROVA SOCIAL) ---
    st.markdown('<div style="padding: 100px 6%; background: var(--gs-accent); text-align: center;">', unsafe_allow_html=True)
    st.markdown('<h2 class="gs-serif" style="font-size: 40px; margin-bottom: 60px;">Feito para o seu melhor eu.</h2>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown('<div class="gs-card"><h3>FOCO</h3><p style="opacity: 0.7; margin-top: 15px;">Clareza cognitiva e energia mental sustentada.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="gs-card"><h3>CALMA</h3><p style="opacity: 0.7; margin-top: 15px;">Equilíbrio para os dias de alta intensidade.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="gs-card"><h3>VITAL</h3><p style="opacity: 0.7; margin-top: 15px;">Recuperação profunda e suporte imunológico.</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SEÇÃO DE NARRATIVA (STORYTELLING) ---
    st.markdown('<div class="gs-section">', unsafe_allow_html=True)
    col_t1, col_t2 = st.columns([1.2, 0.8], gap="large")
    with col_t2:
        st.markdown('<div style="height: 600px; background-image: url(\'https://images.unsplash.com/photo-1498804103079-a6351b050096?w=800\'); background-size: cover; border-radius: 4px;"></div>', unsafe_allow_html=True)
    with col_t1:
        st.markdown('<div style="padding-top: 100px;">', unsafe_allow_html=True)
        st.markdown('<h2 class="gs-h1">A pureza é a nossa <br>única regra.</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 20px; color: var(--gs-text); line-height: 1.8; margin-bottom: 30px;">
            Cada ingrediente em nossos suplementos é selecionado com rigor científico e ético. Não usamos enchimentos, não usamos atalhos. Apenas o que seu corpo realmente precisa.
        </p>
        <p style="font-weight: 600; text-decoration: underline;">Conheça nossa origem →</p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 120px 6%; background: var(--gs-dark); color: white;">
        <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 60px; margin-bottom: 80px;">
            <div>
                <h2 style="font-weight: 400; font-size: 24px; letter-spacing: 5px; margin-bottom: 20px;">GOOD SECRETS</h2>
                <p style="opacity: 0.5;">Inspirando rituais de saúde desde 2026.</p>
            </div>
            <div>
                <p style="font-weight: 600; margin-bottom: 20px;">MENU</p>
                <p style="opacity: 0.6; line-height: 2;">Produtos<br>Nosso Estudo<br>Assinatura<br>Imprensa</p>
            </div>
            <div>
                <p style="font-weight: 600; margin-bottom: 20px;">CONTATO</p>
                <p style="opacity: 0.6; line-height: 2;">Instagram<br>E-mail<br>Lojas</p>
            </div>
        </div>
        <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 40px; display: flex; justify-content: space-between; font-size: 11px; opacity: 0.4; letter-spacing: 1px;">
            <span>© 2026 GOOD SECRETS BRASIL.</span>
            <span>PRIVACIDADE & TERMOS</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Good Secrets | Nutrição Chic")
    render()
