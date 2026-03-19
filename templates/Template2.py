import streamlit as st

def render():
    """Renderiza o template 2 - FitPro Academia"""
    
    # ✅ ALTERE: Configuração da página - Mude o título, ícone e nome conforme sua marca
    st.set_page_config(
        page_title="FitPro Academia - Transforme seu Corpo",  # ✅ Título que aparece na aba do navegador
        page_icon="💪",  # ✅ Ícone que aparece na aba do navegador
        layout="wide",  # ❌ Layout da página (não altere)
        initial_sidebar_state="collapsed"  # ❌ Estado inicial da barra lateral (não altere)
    )

    # ❌ NÃO ALTERE: CSS ULTRA PROFISSIONAL - Toda a estilização visual da página
    # Este bloco CSS é responsável por toda a aparência, cores, fontes, animações e responsividade
    custom_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700;800&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html, body, [data-testid="stAppViewContainer"] {
            background: #f5f5f5;
            font-family: 'Montserrat', sans-serif;
            color: #1a1a1a;
            line-height: 1.6;
        }
        
        [data-testid="stDecoration"] { display: none; }
        
        .main {
            padding: 0 !important;
            background: transparent;
            position: relative;
            z-index: 1;
        }
        
        /* NAVBAR - Barra de navegação no topo */
        .navbar {
            background: #ffffff;
            padding: 18px 60px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 3px solid #FF6B35;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }
        
        .navbar-logo {
            font-size: 26px;
            font-weight: 900;
            color: #1a1a1a;
            text-decoration: none;
            letter-spacing: -0.5px;
            font-family: 'Poppins', sans-serif;
        }
        
        .navbar-logo-highlight {
            color: #FF6B35;
        }
        
        .navbar-links {
            display: flex;
            gap: 50px;
            align-items: center;
        }
        
        .navbar-link {
            color: #1a1a1a;
            text-decoration: none !important;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s ease;
        }
        
        .navbar-link:visited {
            color: #1a1a1a !important;
        }
        
        .navbar-link:hover {
            color: #FF6B35;
        }
        
        .navbar-cta {
            background: #FF6B35;
            color: white;
            padding: 12px 32px;
            border-radius: 4px;
            text-decoration: none !important;
            font-weight: 700;
            font-size: 13px;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(255, 107, 53, 0.25);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .navbar-cta:hover {
            background: #E55A25;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(255, 107, 53, 0.35);
        }
        
        /* HERO SECTION - Seção principal com título grande */
        .hero-section {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            padding: 120px 60px;
            position: relative;
            overflow: hidden;
        }
        
        .hero-section::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 500px;
            height: 500px;
            background: linear-gradient(135deg, rgba(255, 107, 53, 0.15) 0%, transparent 70%);
            border-radius: 50%;
        }
        
        .hero-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
            position: relative;
            z-index: 2;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .hero-text h1 {
            font-size: 68px;
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 24px;
            color: #ffffff;
            letter-spacing: -1.5px;
            font-family: 'Poppins', sans-serif;
        }
        
        .hero-text h1 .highlight {
            color: #FF6B35;
        }
        
        .hero-text p {
            font-size: 18px;
            line-height: 1.8;
            margin-bottom: 40px;
            color: #e0e0e0;
            font-weight: 400;
        }
        
        .hero-stats {
            display: flex;
            gap: 50px;
            margin-bottom: 40px;
        }
        
        .hero-stat {
            border-left: 3px solid #FF6B35;
            padding-left: 20px;
        }
        
        .hero-stat-number {
            font-size: 36px;
            font-weight: 900;
            color: #FF6B35;
            margin-bottom: 4px;
        }
        
        .hero-stat-label {
            font-size: 13px;
            color: #b0b0b0;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .hero-image {
            background: linear-gradient(135deg, #FF6B35 0%, #FF8555 100%);
            height: 400px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 120px;
            color: rgba(255, 255, 255, 0.2);
        }
        
        .hero-cta {
            display: inline-block;
            background: #FF6B35;
            color: white;
            padding: 16px 48px;
            border-radius: 4px;
            font-weight: 700;
            font-size: 14px;
            text-decoration: none !important;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .hero-cta:hover {
            background: #E55A25;
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(255, 107, 53, 0.4);
        }
        
        /* SERVICES SECTION - Seção de serviços com cards */
        .services-section {
            padding: 100px 60px;
            background: #ffffff;
        }
        
        .section-header {
            text-align: center;
            margin-bottom: 80px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .section-title {
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 20px;
            color: #1a1a1a;
            letter-spacing: -0.5px;
            font-family: 'Poppins', sans-serif;
        }
        
        .section-title-highlight {
            color: #FF6B35;
        }
        
        .section-description {
            font-size: 16px;
            color: #666666;
            line-height: 1.7;
            font-weight: 400;
        }
        
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .service-card {
            background: linear-gradient(135deg, #f9f9f9 0%, #ffffff 100%);
            padding: 50px 40px;
            border-radius: 8px;
            border: 1px solid #e5e5e5;
            text-align: center;
            transition: all 0.4s ease;
            cursor: pointer;
            position: relative;
        }
        
        .service-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #FF6B35, #FF8555);
            border-radius: 8px 8px 0 0;
        }
        
        .service-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.1);
            border-color: #FF6B35;
        }
        
        .service-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #FF6B35, #FF8555);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 24px;
            font-size: 28px;
        }
        
        .service-title {
            font-size: 20px;
            font-weight: 800;
            margin-bottom: 12px;
            color: #1a1a1a;
            font-family: 'Poppins', sans-serif;
        }
        
        .service-desc {
            font-size: 14px;
            color: #666666;
            line-height: 1.7;
        }
        
        /* FEATURES SECTION - Seção de diferenciais */
        .features-section {
            padding: 100px 60px;
            background: linear-gradient(180deg, #f5f5f5 0%, #efefef 100%);
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .feature-box {
            background: white;
            padding: 40px;
            border-radius: 8px;
            border-left: 4px solid #FF6B35;
            transition: all 0.4s ease;
        }
        
        .feature-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
        }
        
        .feature-box h3 {
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 12px;
            color: #1a1a1a;
            font-family: 'Poppins', sans-serif;
        }
        
        .feature-box p {
            font-size: 14px;
            color: #666666;
            line-height: 1.7;
        }
        
        /* PRICING SECTION - Seção de planos e preços */
        .pricing-section {
            padding: 100px 60px;
            background: #ffffff;
        }
        
        .pricing-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .pricing-card {
            background: white;
            border: 2px solid #e5e5e5;
            border-radius: 8px;
            padding: 50px 40px;
            text-align: center;
            transition: all 0.4s ease;
            position: relative;
        }
        
        .pricing-card.featured {
            border-color: #FF6B35;
            transform: scale(1.05);
            box-shadow: 0 20px 40px rgba(255, 107, 53, 0.15);
        }
        
        .pricing-card:hover {
            border-color: #FF6B35;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.1);
        }
        
        .pricing-badge {
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            background: #FF6B35;
            color: white;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .pricing-title {
            font-size: 22px;
            font-weight: 800;
            margin-bottom: 16px;
            color: #1a1a1a;
            font-family: 'Poppins', sans-serif;
        }
        
        .pricing-price {
            font-size: 48px;
            font-weight: 900;
            color: #FF6B35;
            margin-bottom: 8px;
        }
        
        .pricing-period {
            font-size: 13px;
            color: #999999;
            margin-bottom: 30px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .pricing-features {
            text-align: left;
            margin-bottom: 30px;
            border-top: 1px solid #e5e5e5;
            border-bottom: 1px solid #e5e5e5;
            padding: 30px 0;
        }
        
        .pricing-feature {
            font-size: 14px;
            color: #666666;
            margin-bottom: 12px;
            padding-left: 24px;
            position: relative;
        }
        
        .pricing-feature::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: #FF6B35;
            font-weight: 900;
        }
        
        .pricing-cta {
            background: #FF6B35;
            color: white;
            padding: 14px 40px;
            border-radius: 4px;
            font-weight: 700;
            font-size: 13px;
            text-decoration: none !important;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            width: 100%;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .pricing-cta:hover {
            background: #E55A25;
            transform: translateY(-2px);
        }
        
        .pricing-card.featured .pricing-cta {
            background: #FF6B35;
        }
        
        /* TESTIMONIALS SECTION - Seção de depoimentos */
        .testimonials-section {
            padding: 100px 60px;
            background: linear-gradient(180deg, #f5f5f5 0%, #efefef 100%);
        }
        
        .testimonial-card {
            background: white;
            padding: 40px;
            border-radius: 8px;
            border-left: 4px solid #FF6B35;
            margin-bottom: 30px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .testimonial-text {
            font-size: 16px;
            color: #1a1a1a;
            line-height: 1.8;
            margin-bottom: 20px;
        }
        
        .testimonial-author {
            font-size: 14px;
            font-weight: 700;
            color: #1a1a1a;
        }
        
        .testimonial-role {
            font-size: 13px;
            color: #999999;
            font-weight: 500;
        }
        
        /* CTA FINAL SECTION - Seção de chamada para ação final */
        .cta-final-section {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            color: white;
            padding: 100px 60px;
            text-align: center;
        }
        
        .cta-final-title {
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 20px;
            letter-spacing: -0.5px;
            font-family: 'Poppins', sans-serif;
        }
        
        .cta-final-title .highlight {
            color: #FF6B35;
        }
        
        .cta-final-desc {
            font-size: 18px;
            margin-bottom: 50px;
            opacity: 0.9;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .cta-final-button {
            background: #FF6B35;
            color: white;
            padding: 16px 48px;
            border-radius: 4px;
            font-weight: 700;
            font-size: 14px;
            text-decoration: none !important;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            display: inline-block;
            box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .cta-final-button:hover {
            background: #E55A25;
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(255, 107, 53, 0.4);
        }
        
        /* FOOTER - Rodapé da página */
        .footer {
            background: #000000;
            color: rgba(255, 255, 255, 0.7);
            padding: 60px;
            text-align: center;
        }
        
        .footer-text {
            font-size: 14px;
            margin-bottom: 10px;
        }
        
        .footer-copyright {
            border-top: 1px solid rgba(255, 107, 53, 0.2);
            padding-top: 30px;
            margin-top: 30px;
            font-size: 12px;
        }
        
        /* RESPONSIVIDADE - Adaptação para celulares e tablets */
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
            
            .hero-content {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            
            .hero-text h1 {
                font-size: 36px;
            }
            
            .hero-stats {
                flex-direction: column;
                gap: 30px;
            }
            
            .services-section,
            .features-section,
            .pricing-section,
            .testimonials-section,
            .cta-final-section {
                padding: 60px 20px;
            }
            
            .section-title {
                font-size: 32px;
            }
            
            .cta-final-title {
                font-size: 32px;
            }
            
            .pricing-card.featured {
                transform: scale(1);
            }
        }
        
        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { 
            display: none;  /* Oculta o header */
        }
    </style>
    """

    # ❌ NÃO ALTERE: Injetar CSS na página
    # Esta linha aplica todo o CSS customizado ao Streamlit
    st.markdown(custom_css, unsafe_allow_html=True)

    # ==================== NAVBAR ====================
    # ✅ ALTERE: Navbar - Mude os textos dos links e URLs
    # Esta é a barra de navegação que aparece no topo da página
    navbar_html = '<div class="navbar"><a href="#" class="navbar-logo">FIT<span class="navbar-logo-highlight">PRO</span></a><div class="navbar-links"><a href="#recursos" class="navbar-link">Recursos</a><a href="#galeria" class="navbar-link">Galeria</a><a href="#sobre" class="navbar-link">Sobre</a><a href="#contato" class="navbar-link">Contato</a><a href="https://www.google.com/" target="_blank" class="navbar-cta">Começar Agora</a></div></div>'
    st.markdown(navbar_html, unsafe_allow_html=True)

    # ==================== HERO SECTION ====================
    # ✅ ALTERE: Hero Section - Mude o título, descrição, números e URL do botão
    # Esta é a seção principal com o título grande e chamada para ação
    hero_html = '''<div class="hero-section">
        <div class="hero-content">
            <div class="hero-text">
                <h1>Transforme seu <span class="highlight">corpo</span> e mente</h1>
                <p>Programas personalizados, treinadores experientes e ambiente de primeira qualidade. Alcance seus objetivos conosco.</p>
                <div class="hero-stats">
                    <div class="hero-stat">
                        <div class="hero-stat-number">5.000+</div>
                        <div class="hero-stat-label">Alunos Ativos</div>
                    </div>
                    <div class="hero-stat">
                        <div class="hero-stat-number">15+</div>
                        <div class="hero-stat-label">Anos de Experiência</div>
                    </div>
                </div>
                <a href="https://www.google.com/" target="_blank" class="hero-cta">Agende uma Avaliação Gratuita</a>
            </div>
            <div class="hero-image">🏋️‍♂️</div>
        </div>
    </div>'''
    st.markdown(hero_html, unsafe_allow_html=True)

    # ==================== SERVICES SECTION ====================
    # ✅ ALTERE: Services Section - Mude os títulos, descrições, emojis e adicione/remova cards
    # Esta seção mostra os serviços oferecidos em cards com ícones
    services_html = '''<div class="services-section" id="recursos">
        <div class="section-header">
            <div class="section-title">Nossos <span class="section-title-highlight">Serviços</span></div>
            <div class="section-description">Oferecemos uma variedade de programas e serviços para atender todos os seus objetivos fitness</div>
        </div>
        <div class="services-grid">
            <div class="service-card">
                <div class="service-icon">🏋️</div>
                <div class="service-title">Musculação</div>
                <div class="service-desc">Programas de treinamento com pesos para ganho de massa e força muscular.</div>
            </div>
            <div class="service-card">
                <div class="service-icon">🏃</div>
                <div class="service-title">Cardio</div>
                <div class="service-desc">Equipamentos modernos para treinos cardiovasculares de alta performance.</div>
            </div>
            <div class="service-card">
                <div class="service-icon">🧘</div>
                <div class="service-title">Yoga e Pilates</div>
                <div class="service-desc">Aulas de flexibilidade, equilíbrio e bem-estar mental.</div>
            </div>
            <div class="service-card">
                <div class="service-icon">👨‍🏫</div>
                <div class="service-title">Personal Training</div>
                <div class="service-desc">Acompanhamento individual com treinadores certificados.</div>
            </div>
            <div class="service-card">
                <div class="service-icon">🥗</div>
                <div class="service-title">Nutrição</div>
                <div class="service-desc">Orientação nutricional personalizada para seus objetivos.</div>
            </div>
            <div class="service-card">
                <div class="service-icon">💪</div>
                <div class="service-title">Grupos Funcionais</div>
                <div class="service-desc">Treinos em grupo para motivação e diversão.</div>
            </div>
        </div>
    </div>'''
    st.markdown(services_html, unsafe_allow_html=True)

    # ==================== FEATURES SECTION ====================
    # ✅ ALTERE: Features Section - Mude os títulos e descrições dos diferenciais
    # Esta seção destaca os pontos fortes e diferenciais da academia
    features_html = '''<div class="features-section" id="galeria">
        <div class="section-header">
            <div class="section-title">Por que escolher a <span class="section-title-highlight">FitPro</span></div>
            <div class="section-description">Diferenciais que fazem a diferença na sua jornada fitness</div>
        </div>
        <div class="features-grid">
            <div class="feature-box">
                <h3>Equipamentos Modernos</h3>
                <p>Máquinas de última geração importadas, sempre mantidas em perfeito funcionamento.</p>
            </div>
            <div class="feature-box">
                <h3>Treinadores Certificados</h3>
                <p>Profissionais qualificados e experientes para orientar seu treino.</p>
            </div>
            <div class="feature-box">
                <h3>Ambiente Acolhedor</h3>
                <p>Espaço limpo, climatizado e seguro para você treinar com conforto.</p>
            </div>
            <div class="feature-box">
                <h3>Horários Flexíveis</h3>
                <p>Aberto de segunda a domingo, com horários que se adaptam à sua rotina.</p>
            </div>
            <div class="feature-box">
                <h3>Comunidade Ativa</h3>
                <p>Faça parte de uma comunidade motivada e comprometida com resultados.</p>
            </div>
            <div class="feature-box">
                <h3>Acompanhamento Contínuo</h3>
                <p>Avaliações periódicas para acompanhar sua evolução e ajustar treinos.</p>
            </div>
        </div>
    </div>'''
    st.markdown(features_html, unsafe_allow_html=True)

    # ==================== PRICING SECTION ====================
    # ✅ ALTERE: Pricing Section - Mude os nomes dos planos, preços, features e URLs dos botões
    # Esta seção mostra os planos de preços disponíveis
    pricing_html = '''<div class="pricing-section" id="sobre">
        <div class="section-header">
            <div class="section-title">Planos e <span class="section-title-highlight">Preços</span></div>
            <div class="section-description">Escolha o plano que melhor se adequa aos seus objetivos</div>
        </div>
        <div class="pricing-grid">
            <div class="pricing-card">
                <div class="pricing-title">Básico</div>
                <div class="pricing-price">R$ 99</div>
                <div class="pricing-period">Por mês</div>
                <div class="pricing-features">
                    <div class="pricing-feature">Acesso à academia</div>
                    <div class="pricing-feature">Uso de todos os equipamentos</div>
                    <div class="pricing-feature">Vestiário e chuveiro</div>
                </div>
                <a href="https://www.google.com/" target="_blank" class="pricing-cta">Escolher Plano</a>
            </div>
            <div class="pricing-card featured">
                <div class="pricing-badge">Mais Popular</div>
                <div class="pricing-title">Premium</div>
                <div class="pricing-price">R$ 199</div>
                <div class="pricing-period">Por mês</div>
                <div class="pricing-features">
                    <div class="pricing-feature">Acesso à academia</div>
                    <div class="pricing-feature">Aulas em grupo ilimitadas</div>
                    <div class="pricing-feature">2 sessões personal/mês</div>
                    <div class="pricing-feature">Avaliação física mensal</div>
                </div>
                <a href="https://www.google.com/" target="_blank" class="pricing-cta">Escolher Plano</a>
            </div>
            <div class="pricing-card">
                <div class="pricing-title">Elite</div>
                <div class="pricing-price">R$ 399</div>
                <div class="pricing-period">Por mês</div>
                <div class="pricing-features">
                    <div class="pricing-feature">Acesso 24/7</div>
                    <div class="pricing-feature">Personal training ilimitado</div>
                    <div class="pricing-feature">Aulas em grupo ilimitadas</div>
                    <div class="pricing-feature">Suplementos com desconto</div>
                </div>
                <a href="https://www.google.com/" target="_blank" class="pricing-cta">Escolher Plano</a>
            </div>
        </div>
    </div>'''
    st.markdown(pricing_html, unsafe_allow_html=True)

    # ==================== TESTIMONIALS SECTION ====================
    # ✅ ALTERE: Testimonials Section - Mude os depoimentos, nomes e funções dos clientes
    # Esta seção mostra histórias de sucesso de clientes
    testimonials_html = '''<div class="testimonials-section">
        <div class="section-header">
            <div class="section-title">Histórias de <span class="section-title-highlight">Sucesso</span></div>
            <div class="section-description">Veja como nossos alunos transformaram suas vidas</div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">"Entrei na FitPro sem conhecimento nenhum sobre treino. Os profissionais me orientaram perfeitamente e em 6 meses consegui resultados incríveis. Recomendo muito!"</div>
            <div class="testimonial-author">Roberto Silva</div>
            <div class="testimonial-role">Aluno há 2 anos</div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">"O ambiente é acolhedor, os treinadores são atenciosos e os resultados falam por si. Já perdi 20kg e ganhei muita confiança. Melhor decisão que tomei!"</div>
            <div class="testimonial-author">Juliana Costa</div>
            <div class="testimonial-role">Aluna Premium</div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">"A comunidade da FitPro é incrível. Tenho amigos, motivação e profissionais que realmente se importam com meu progresso. Voltaria mil vezes!"</div>
            <div class="testimonial-author">Marcus Oliveira</div>
            <div class="testimonial-role">Aluno Elite</div>
        </div>
    </div>'''
    st.markdown(testimonials_html, unsafe_allow_html=True)

    # ==================== CTA FINAL SECTION ====================
    # ✅ ALTERE: CTA Final Section - Mude o título, descrição e URL do botão
    # Esta é a seção final de chamada para ação antes do rodapé
    cta_final_html = '''<div class="cta-final-section" id="contato">
        <div class="cta-final-title">Comece sua transformação <span class="highlight">hoje</span></div>
        <div class="cta-final-desc">Agende uma avaliação gratuita e conheça nossas instalações. Nossos profissionais estão prontos para ajudá-lo!</div>
        <a href="https://www.google.com/" target="_blank" class="cta-final-button">Agende Sua Avaliação</a>
    </div>'''
    st.markdown(cta_final_html, unsafe_allow_html=True)

    # ==================== FOOTER ====================
    # ✅ ALTERE: Footer - Mude o telefone, email, endereço e copyright
    # Esta é a seção do rodapé com informações de contato
    footer_html = '<div class="footer"><div class="footer-text">Telefone: (99) 99999-9999 | Email: contato@fitpro.com.br</div><div class="footer-text">Endereço: Av. Principal, 1234 - São Paulo, SP</div><div class="footer-copyright">© 2025 FitPro Academia. Todos os direitos reservados. Transformando vidas através do fitness.</div></div>'
    st.markdown(footer_html, unsafe_allow_html=True)

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template2" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)
