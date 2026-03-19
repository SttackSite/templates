import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

def render():
    """Renderiza o template 16 - LITIGUARD"""
    
    # ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
    # ❌ NÃO ALTERE: Define as configurações básicas da página
    st.set_page_config(
        page_title="LITIGUARD | Excellence in Legal Services",  # ✅ ALTERE: Título que aparece na aba do navegador
        page_icon="⚖️",  # ✅ ALTERE: Emoji que aparece na aba do navegador
        layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
    )

    # ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
    # ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
    # Alterar aqui pode quebrar completamente o design da página
    st.markdown("""
    <style>
        /* ❌ NÃO ALTERE: Importa as fontes do Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');

        /* ❌ NÃO ALTERE: Reset geral - Define o fundo branco e texto azul marinho */
        .stApp {
            background-color: #ffffff;  /* Fundo branco */
        }
        
        /* ❌ NÃO ALTERE: Tipografia padrão */
        html, body, [class*="css"] {
            font-family: 'Montserrat', sans-serif;  /* Fonte moderna */
            color: #1a2b3c;  /* Azul marinho profundo */
        }

        /* ❌ NÃO ALTERE: Tipografia dos títulos */
        h1, h2, h3 {
            font-family: 'Playfair Display', serif;  /* Fonte serif elegante */
        }

        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { 
            display: none;  /* Oculta o header */
        }

        /* ❌ NÃO ALTERE: Barra superior */
        .top-bar {
            background-color: #1a2b3c;  /* Fundo azul marinho */
            color: #c5a059;  /* Dourado */
            padding: 10px 8%;  /* Espaçamento interno */
            font-size: 12px;  /* Tamanho pequeno */
            display: flex;  /* Layout flexível */
            justify-content: space-between;  /* Espaça itens nas extremidades */
            margin: -5rem -5rem 0 -5rem;  /* Margem negativa para ocupar tela toda */
        }

        /* ❌ NÃO ALTERE: Barra de navegação */
        .nav-litiguard {
            display: flex;  /* Layout flexível */
            justify-content: space-between;  /* Espaça itens nas extremidades */
            align-items: center;  /* Alinha itens no centro verticalmente */
            padding: 30px 8%;  /* Espaçamento interno */
            background: white;  /* Fundo branco */
            border-bottom: 1px solid #eee;  /* Linha divisória cinza clara */
            margin: 0 -5rem 0 -5rem;  /* Margem negativa para ocupar tela toda */
        }

        /* ❌ NÃO ALTERE: Seção hero com imagem de fundo */
        .hero-litiguard {
            height: 600px;  /* Altura fixa */
            background-image: linear-gradient(rgba(26, 43, 60, 0.7), rgba(26, 43, 60, 0.7)), 
                              url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80');  /* Imagem com overlay */
            background-size: cover;  /* Imagem cobre toda a área */
            background-position: center;  /* Imagem centralizada */
            display: flex;  /* Layout flexível */
            flex-direction: column;  /* Itens em coluna */
            justify-content: center;  /* Centraliza verticalmente */
            align-items: center;  /* Centraliza horizontalmente */
            color: white;  /* Texto branco */
            text-align: center;  /* Texto centralizado */
            margin: 0 -5rem 80px -5rem;  /* Margem negativa e espaçamento inferior */
        }

        /* ❌ NÃO ALTERE: Cards de serviços */
        .service-card {
            padding: 40px;  /* Espaçamento interno */
            border: 1px solid #eee;  /* Borda cinza clara */
            transition: all 0.3s ease;  /* Animação suave */
            height: 100%;  /* Altura total */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos cards */
        .service-card:hover {
            background-color: #1a2b3c;  /* Fundo azul marinho */
            color: white;  /* Texto branco */
            border-color: #1a2b3c;  /* Borda azul marinho */
        }
        
        /* ❌ NÃO ALTERE: Ícone do serviço */
        .service-icon {
            color: #c5a059;  /* Dourado */
            font-size: 40px;  /* Tamanho grande */
            margin-bottom: 20px;  /* Espaçamento inferior */
        }

        /* ❌ NÃO ALTERE: Seções de texto compridas */
        .section-box {
            padding: 100px 15%;  /* Espaçamento interno */
            border-bottom: 1px solid #eee;  /* Linha divisória cinza clara */
        }

        /* ❌ NÃO ALTERE: Estilo dos botões nativos do Streamlit */
        div.stButton > button {
            background-color: #c5a059;  /* Fundo dourado */
            color: white;  /* Texto branco */
            border-radius: 0;  /* Sem arredondamento */
            border: none;  /* Sem borda */
            padding: 15px 40px;  /* Espaçamento interno */
            font-weight: 600;  /* Peso pesado */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 2px;  /* Espaçamento entre letras */
        }

        /* ❌ NÃO ALTERE: Estilo dos botões em links */
        .action-button {
            display: inline-block !important;  /* Exibe como bloco inline */
            background-color: #c5a059 !important;  /* Fundo dourado */
            color: white !important;  /* Texto branco */
            border: none !important;  /* Sem borda */
            border-radius: 0px !important;  /* Sem arredondamento */
            padding: 15px 40px !important;  /* Espaçamento interno */
            font-weight: 600 !important;  /* Peso pesado */
            font-size: 13px !important;  /* Tamanho pequeno */
            text-transform: uppercase !important;  /* Maiúsculas */
            letter-spacing: 2px !important;  /* Espaçamento entre letras */
            transition: 0.3s !important;  /* Animação suave */
            text-decoration: none !important;  /* Remove sublinhado */
            cursor: pointer !important;  /* Cursor de clique */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
        .action-button:hover {
            background-color: #1a2b3c !important;  /* Fundo azul marinho */
            color: white !important;  /* Texto branco */
            border: none !important;  /* Sem borda */
            text-decoration: none !important;  /* Remove sublinhado */
        }
        
        /* ❌ NÃO ALTERE: Estilo para links visitados */
        .action-button:visited {
            color: white !important;  /* Texto branco */
            text-decoration: none !important;  /* Remove sublinhado */
        }
    </style>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 3: NAVEGAÇÃO (TOP BAR E HEADER) ==========
    # ✅ ALTERE: Textos da navegação
    st.markdown("""
    <div class="top-bar">
        <!-- ✅ ALTERE: Texto da barra superior esquerda -->
        <div>LITIGATION & ADVISORY SERVICES</div>
        <!-- ✅ ALTERE: Idiomas ou informações da barra superior direita -->
        <div>EN | FR | DE</div>
    </div>
    <div class="nav-litiguard">
        <!-- ✅ ALTERE: Nome da empresa/marca -->
        <div style="font-size: 28px; font-weight: 700; letter-spacing: 3px;">LITIGUARD</div>
        <!-- ✅ ALTERE: Menu de navegação -->
        <div style="display: flex; gap: 40px; font-size: 13px; font-weight: 600;">
            <a href="#about" style="color: #1a2b3c; text-decoration: none; cursor: pointer;">ABOUT</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#services" style="color: #1a2b3c; text-decoration: none; cursor: pointer;">SERVICES</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#network" style="color: #1a2b3c; text-decoration: none; cursor: pointer;">NETWORK</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#contact" style="color: #1a2b3c; text-decoration: none; cursor: pointer;">CONTACT</a>  <!-- ✅ ALTERE: Texto do menu -->
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 4: HERO SECTION ==========
    # ✅ ALTERE: Título, descrição e imagem
    st.markdown("""
    <div class="hero-litiguard">
        <!-- ✅ ALTERE: Título principal -->
        <h1 style="font-size: 60px; margin-bottom: 20px;">Protecting Your Interests</h1>
        <!-- ✅ ALTERE: Descrição do hero -->
        <p style="font-size: 20px; max-width: 700px; font-weight: 300;">
            A global network of legal experts dedicated to complex litigation and strategic advisory.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 5: ABOUT (SECTION 1) ==========
    # ✅ ALTERE: Título, descrição e botão
    st.markdown('<div id="about" class="section-box">', unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Estrutura de 2 colunas
    c_about1, c_about2 = st.columns([1, 1])

    with c_about1:
        # ✅ ALTERE: Título da seção
        st.markdown("<h2 style='font-size: 40px;'>Strategic Legal<br>Representation</h2>", unsafe_allow_html=True)

    with c_about2:
        # ✅ ALTERE: Descrição da seção
        st.write("""
        Litiguard provides comprehensive support in cross-border disputes. 
        Our approach combines local expertise with a global perspective to ensure 
        the best possible outcome for institutional and private clients.
        """)
        # ✅ ALTERE: Texto do botão e URL
        st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">Discover Our Vision</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 6: SERVICES (GRID) ==========
    # ✅ ALTERE: Título e serviços
    st.markdown('<div id="services" class="section-box" style="background-color: #fcfcfc;">', unsafe_allow_html=True)

    # ✅ ALTERE: Título da seção
    st.markdown("<h2 style='text-align: center; margin-bottom: 60px;'>Our Expertise</h2>", unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Função que renderiza os serviços
    def service_box(col, icon, title, text):
        # ❌ NÃO ALTERE: Função que cria os cards de serviço
        with col:
            st.markdown(f"""
            <div class="service-card">
                <!-- ✅ ALTERE: Emoji/ícone do serviço -->
                <div class="service-icon">{icon}</div>
                <!-- ✅ ALTERE: Título do serviço -->
                <h3 style="margin-bottom: 15px;">{title}</h3>
                <!-- ✅ ALTERE: Descrição do serviço -->
                <p style="font-size: 14px; opacity: 0.8;">{text}</p>
            </div>
            """, unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Primeira linha de serviços (3 colunas)
    s1, s2, s3 = st.columns(3)
    service_box(s1, "⚖️", "Commercial Litigation", "Resolving complex business disputes with precision and strategic foresight.")  # ✅ ALTERE: Ícone, título e descrição
    service_box(s2, "🌍", "Cross-Border Claims", "Navigating multiple jurisdictions to protect assets and enforce rights worldwide.")  # ✅ ALTERE: Ícone, título e descrição
    service_box(s3, "🤝", "Arbitration", "Expert representation in international arbitration proceedings and alternative dispute resolution.")  # ✅ ALTERE: Ícone, título e descrição

    st.markdown("<br>", unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Segunda linha de serviços (3 colunas)
    s4, s5, s6 = st.columns(3)
    service_box(s4, "🛡️", "Asset Recovery", "Tracing and recovering assets across global financial centers and tax havens.")  # ✅ ALTERE: Ícone, título e descrição
    service_box(s5, "📈", "Investment Disputes", "Protecting investors' rights under bilateral treaties and international law.")  # ✅ ALTERE: Ícone, título e descrição
    service_box(s6, "📜", "Corporate Advisory", "Proactive legal strategies to mitigate risk and ensure regulatory compliance.")  # ✅ ALTERE: Ícone, título e descrição

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 7: NETWORK SECTION (BANNER COMPRIDO) ==========
    # ✅ ALTERE: Título, descrição e cidades
    st.markdown("""
    <div id="network" style="background-color: #1a2b3c; color: white; padding: 120px 8%; text-align: center; margin: 0 -5rem;">
        <!-- ✅ ALTERE: Título da seção -->
        <h2 style="font-size: 45px; margin-bottom: 30px;">A Truly Global Presence</h2>
        <!-- ✅ ALTERE: Descrição da seção -->
        <p style="max-width: 800px; margin: 0 auto 40px auto; font-size: 18px; opacity: 0.8;">
            Our network spans over 40 countries, providing seamless legal support 
            whenever and wherever our clients need it most.
        </p>
        <!-- ✅ ALTERE: Cidades/locais da rede -->
        <div style="display: flex; justify-content: center; gap: 80px; font-weight: 700; color: #c5a059;">
            <div>LONDON</div>  <!-- ✅ ALTERE: Cidade -->
            <div>BRUSSELS</div>  <!-- ✅ ALTERE: Cidade -->
            <div>DUBAI</div>  <!-- ✅ ALTERE: Cidade -->
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 8: FOOTER (RODAPÉ) ==========
    # ✅ ALTERE: Informações de contato, endereços e links
    st.markdown("""
    <div id="contact" style="background-color: #f4f4f4; padding: 80px 8% 40px 8%; margin: 0 -5rem -5rem -5rem; border-top: 5px solid #c5a059;">
        <!-- ❌ NÃO ALTERE: Grid de 3 colunas -->
        <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 100px;">
            <!-- COLUNA 1: Informações da empresa -->
            <div>
                <!-- ✅ ALTERE: Nome da empresa -->
                <h3 style="letter-spacing: 2px;">LITIGUARD</h3>
                <!-- ✅ ALTERE: Descrição da empresa -->
                <p style="font-size: 13px; margin-top: 20px;">International Litigation & Advisory Support Network.</p>
            </div>
            <!-- COLUNA 2: Endereços -->
            <div>
                <!-- ✅ ALTERE: Título da coluna -->
                <h4 style="font-size: 14px; color: #1a2b3c;">OFFICES</h4>
                <!-- ✅ ALTERE: Endereços dos escritórios -->
                <p style="font-size: 12px; line-height: 2;">
                    <a href="https://www.google.com/" target="_blank" style="color: #1a2b3c; text-decoration: none;">Brussels, Belgium</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #1a2b3c; text-decoration: none;">Geneva, Switzerland</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #1a2b3c; text-decoration: none;">London, UK</a>
                </p>
            </div>
            <!-- COLUNA 3: Links legais -->
            <div>
                <!-- ✅ ALTERE: Título da coluna -->
                <h4 style="font-size: 14px; color: #1a2b3c;">LEGAL</h4>
                <!-- ✅ ALTERE: Links legais -->
                <p style="font-size: 12px; line-height: 2;">
                    <a href="https://www.google.com/" target="_blank" style="color: #1a2b3c; text-decoration: none;">Privacy Policy</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #1a2b3c; text-decoration: none;">Terms of Service</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #1a2b3c; text-decoration: none;">Cookies</a>
                </p>
            </div>
        </div>
        <!-- ❌ NÃO ALTERE: Linha divisória e copyright -->
        <div style="text-align: center; margin-top: 60px; font-size: 11px; color: #999;">
            <!-- ✅ ALTERE: Texto de copyright -->
            © 2026 LITIGUARD. ALL RIGHTS RESERVED.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== FIM DO TEMPLATE ==========
    # Lembre-se: Altere apenas o que tem ✅ ALTERE
    # Não mexa no que tem ❌ NÃO ALTERE

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template16" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

