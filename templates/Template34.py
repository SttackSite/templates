import streamlit as st

def render():
    # --- SISTEMA DE DESIGN FREQUENCY ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,500;1,300&family=Inter:wght@200;400;600&display=swap');

        :root {
            --fq-bg: #050505;
            --fq-accent: #b5ff00;
            --fq-purple: #4a148c;
            --fq-text: #ffffff;
            --fq-glass: rgba(255, 255, 255, 0.03);
        }

        .stApp {
            background-color: var(--fq-bg);
            color: var(--fq-text);
            background-image:
                radial-gradient(at 0% 0%, rgba(74, 20, 140, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(181, 255, 0, 0.05) 0px, transparent 50%);
        }

        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        /* --- TYPOGRAPHY --- */
        .fq-serif { font-family: 'Cormorant Garamond', serif; }

        .fq-h1 {
            font-family: 'Cormorant Garamond', serif;
            font-size: clamp(40px, 8vw, 110px);
            font-weight: 300;
            line-height: 0.9;
            letter-spacing: -0.02em;
            margin-bottom: 40px;
            font-style: italic;
        }

        /* --- NAVEGAÇÃO --- */
        .fq-nav {
            padding: 30px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            background: rgba(5, 5, 5, 0.8);
            backdrop-filter: blur(10px);
            box-sizing: border-box;
        }

        /* --- CARDS ATMOSFÉRICOS --- */
        .fq-card {
            background: var(--fq-glass);
            border: 1px solid rgba(255,255,255,0.05);
            padding: 50px;
            border-radius: 2px;
            height: 100%;
            transition: 0.5s;
        }

        .fq-card:hover {
            border-color: rgba(181, 255, 0, 0.4);
            background: rgba(255,255,255,0.06);
        }

        .fq-label {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: var(--fq-accent);
            margin-bottom: 20px;
            display: block;
        }

        /* Botão Frequency (link estilizado) */
        .fq-btn {
            display: inline-block;
            background-color: transparent;
            color: var(--fq-text) !important;
            border: 1px solid rgba(255,255,255,0.3);
            padding: 12px 35px;
            border-radius: 100px;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            text-decoration: none !important;
            transition: all 0.4s ease;
            cursor: pointer;
            margin-top: 14px;
        }
        .fq-btn:hover {
            border-color: var(--fq-accent);
            color: var(--fq-accent) !important;
            background-color: rgba(181, 255, 0, 0.05);
            transform: scale(1.05);
        }

        /* Links da navbar */
        .nav-link-fq {
            color: var(--fq-text) !important;
            text-decoration: none !important;
            font-size: 12px;
            font-weight: 400;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: color 0.2s;
        }
        .nav-link-fq:hover { color: var(--fq-accent) !important; }
        .nav-link-fq.accent { color: var(--fq-accent) !important; }

        /* Links do footer */
        .footer-link-fq {
            color: rgba(255,255,255,0.5) !important;
            text-decoration: none !important;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: color 0.2s;
        }
        .footer-link-fq:hover { color: var(--fq-accent) !important; opacity: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div class="fq-nav">
        <div style="font-weight: 600; font-size: 20px; letter-spacing: 4px;">FREQUENCY</div>
        <div style="display: flex; gap: 40px; align-items: center;">
            <a href="#beneficios" class="nav-link-fq">A Jornada</a>
            <a href="#aulas" class="nav-link-fq">Estúdios</a>
            <a href="#aulas" class="nav-link-fq">Digital</a>
            <a href="https://www.google.com/" target="_blank" class="nav-link-fq accent">Membro</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown('<div id="hero" style="padding: 220px 8% 120px 8%; text-align: center;">', unsafe_allow_html=True)
    st.markdown('<span class="fq-label">Sinta sua própria energia</span>', unsafe_allow_html=True)
    st.markdown('<h1 class="fq-h1">Mude sua respiração.<br>Mude sua <span style="opacity: 0.6">consciência.</span></h1>', unsafe_allow_html=True)

    col_h1, col_h2, col_h3 = st.columns([1, 0.8, 1])
    with col_h2:
        st.markdown('<a href="#beneficios" class="fq-btn">COMECE SUA VIAGEM</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- VIDEO / MÍDIA PLACEHOLDER ---
    st.markdown("""
    <div style="width: 100%; height: 70vh; background: #111; display: flex; align-items: center; justify-content: center; overflow: hidden; position: relative;">
        <img src="https://images.unsplash.com/photo-1511216335778-7cb8f49fa7a3?w=1600" style="width: 100%; opacity: 0.4; filter: contrast(1.2) saturate(0.5); position: absolute;">
        <div style="position: relative; text-align: center;">
            <p class="fq-serif" style="font-size: 32px; font-style: italic;">O poder de se reconectar.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- SEÇÃO DE BENEFÍCIOS ---
    st.markdown('<div id="beneficios" style="padding: 120px 8%; background: #000;">', unsafe_allow_html=True)
    st.markdown('<h2 class="fq-serif" style="font-size: 50px; margin-bottom: 80px; text-align: center;">Por que Frequency?</h2>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="large")

    def render_fq_card(col, title, desc):
        with col:
            st.markdown(f"""
            <div class="fq-card">
                <h3 class="fq-serif" style="font-size: 32px; margin-bottom: 25px;">{title}</h3>
                <p style="color: rgba(255,255,255,0.6); line-height: 1.8; font-size: 15px;">{desc}</p>
                <a href="https://www.google.com/" target="_blank" class="fq-btn" style="margin-top:30px; font-size:12px; padding:10px 25px;">SAIBA MAIS</a>
            </div>
            """, unsafe_allow_html=True)

    render_fq_card(c1, "Clareza Mental",       "Remova o ruído cotidiano e acesse estados profundos de foco através de técnicas rítmicas de respiração.")
    render_fq_card(c2, "Liberação Emocional",  "Acesse e processe emoções estocadas no corpo de forma segura e guiada por especialistas.")
    render_fq_card(c3, "Conexão Vital",        "Sinta o fluxo de energia vital percorrendo seu sistema, revitalizando cada célula do seu ser.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SEÇÃO DE CRONOGRAMA / CLASSES ---
    st.markdown('<div id="aulas" style="padding: 120px 8%;">', unsafe_allow_html=True)
    col_t1, col_t2 = st.columns([1, 1.5], gap="large")
    with col_t1:
        st.markdown('<span class="fq-label">Aulas Ao Vivo</span>', unsafe_allow_html=True)
        st.markdown('<h2 class="fq-serif" style="font-size: 60px;">Encontre seu ritmo.</h2>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.google.com/" target="_blank" class="fq-btn" style="margin-top:30px;">VER AGENDA COMPLETA</a>', unsafe_allow_html=True)
    with col_t2:
        st.markdown("""
        <a href="https://www.google.com/" target="_blank" style="text-decoration:none; color:inherit; display:block; border-bottom: 1px solid rgba(255,255,255,0.1); padding: 30px 0; display: flex; justify-content: space-between; align-items: center; transition: color 0.2s;" onmouseover="this.style.color='#b5ff00'" onmouseout="this.style.color='inherit'">
            <span style="font-weight: 600;">Breathwork Fundamental</span>
            <span style="opacity: 0.6;">Segundas | 19:00</span>
        </a>
        <a href="https://www.google.com/" target="_blank" style="text-decoration:none; color:inherit; display:block; border-bottom: 1px solid rgba(255,255,255,0.1); padding: 30px 0; display: flex; justify-content: space-between; align-items: center; transition: color 0.2s;" onmouseover="this.style.color='#b5ff00'" onmouseout="this.style.color='inherit'">
            <span style="font-weight: 600;">Jornada de Expansão</span>
            <span style="opacity: 0.6;">Quartas | 20:30</span>
        </a>
        <a href="https://www.google.com/" target="_blank" style="text-decoration:none; color:inherit; display:block; border-bottom: 1px solid rgba(255,255,255,0.1); padding: 30px 0; display: flex; justify-content: space-between; align-items: center; transition: color 0.2s;" onmouseover="this.style.color='#b5ff00'" onmouseout="this.style.color='inherit'">
            <span style="font-weight: 600;">Detox Dopaminérgico</span>
            <span style="opacity: 0.6;">Sábados | 10:00</span>
        </a>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div id="footer" style="padding: 120px 8% 60px 8%; border-top: 1px solid rgba(255,255,255,0.05); text-align: center;">
        <h2 style="font-weight: 600; font-size: 24px; letter-spacing: 8px; margin-bottom: 60px;">FREQUENCY</h2>
        <div style="display: flex; justify-content: center; gap: 50px; flex-wrap: wrap;">
            <a href="https://www.google.com/" target="_blank" class="footer-link-fq">Instagram</a>
            <a href="https://www.google.com/" target="_blank" class="footer-link-fq">Spotify</a>
            <a href="https://www.google.com/" target="_blank" class="footer-link-fq">Política de Privacidade</a>
            <a href="mailto:contato@frequency.com" class="footer-link-fq">Contato</a>
        </div>
        <div style="margin-top: 80px; font-size: 11px; opacity: 0.3;">
            © 2026 FREQUENCY BREATHWORK. TODOS OS DIREITOS RESERVADOS. <br> SINTA A FREQUÊNCIA.
        </div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Frequency | Breathwork Experience")
    render()
