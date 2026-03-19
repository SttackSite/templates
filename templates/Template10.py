import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

def render():
    """Renderiza o template 10 - GetResponse Style"""
    
    # ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
    # ❌ NÃO ALTERE: Define as configurações básicas da página
    st.set_page_config(
        page_title="GetResponse Style - Email Marketing",  # ✅ ALTERE: Título que aparece na aba do navegador
        page_icon="📧",  # ✅ ALTERE: Emoji que aparece na aba do navegador
        layout="wide",  # ❌ NÃO ALTERE: Define o layout como largura total
        initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Oculta a barra lateral
    )

    # ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
    # ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
    # Alterar aqui pode quebrar completamente o design da página
    custom_css = """
    <style>
        /* ❌ NÃO ALTERE: Importa as fontes do Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Poppins:wght@400;500;600;700;800&display=swap');
        
        /* ❌ NÃO ALTERE: Reset de estilos padrão */
        * {
            margin: 0;  /* Remove margem padrão */
            padding: 0;  /* Remove preenchimento padrão */
            box-sizing: border-box;  /* Inclui borda no tamanho total */
        }
        
        /* ❌ NÃO ALTERE: Estilos globais */
        html, body, [data-testid="stAppViewContainer"] {
            background: #ffffff;  /* Fundo branco */
            font-family: 'Montserrat', sans-serif;  /* Fonte padrão */
            color: #1a1a1a;  /* Cor de texto padrão */
            overflow-x: hidden;  /* Oculta scroll horizontal */
        }
        
        /* ❌ NÃO ALTERE: Remove decorações do Streamlit */
        [data-testid="stDecoration"] { display: none; }
        .main { padding: 0 !important; background: transparent; }
        
        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { 
            display: none;  /* Oculta o header */
        }
        
        /* ❌ NÃO ALTERE: Animações */
        @keyframes slideInLeft {
            0% { transform: translateX(-100px); opacity: 0; }  /* Começa fora da tela à esquerda */
            100% { transform: translateX(0); opacity: 1; }  /* Termina na posição normal */
        }
        
        @keyframes slideInRight {
            0% { transform: translateX(100px); opacity: 0; }  /* Começa fora da tela à direita */
            100% { transform: translateX(0); opacity: 1; }  /* Termina na posição normal */
        }
        
        @keyframes fadeInUp {
            0% { transform: translateY(40px); opacity: 0; }  /* Começa abaixo com opacidade 0 */
            100% { transform: translateY(0); opacity: 1; }  /* Termina na posição normal */
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }  /* Tamanho normal */
            50% { transform: scale(1.05); }  /* Aumenta 5% no meio */
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }  /* Posição normal */
            50% { transform: translateY(-20px); }  /* Sobe 20px no meio */
        }
        
        /* ❌ NÃO ALTERE: Navbar */
        .navbar {
            background: #ffffff;  /* Fundo branco */
            padding: 20px 80px;  /* Espaçamento interno */
            display: flex;  /* Layout flexível */
            justify-content: space-between;  /* Espaça itens nas extremidades */
            align-items: center;  /* Alinha itens no centro */
            border-bottom: 1px solid #e0e0e0;  /* Borda inferior cinza clara */
            position: sticky;  /* Fica fixo ao scroll */
            top: 0;  /* No topo */
            z-index: 100;  /* Acima de outros elementos */
        }
        
        /* ❌ NÃO ALTERE: Logo da navbar */
        .navbar-logo {
            font-size: 20px;  /* Tamanho grande */
            font-weight: 800;  /* Peso muito pesado */
            color: #0066FF;  /* Azul */
            letter-spacing: 1px;  /* Espaçamento entre letras */
            font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
        }
        
        /* ❌ NÃO ALTERE: Menu de navegação */
        .navbar-nav {
            display: flex;  /* Layout flexível */
            gap: 50px;  /* Espaçamento entre itens */
        }
        
        /* ❌ NÃO ALTERE: Links do menu */
        .nav-link {
            color: #1a1a1a;  /* Cor cinza escuro */
            text-decoration: none;  /* Remove sublinhado */
            font-size: 13px;  /* Tamanho pequeno */
            font-weight: 600;  /* Peso pesado */
            text-transform: capitalize;  /* Primeira letra maiúscula */
            transition: all 0.3s ease;  /* Animação suave */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos links */
        .nav-link:hover { color: #0066FF; }  /* Fica azul ao passar o mouse */
        
        /* ❌ NÃO ALTERE: CTA da navbar */
        .navbar-cta {
            display: flex;  /* Layout flexível */
            gap: 20px;  /* Espaçamento entre itens */
            align-items: center;  /* Alinha itens no centro */
        }
        
        /* ❌ NÃO ALTERE: Link de login */
        .nav-login {
            color: #1a1a1a;  /* Cor cinza escuro */
            text-decoration: none;  /* Remove sublinhado */
            font-size: 13px;  /* Tamanho pequeno */
            font-weight: 600;  /* Peso pesado */
        }
        
        /* ❌ NÃO ALTERE: Botão da navbar */
        .nav-btn {
            background: #0066FF;  /* Fundo azul */
            color: #ffffff;  /* Texto branco */
            padding: 12px 30px;  /* Espaçamento interno */
            border: none;  /* Sem borda */
            border-radius: 4px;  /* Arredondamento suave */
            font-weight: 700;  /* Peso pesado */
            font-size: 12px;  /* Tamanho pequeno */
            cursor: pointer;  /* Cursor de clique */
            transition: all 0.3s ease;  /* Animação suave */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover no botão da navbar */
        .nav-btn:hover {
            background: #0052CC;  /* Azul mais escuro */
        }
        
        /* ❌ NÃO ALTERE: Seção hero */
        .hero {
            background: linear-gradient(135deg, #0066FF 0%, #0052CC 100%);  /* Gradiente azul */
            color: #ffffff;  /* Texto branco */
            padding: 120px 80px;  /* Espaçamento interno */
            min-height: 100vh;  /* Altura mínima da tela */
            display: flex;  /* Layout flexível */
            align-items: center;  /* Alinha itens no centro */
            justify-content: space-between;  /* Espaça itens nas extremidades */
            position: relative;  /* Posicionamento relativo */
            overflow: hidden;  /* Oculta conteúdo que sai da área */
        }
        
        /* ❌ NÃO ALTERE: Efeito de fundo do hero */
        .hero::before {
            content: '';  /* Cria elemento vazio */
            position: absolute;  /* Posicionamento absoluto */
            width: 600px;  /* Largura */
            height: 600px;  /* Altura */
            background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);  /* Gradiente radial */
            border-radius: 50%;  /* Círculo */
            top: -200px;  /* Posição no topo */
            right: -200px;  /* Posição à direita */
        }
        
        /* ❌ NÃO ALTERE: Conteúdo do hero */
        .hero-content {
            max-width: 700px;  /* Largura máxima */
            position: relative;  /* Posicionamento relativo */
            z-index: 2;  /* Acima do efeito de fundo */
            animation: slideInLeft 0.8s ease-out;  /* Animação de entrada */
        }
        
        /* ❌ NÃO ALTERE: Label do hero */
        .hero-label {
            font-size: 13px;  /* Tamanho pequeno */
            color: rgba(255, 255, 255, 0.9);  /* Branco semi-transparente */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 2px;  /* Espaçamento entre letras */
            margin-bottom: 20px;  /* Espaçamento inferior */
            font-weight: 600;  /* Peso pesado */
        }
        
        /* ❌ NÃO ALTERE: Título do hero */
        .hero-title {
            font-size: 72px;  /* Tamanho muito grande */
            font-weight: 900;  /* Peso extremamente pesado */
            line-height: 1.1;  /* Altura da linha compacta */
            margin-bottom: 30px;  /* Espaçamento inferior */
            color: #ffffff;  /* Texto branco */
            font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
            letter-spacing: -1px;  /* Espaçamento negativo entre letras */
        }
        
        /* ❌ NÃO ALTERE: Descrição do hero */
        .hero-desc {
            font-size: 18px;  /* Tamanho médio */
            color: rgba(255, 255, 255, 0.95);  /* Branco semi-transparente */
            margin-bottom: 50px;  /* Espaçamento inferior */
            line-height: 1.8;  /* Altura da linha generosa */
            font-weight: 400;  /* Peso normal */
        }
        
        /* ❌ NÃO ALTERE: CTA do hero */
        .hero-cta {
            display: flex;  /* Layout flexível */
            gap: 20px;  /* Espaçamento entre itens */
            flex-wrap: wrap;  /* Quebra em múltiplas linhas */
        }
        
        /* ❌ NÃO ALTERE: Botão primário */
        .btn-primary {
            background: #FFD60A;  /* Fundo amarelo */
            color: #1a1a1a;  /* Texto cinza escuro */
            padding: 16px 50px;  /* Espaçamento interno */
            border: none;  /* Sem borda */
            border-radius: 4px;  /* Arredondamento suave */
            font-weight: 800;  /* Peso muito pesado */
            font-size: 13px;  /* Tamanho pequeno */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 1px;  /* Espaçamento entre letras */
            cursor: pointer;  /* Cursor de clique */
            transition: all 0.3s ease;  /* Animação suave */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover no botão primário */
        .btn-primary:hover {
            background: #FFC700;  /* Amarelo mais escuro */
            transform: translateY(-2px);  /* Levanta o botão */
        }
        
        /* ❌ NÃO ALTERE: Botão secundário */
        .btn-secondary {
            background: transparent;  /* Fundo transparente */
            color: #ffffff !important;  /* Texto branco */
            text-decoration: none !important;  /* Remove sublinhado de link */
            display: inline-block;  /* Garante padding correto em <a> */
            padding: 16px 50px;  /* Espaçamento interno */
            border: 2px solid #ffffff;  /* Borda branca */
            border-radius: 4px;  /* Arredondamento suave */
            font-weight: 700;  /* Peso pesado */
            font-size: 13px;  /* Tamanho pequeno */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 1px;  /* Espaçamento entre letras */
            cursor: pointer;  /* Cursor de clique */
            transition: all 0.3s ease;  /* Animação suave */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover no botão secundário */
        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.1);  /* Fundo branco semi-transparente */
        }
        
        /* ❌ NÃO ALTERE: Visual do hero */
        .hero-visual {
            position: relative;  /* Posicionamento relativo */
            z-index: 2;  /* Acima do efeito de fundo */
            width: 500px;  /* Largura */
            height: 500px;  /* Altura */
            background: rgba(255, 255, 255, 0.1);  /* Fundo branco semi-transparente */
            border: 2px solid rgba(255, 255, 255, 0.2);  /* Borda branca semi-transparente */
            border-radius: 50%;  /* Círculo */
            display: flex;  /* Layout flexível */
            align-items: center;  /* Alinha itens no centro */
            justify-content: center;  /* Centraliza itens */
            font-size: 100px;  /* Tamanho muito grande */
            animation: slideInRight 0.8s ease-out;  /* Animação de entrada */
        }
        
        /* ❌ NÃO ALTERE: Seção de estatísticas */
        .stats-section {
            padding: 80px;  /* Espaçamento interno */
            background: #ffffff;  /* Fundo branco */
            border-bottom: 1px solid #f0f0f0;  /* Borda inferior */
        }
        
        /* ❌ NÃO ALTERE: Grid de estatísticas */
        .stats-grid {
            display: grid;  /* Layout em grade */
            grid-template-columns: repeat(4, 1fr);  /* 4 colunas iguais */
            gap: 40px;  /* Espaçamento entre itens */
            max-width: 1200px;  /* Largura máxima */
            margin: 0 auto;  /* Centraliza */
        }
        
        /* ❌ NÃO ALTERE: Item de estatística */
        .stat-item {
            text-align: center;  /* Texto centralizado */
            padding: 20px;  /* Espaçamento interno */
            animation: fadeInUp 0.8s ease-out;  /* Animação de entrada */
        }
        
        /* ❌ NÃO ALTERE: Número da estatística */
        .stat-number {
            font-size: 48px;  /* Tamanho muito grande */
            font-weight: 800;  /* Peso muito pesado */
            color: #0066FF;  /* Cor azul */
            margin-bottom: 10px;  /* Espaçamento inferior */
            font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
        }
        
        /* ❌ NÃO ALTERE: Label da estatística */
        .stat-label {
            font-size: 13px;  /* Tamanho pequeno */
            color: #666666;  /* Cor cinza */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 1px;  /* Espaçamento entre letras */
            font-weight: 600;  /* Peso pesado */
        }
        
        /* ❌ NÃO ALTERE: Seção de features */
        .features-section {
            padding: 120px 80px;  /* Espaçamento interno */
            background: #f8f9fa;  /* Fundo cinza claro */
        }
        
        /* ❌ NÃO ALTERE: Título da seção */
        .section-title {
            font-size: 36px;  /* Tamanho grande */
            font-weight: 800;  /* Peso muito pesado */
            color: #1a1a1a;  /* Cor preta */
            margin-bottom: 80px;  /* Espaçamento inferior */
            text-align: center;  /* Texto centralizado */
            font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
        }
        
        /* ❌ NÃO ALTERE: Grid de features */
        .features-grid {
            display: grid;  /* Layout em grade */
            grid-template-columns: repeat(3, 1fr);  /* 3 colunas iguais */
            gap: 40px;  /* Espaçamento entre itens */
            max-width: 1200px;  /* Largura máxima */
            margin: 0 auto;  /* Centraliza */
        }
        
        /* ❌ NÃO ALTERE: Card de feature */
        .feature-card {
            background: #ffffff;  /* Fundo branco */
            padding: 50px 40px;  /* Espaçamento interno */
            border-radius: 8px;  /* Arredondamento suave */
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);  /* Sombra suave */
            transition: all 0.4s ease;  /* Animação suave */
            text-align: center;  /* Texto centralizado */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover no card de feature */
        .feature-card:hover {
            transform: translateY(-10px);  /* Levanta o card */
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);  /* Sombra aumentada */
        }
        
        /* ❌ NÃO ALTERE: Ícone da feature */
        .feature-icon {
            font-size: 50px;  /* Tamanho grande */
            margin-bottom: 30px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Título da feature */
        .feature-title {
            font-size: 20px;  /* Tamanho médio */
            font-weight: 700;  /* Peso pesado */
            color: #1a1a1a;  /* Cor preta */
            margin-bottom: 20px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Descrição da feature */
        .feature-desc {
            font-size: 14px;  /* Tamanho pequeno */
            color: #666666;  /* Cor cinza */
            line-height: 1.8;  /* Altura da linha generosa */
        }
        
        /* ❌ NÃO ALTERE: Seção de depoimento */
        .testimonial-section {
            padding: 120px 80px;  /* Espaçamento interno */
            background: #ffffff;  /* Fundo branco */
        }
        
        /* ❌ NÃO ALTERE: Card de depoimento */
        .testimonial-card {
            max-width: 900px;  /* Largura máxima */
            margin: 0 auto;  /* Centraliza */
            text-align: center;  /* Texto centralizado */
            padding: 60px;  /* Espaçamento interno */
            background: #f0f7ff;  /* Fundo azul muito claro */
            border-radius: 16px;  /* Arredondamento */
        }
        
        /* ❌ NÃO ALTERE: Texto do depoimento */
        .testimonial-text {
            font-size: 24px;  /* Tamanho grande */
            font-weight: 600;  /* Peso pesado */
            color: #0066FF;  /* Cor azul */
            margin-bottom: 30px;  /* Espaçamento inferior */
            line-height: 1.6;  /* Altura da linha */
            font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
        }
        
        /* ❌ NÃO ALTERE: Autor do depoimento */
        .testimonial-author {
            font-size: 14px;  /* Tamanho pequeno */
            color: #666666;  /* Cor cinza */
            font-weight: 600;  /* Peso pesado */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 1px;  /* Espaçamento entre letras */
        }
        
        /* ❌ NÃO ALTERE: Seção CTA */
        .cta-section {
            padding: 120px 80px;  /* Espaçamento interno */
            background: #0066FF;  /* Fundo azul */
            text-align: center;  /* Texto centralizado */
            color: #ffffff;  /* Texto branco */
        }
        
        /* ❌ NÃO ALTERE: Título CTA */
        .cta-title {
            font-size: 48px;  /* Tamanho muito grande */
            font-weight: 800;  /* Peso muito pesado */
            margin-bottom: 50px;  /* Espaçamento inferior */
            font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
        }
        
        /* ❌ NÃO ALTERE: Formulário CTA */
        .cta-form {
            display: flex;  /* Layout flexível */
            justify-content: center;  /* Centraliza */
            gap: 15px;  /* Espaçamento entre itens */
            max-width: 600px;  /* Largura máxima */
            margin: 0 auto 30px;  /* Centraliza e margem inferior */
        }
        
        /* ❌ NÃO ALTERE: Input do CTA */
        .cta-input {
            padding: 16px 20px;  /* Espaçamento interno */
            border: none;  /* Sem borda */
            border-radius: 4px;  /* Arredondamento suave */
            width: 100%;  /* Largura total */
            font-family: 'Montserrat', sans-serif;  /* Fonte padrão */
        }
        
        /* ❌ NÃO ALTERE: Botão CTA */
        .cta-btn {
            background: #FFD60A;  /* Fundo amarelo */
            color: #1a1a1a;  /* Texto cinza escuro */
            padding: 16px 40px;  /* Espaçamento interno */
            border: none;  /* Sem borda */
            border-radius: 4px;  /* Arredondamento suave */
            font-weight: 800;  /* Peso muito pesado */
            font-size: 13px;  /* Tamanho pequeno */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 1px;  /* Espaçamento entre letras */
            cursor: pointer;  /* Cursor de clique */
            white-space: nowrap;  /* Não quebra linha */
            text-decoration: none;  /* Remove sublinhado */
            display: inline-block;  /* Exibe como bloco inline */
            transition: all 0.3s ease;  /* Animação suave */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover no botão CTA */
        .cta-btn:hover {
            background: #FFC700;  /* Amarelo mais escuro */
            transform: translateY(-2px);  /* Levanta o botão */
        }
        
        /* ❌ NÃO ALTERE: Nota do CTA */
        .cta-note {
            font-size: 13px;  /* Tamanho pequeno */
            color: rgba(255, 255, 255, 0.8);  /* Branco semi-transparente */
            margin-top: 20px;  /* Espaçamento superior */
        }
        
        /* ❌ NÃO ALTERE: Footer */
        .footer {
            background: #ffffff;  /* Fundo branco */
            padding: 80px 80px 40px;  /* Espaçamento interno */
            color: #666666;  /* Texto cinza */
            border-top: 1px solid #f0f0f0;  /* Borda superior */
        }
        
        /* ❌ NÃO ALTERE: Grid do footer */
        .footer-grid {
            display: grid;  /* Layout em grade */
            grid-template-columns: repeat(4, 1fr);  /* 4 colunas iguais */
            gap: 40px;  /* Espaçamento entre itens */
            max-width: 1200px;  /* Largura máxima */
            margin: 0 auto 60px;  /* Centraliza e margem inferior */
        }
        
        /* ❌ NÃO ALTERE: Títulos do footer */
        .footer-col h4 {
            color: #1a1a1a;  /* Texto preto */
            font-size: 14px;  /* Tamanho pequeno */
            font-weight: 700;  /* Peso pesado */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 1px;  /* Espaçamento entre letras */
            margin-bottom: 25px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Links do footer */
        .footer-col a {
            display: block;  /* Exibe como bloco */
            color: #999999;  /* Texto cinza */
            text-decoration: none;  /* Remove sublinhado */
            font-size: 13px;  /* Tamanho pequeno */
            margin-bottom: 12px;  /* Espaçamento inferior */
            transition: color 0.3s ease;  /* Animação suave */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos links do footer */
        .footer-col a:hover { color: #0066FF; }  /* Fica azul ao passar o mouse */
        
        /* ❌ NÃO ALTERE: Rodapé do footer */
        .footer-bottom {
            text-align: center;  /* Texto centralizado */
            padding-top: 40px;  /* Espaçamento superior */
            border-top: 1px solid #333333;  /* Borda superior cinza */
            font-size: 12px;  /* Tamanho muito pequeno */
        }
        
        /* ❌ NÃO ALTERE: Responsividade */
        @media (max-width: 768px) {
            .navbar { padding: 15px 20px; flex-direction: column; gap: 15px; }
            .hero { flex-direction: column; padding: 50px 20px; }
            .hero-title { font-size: 42px; }
            .hero-visual { width: 100%; margin-top: 40px; }
            .stats-grid { grid-template-columns: repeat(2, 1fr); }
            .features-grid { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: repeat(2, 1fr); }
        }
    </style>
    """

    st.markdown(custom_css, unsafe_allow_html=True)

    # ========== SEÇÃO 3: NAVBAR ==========
    # ✅ ALTERE: Logo e menu
    navbar_html = '''<div class="navbar">
        <!-- ✅ ALTERE: Nome da empresa -->
        <div class="navbar-logo">GetResponse</div>
        <!-- ✅ ALTERE: Menu de navegação -->
        <div class="navbar-nav">
            <a href="#produto" class="nav-link">Produto</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#recursos" class="nav-link">Recursos</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#precos" class="nav-link">Preços</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#sobre" class="nav-link">Sobre</a>  <!-- ✅ ALTERE: Texto do menu -->
        </div>
    </div>'''
    st.markdown(navbar_html, unsafe_allow_html=True)

    # ========== SEÇÃO 4: HERO ==========
    # ✅ ALTERE: Título, descrição, emojis e botões
    hero_html = '''<div class="hero">
        <div class="hero-content">
            <!-- ✅ ALTERE: Label do hero -->
            <div class="hero-label">Email Marketing & Automação</div>
            <!-- ✅ ALTERE: Título principal -->
            <div class="hero-title">Não é você, é o algoritmo</div>
            <!-- ✅ ALTERE: Descrição -->
            <div class="hero-desc">Plataforma de email marketing, automação e landing pages com IA integrada. Crie, teste e venda mais rápido.</div>
            <!-- ✅ ALTERE: Botões e URLs -->
            <div class="hero-cta">
                <a href="https://www.google.com/" target="_blank" class="btn-primary">Comece Grátis</a>
                <a href="https://www.google.com/" target="_blank" class="btn-secondary">Saiba Mais</a>
            </div>
        </div>
        <!-- ✅ ALTERE: Emoji do visual -->
        <div class="hero-visual">📧</div>
    </div>'''
    st.markdown(hero_html, unsafe_allow_html=True)

    # ========== SEÇÃO 5: ESTATÍSTICAS ==========
    # ✅ ALTERE: Números e descrições
    stats_html = '''<div class="stats-section">
        <div class="stats-grid">
            <!-- ✅ ALTERE: Estatística 1 -->
            <div class="stat-item">
                <div class="stat-number">99%</div>
                <div class="stat-label">Taxa de Entregabilidade para 160+ países</div>
            </div>
            <!-- ✅ ALTERE: Estatística 2 -->
            <div class="stat-item">
                <div class="stat-number">+150</div>
                <div class="stat-label">Integrações Disponíveis</div>
            </div>
            <!-- ✅ ALTERE: Estatística 3 -->
            <div class="stat-item">
                <div class="stat-number">350K+</div>
                <div class="stat-label">Clientes ao Redor do Mundo</div>
            </div>
            <!-- ✅ ALTERE: Estatística 4 -->
            <div class="stat-item">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Suporte de Sucesso do Cliente</div>
            </div>
        </div>
    </div>'''
    st.markdown(stats_html, unsafe_allow_html=True)

    # ========== SEÇÃO 6: FEATURES ==========
    # ✅ ALTERE: Título, ícones, títulos e descrições
    features_html = '''<div class="features-section">
        <!-- ✅ ALTERE: Título da seção -->
        <div class="section-title">Ferramentas Poderosas para Seu Negócio</div>
        <div class="features-grid">
            <!-- ✅ ALTERE: Feature 1 -->
            <div class="feature-card">
                <div class="feature-icon">📧</div>  <!-- ✅ ALTERE: Emoji -->
                <div class="feature-title">Email Marketing</div>  <!-- ✅ ALTERE: Título -->
                <div class="feature-desc">Envie newsletters ilimitadas com IA que cria linhas de assunto e personaliza conteúdo para seu público.</div>  <!-- ✅ ALTERE: Descrição -->
            </div>
            <!-- ✅ ALTERE: Feature 2 -->
            <div class="feature-card">
                <div class="feature-icon">🤖</div>  <!-- ✅ ALTERE: Emoji -->
                <div class="feature-title">Automação com IA</div>  <!-- ✅ ALTERE: Título -->
                <div class="feature-desc">Crie jornadas automáticas que identificam o melhor momento para contatar seus clientes.</div>  <!-- ✅ ALTERE: Descrição -->
            </div>
            <!-- ✅ ALTERE: Feature 3 -->
            <div class="feature-card">
                <div class="feature-icon">🌐</div>  <!-- ✅ ALTERE: Emoji -->
                <div class="feature-title">Landing Pages</div>  <!-- ✅ ALTERE: Título -->
                <div class="feature-desc">Publique landing pages ilimitadas com IA que escreve o texto e escolhe o layout ideal.</div>  <!-- ✅ ALTERE: Descrição -->
            </div>
        </div>
    </div>'''
    st.markdown(features_html, unsafe_allow_html=True)

    # ========== SEÇÃO 7: DEPOIMENTO ==========
    # ✅ ALTERE: Texto do depoimento e autor
    testimonial_html = '''<div class="testimonial-section">
        <div class="testimonial-card">
            <!-- ✅ ALTERE: Texto do depoimento -->
            <div class="testimonial-text">"Geramos US$ 43.000 em vendas com apenas 10 e-mails usando a GetResponse. A automação e a IA mudaram nosso negócio."</div>
            <!-- ✅ ALTERE: Nome e cargo do autor -->
            <div class="testimonial-author">João Silva - CEO da Tech Company</div>
        </div>
    </div>'''
    st.markdown(testimonial_html, unsafe_allow_html=True)

    # ========== SEÇÃO 8: CTA ==========
    # ✅ ALTERE: Título, placeholder, botão e nota
    cta_html = '''<div class="cta-section">
        <!-- ✅ ALTERE: Título CTA -->
        <div class="cta-title">Junte-se a 350.000+ Empresas</div>
        <div class="cta-form">
            <!-- ✅ ALTERE: Placeholder do input -->
            <input type="email" class="cta-input" placeholder="Seu endereço de e-mail">
            <!-- ✅ ALTERE: Texto do botão e URL -->
            <a href="https://www.google.com/" target="_blank" class="cta-btn">Começar Grátis</a>
        </div>
        <!-- ✅ ALTERE: Nota do CTA -->
        <div class="cta-note">Teste gratuito de 14 dias | Não precisa de cartão | Cancele a qualquer momento</div>
    </div>'''
    st.markdown(cta_html, unsafe_allow_html=True)

    # ========== SEÇÃO 9: FOOTER ==========
    # ✅ ALTERE: Títulos, links e copyright
    footer_html = '''<div class="footer">
        <div class="footer-grid">
            <!-- ✅ ALTERE: Coluna 1 - Produto -->
            <div class="footer-col">
                <h4>Produto</h4>
                <a href="https://www.google.com/" target="_blank">Email Marketing</a>
                <a href="https://www.google.com/" target="_blank">Automação</a>
                <a href="https://www.google.com/" target="_blank">Landing Pages</a>
                <a href="https://www.google.com/" target="_blank">Formulários</a>
            </div>
            <!-- ✅ ALTERE: Coluna 2 - Recursos -->
            <div class="footer-col">
                <h4>Recursos</h4>
                <a href="https://www.google.com/" target="_blank">Blog</a>
                <a href="https://www.google.com/" target="_blank">Webinars</a>
                <a href="https://www.google.com/" target="_blank">Templates</a>
                <a href="https://www.google.com/" target="_blank">Integrações</a>
            </div>
            <!-- ✅ ALTERE: Coluna 3 - Empresa -->
            <div class="footer-col">
                <h4>Empresa</h4>
                <a href="https://www.google.com/" target="_blank">Sobre Nós</a>
                <a href="https://www.google.com/" target="_blank">Carreiras</a>
                <a href="https://www.google.com/" target="_blank">Imprensa</a>
                <a href="https://www.google.com/" target="_blank">Contato</a>
            </div>
            <!-- ✅ ALTERE: Coluna 4 - Legal -->
            <div class="footer-col">
                <h4>Legal</h4>
                <a href="https://www.google.com/" target="_blank">Privacidade</a>
                <a href="https://www.google.com/" target="_blank">Termos</a>
                <a href="https://www.google.com/" target="_blank">Cookies</a>
                <a href="https://www.google.com/" target="_blank">Suporte</a>
            </div>
        </div>
        <!-- ✅ ALTERE: Copyright -->
        <div class="footer-bottom">
            © 2026 GetResponse. Todos os direitos reservados.
        </div>
    </div>'''
    st.markdown(footer_html, unsafe_allow_html=True)

    # ========== FIM DO TEMPLATE ==========
    # Lembre-se: Altere apenas o que tem ✅ ALTERE
    # Não mexa no que tem ❌ NÃO ALTERE

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template10" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

