import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

def render():
    """Renderiza o template 13 - ogreen"""
    
    # ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
    # ❌ NÃO ALTERE: Define as configurações básicas da página
    st.set_page_config(
        page_title="ogreen | Valor que se renova",  # ✅ ALTERE: Título que aparece na aba do navegador
        page_icon="🌲",  # ✅ ALTERE: Emoji que aparece na aba do navegador
        layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
    )

    # ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
    # ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
    # Alterar aqui pode quebrar completamente o design da página
    st.markdown("""
    <style>
        /* ❌ NÃO ALTERE: Importa a fonte do Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap');

        /* ❌ NÃO ALTERE: Tipografia padrão */
        html, body, [class*="css"] {
            font-family: 'Montserrat', sans-serif;  /* Fonte moderna */
            color: #333;  /* Texto cinza escuro */
        }

        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { 
            display: none;  /* Oculta o header */
        }

        /* ❌ NÃO ALTERE: Header */
        .header-ogreen {
            display: flex;  /* Layout flexível */
            justify-content: space-between;  /* Espaça itens nas extremidades */
            align-items: center;  /* Alinha itens no centro verticalmente */
            padding: 20px 8%;  /* Espaçamento interno */
            background-color: white;  /* Fundo branco */
            border-bottom: 2px solid #005a31;  /* Borda inferior verde */
            margin: -5rem -5rem 0rem -5rem;  /* Margem negativa para ocupar tela toda */
        }

        /* ❌ NÃO ALTERE: Seção hero com imagem de fundo */
        .hero-section {
            background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1600&q=80');  /* Imagem com overlay */
            background-size: cover;  /* Imagem cobre toda a área */
            background-position: center;  /* Imagem centralizada */
            height: 550px;  /* Altura fixa */
            display: flex;  /* Layout flexível */
            flex-direction: column;  /* Itens em coluna */
            justify-content: center;  /* Centraliza verticalmente */
            align-items: center;  /* Centraliza horizontalmente */
            color: white;  /* Texto branco */
            text-align: center;  /* Texto centralizado */
            margin: 0 -5rem 50px -5rem;  /* Margem negativa e espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Estilo do título do hero */
        .hero-title { 
            font-size: 56px;  /* Tamanho grande */
            font-weight: 800;  /* Peso muito pesado */
            text-shadow: 2px 2px 10px rgba(0,0,0,0.5);  /* Sombra de texto */
        }

        /* ❌ NÃO ALTERE: Seções de conteúdo */
        .section-padding { 
            padding: 80px 10%;  /* Espaçamento interno */
        }
        
        /* ❌ NÃO ALTERE: Estilo dos títulos das seções */
        .section-title { 
            color: #005a31;  /* Cor verde */
            font-weight: 800;  /* Peso muito pesado */
            font-size: 32px;  /* Tamanho grande */
            margin-bottom: 30px;  /* Espaçamento inferior */
            border-left: 5px solid #005a31;  /* Borda esquerda verde */
            padding-left: 15px;  /* Espaçamento interno esquerdo */
        }

        /* ❌ NÃO ALTERE: Cards de negócios */
        .business-card {
            background: #f8f9fa;  /* Fundo cinza claro */
            border-radius: 10px;  /* Arredondamento */
            overflow: hidden;  /* Oculta conteúdo que sai da área */
            border-bottom: 4px solid #005a31;  /* Borda inferior verde */
            transition: 0.3s;  /* Animação suave */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos cards */
        .business-card:hover { 
            transform: translateY(-10px);  /* Levanta o card */
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);  /* Sombra aumentada */
        }
        
        /* ❌ NÃO ALTERE: Conteúdo do card */
        .card-label { 
            padding: 25px;  /* Espaçamento interno */
        }

        /* ❌ NÃO ALTERE: Seção de estatísticas */
        .stats-bg { 
            background-color: #005a31;  /* Fundo verde */
            color: white;  /* Texto branco */
            padding: 60px 10%;  /* Espaçamento interno */
            text-align: center;  /* Texto centralizado */
            margin: 50px -5rem;  /* Margem negativa */
        }
        
        /* ❌ NÃO ALTERE: Número da estatística */
        .stat-number { 
            font-size: 48px;  /* Tamanho grande */
            font-weight: 800;  /* Peso muito pesado */
            color: #8ec641;  /* Verde limão */
        }
        
        /* ❌ NÃO ALTERE: Descrição da estatística */
        .stat-desc { 
            font-size: 14px;  /* Tamanho pequeno */
            opacity: 0.9;  /* Opacidade */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 1px;  /* Espaçamento entre letras */
        }

        /* ❌ NÃO ALTERE: Rodapé */
        .footer-ogreen {
            background-color: #222;  /* Fundo cinza escuro */
            color: #ccc;  /* Texto cinza claro */
            padding: 80px 10% 40px 10%;  /* Espaçamento interno */
            margin: 50px -5rem -5rem -5rem;  /* Margem negativa */
        }

        /* ❌ NÃO ALTERE: Estilo dos botões em links */
        .action-button {
            display: inline-block !important;  /* Exibe como bloco inline */
            background-color: #005a31 !important;  /* Fundo verde */
            color: white !important;  /* Texto branco */
            border: none !important;  /* Sem borda */
            border-radius: 5px !important;  /* Arredondamento suave */
            padding: 12px 30px !important;  /* Espaçamento interno */
            font-weight: 700 !important;  /* Peso pesado */
            font-size: 13px !important;  /* Tamanho pequeno */
            text-transform: uppercase !important;  /* Maiúsculas */
            letter-spacing: 1px !important;  /* Espaçamento entre letras */
            transition: 0.3s !important;  /* Animação suave */
            text-decoration: none !important;  /* Remove sublinhado */
            cursor: pointer !important;  /* Cursor de clique */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
        .action-button:hover {
            background-color: #004a26 !important;  /* Fundo verde escuro */
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

    # ========== SEÇÃO 3: NAVEGAÇÃO (HEADER) ==========
    # ✅ ALTERE: Logo e menu
    st.markdown("""
    <div class="header-ogreen">
        <!-- ✅ ALTERE: Nome da empresa -->
        <div style="font-size: 30px; font-weight: 800; color: #005a31; letter-spacing: -1px;">ogreen</div>
        <!-- ✅ ALTERE: Menu de navegação -->
        <div style="display: flex; gap: 30px; font-size: 13px; font-weight: 700; color: #555;">
            <a href="#about" style="color: #555; text-decoration: none; cursor: pointer;">A ogreen</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#business" style="color: #555; text-decoration: none; cursor: pointer;">NOSSOS NEGÓCIOS</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#sustainability" style="color: #555; text-decoration: none; cursor: pointer;">SUSTENTABILIDADE</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#investors" style="color: #555; text-decoration: none; cursor: pointer;">INVESTIDORES</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#products" style="color: #555; text-decoration: none; cursor: pointer;">PRODUTOS</a>  <!-- ✅ ALTERE: Texto do menu -->
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 4: HERO BANNER ==========
    # ✅ ALTERE: Título e descrição
    st.markdown("""
    <div class="hero-section">
        <!-- ✅ ALTERE: Título principal -->
        <div class="hero-title">O FUTURO É RENOVÁVEL</div>
        <!-- ✅ ALTERE: Descrição do hero -->
        <p style="font-size: 20px; font-weight: 400; max-width: 800px; margin-top: 20px;">
            Líder na produção de papéis e cartões para embalagens, embalagens de papelão ondulado e sacos industriais.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 5: QUEM SOMOS ==========
    # ✅ ALTERE: Título, descrição, imagem e botão
    st.markdown('<div id="about" class="section-padding">', unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Estrutura de 2 colunas
    c_text, c_img = st.columns([1, 1], gap="large")

    with c_text:
        # ✅ ALTERE: Título da seção
        st.markdown('<div class="section-title">Sobre a ogreen</div>', unsafe_allow_html=True)
        # ✅ ALTERE: Descrição
        st.write("""
        Com 125 anos de história, somos a maior produtora e exportadora de papéis para embalagens e soluções sustentáveis do Brasil. 
        Nossa atuação é baseada no desenvolvimento sustentável, com florestas 100% plantadas e certificadas.
        """)
        # ✅ ALTERE: Texto do botão e URL
        st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">CONHEÇA NOSSA HISTÓRIA</a>', unsafe_allow_html=True)

    with c_img:
        # ✅ ALTERE: URL da imagem e legenda
        st.image("https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=800&q=80", caption="Gestão Florestal Responsável")

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 6: NÚMEROS DE IMPACTO (STATS) ==========
    # ✅ ALTERE: Números, descrições e valores
    st.markdown('<div class="stats-bg">', unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Estrutura de 4 colunas
    s1, s2, s3, s4 = st.columns(4)

    with s1:
        # ✅ ALTERE: Número e descrição
        st.markdown('<div class="stat-number">22</div><div class="stat-desc">Fábricas no Brasil e Argentina</div>', unsafe_allow_html=True)

    with s2:
        # ✅ ALTERE: Número e descrição
        st.markdown('<div class="stat-number">125</div><div class="stat-desc">Anos de Inovação</div>', unsafe_allow_html=True)

    with s3:
        # ✅ ALTERE: Número e descrição
        st.markdown('<div class="stat-number">719k</div><div class="stat-desc">Hectares de Florestas</div>', unsafe_allow_html=True)

    with s4:
        # ✅ ALTERE: Número e descrição
        st.markdown('<div class="stat-number">25k</div><div class="stat-desc">Colaboradores</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 7: NOSSOS NEGÓCIOS (GRID DE CARDS) ==========
    # ✅ ALTERE: Título da seção
    st.markdown('<div id="business" class="section-padding" style="padding-top: 20px;">', unsafe_allow_html=True)

    st.markdown('<div class="section-title" style="text-align: center; border-left: none;">Nossas Frentes de Atuação</div>', unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Função que renderiza os negócios
    def business_item(col, img, title, desc):
        # ❌ NÃO ALTERE: Função que cria os cards de negócio
        with col:
            st.markdown(f"""
            <div class="business-card">
                <!-- ✅ ALTERE: URL da imagem -->
                <img src="{img}" style="width:100%; height:200px; object-fit:cover;">
                <!-- ✅ ALTERE: Título e descrição -->
                <div class="card-label">
                    <h4 style="color:#005a31; margin-bottom:10px;">{title}</h4>  <!-- ✅ ALTERE: Título -->
                    <p style="font-size:14px; color:#666;">{desc}</p>  <!-- ✅ ALTERE: Descrição -->
                </div>
            </div>
            """, unsafe_allow_html=True)
            # ✅ ALTERE: Texto do botão e URL
            st.markdown(f'<a href="https://www.google.com/" target="_blank" class="action-button" style="width: 100%; text-align: center; display: block;">Saiba Mais</a>', unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Primeira linha de negócios (3 colunas)
    cb1, cb2, cb3 = st.columns(3)

    business_item(cb1, "https://images.unsplash.com/photo-1603484477859-abe6a73f9366?w=500", "Celulose", "Fibra curta, fibra longa e celulose fluff para diversas aplicações.")  # ✅ ALTERE: Imagem, título e descrição
    business_item(cb2, "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=500", "Embalagens", "Soluções inteligentes em papelão ondulado e sacos industriais.")  # ✅ ALTERE: Imagem, título e descrição
    business_item(cb3, "https://images.unsplash.com/photo-1603484477859-abe6a73f9366?w=500", "Papéis", "Papel-cartão e Kraftliner de alta performance para o mercado.")  # ✅ ALTERE: Imagem, título e descrição

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 8: SUSTENTABILIDADE ==========
    # ✅ ALTERE: Título, descrição e informações
    st.write("---")

    with st.container():
        st.markdown('<div id="sustainability" class="section-padding">', unsafe_allow_html=True)
        
        # ❌ NÃO ALTERE: Estrutura de 2 colunas
        sc1, sc2 = st.columns([2, 3])
        
        with sc1:
            # ✅ ALTERE: Título da seção
            st.markdown('<div class="section-title">KODS - Objetivos ogreen para o Desenvolvimento Sustentável</div>', unsafe_allow_html=True)
            # ✅ ALTERE: Descrição
            st.write("Nossa agenda de sustentabilidade está alinhada aos ODS da ONU, com metas claras até 2030 para biodiversidade, clima e impacto social.")
        
        with sc2:
            # ✅ ALTERE: Informações de sustentabilidade
            st.info("🌳 Conservação da Biodiversidade")
            st.success("♻️ Economia Circular e Resíduo Zero")
            st.warning("💧 Gestão Eficiente de Recursos Hídricos")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 9: INVESTIDORES E GOVERNANÇA ==========
    # ✅ ALTERE: Título, métricas e informações
    st.write("---")

    st.markdown('<div id="investors" style="background-color:#f4f7f9; padding: 60px 10%;">', unsafe_allow_html=True)

    # ✅ ALTERE: Título da seção
    st.subheader("Relações com Investidores")

    # ❌ NÃO ALTERE: Estrutura de 3 colunas
    col_ri1, col_ri2, col_ri3 = st.columns(3)

    with col_ri1:
        # ✅ ALTERE: Métrica de ações
        st.metric(label="KLBN11 (Units)", value="R$ 22,45", delta="+1.20%")

    with col_ri2:
        # ✅ ALTERE: Título e descrição
        st.write("**Central de Resultados**")
        st.caption("Acesse os relatórios do 4T25 e demonstrações financeiras.")
        # ✅ ALTERE: Texto do botão e URL
        st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">Acessar Central</a>', unsafe_allow_html=True)

    with col_ri3:
        # ✅ ALTERE: Título e descrição
        st.write("**Governança Corporativa**")
        st.caption("Transparência e ética em todos os níveis da companhia.")
        # ✅ ALTERE: Texto do botão e URL
        st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">Ver Diretoria</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 10: FOOTER (RODAPÉ) ==========
    # ✅ ALTERE: Informações da empresa, links e copyright
    st.markdown("""
    <div class="footer-ogreen">
        <!-- ❌ NÃO ALTERE: Grid de 4 colunas -->
        <div style="display:grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap:50px;">
            <!-- COLUNA 1: Sobre a empresa -->
            <div>
                <!-- ✅ ALTERE: Nome da empresa -->
                <div style="font-size:24px; font-weight:800; color:white; margin-bottom:20px;">ogreen</div>
                <!-- ✅ ALTERE: Descrição da empresa -->
                <p style="font-size:13px;">Líder no mercado de papéis e embalagens, focada na inovação e na sustentabilidade do ciclo da floresta ao consumidor final.</p>
            </div>
            <!-- COLUNA 2: Nossos sites -->
            <div>
                <!-- ✅ ALTERE: Título da coluna -->
                <h4 style="color:white; margin-bottom:15px;">NOSSOS SITES</h4>
                <!-- ✅ ALTERE: Links -->
                <p style="font-size:12px; line-height:2;">
                    <a href="https://www.google.com/" target="_blank" style="color: #ccc; text-decoration: none;">Relações com Investidores</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #ccc; text-decoration: none;">ogreen ForYou</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #ccc; text-decoration: none;">Blog ogreen</a>
                </p>
            </div>
            <!-- COLUNA 3: Contato -->
            <div>
                <!-- ✅ ALTERE: Título da coluna -->
                <h4 style="color:white; margin-bottom:15px;">CONTATO</h4>
                <!-- ✅ ALTERE: Links -->
                <p style="font-size:12px; line-height:2;">
                    <a href="https://www.google.com/" target="_blank" style="color: #ccc; text-decoration: none;">Fale Conosco</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #ccc; text-decoration: none;">Imprensa</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #ccc; text-decoration: none;">Trabalhe Conosco</a>
                </p>
            </div>
            <!-- COLUNA 4: Redes sociais -->
            <div>
                <!-- ✅ ALTERE: Título da coluna -->
                <h4 style="color:white; margin-bottom:15px;">REDES SOCIAIS</h4>
                <!-- ✅ ALTERE: Links de redes sociais -->
                <p style="font-size:12px; line-height:2;">
                    <a href="https://www.google.com/" target="_blank" style="color: #ccc; text-decoration: none;">LinkedIn</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #ccc; text-decoration: none;">Instagram</a><br>
                    <a href="https://www.google.com/" target="_blank" style="color: #ccc; text-decoration: none;">YouTube</a>
                </p>
            </div>
        </div>
        <!-- ❌ NÃO ALTERE: Linha divisória e copyright -->
        <div style="text-align:center; border-top:1px solid #444; margin-top:50px; padding-top:20px; font-size:11px;">
            <!-- ✅ ALTERE: Texto de copyright -->
            © 2026 ogreen S.A. | Todos os direitos reservados.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== FIM DO TEMPLATE ==========
    # Lembre-se: Altere apenas o que tem ✅ ALTERE
    # Não mexa no que tem ❌ NÃO ALTERE

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template13" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

