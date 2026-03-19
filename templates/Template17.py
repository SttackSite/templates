import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

def render():
    """Renderiza o template 17 - Breakfast"""
    
    # ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
    # ❌ NÃO ALTERE: Define as configurações básicas da página
    st.set_page_config(
        page_title="Breakfast | Digital Design Agency",  # ✅ ALTERE: Título que aparece na aba do navegador
        page_icon="🍳",  # ✅ ALTERE: Emoji que aparece na aba do navegador
        layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
    )

    # ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
    # ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
    # Alterar aqui pode quebrar completamente o design da página
    st.markdown("""
    <style>
        /* ❌ NÃO ALTERE: Importa a fonte do Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

        /* ❌ NÃO ALTERE: Reset geral - Define o fundo branco e texto preto */
        .stApp {
            background-color: #ffffff;  /* Fundo branco */
        }
        
        /* ❌ NÃO ALTERE: Tipografia padrão */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;  /* Fonte moderna */
            color: #000000;  /* Texto preto */
            line-height: 1.2;  /* Altura da linha compacta */
        }

        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { 
            display: none;  /* Oculta o header */
        }

        /* ❌ NÃO ALTERE: Header brutalista */
        .header-bf {
            display: flex;  /* Layout flexível */
            justify-content: space-between;  /* Espaça itens nas extremidades */
            padding: 30px 5%;  /* Espaçamento interno */
            border-bottom: 1px solid #000;  /* Linha divisória preta */
            font-weight: 700;  /* Peso pesado */
            text-transform: uppercase;  /* Maiúsculas */
            font-size: 14px;  /* Tamanho médio */
            letter-spacing: 1px;  /* Espaçamento entre letras */
        }

        /* ❌ NÃO ALTERE: Seção hero */
        .hero-bf {
            padding: 100px 5%;  /* Espaçamento interno */
            border-bottom: 1px solid #000;  /* Linha divisória preta */
        }
        
        /* ❌ NÃO ALTERE: Estilo do título principal */
        .hero-text {
            font-size: clamp(40px, 10vw, 150px);  /* Tamanho responsivo */
            font-weight: 900;  /* Peso muito pesado */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: -4px;  /* Espaçamento negativo entre letras */
            line-height: 0.85;  /* Altura da linha compacta */
        }

        /* ❌ NÃO ALTERE: Grid de projetos */
        .project-grid {
            display: grid;  /* Layout grid */
            grid-template-columns: 1fr 1fr;  /* 2 colunas iguais */
            border-bottom: 1px solid #000;  /* Linha divisória preta */
        }
        
        /* ❌ NÃO ALTERE: Item individual do grid */
        .grid-item {
            border-right: 1px solid #000;  /* Borda direita preta */
            padding: 0;  /* Sem espaçamento */
            transition: all 0.5s ease;  /* Animação suave */
        }
        
        /* ❌ NÃO ALTERE: Remove borda do último item */
        .grid-item:last-child {
            border-right: none;  /* Remove borda */
        }

        /* ❌ NÃO ALTERE: Informações do projeto */
        .project-info {
            padding: 20px;  /* Espaçamento interno */
            font-weight: 700;  /* Peso pesado */
            text-transform: uppercase;  /* Maiúsculas */
            font-size: 13px;  /* Tamanho pequeno */
            display: flex;  /* Layout flexível */
            justify-content: space-between;  /* Espaça itens nas extremidades */
        }

        /* ❌ NÃO ALTERE: Seções de texto (filosofia) */
        .text-section {
            padding: 120px 5%;  /* Espaçamento interno */
            font-size: 42px;  /* Tamanho grande */
            font-weight: 700;  /* Peso pesado */
            border-bottom: 1px solid #000;  /* Linha divisória preta */
        }

        /* ❌ NÃO ALTERE: Rodapé brutalista */
        .footer-bf {
            padding: 100px 5%;  /* Espaçamento interno */
            background-color: #000;  /* Fundo preto */
            color: #fff;  /* Texto branco */
        }

        /* ❌ NÃO ALTERE: Estilo dos botões nativos do Streamlit */
        div.stButton > button {
            background: transparent;  /* Fundo transparente */
            border: 1px solid #000;  /* Borda preta */
            color: #000;  /* Texto preto */
            border-radius: 0;  /* Sem arredondamento */
            font-weight: 700;  /* Peso pesado */
            text-transform: uppercase;  /* Maiúsculas */
            padding: 20px 40px;  /* Espaçamento interno */
            width: 100%;  /* Largura total */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos botões */
        div.stButton > button:hover {
            background: #000;  /* Fundo preto */
            color: #fff;  /* Texto branco */
        }

        /* ❌ NÃO ALTERE: Estilo dos botões em links */
        .action-button {
            display: inline-block !important;  /* Exibe como bloco inline */
            background-color: transparent !important;  /* Fundo transparente */
            color: #fff !important;  /* Texto branco */
            border: 1px solid #fff !important;  /* Borda branca */
            border-radius: 0px !important;  /* Sem arredondamento */
            padding: 20px 40px !important;  /* Espaçamento interno */
            font-weight: 700 !important;  /* Peso pesado */
            font-size: 14px !important;  /* Tamanho médio */
            text-transform: uppercase !important;  /* Maiúsculas */
            letter-spacing: 1px !important;  /* Espaçamento entre letras */
            transition: 0.3s !important;  /* Animação suave */
            text-decoration: none !important;  /* Remove sublinhado */
            cursor: pointer !important;  /* Cursor de clique */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
        .action-button:hover {
            background-color: #fff !important;  /* Fundo branco */
            color: #000 !important;  /* Texto preto */
            border: 1px solid #fff !important;  /* Borda branca */
            text-decoration: none !important;  /* Remove sublinhado */
        }
        
        /* ❌ NÃO ALTERE: Estilo para links visitados */
        .action-button:visited {
            color: #fff !important;  /* Texto branco */
            text-decoration: none !important;  /* Remove sublinhado */
        }
    </style>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 3: NAVEGAÇÃO (HEADER) ==========
    # ✅ ALTERE: Textos do header
    st.markdown("""
    <div class="header-bf">
        <!-- ✅ ALTERE: Nome da agência -->
        <div>Breakfast.</div>
        <!-- ✅ ALTERE: Tagline/descrição -->
        <div>Design & Technology</div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 4: HERO SECTION ==========
    # ✅ ALTERE: Título principal
    st.markdown("""
    <div class="hero-bf">
        <!-- ✅ ALTERE: Título (quebrado em linhas) -->
        <div class="hero-text">WE DESIGN<br>DIGITAL<br>EXPERIENCES</div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 5: PROJETOS (GRID COMPRIDA) ==========
    # ❌ NÃO ALTERE: Função que renderiza os projetos
    def breakfast_project(col, img_url, name, client):
        # ❌ NÃO ALTERE: Função que cria os cards de projeto
        with col:
            st.markdown(f"""
            <div style="border-bottom: 1px solid #000;">
                <!-- ✅ ALTERE: URL da imagem do projeto -->
                <img src="{img_url}" style="width:100%; filter: grayscale(100%) contrast(1.1); display:block;">
                <!-- ✅ ALTERE: Nome do projeto e cliente -->
                <div class="project-info">
                    <span>{name}</span>  <!-- ✅ ALTERE: Nome do projeto -->
                    <span style="color: #888;">{client}</span>  <!-- ✅ ALTERE: Tipo/cliente do projeto -->
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Primeira linha de projetos (2 colunas)
    c1, c2 = st.columns(2, gap="small")
    breakfast_project(c1, "https://images.unsplash.com/photo-1558655146-d09347e92766?w=800", "Solar System", "Editorial")  # ✅ ALTERE: Imagem, nome e cliente
    breakfast_project(c2, "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800", "Neon Future", "Web Design")  # ✅ ALTERE: Imagem, nome e cliente

    # ❌ NÃO ALTERE: Segunda linha de projetos (2 colunas)
    c3, c4 = st.columns(2, gap="small")
    breakfast_project(c3, "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800", "Cyber Identity", "Branding")  # ✅ ALTERE: Imagem, nome e cliente
    breakfast_project(c4, "https://images.unsplash.com/photo-1509343256512-d77a5cb3791b?w=800", "Monochrome Studio", "CGI")  # ✅ ALTERE: Imagem, nome e cliente

    # ========== SEÇÃO 6: SEÇÃO DE FILOSOFIA (TEXTO COMPRIDO) ==========
    # ✅ ALTERE: Descrição/filosofia da agência
    st.markdown("""
    <div class="text-section">
        <!-- ✅ ALTERE: Texto de filosofia/descrição -->
        Independent studio for strategy, design and code. We turn complex ideas into simple, functional and beautiful digital products.
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 7: SERVIÇOS EM LISTA ==========
    # ✅ ALTERE: Títulos e descrições dos serviços
    st.markdown('<div style="padding: 80px 5%; border-bottom: 1px solid #000;">', unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Estrutura de 3 colunas
    col_s1, col_s2, col_s3 = st.columns(3)

    with col_s1:
        st.markdown("### STRATEGY")  # ✅ ALTERE: Título do serviço
        st.write("Product Discovery / User Research / Brand Positioning")  # ✅ ALTERE: Descrição do serviço

    with col_s2:
        st.markdown("### DESIGN")  # ✅ ALTERE: Título do serviço
        st.write("UI/UX Design / Visual Identity / Motion Graphics")  # ✅ ALTERE: Descrição do serviço

    with col_s3:
        st.markdown("### CODE")  # ✅ ALTERE: Título do serviço
        st.write("React / Webflow / Headless CMS / E-commerce")  # ✅ ALTERE: Descrição do serviço

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 8: CTA / CONTATO ==========
    # ✅ ALTERE: Título e texto do botão
    st.markdown('<div style="padding: 100px 5%;">', unsafe_allow_html=True)

    # ✅ ALTERE: Título da chamada para ação
    st.markdown("<h2 style='font-size: 80px; font-weight: 900; margin-bottom: 40px;'>LET'S TALK?</h2>", unsafe_allow_html=True)

    # ✅ ALTERE: Texto do botão e URL (use link em vez de st.button)
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">Start a Project</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 9: FOOTER (RODAPÉ) ==========
    # ✅ ALTERE: Informações de contato, links e copyright
    st.markdown("""
    <div class="footer-bf">
        <!-- ❌ NÃO ALTERE: Grid de 2 colunas -->
        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
            <!-- COLUNA 1: Informações da agência -->
            <div>
                <!-- ✅ ALTERE: Nome da agência -->
                <h2 style="font-size: 40px; margin-bottom: 20px;">Breakfast.</h2>
                <!-- ✅ ALTERE: Endereço e email -->
                <p>Rua de Trás, Porto, Portugal<br>
                <a href="mailto:hello@wearebreakfast.com" style="color: #fff; text-decoration: none;">hello@wearebreakfast.com</a></p>
            </div>
            <!-- COLUNA 2: Redes sociais e copyright -->
            <div style="text-align: right; font-size: 12px; opacity: 0.6;">
                <!-- ✅ ALTERE: Links de redes sociais -->
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">INSTAGRAM</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">LINKEDIN</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">TWITTER</a><br>
                <!-- ✅ ALTERE: Texto de copyright -->
                © 2026 ALL RIGHTS RESERVED
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== FIM DO TEMPLATE ==========
    # Lembre-se: Altere apenas o que tem ✅ ALTERE
    # Não mexa no que tem ❌ NÃO ALTERE

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template17" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

