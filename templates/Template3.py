import streamlit as st

def render():
    """Renderiza o template 3 - Experiência Absurda (Premium)"""
    
    # ❌ NÃO ALTERE: Configuração da página - Define o título da aba, ícone e layout
    st.set_page_config(
        page_title="Experiência Absurda",  # ✅ ALTERE: Título da aba do navegador
        page_icon="✨",  # ✅ ALTERE: Ícone que aparece na aba
        layout="wide",  # ❌ NÃO ALTERE: Layout da página
        initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Esconde a sidebar
    )

    # ❌ NÃO ALTERE: CSS ORIGINAL E INOVADOR - Estilos visuais da página inteira com cores dinâmicas
    custom_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Outfit:wght@300;400;500;600;700;800;900&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 50%, #16213e 100%);
            font-family: 'Space Grotesk', sans-serif;
            color: #ffffff;
            line-height: 1.6;
            overflow-x: hidden;
        }
        
        [data-testid="stDecoration"] { display: none; }
        
        .main {
            padding: 0 !important;
            background: transparent;
            position: relative;
            z-index: 1;
        }
        
        /* ❌ NÃO ALTERE: Animações absurdas que fazem elementos pulsar, flutuar e mudar de cor */
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        @keyframes floatUp {
            0% { transform: translateY(0px); opacity: 0; }
            50% { opacity: 1; }
            100% { transform: translateY(-20px); opacity: 0; }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        @keyframes slideIn {
            from { transform: translateX(-100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        @keyframes glow {
            0%, 100% { box-shadow: 0 0 20px rgba(255, 0, 150, 0.5); }
            50% { box-shadow: 0 0 40px rgba(255, 0, 150, 0.8); }
        }
        
        /* ❌ NÃO ALTERE: Navbar absurda com backdrop blur e borda gradiente */
        .navbar {
            background: rgba(15, 15, 30, 0.95);
            backdrop-filter: blur(20px);
            padding: 20px 60px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid;
            border-image: linear-gradient(90deg, #FF006E, #00D9FF, #FFD60A, #FF006E) 1;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 8px 32px rgba(255, 0, 110, 0.15);
        }
        
        /* ✅ ALTERE: Logo - Mude o texto "PREMIUM" na navbar */
        .navbar-logo {
            font-size: 32px;
            font-weight: 900;
            background: linear-gradient(135deg, #FF006E, #00D9FF, #FFD60A);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 2px;
            animation: pulse 2s ease-in-out infinite;
        }
        
        /* ❌ NÃO ALTERE: Container dos links da navbar */
        .navbar-links {
            display: flex;
            gap: 50px;
            align-items: center;
        }
        
        /* ✅ ALTERE: Links da navbar - Mude cor, tamanho e espaçamento */
        .navbar-link {
            color: #00D9FF;
            text-decoration: none !important;
            font-weight: 600;
            font-size: 13px;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
            position: relative;
        }
        
        /* ❌ NÃO ALTERE: Underline animado dos links - Aparece ao passar o mouse */
        .navbar-link::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #FF006E, #00D9FF);
            transition: width 0.3s ease;
        }
        
        .navbar-link:hover::after {
            width: 100%;
        }
        
        .navbar-link:hover {
            color: #FFD60A;
        }
        
        /* ✅ ALTERE: Botão CTA da navbar - Mude cor, texto e tamanho */
        .navbar-cta {
            background: linear-gradient(135deg, #FF006E, #FF4D6D);
            color: white;
            padding: 12px 32px;
            border-radius: 50px;
            text-decoration: none !important;
            font-weight: 700;
            font-size: 12px;
            transition: all 0.3s ease;
            border: 2px solid #FF006E;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 4px 15px rgba(255, 0, 110, 0.4);
        }
        
        .navbar-cta:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(255, 0, 110, 0.6);
            border-color: #00D9FF;
        }
        
        /* ❌ NÃO ALTERE: Hero section - Seção principal com fundo gradiente animado */
        .hero-section {
            background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #1a1a2e 100%);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            min-height: 800px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(255, 0, 110, 0.2) 0%, transparent 70%);
            border-radius: 50%;
            top: -100px;
            right: -100px;
            animation: pulse 4s ease-in-out infinite;
        }
        
        .hero-section::after {
            content: '';
            position: absolute;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(0, 217, 255, 0.15) 0%, transparent 70%);
            border-radius: 50%;
            bottom: -150px;
            left: -150px;
            animation: pulse 5s ease-in-out infinite;
        }
        
        .hero-content {
            text-align: center;
            z-index: 2;
            position: relative;
            max-width: 900px;
        }
        
        /* ✅ ALTERE: Título do hero - Mude o texto principal */
        .hero-title {
            font-size: 80px;
            font-weight: 900;
            margin-bottom: 20px;
            background: linear-gradient(135deg, #FF006E, #00D9FF, #FFD60A, #FF006E);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 8s ease infinite;
            letter-spacing: -2px;
            line-height: 1.1;
        }
        
        /* ✅ ALTERE: Subtítulo do hero - Mude o texto secundário */
        .hero-subtitle {
            font-size: 24px;
            font-weight: 300;
            margin-bottom: 50px;
            color: #00D9FF;
            letter-spacing: 1px;
            animation: slideIn 1s ease-out;
        }
        
        .hero-cta-group {
            display: flex;
            gap: 20px;
            justify-content: center;
            animation: slideIn 1.2s ease-out;
        }
        
        /* ✅ ALTERE: Botão primário do hero - Mude cor, texto e tamanho */
        .hero-cta-primary {
            background: linear-gradient(135deg, #FF006E, #FF4D6D);
            color: white;
            padding: 18px 50px;
            border-radius: 50px;
            font-weight: 700;
            font-size: 14px;
            text-decoration: none !important;
            transition: all 0.3s ease;
            border: 2px solid #FF006E;
            cursor: pointer;
            display: inline-block;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 8px 25px rgba(255, 0, 110, 0.4);
        }
        
        .hero-cta-primary:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(255, 0, 110, 0.6);
        }
        
        /* ✅ ALTERE: Botão secundário do hero - Mude cor, texto e tamanho */
        .hero-cta-secondary {
            background: transparent;
            color: #00D9FF;
            padding: 18px 50px;
            border-radius: 50px;
            font-weight: 700;
            font-size: 14px;
            text-decoration: none !important;
            transition: all 0.3s ease;
            border: 2px solid #00D9FF;
            cursor: pointer;
            display: inline-block;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .hero-cta-secondary:hover {
            background: #00D9FF;
            color: #0f0f1e;
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(0, 217, 255, 0.4);
        }
        
        /* ❌ NÃO ALTERE: Features section - Container com grid de cards */
        .features-section {
            padding: 120px 60px;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            position: relative;
        }
        
        .section-header {
            text-align: center;
            margin-bottom: 100px;
        }
        
        /* ✅ ALTERE: Título da seção - Mude "Recursos Incríveis" */
        .section-title {
            font-size: 56px;
            font-weight: 900;
            margin-bottom: 20px;
            background: linear-gradient(135deg, #FFD60A, #FF006E, #00D9FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -1px;
        }
        
        /* ✅ ALTERE: Descrição da seção - Mude o texto descritivo */
        .section-description {
            font-size: 18px;
            color: #00D9FF;
            font-weight: 300;
            max-width: 600px;
            margin: 0 auto;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .feature-card {
            background: linear-gradient(135deg, rgba(255, 0, 110, 0.1), rgba(0, 217, 255, 0.1));
            border: 2px solid;
            border-image: linear-gradient(135deg, #FF006E, #00D9FF) 1;
            padding: 50px 40px;
            border-radius: 20px;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(255, 0, 110, 0.2), rgba(0, 217, 255, 0.2));
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: -1;
        }
        
        .feature-card:hover {
            transform: translateY(-15px);
            border-image: linear-gradient(135deg, #00D9FF, #FFD60A) 1;
            box-shadow: 0 20px 50px rgba(255, 0, 110, 0.2);
        }
        
        .feature-card:hover::before {
            opacity: 1;
        }
        
        .feature-icon {
            font-size: 48px;
            margin-bottom: 20px;
            animation: floatUp 3s ease-in-out infinite;
        }
        
        .feature-title {
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 15px;
            color: #FFD60A;
            letter-spacing: 1px;
        }
        
        .feature-desc {
            font-size: 15px;
            color: #b0b0b0;
            line-height: 1.8;
            font-weight: 300;
        }
        
        /* ❌ NÃO ALTERE: Showcase section - Container com cards de números */
        .showcase-section {
            padding: 120px 60px;
            background: linear-gradient(135deg, #0f3460 0%, #1a1a2e 50%, #16213e 100%);
            background-size: 400% 400%;
            animation: gradientShift 20s ease infinite;
        }
        
        .showcase-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .showcase-card {
            background: linear-gradient(135deg, rgba(255, 0, 110, 0.15), rgba(0, 217, 255, 0.15));
            border: 2px solid #FF006E;
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            transition: all 0.4s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        
        .showcase-card::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.5s ease;
        }
        
        .showcase-card:hover::after {
            left: 100%;
        }
        
        .showcase-card:hover {
            transform: translateY(-10px) scale(1.05);
            border-color: #00D9FF;
            box-shadow: 0 20px 50px rgba(0, 217, 255, 0.3);
        }
        
        .showcase-number {
            font-size: 48px;
            font-weight: 900;
            background: linear-gradient(135deg, #FF006E, #00D9FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
        }
        
        .showcase-label {
            font-size: 18px;
            font-weight: 700;
            color: #FFD60A;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* ❌ NÃO ALTERE: CTA final - Seção com fundo gradiente colorido */
        .cta-final-section {
            padding: 150px 60px;
            background: linear-gradient(135deg, #FF006E 0%, #FF4D6D 25%, #00D9FF 50%, #FFD60A 75%, #FF006E 100%);
            background-size: 400% 400%;
            animation: gradientShift 10s ease infinite;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .cta-final-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 15, 30, 0.3);
        }
        
        .cta-final-content {
            position: relative;
            z-index: 2;
        }
        
        /* ✅ ALTERE: Título final - Mude o texto "Pronto para Transformar?" */
        .cta-final-title {
            font-size: 56px;
            font-weight: 900;
            margin-bottom: 20px;
            color: white;
            letter-spacing: -1px;
        }
        
        /* ✅ ALTERE: Descrição final - Mude o texto descritivo */
        .cta-final-desc {
            font-size: 20px;
            margin-bottom: 50px;
            color: rgba(255, 255, 255, 0.95);
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            font-weight: 300;
        }
        
        /* ✅ ALTERE: Botão final - Mude cor, texto e tamanho */
        .cta-final-button {
            background: rgba(15, 15, 30, 0.9);
            color: #FFD60A;
            padding: 18px 60px;
            border: 3px solid #FFD60A;
            border-radius: 50px;
            font-weight: 800;
            font-size: 14px;
            text-decoration: none !important;
            transition: all 0.3s ease;
            cursor: pointer;
            display: inline-block;
            text-transform: uppercase;
            letter-spacing: 2px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        }
        
        .cta-final-button:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
            background: #FFD60A;
            color: #0f0f1e;
        }
        
        /* ❌ NÃO ALTERE: Footer - Rodapé com informações de contato */
        .footer {
            background: #0f0f1e;
            color: #888888;
            padding: 60px;
            text-align: center;
            border-top: 2px solid;
            border-image: linear-gradient(90deg, #FF006E, #00D9FF) 1;
        }
        
        /* ✅ ALTERE: Texto do footer - Mude email, telefone e endereço */
        .footer-text {
            font-size: 14px;
            margin-bottom: 10px;
            font-weight: 300;
        }
        
        /* ✅ ALTERE: Copyright - Mude o ano e nome da empresa */
        .footer-copyright {
            border-top: 1px solid rgba(255, 0, 110, 0.2);
            padding-top: 30px;
            margin-top: 30px;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* ❌ NÃO ALTERE: Responsividade - Ajusta layout para telas menores */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                gap: 20px;
                padding: 15px 20px;
            }
            
            .navbar-links {
                flex-direction: column;
                gap: 15px;
                width: 100%;
            }
            
            .hero-section {
                min-height: 500px;
            }
            
            .hero-title {
                font-size: 42px;
            }
            
            .hero-subtitle {
                font-size: 18px;
            }
            
            .hero-cta-group {
                flex-direction: column;
            }
            
            .features-section,
            .showcase-section,
            .cta-final-section {
                padding: 80px 20px;
            }
            
            .section-title {
                font-size: 36px;
            }
            
            .cta-final-title {
                font-size: 36px;
            }
        }
        
        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { 
            display: none;  /* Oculta o header */
        }
    </style>
    """

    # ❌ NÃO ALTERE: Injetar CSS na página - Aplica todos os estilos acima
    st.markdown(custom_css, unsafe_allow_html=True)

    # ==================== NAVBAR ====================
    # ✅ ALTERE: Navbar - Mude os textos dos links e URLs das seções
    navbar_html = '''<div class="navbar">
        <div class="navbar-logo">PREMIUM</div>
        <div class="navbar-links">
            <a href="#recursos" class="navbar-link">Recursos</a>
            <a href="#galeria" class="navbar-link">Galeria</a>
            <a href="#sobre" class="navbar-link">Sobre</a>
            <a href="#contato" class="navbar-link">Contato</a>
            <a href="https://www.google.com/" target="_blank" class="navbar-cta">Começar Agora</a>
        </div>
    </div>'''
    st.markdown(navbar_html, unsafe_allow_html=True)

    # ==================== HERO SECTION ====================
    # ✅ ALTERE: Hero - Mude os textos dos botões e URLs
    hero_html = '''<div class="hero-section" id="recursos">
        <div class="hero-content">
            <div class="hero-title">Experiência Absurda</div>
            <div class="hero-subtitle">Design que transforma, cores que inspiram</div>
            <div class="hero-cta-group">
                <a href="https://www.google.com/" target="_blank" class="hero-cta-primary">Explorar Agora</a>
                <a href="https://www.google.com/" target="_blank" class="hero-cta-secondary">Saiba Mais</a>
            </div>
        </div>
    </div>'''
    st.markdown(hero_html, unsafe_allow_html=True)

    # ==================== FEATURES SECTION ====================
    # ✅ ALTERE: Recursos - Mude os títulos, descrições e emojis dos cards
    features_html = '''<div class="features-section">
        <div class="section-header">
            <div class="section-title">Recursos Incríveis</div>
            <div class="section-description">Tudo que você precisa para impressionar seus clientes</div>
        </div>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">Ultra Rápido</div>
                <div class="feature-desc">Performance otimizada para a melhor experiência do usuário em qualquer dispositivo.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎨</div>
                <div class="feature-title">Design Moderno</div>
                <div class="feature-desc">Interface visual impressionante com animações suaves e cores dinâmicas.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔧</div>
                <div class="feature-title">Totalmente Customizável</div>
                <div class="feature-desc">Adapte cores, textos e conteúdo facilmente para seu negócio específico.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📱</div>
                <div class="feature-title">Responsivo</div>
                <div class="feature-desc">Funciona perfeitamente em desktop, tablet e mobile com experiência fluida.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🚀</div>
                <div class="feature-title">Conversão Máxima</div>
                <div class="feature-desc">Design estratégico focado em converter visitantes em clientes.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">✨</div>
                <div class="feature-title">Experiência Premium</div>
                <div class="feature-desc">Cada detalhe foi pensado para criar uma experiência memorável.</div>
            </div>
        </div>
    </div>'''
    st.markdown(features_html, unsafe_allow_html=True)

    # ==================== SHOWCASE SECTION ====================
    # ✅ ALTERE: Números - Mude os valores e labels dos cards
    showcase_html = '''<div class="showcase-section" id="galeria">
        <div class="section-header">
            <div class="section-title">Números que Falam</div>
            <div class="section-description">Resultados comprovados de padrões premium</div>
        </div>
        <div class="showcase-grid">
            <div class="showcase-card">
                <div class="showcase-number">300%</div>
                <div class="showcase-label">Mais Conversões</div>
            </div>
            <div class="showcase-card">
                <div class="showcase-number">50K+</div>
                <div class="showcase-label">Clientes Felizes</div>
            </div>
            <div class="showcase-card">
                <div class="showcase-number">99%</div>
                <div class="showcase-label">Satisfação</div>
            </div>
            <div class="showcase-card">
                <div class="showcase-number">24/7</div>
                <div class="showcase-label">Suporte</div>
            </div>
        </div>
    </div>'''
    st.markdown(showcase_html, unsafe_allow_html=True)

    # ==================== CTA FINAL ====================
    # ✅ ALTERE: CTA Final - Mude o texto e URL do botão
    cta_final_html = '''<div class="cta-final-section" id="sobre">
        <div class="cta-final-content">
            <div class="cta-final-title">Pronto para Transformar?</div>
            <div class="cta-final-desc">Junte-se a milhares de empresas que já estão usando padrões premium para crescer exponencialmente.</div>
            <a href="https://www.google.com/" target="_blank" class="cta-final-button">Começar Sua Jornada</a>
        </div>
    </div>'''
    st.markdown(cta_final_html, unsafe_allow_html=True)

    # ==================== FOOTER ====================
    # ✅ ALTERE: Footer - Mude email, telefone, endereço e copyright
    footer_html = '''<div class="footer" id="contato">
        <div class="footer-text">Email: contato@premium.com.br | Telefone: (99) 99999-9999</div>
        <div class="footer-text">Endereço: Av. Principal, 1000 - São Paulo, SP</div>
        <div class="footer-copyright">© 2025 Premium padrões. Todos os direitos reservados. Transformando negócios com design excepcional.</div>
    </div>'''
    st.markdown(footer_html, unsafe_allow_html=True)

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template3" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

