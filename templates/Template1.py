import streamlit as st

def render():
    """Renderiza o template 1 - Agência Digital"""
    
    # ✅ ALTERE: Configuração da página - Mude o título, ícone e nome conforme sua marca
    st.set_page_config(
        page_title="Agência Digital - Transforme seu Negócio",  # ✅ ALTERE: Título que aparece na aba do navegador
        page_icon="🚀",  # ✅ ALTERE: Ícone que aparece na aba do navegador
        layout="wide",  # ❌ NÃO ALTERE: Define o layout da página em modo wide
        initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Esconde a barra lateral do Streamlit
    )

    # ❌ NÃO ALTERE: CSS ULTRA PROFISSIONAL - Responsável por todo o visual da página
    custom_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(180deg, #f8f9ff 0%, #f0f4ff 50%, #f8f9ff 100%);
            background-attachment: fixed;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            color: #1a1a1a;
            line-height: 1.6;
        }
        
        html::before, body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 50%, rgba(0, 102, 255, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(0, 102, 255, 0.05) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }
        
        [data-testid="stDecoration"] { display: none; }
        
        .main {
            padding: 0 !important;
            background: transparent;
            position: relative;
            z-index: 1;
        }
        
        /* ❌ NÃO ALTERE: NAVBAR - Barra de navegação no topo da página */
        .navbar {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 16px 60px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(0, 102, 255, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0, 102, 255, 0.08);
        }
        
        /* ✅ ALTERE: Logo da navbar - Mude o texto e cor conforme sua marca */
        .navbar-logo {
            font-size: 24px;
            font-weight: 900;
            text-decoration: none;
            letter-spacing: -0.5px;
        }
        
        /* ❌ NÃO ALTERE: Container dos links da navbar */
        .navbar-links {
            display: flex;
            gap: 50px;
            align-items: center;
        }
        
        /* ❌ NÃO ALTERE: Estilo dos links da navbar com underline animado */
        .navbar-link {
            color: #1a1a1a;
            text-decoration: none !important;
            font-weight: 500;
            font-size: 15px;
            transition: all 0.3s ease;
            position: relative;
            cursor: pointer;
        }
        
        /* ❌ NÃO ALTERE: Efeito hover dos links - Underline animado */
        .navbar-link::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: #0066FF;
            transition: width 0.3s ease;
        }
        
        .navbar-link:hover::after {
            width: 100%;
        }
        
        .navbar-link:hover {
            color: #0066FF;
        }
        
        /* ✅ ALTERE: Botão CTA da navbar - Mude o texto e URL */
        .navbar-cta {
            background: linear-gradient(90deg, #0066FF, #0052CC);
            color: white !important;
            padding: 10px 28px;
            border-radius: 8px;
            text-decoration: none !important;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0, 102, 255, 0.2);
            display: inline-block;
        }
        
        .navbar-cta:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 102, 255, 0.3);
        }
        
        /* ❌ NÃO ALTERE: HERO SECTION - Seção principal de apresentação */
        .hero-section {
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.8) 0%, rgba(248, 249, 255, 0.6) 100%);
            backdrop-filter: blur(10px);
            padding: 120px 60px;
            text-align: center;
            position: relative;
            overflow: hidden;
            border-bottom: 1px solid rgba(0, 102, 255, 0.1);
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(0, 102, 255, 0.08) 0%, transparent 70%);
            border-radius: 50%;
        }
        
        .hero-section::after {
            content: '';
            position: absolute;
            bottom: -30%;
            left: -10%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(0, 102, 255, 0.05) 0%, transparent 70%);
            border-radius: 50%;
        }
        
        .hero-content {
            position: relative;
            z-index: 2;
            max-width: 900px;
            margin: 0 auto;
        }
        
        /* ✅ ALTERE: Título principal do hero - Mude o texto conforme sua marca */
        .hero-title {
            font-size: 64px;
            font-weight: 900;
            line-height: 1.15;
            margin-bottom: 24px;
            color: #1a1a1a;
            letter-spacing: -1px;
        }
        
        /* ✅ ALTERE: Parte destacada do título - Mude a cor conforme sua marca */
        .hero-title-highlight {
            color: #0066FF;
        }
        
        /* ✅ ALTERE: Subtítulo do hero - Mude o texto conforme sua marca */
        .hero-subtitle {
            font-size: 20px;
            line-height: 1.6;
            margin-bottom: 50px;
            color: #666666;
            font-weight: 400;
        }
        
        /* ❌ NÃO ALTERE: Container das estatísticas do hero */
        .hero-stats {
            display: flex;
            justify-content: center;
            gap: 80px;
            margin-top: 60px;
            padding-top: 60px;
            border-top: 1px solid #e0e0e0;
        }
        
        .hero-stat {
            text-align: center;
        }
        
        /* ✅ ALTERE: Números das estatísticas - Mude os números conforme seus dados */
        .hero-stat-number {
            font-size: 36px;
            font-weight: 900;
            color: #0066FF;
            margin-bottom: 8px;
        }
        
        /* ✅ ALTERE: Labels das estatísticas - Mude os textos conforme seus dados */
        .hero-stat-label {
            font-size: 14px;
            color: #666666;
            font-weight: 500;
        }
        
        /* ❌ NÃO ALTERE: BADGES - Pequenos rótulos de destaque */
        .badges-container {
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 30px;
        }
        
        .badge {
            background: #f0f0f0;
            color: #1a1a1a;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        
        .badge-icon {
            font-size: 14px;
        }
        
        .badge-primary {
            background: #0066FF;
            color: white;
        }
        
        .badge-success {
            background: #00AA44;
            color: white;
        }
        
        .badge-warning {
            background: #FF6600;
            color: white;
        }
        
        /* ❌ NÃO ALTERE: BUTTONS - Botões de ação */
        .cta-button {
            display: inline-block;
            background: linear-gradient(135deg, #0066FF, #0052CC);
            color: white !important;
            padding: 16px 48px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 16px;
            text-decoration: none !important;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0, 102, 255, 0.25);
            margin-right: 20px;
            margin-bottom: 20px;
        }
        
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(0, 102, 255, 0.35);
        }
        
        .cta-button-secondary {
            background: white;
            color: #0066FF !important;
            border: 2px solid #0066FF;
            box-shadow: none;
        }
        
        .cta-button-secondary:visited {
            color: #0066FF !important;
        }
        
        .cta-button-secondary:hover {
            background: #f0f6ff;
        }
        
        /* ❌ NÃO ALTERE: FEATURES SECTION - Seção de características */
        .features-section {
            padding: 100px 60px;
            background: linear-gradient(180deg, rgba(255, 255, 255, 0.7) 0%, rgba(248, 249, 255, 0.5) 100%);
            backdrop-filter: blur(5px);
        }
        
        .section-header {
            text-align: center;
            margin-bottom: 80px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }
        
        /* ✅ ALTERE: Título das seções - Mude o texto conforme sua marca */
        .section-title {
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 20px;
            color: #1a1a1a;
        }
        
        /* ✅ ALTERE: Parte destacada do título da seção */
        .section-title-highlight {
            color: #0066FF;
        }
        
        /* ✅ ALTERE: Descrição da seção - Mude o texto conforme sua marca */
        .section-description {
            font-size: 18px;
            color: #666666;
            line-height: 1.6;
        }
        
        /* ❌ NÃO ALTERE: Grid de features */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
        }
        
        /* ❌ NÃO ALTERE: Card de feature */
        .feature-card {
            background: white;
            padding: 40px 30px;
            border-radius: 12px;
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid rgba(0, 102, 255, 0.1);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        
        .feature-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 24px rgba(0, 102, 255, 0.15);
            border-color: rgba(0, 102, 255, 0.3);
        }
        
        /* ✅ ALTERE: Ícone da feature */
        .feature-icon {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        /* ✅ ALTERE: Título da feature */
        .feature-title {
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 15px;
            color: #1a1a1a;
        }
        
        /* ✅ ALTERE: Descrição da feature */
        .feature-description {
            font-size: 15px;
            color: #666666;
            line-height: 1.6;
        }
        
        /* ❌ NÃO ALTERE: CTA SECTION - Seção de chamada para ação */
        .cta-section {
            background: linear-gradient(135deg, #0066FF, #0052CC);
            color: white;
            padding: 100px 60px;
            text-align: center;
        }
        
        .cta-section h2 {
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 20px;
        }
        
        .cta-section p {
            font-size: 18px;
            margin-bottom: 40px;
            opacity: 0.9;
        }
        
        /* ❌ NÃO ALTERE: FOOTER - Rodapé da página */
        .footer {
            background: #1a1a1a;
            color: white;
            padding: 60px;
            text-align: center;
        }
        
        .footer p {
            font-size: 14px;
            color: #999999;
        }
        
        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { 
            display: none;
        }
        
        /* ❌ NÃO ALTERE: Esconde o ícone do GitHub do Streamlit */
        [data-testid="stToolbarActions"] { display: none; }
    </style>
    """

    st.markdown(custom_css, unsafe_allow_html=True)

    # ❌ NÃO ALTERE: NAVBAR HTML
    navbar_html = """
    <div class="navbar">
        <div class="navbar-logo">🚀 AGÊNCIA</div>
        <div class="navbar-links">
            <a href="#features" class="navbar-link">Serviços</a>
            <a href="#cta" class="navbar-link">Sobre</a>
            <a href="#footer" class="navbar-link">Contato</a>
            <a href="https://www.google.com/" class="navbar-cta">Começar</a>
        </div>
    </div>
    """
    st.markdown(navbar_html, unsafe_allow_html=True)

    # ❌ NÃO ALTERE: HERO SECTION HTML
    hero_html = """
    <div class="hero-section">
        <div class="hero-content">
            <div class="badges-container">
                <span class="badge badge-primary">✨ Novo</span>
                <span class="badge">Transformação Digital</span>
                <span class="badge badge-success">⭐ Top Rated</span>
            </div>
            <h1 class="hero-title">
                Transforme seu Negócio com <span class="hero-title-highlight">Estratégia Digital</span>
            </h1>
            <p class="hero-subtitle">
                Soluções completas de marketing digital que aumentam suas vendas e presença online
            </p>
            <div style="margin-bottom: 60px;">
                <a href="https://www.google.com/" class="cta-button">Solicitar Consultoria</a>
                <a href="https://www.google.com/" class="cta-button cta-button-secondary">Ver Portfólio</a>
            </div>
            <div class="hero-stats">
                <div class="hero-stat">
                    <div class="hero-stat-number">500+</div>
                    <div class="hero-stat-label">Clientes Satisfeitos</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-number">10+</div>
                    <div class="hero-stat-label">Anos de Experiência</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-number">300%</div>
                    <div class="hero-stat-label">Crescimento Médio</div>
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

    # ❌ NÃO ALTERE: FEATURES SECTION HTML
    features_html = """
    <div id="features" class="features-section">
        <div class="section-header">
            <h2 class="section-title">Nossos <span class="section-title-highlight">Serviços</span></h2>
            <p class="section-description">
                Oferecemos soluções completas de marketing digital para impulsionar seu negócio
            </p>
        </div>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">📱</div>
                <h3 class="feature-title">Social Media</h3>
                <p class="feature-description">Gerenciamento completo de suas redes sociais com estratégia de conteúdo</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3 class="feature-title">Publicidade Digital</h3>
                <p class="feature-description">Campanhas otimizadas em Google Ads e Facebook para máximo ROI</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 class="feature-title">Análise de Dados</h3>
                <p class="feature-description">Relatórios detalhados e insights para melhorar seu desempenho</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🌐</div>
                <h3 class="feature-title">SEO & Conteúdo</h3>
                <p class="feature-description">Otimização para buscas e criação de conteúdo de alta qualidade</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">💻</div>
                <h3 class="feature-title">Web Design</h3>
                <p class="feature-description">Websites modernos e responsivos que convertem visitantes em clientes</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📧</div>
                <h3 class="feature-title">Email Marketing</h3>
                <p class="feature-description">Campanhas de email personalizadas que geram resultados</p>
            </div>
        </div>
    </div>
    """
    st.markdown(features_html, unsafe_allow_html=True)

    # ❌ NÃO ALTERE: CTA SECTION HTML
    cta_html = """
    <div id="cta" class="cta-section">
        <h2>Pronto para Transformar seu Negócio?</h2>
        <p>Agende uma consultoria gratuita com nossos especialistas</p>
        <a href="https://www.google.com/" class="cta-button cta-button-secondary" style="padding: 16px 48px;">Agendar Agora</a>
    </div>
    """
    st.markdown(cta_html, unsafe_allow_html=True)

    # ❌ NÃO ALTERE: FOOTER HTML
    footer_html = """
    <div id="footer" class="footer">
        <p>&copy; 2026 Agência Digital. Todos os direitos reservados.</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 50px 0 40px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template1" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)
