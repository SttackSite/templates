import streamlit as st

def render():
    # --- CSS AVANÇADO FORZY PRO ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

        :root {
            --fz-black: #000000;
            --fz-white: #ffffff;
            --fz-gray-100: #f5f5f7;
            --fz-gray-200: #e8e8ed;
            --fz-text-sec: #86868b;
            --fz-accent: #0066cc;
        }

        /* Reset e Configuração Base */
        .stApp { background-color: var(--fz-white); color: var(--fz-black); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
        
        html, body, [class*="css"] { 
            font-family: 'Inter', sans-serif; 
            letter-spacing: -0.02em; 
            scroll-behavior: smooth;
        }

        /* Typography - Forzy Style */
        .display-title {
            font-size: clamp(48px, 10vw, 110px);
            font-weight: 900;
            line-height: 0.95;
            letter-spacing: -0.06em;
            margin-bottom: 30px;
        }

        .section-label {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: var(--fz-text-sec);
            margin-bottom: 20px;
            display: block;
        }

        /* Hero Full Screen */
        .hero-section {
            min-height: 90vh;
            padding: 120px 8% 60px 8%;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        /* Botão Minimalista "Apple" */
        div.stButton > button {
            background-color: var(--fz-black) !important;
            color: var(--fz-white) !important;
            border: none !important;
            padding: 14px 38px !important;
            font-weight: 600 !important;
            border-radius: 50px !important;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
            font-size: 16px !important;
            border: 1px solid var(--fz-black) !important;
        }

        div.stButton > button:hover {
            background-color: transparent !important;
            color: var(--fz-black) !important;
            transform: translateY(-2px);
        }

        /* Grid de Serviços Complexo */
        .service-grid {
            padding: 100px 8%;
            background: var(--fz-white);
        }

        .service-card {
            border-top: 1px solid var(--fz-gray-200);
            padding: 60px 0;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            transition: all 0.3s ease;
        }

        .service-card:hover {
            border-top-color: var(--fz-black);
        }

        .service-num { font-weight: 700; font-size: 14px; color: var(--fz-text-sec); }
        .service-content { width: 60%; }
        .service-title { font-size: 32px; font-weight: 700; margin-bottom: 15px; }
        .service-desc { font-size: 18px; color: var(--fz-text-sec); line-height: 1.5; }

        /* Footer Black */
        .footer-pro {
            background: var(--fz-black);
            color: var(--fz-white);
            padding: 100px 8% 50px 8%;
        }

        .footer-big-text {
            font-size: clamp(30px, 5vw, 60px);
            font-weight: 700;
            margin-bottom: 60px;
            line-height: 1.1;
            letter-spacing: -0.04em;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div style="padding: 30px 8%; display: flex; justify-content: space-between; align-items: center; position: fixed; width: 100%; top: 0; background: rgba(255,255,255,0.8); backdrop-filter: blur(20px); z-index: 999;">
        <div style="font-weight: 900; font-size: 24px;">FORZY</div>
        <div style="display: flex; gap: 40px; font-size: 11px; font-weight: 700; letter-spacing: 1px;">
            <span>SOLUÇÕES</span>
            <span>ECOSSISTEMA</span>
            <span>RESULTADOS</span>
            <span style="padding-bottom: 2px; border-bottom: 2px solid var(--fz-black);">CONTATO</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO ---
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    st.markdown('<span class="section-label">Performance & Design Agnostic</span>', unsafe_allow_html=True)
    st.markdown('<h1 class="display-title">Design que vende.<br>Tecnologia que escala.</h1>', unsafe_allow_html=True)
    
    col_h1, col_h2 = st.columns([1.5, 1])
    with col_h1:
        st.markdown("""
        <p style="font-size: 22px; color: var(--fz-text-sec); line-height: 1.4; margin-bottom: 40px;">
            A Forzy é uma consultoria estratégica focada em criar produtos digitais que dominam mercados. 
            Não fazemos apenas sites; construímos ativos de alta performance.
        </p>
        """, unsafe_allow_html=True)
        st.button("VAMOS CONSTRUIR ALGO NOVO?")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CASES / IMAGEM LARGA ---
    st.markdown("""
    <div style="padding: 0 8%;">
        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1600" 
             style="width: 100%; border-radius: 30px; filter: grayscale(100%) contrast(1.1);">
    </div>
    """, unsafe_allow_html=True)

    # --- SERVICES SECTION ---
    st.markdown('<div class="service-grid">', unsafe_allow_html=True)
    st.markdown('<span class="section-label">O que fazemos</span>', unsafe_allow_html=True)
    
    def render_service(num, title, desc):
        st.markdown(f"""
        <div class="service-card">
            <div class="service-num">{num}</div>
            <div class="service-content">
                <div class="service-title">{title}</div>
                <div class="service-desc">{desc}</div>
            </div>
            <div style="font-size: 24px;">↗</div>
        </div>
        """, unsafe_allow_html=True)

    render_service("01", "Identidade Visual & Branding", "Construímos marcas que são impossíveis de ignorar, unindo psicologia e estética.")
    render_service("02", "Desenvolvimento Web & Mobile", "Sistemas robustos com as tecnologias mais rápidas do mundo para garantir 99.9% de uptime.")
    render_service("03", "Growth Marketing", "Estratégias de aquisição baseadas em dados para escalar o seu faturamento de forma previsível.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- TEXTO DE IMPACTO ---
    st.markdown("""
    <div style="padding: 150px 8%; background: var(--fz-gray-100);">
        <h2 style="font-size: clamp(28px, 4vw, 48px); max-width: 900px; line-height: 1.2;">
            "A simplicidade é o último grau de sofisticação. Na Forzy, eliminamos o ruído para que sua mensagem brilhe."
        </h2>
    </div>
    """, unsafe_allow_html=True)

    # --- FOOTER PRO ---
    st.markdown('<div class="footer-pro">', unsafe_allow_html=True)
    st.markdown('<p class="footer-big-text">Pronto para elevar o padrão do seu negócio?</p>', unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3 = st.columns([2, 1, 1])
    with col_f1:
        st.markdown("""
        <div style="font-weight: 900; font-size: 32px; margin-bottom: 20px;">FORZY</div>
        <p style="color: #86868b; max-width: 300px;">Transformando ideias em interfaces de alto impacto desde 2018.</p>
        """, unsafe_allow_html=True)
    
    with col_f2:
        st.markdown("""
        <p style="font-weight: 700;">CONTATO</p>
        <p style="color: #86868b;">hello@forzy.com.br<br>+55 11 99999-9999</p>
        """, unsafe_allow_html=True)
        
    with col_f3:
        st.markdown("""
        <p style="font-weight: 700;">FOLLOW</p>
        <p style="color: #86868b;">Instagram<br>LinkedIn<br>Behance</p>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 80px; padding-top: 40px; border-top: 1px solid #333; font-size: 12px; color: #555;">
        © 2026 FORZY INTERFACE DESIGN. ALL RIGHTS RESERVED.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Render direto
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="FORZY | Pro Version")
    render()
