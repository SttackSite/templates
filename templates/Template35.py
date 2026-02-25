import streamlit as st

def render():
    # --- SISTEMA DE DESIGN ALCRE (KOREAN MINIMALISM) ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@300;400&display=swap');

        :root {
            --al-bg: #ffffff;
            --al-black: #000000;
            --al-gray: #f2f2f2;
            --al-text-muted: #888888;
            --al-border: #e5e5e5;
        }

        .stApp { background-color: var(--al-bg); color: var(--al-black); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { 
            font-family: 'Inter', sans-serif; 
            -webkit-font-smoothing: antialiased;
        }

        .mono { font-family: 'JetBrains Mono', monospace; font-size: 12px; }

        /* --- NAVEGAÇÃO (CLEAN OS STYLE) --- */
        .al-nav {
            padding: 25px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--al-border);
            position: sticky;
            top: 0;
            background: rgba(255,255,255,0.9);
            backdrop-filter: blur(10px);
            z-index: 1000;
        }

        /* --- HERO SECTION --- */
        .al-hero {
            padding: 120px 5% 80px 5%;
            border-bottom: 1px solid var(--al-border);
        }

        .al-h1 {
            font-size: clamp(40px, 8vw, 110px);
            font-weight: 500;
            line-height: 1;
            letter-spacing: -0.04em;
            margin-bottom: 60px;
        }

        /* --- GRID DE PROJETOS (BENTO MODERNO) --- */
        .al-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            border-bottom: 1px solid var(--al-border);
        }

        .al-grid-item {
            border-right: 1px solid var(--al-border);
            padding: 0;
            position: relative;
            overflow: hidden;
            aspect-ratio: 16/10;
        }

        .al-grid-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .al-grid-item:hover img {
            transform: scale(1.05);
        }

        .al-project-info {
            padding: 30px;
            border-bottom: 1px solid var(--al-border);
        }

        /* --- BOTÃO ALCRE (STARK) --- */
        div.stButton > button {
            background-color: var(--al-black) !important;
            color: white !important;
            border: none !important;
            padding: 15px 40px !important;
            border-radius: 0px !important;
            font-size: 12px !important;
            font-weight: 500 !important;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            transition: 0.3s !important;
        }

        div.stButton > button:hover {
            background-color: #333 !important;
            opacity: 0.8;
        }

        /* --- FOOTER --- */
        .al-footer {
            padding: 100px 5%;
            background: var(--al-bg);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div class="al-nav">
        <div style="font-weight: 600; font-size: 22px; letter-spacing: -1px;">ALCRE</div>
        <div class="mono" style="display: flex; gap: 40px; text-transform: uppercase;">
            <span>Trabalhos</span>
            <span>Sobre</span>
            <span>Contato</span>
            <span style="opacity: 0.4;">KR / EN</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO ---
    st.markdown('<div class="al-hero">', unsafe_allow_html=True)
    st.markdown('<p class="mono" style="margin-bottom: 20px;">[ ALQUIMIA & CRIAÇÃO ]</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="al-h1">Moldando o futuro<br>através do design<br>atemporal.</h1>', unsafe_allow_html=True)
    
    col_h1, col_h2 = st.columns([1, 1])
    with col_h1:
        st.markdown('<p style="font-size: 18px; color: var(--al-text-muted); line-height: 1.6; max-width: 450px;">Somos um estúdio de design estratégico com sede em Seul, focado em transformar ideias complexas em experiências digitais simples e potentes.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- GRID DE PROJETOS (FULL WIDTH) ---
    # Linha 1
    c1, c2 = st.columns(2, gap="none")
    with c1:
        st.markdown('<div class="al-grid-item"><img src="https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=1200"></div>', unsafe_allow_html=True)
        st.markdown('<div class="al-project-info"><p class="mono">01 / BRANDING</p><h3 style="font-weight:500;">Oasis Smart Home</h3></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="al-grid-item" style="border-right:none;"><img src="https://images.unsplash.com/photo-1558655146-d09347e92766?w=1200"></div>', unsafe_allow_html=True)
        st.markdown('<div class="al-project-info" style="border-right:none;"><p class="mono">02 / UIUX</p><h3 style="font-weight:500;">Nebula Dashboard</h3></div>', unsafe_allow_html=True)

    # Linha 2
    c3, c4 = st.columns(2, gap="none")
    with c3:
        st.markdown('<div class="al-grid-item"><img src="https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=1200"></div>', unsafe_allow_html=True)
        st.markdown('<div class="al-project-info"><p class="mono">03 / WEB</p><h3 style="font-weight:500;">Kinetica Architecture</h3></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="al-grid-item" style="border-right:none;"><img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200"></div>', unsafe_allow_html=True)
        st.markdown('<div class="al-project-info" style="border-right:none;"><p class="mono">04 / R&D</p><h3 style="font-weight:500;">Experimental Lab</h3></div>', unsafe_allow_html=True)

    # --- SEÇÃO DE SERVIÇOS (TABELA TÉCNICA) ---
    st.markdown('<div style="padding: 100px 5%; border-bottom: 1px solid var(--al-border);">', unsafe_allow_html=True)
    st.markdown('<h2 class="mono" style="margin-bottom: 50px;">SERVIÇOS_</h2>', unsafe_allow_html=True)
    
    col_s1, col_s2, col_s3 = st.columns(3)
    service_style = "border-top: 1px solid black; padding-top: 20px; font-size: 14px;"
    
    with col_s1:
        st.markdown(f'<div style="{service_style}"><b>ESTRATÉGIA</b><br><br><span style="color:var(--al-text-muted)">Análise de Mercado<br>Posicionamento de Marca<br>Naming</span></div>', unsafe_allow_html=True)
    with col_s2:
        st.markdown(f'<div style="{service_style}"><b>DESIGN</b><br><br><span style="color:var(--al-text-muted)">Identidade Visual<br>Design de Produto<br>Sistemas de Design</span></div>', unsafe_allow_html=True)
    with col_s3:
        st.markdown(f'<div style="{service_style}"><b>DIGITAL</b><br><br><span style="color:var(--al-text-muted)">Desenvolvimento Web<br>Apps Mobile<br>E-commerce</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div class="al-footer">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
                <h2 style="font-size: 40px; font-weight: 500; margin-bottom: 40px;">Vamos criar algo<br>memorável.</h2>
                <div class="mono">hello@alcre.co.kr</div>
            </div>
            <div style="text-align: right;" class="mono">
                <p>SEUL, COREIA DO SUL</p>
                <p>INSTAGRAM / LINKEDIN</p>
                <p style="margin-top: 40px; opacity: 0.3;">© 2026 ALCRE STUDIO</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="ALCRE | Design Studio")
    render()
