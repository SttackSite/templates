import streamlit as st

def render():
    # --- SISTEMA DE DESIGN SAULO SIMON ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bungee&family=Inter:wght@400;700;900&display=swap');

        :root {
            --ss-bg: #ffae00;
            --ss-black: #222222;
            --ss-white: #ffffff;
            --ss-card: #ffc445;
        }

        .stApp {
            background-color: var(--ss-bg);
            color: var(--ss-black);
            background-image: radial-gradient(circle at 20% 20%, rgba(255,255,255,0.2) 0%, transparent 40%);
        }

        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            cursor: url('https://cdn.custom-cursor.com/db/cursor/32/Game_Cursor_Hand.png'), auto;
        }

        /* --- TITULOS ESTILO JOGO --- */
        .ss-title {
            font-family: 'Bungee', cursive;
            font-size: clamp(40px, 10vw, 120px);
            line-height: 0.9;
            color: var(--ss-white);
            text-shadow: 8px 8px 0px var(--ss-black);
            margin-bottom: 20px;
            text-transform: uppercase;
        }

        .ss-subtitle {
            font-family: 'Bungee', cursive;
            font-size: 24px;
            color: var(--ss-black);
            margin-bottom: 40px;
        }

        /* --- CARDS DE PROJETOS (BENTO 3D) --- */
        .ss-project-card {
            background: var(--ss-card);
            border: 6px solid var(--ss-black);
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 12px 12px 0px var(--ss-black);
            transition: 0.3s;
        }

        .ss-project-card:hover {
            background: var(--ss-white);
            transform: rotate(-1deg);
        }

        .project-tag {
            background: var(--ss-black);
            color: var(--ss-white);
            padding: 4px 12px;
            font-size: 12px;
            font-weight: 800;
            display: inline-block;
            margin-bottom: 15px;
        }

        /* --- SEÇÕES --- */
        .ss-section { padding: 100px 8%; }

        .ss-footer {
            background: var(--ss-black);
            color: var(--ss-white);
            padding: 80px 8%;
            text-align: center;
        }

        /* Botão Gamer (link estilizado) */
        .ss-btn {
            display: inline-block;
            background-color: var(--ss-black);
            color: var(--ss-white) !important;
            border: 4px solid var(--ss-black);
            padding: 20px 40px;
            font-family: 'Bungee', cursive;
            font-size: 18px;
            border-radius: 0px;
            box-shadow: 8px 8px 0px rgba(0,0,0,0.2);
            text-decoration: none !important;
            transition: all 0.1s ease;
            cursor: pointer;
            width: 100%;
            box-sizing: border-box;
            text-align: center;
            margin-top: 14px;
        }
        .ss-btn:hover {
            transform: translate(-4px, -4px);
            box-shadow: 12px 12px 0px var(--ss-black);
            background-color: #333;
            color: var(--ss-white) !important;
        }
        .ss-btn:active {
            transform: translate(4px, 4px);
            box-shadow: 0px 0px 0px var(--ss-black);
        }

        /* Links da navbar */
        .nav-link-ss {
            color: var(--ss-black) !important;
            text-decoration: none !important;
            font-weight: 800;
            text-transform: uppercase;
            font-size: 14px;
            transition: opacity 0.2s;
        }
        .nav-link-ss:hover { opacity: 0.6; }
        .nav-link-ss.play {
            color: white !important;
            text-shadow: 2px 2px 0 #000;
        }

        /* Links do footer */
        .footer-link-ss {
            color: var(--ss-white) !important;
            text-decoration: none !important;
            font-family: 'Bungee', cursive;
            font-size: 20px;
            transition: opacity 0.2s;
        }
        .footer-link-ss:hover { opacity: 0.6; }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 30px 8%; display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.05);">
        <div style="font-family: 'Bungee'; font-size: 28px; border: 4px solid #222; padding: 5px 15px;">ss</div>
        <div style="display: flex; gap: 30px; align-items: center;">
            <a href="#projetos" class="nav-link-ss">Projetos</a>
            <a href="#sobre" class="nav-link-ss">Experiências</a>
            <a href="#sobre" class="nav-link-ss">Sobre</a>
            <a href="#footer" class="nav-link-ss play">Dê o Play</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO ---
    st.markdown('<div id="hero" class="ss-section" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown('<h1 class="ss-title">SAULO<br>SIMON</h1>', unsafe_allow_html=True)
    st.markdown('<p class="ss-subtitle">DESENVOLVEDOR CREATIVO & MESTRE DO WEBGL</p>', unsafe_allow_html=True)

    col_h1, col_h2, col_h3 = st.columns([1, 1, 1])
    with col_h2:
        st.markdown('<a href="#projetos" class="ss-btn">DIRIGIR PELO SITE</a>', unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-top: 60px; border: 8px solid #222; background: #eee; height: 400px; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
            <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; position: absolute;">
            <div style="position: relative; background: #222; color: #fff; padding: 10px 20px; font-family: 'Bungee';">SIMULAÇÃO INTERATIVA 3D</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PROJETOS (GRID COMPLETO) ---
    st.markdown('<div id="projetos" class="ss-section">', unsafe_allow_html=True)
    st.markdown('<h2 class="ss-subtitle">TRABALHOS EM DESTAQUE</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="ss-project-card">
            <div class="project-tag">THREE.JS JOURNEY</div>
            <h3 style="font-family: 'Bungee'; font-size: 28px;">O curso definitivo de Three.js</h3>
            <p style="margin: 20px 0; font-weight: 600;">Aprenda a criar mundos 3D incríveis para a web partindo do zero absoluto.</p>
            <div style="height: 200px; background: #222; margin-top: 20px;"></div>
            <a href="https://www.google.com/" target="_blank" class="ss-btn" style="margin-top:20px;">VER CURSO</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="ss-project-card">
            <div class="project-tag">WEBGL EXPERIENCE</div>
            <h3 style="font-family: 'Bungee'; font-size: 28px;">Oris: O Relógio Interativo</h3>
            <p style="margin: 20px 0; font-weight: 600;">Uma experiência imersiva para explorar cada detalhe da mecânica de luxo em tempo real.</p>
            <div style="height: 200px; background: #fff; border: 4px solid #222; margin-top: 20px;"></div>
            <a href="https://www.google.com/" target="_blank" class="ss-btn" style="margin-top:20px;">VER PROJETO</a>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SEÇÃO SOBRE (BIO COMPLETA) ---
    st.markdown('<div id="sobre" class="ss-section" style="background: rgba(255,255,255,0.3); border-top: 6px solid #222;">', unsafe_allow_html=True)
    c_b1, c_b2 = st.columns([1, 1.5], gap="large")
    with c_b1:
        st.markdown('<div style="width:100%; height:400px; background:#222; border: 8px solid white;"></div>', unsafe_allow_html=True)
    with c_b2:
        st.markdown('<h2 class="ss-subtitle" style="margin-bottom:20px;">QUEM É O SAULO?</h2>', unsafe_allow_html=True)
        st.markdown("""
            <p style="font-size: 20px; font-weight: 700; line-height: 1.4;">
                Sou um desenvolvedor freelancer francês apaixonado por criar experiências digitais que desafiam os limites do navegador.
                Especialista em WebGL, Three.js e animações de alta performance.
            </p>
            <p style="font-size: 18px; margin-top: 20px;">
                Trabalho com agências e marcas globais para transformar conceitos abstratos em mundos interativos onde o usuário é o protagonista.
            </p>
            <a href="https://www.google.com/" target="_blank" class="ss-btn" style="margin-top:30px; display:inline-block; width:auto;">MEU SETUP DE TRABALHO</a>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div id="footer" class="ss-footer">
        <h2 style="font-family: 'Bungee'; font-size: 50px; margin-bottom: 40px;">VAMOS JOGAR?</h2>
        <div style="display: flex; justify-content: center; gap: 50px; flex-wrap: wrap;">
            <a href="https://www.google.com/" target="_blank" class="footer-link-ss">TWITTER</a>
            <a href="https://www.google.com/" target="_blank" class="footer-link-ss">GITHUB</a>
            <a href="https://www.google.com/" target="_blank" class="footer-link-ss">LINKEDIN</a>
            <a href="mailto:saulo@simon.dev" class="footer-link-ss">E-MAIL</a>
        </div>
        <div style="margin-top: 60px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 40px; font-size: 12px; font-weight: 700;">
            © 2026 SAULO SIMON — DESENVOLVIDO COM CÓDIGO E PAIXÃO.
        </div>
    </div>
    """, unsafe_allow_html=True)


    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template33" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="SAULO Simon | Creative Developer")
    render()
