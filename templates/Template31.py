import streamlit as st

def render():
    # --- CSS FULL FIDELITY ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        :root {
            --epi-bg: #F8F9FF;
            --epi-purple: #6c5ce7;
            --epi-peach: #ff8a71;
            --epi-text: #1A1A2E;
            --epi-text-light: #64648C;
            --epi-glass: rgba(255, 255, 255, 0.8);
            --epi-border: rgba(108, 92, 231, 0.15);
        }

        .stApp { background-color: var(--epi-bg); color: var(--epi-text); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }

        /* --- NAVBAR --- */
        .nav-container {
            position: fixed; top: 0; width: 100%; z-index: 1000;
            background: rgba(248, 249, 255, 0.8);
            backdrop-filter: blur(15px);
            padding: 20px 8%;
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid var(--epi-border);
            box-sizing: border-box;
        }

        /* --- HERO --- */
        .hero-full {
            padding: 160px 8% 100px 8%;
            background: radial-gradient(circle at 90% 10%, rgba(108, 92, 231, 0.08) 0%, transparent 40%),
                        radial-gradient(circle at 10% 90%, rgba(255, 138, 113, 0.08) 0%, transparent 40%);
        }

        .hero-tag {
            background: white; border: 1px solid var(--epi-border);
            padding: 6px 16px; border-radius: 100px;
            font-size: 12px; font-weight: 700; color: var(--epi-purple);
            display: inline-block; margin-bottom: 24px;
        }

        .hero-title {
            font-size: clamp(48px, 8vw, 92px);
            font-weight: 800; line-height: 1;
            letter-spacing: -0.04em; margin-bottom: 32px;
        }

        /* --- SEÇÕES --- */
        .section-full { padding: 100px 8%; }

        .section-header { margin-bottom: 60px; max-width: 700px; }
        .section-header h2 { font-size: 48px; font-weight: 800; letter-spacing: -0.02em; }

        /* --- CARDS METODOLOGIA --- */
        .method-card {
            background: white; border: 1px solid var(--epi-border);
            padding: 40px; border-radius: 32px; height: 100%;
            transition: 0.4s;
        }
        .method-card:hover { border-color: var(--epi-purple); background: #FDFDFF; }

        /* --- LOGOS / PROVA SOCIAL --- */
        .logo-bar {
            display: flex; justify-content: space-between; align-items: center;
            opacity: 0.5; filter: grayscale(1); padding: 40px 0;
            border-top: 1px solid var(--epi-border); border-bottom: 1px solid var(--epi-border);
        }

        /* Botão Epiminds (link estilizado) */
        .epi-btn {
            display: inline-block;
            background: var(--epi-purple);
            color: white !important;
            border: none;
            padding: 18px 42px;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 700;
            font-size: 15px;
            border-radius: 16px;
            text-decoration: none !important;
            transition: all 0.3s ease;
            cursor: pointer;
            margin-top: 14px;
        }
        .epi-btn:hover {
            color: white !important;
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(108, 92, 231, 0.3);
        }

        /* Links da navbar */
        .nav-link-epi {
            color: var(--epi-text) !important;
            text-decoration: none !important;
            font-size: 14px;
            font-weight: 600;
            transition: color 0.2s;
        }
        .nav-link-epi:hover { color: var(--epi-purple) !important; }
        .nav-link-epi.cta {
            color: var(--epi-purple) !important;
            border: 1px solid var(--epi-purple);
            padding: 8px 20px;
            border-radius: 12px;
        }
        .nav-link-epi.cta:hover {
            background: var(--epi-purple);
            color: white !important;
        }

        /* Links do footer */
        .footer-link-epi {
            color: rgba(255,255,255,0.6) !important;
            text-decoration: none !important;
            display: block;
            line-height: 2.5;
            transition: color 0.2s;
        }
        .footer-link-epi:hover { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

    # --- 1. HEADER / NAV ---
    st.markdown("""
    <div class="nav-container">
        <div style="font-weight: 800; font-size: 26px;">epiminds<span style="color:var(--epi-peach)">.</span></div>
        <div style="display: flex; gap: 40px; align-items: center;">
            <a href="#metodologia" class="nav-link-epi">Produtos</a>
            <a href="#metodologia" class="nav-link-epi">Neurociência</a>
            <a href="#beneficios" class="nav-link-epi">Casos de Sucesso</a>
            <a href="#footer" class="nav-link-epi">Sobre nós</a>
            <a href="https://www.google.com/" target="_blank" class="nav-link-epi cta">Agendar Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 2. HERO SECTION ---
    st.markdown('<div class="hero-full" id="hero">', unsafe_allow_html=True)
    st.markdown('<div class="hero-tag">A NOVA ERA DA SAÚDE MENTAL</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Sua mente é o seu maior <span style="color:var(--epi-purple)">ativo tecnológico.</span></h1>', unsafe_allow_html=True)

    c_h1, c_h2 = st.columns([1.2, 1])
    with c_h1:
        st.markdown("""
        <p style="font-size: 22px; color: var(--epi-text-light); line-height: 1.5; margin-bottom: 40px;">
            Unimos neurociência aplicada e inteligência artificial para decodificar o comportamento humano
            e potencializar a performance sustentável de líderes e equipes.
        </p>
        <a href="#metodologia" class="epi-btn">QUERO CONHECER A PLATAFORMA</a>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 3. PROVA SOCIAL (LOGOS) ---
    st.markdown('<div class="section-full" id="clientes">', unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: center; font-weight: 600; color: var(--epi-text-light); margin-bottom: 30px; font-size: 13px; letter-spacing: 2px;">CONFIADO POR GIGANTES DO MERCADO</p>
    <div class="logo-bar">
        <span style="font-size: 24px; font-weight: 800;">MICROSOFT</span>
        <span style="font-size: 24px; font-weight: 800;">AMAZON</span>
        <span style="font-size: 24px; font-weight: 800;">NUBANK</span>
        <span style="font-size: 24px; font-weight: 800;">IFood</span>
        <span style="font-size: 24px; font-weight: 800;">GOOGLE</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 4. SEÇÃO DE METODOLOGIA ---
    st.markdown('<div id="metodologia" class="section-full" style="background: white;">', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header">
        <p style="color: var(--epi-purple); font-weight: 700; font-size: 14px; margin-bottom: 10px;">NOSSA METODOLOGIA</p>
        <h2>Como hackeamos a alta performance</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("""
        <div class="method-card">
            <h3 style="font-size: 24px; margin-bottom: 20px;">01. Mapeamento</h3>
            <p style="color: var(--epi-text-light);">Utilizamos biomarcadores para entender o estado atual de estresse, foco e resiliência da sua equipe sem invasão de privacidade.</p>
            <a href="https://www.google.com/" target="_blank" style="color:var(--epi-purple); font-weight:700; text-decoration:none; display:inline-block; margin-top:20px;">Saiba mais →</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="method-card">
            <h3 style="font-size: 24px; margin-bottom: 20px;">02. Diagnóstico IA</h3>
            <p style="color: var(--epi-text-light);">Nossa inteligência analisa padrões comportamentais e prevê riscos de burnout com até 3 meses de antecedência.</p>
            <a href="https://www.google.com/" target="_blank" style="color:var(--epi-purple); font-weight:700; text-decoration:none; display:inline-block; margin-top:20px;">Saiba mais →</a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="method-card">
            <h3 style="font-size: 24px; margin-bottom: 20px;">03. Intervenção</h3>
            <p style="color: var(--epi-text-light);">Protocolos de neuroplasticidade personalizados para cada indivíduo, focados em recuperação rápida e foco profundo.</p>
            <a href="https://www.google.com/" target="_blank" style="color:var(--epi-purple); font-weight:700; text-decoration:none; display:inline-block; margin-top:20px;">Saiba mais →</a>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. SEÇÃO DE CONTEÚDO (IMAGEM + TEXTO) ---
    st.markdown('<div id="beneficios" class="section-full">', unsafe_allow_html=True)
    cl1, cl2 = st.columns([1, 1.2], gap="large")
    with cl1:
        st.markdown("""
        <div style="background: var(--epi-purple); border-radius: 40px; height: 500px; padding: 40px; color: white;">
            <p style="font-size: 14px; font-weight: 600; opacity: 0.8;">INSIGHTS EM TEMPO REAL</p>
            <h2 style="font-size: 40px; margin-top: 20px;">O Dashboard do cérebro.</h2>
            <div style="margin-top: 40px; height: 250px; background: rgba(255,255,255,0.1); border-radius: 20px;"></div>
        </div>
        """, unsafe_allow_html=True)
    with cl2:
        st.markdown('<div style="padding-top: 40px;">', unsafe_allow_html=True)
        st.markdown('<h2>Decisões baseadas em dados biológicos, não em suposições.</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 18px; color: var(--epi-text-light); margin: 30px 0;">
            A Epiminds integra-se às ferramentas que sua equipe já usa (Slack, Teams, Calendar) para fornecer
            uma camada de inteligência emocional e cognitiva.
        </p>
        <ul style="color: var(--epi-text-light); line-height: 2;">
            <li>✓ Redução de 40% no turnover por burnout</li>
            <li>✓ Aumento de 25% na capacidade de foco profundo</li>
            <li>✓ Melhora comprovada no clima organizacional</li>
        </ul>
        <a href="https://www.google.com/" target="_blank" class="epi-btn" style="margin-top:30px;">VER TODOS OS BENEFÍCIOS</a>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 6. FOOTER DENSO ---
    st.markdown("""
    <div id="footer" style="background: #1A1A2E; color: white; padding: 100px 8% 40px 8%;">
        <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 60px; margin-bottom: 80px;">
            <div>
                <h2 style="font-weight: 800; margin-bottom: 20px;">epiminds.</h2>
                <p style="opacity: 0.6; max-width: 250px;">Liderando a fronteira da neurotecnologia aplicada ao trabalho no Brasil e no mundo.</p>
            </div>
            <div>
                <p style="font-weight: 700; margin-bottom: 20px;">PRODUTO</p>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">Plataforma IA</a>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">Treinamentos</a>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">Segurança</a>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">API</a>
            </div>
            <div>
                <p style="font-weight: 700; margin-bottom: 20px;">RECURSOS</p>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">Whitepapers</a>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">Blog</a>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">Neuro-Guia</a>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">Suporte</a>
            </div>
            <div>
                <p style="font-weight: 700; margin-bottom: 20px;">CONTATO</p>
                <a href="mailto:contato@epiminds.com" class="footer-link-epi">contato@epiminds.com</a>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">LinkedIn</a>
                <a href="https://www.google.com/" target="_blank" class="footer-link-epi">Instagram</a>
            </div>
        </div>
        <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 40px; display: flex; justify-content: space-between; font-size: 12px; opacity: 0.5;">
            <span>© 2026 EPIMINDS NEUROTECH S.A.</span>
            <span>
                <a href="https://www.google.com/" target="_blank" style="color:inherit; text-decoration:none;">POLÍTICA DE PRIVACIDADE</a>
                &nbsp;|&nbsp;
                <a href="https://www.google.com/" target="_blank" style="color:inherit; text-decoration:none;">LGPD</a>
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Epiminds Full | Neurotech")
    render()
