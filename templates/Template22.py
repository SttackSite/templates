import streamlit as st

def render():
    """Renderiza o template 22 - Zajno Motion"""
    
    # ❌ NÃO ALTERE: Importações necessárias para o funcionamento do Streamlit
    # Estas linhas carregam as bibliotecas essenciais para a aplicação rodar

    # ✅ ALTERE: Configuração da Página (Título, Ícone, Layout)
    # Você pode mudar o "page_title" para o nome do seu projeto
    # Você pode mudar o "page_icon" para o emoji que preferir
    st.set_page_config(
        page_title="Zajno Motion | Estúdio de Design Digital",  # ✅ ALTERE: Nome da página (aparece na aba do navegador)
        page_icon="🎬",  # ✅ ALTERE: Emoji do ícone
        layout="wide"  # ❌ NÃO ALTERE: Define o layout da página como largura total
    )

    # ❌ NÃO ALTERE: Bloco de CSS (Estilos Visuais)
    # Este bloco define todas as cores, fontes, animações e efeitos visuais da página
    # Alterar aqui pode quebrar completamente o design
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

        .stApp {
            background-color: #0b0b0b;  /* ✅ ALTERE: Cor de fundo (preto profundo) */
            color: #ffffff;  /* ✅ ALTERE: Cor do texto principal */
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            -webkit-font-smoothing: antialiased;
        }

        .nav-zajno {
            display: flex;
            justify-content: space-between;
            padding: 40px 60px;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 700;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            background: linear-gradient(180deg, rgba(11,11,11,1) 0%, rgba(11,11,11,0) 100%);
        }

        .nav-link {
            color: #ffffff;
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none;
            background: none;
            border: none;
            padding: 0;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 700;
            font-family: 'Inter', sans-serif;
        }

        .nav-link:hover {
            opacity: 0.6;
        }

        .hero-container {
            padding: 200px 60px 100px 60px;
        }
        
        .hero-title {
            font-size: clamp(40px, 12vw, 180px);
            font-weight: 900;
            line-height: 0.8;
            letter-spacing: -0.05em;
            text-transform: uppercase;
            margin-bottom: 60px;
        }

        .project-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2px;
            background-color: #1a1a1a;
            border-top: 1px solid #1a1a1a;
            border-bottom: 1px solid #1a1a1a;
        }

        .project-item {
            background-color: #0b0b0b;
            padding: 40px;
            position: relative;
            overflow: hidden;
            aspect-ratio: 16 / 9;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }

        .project-thumb {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            object-fit: cover;
            opacity: 0.4;
            transition: opacity 0.5s ease, transform 0.8s ease;
        }

        .project-item:hover .project-thumb {
            opacity: 0.8;
            transform: scale(1.05);
        }

        .project-meta {
            position: relative;
            z-index: 2;
        }

        .project-category {
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #888;
            margin-bottom: 10px;
        }

        .footer-zajno {
            padding: 100px 60px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-top: 1px solid #1a1a1a;
        }

        .big-footer-text {
            font-size: clamp(30px, 6vw, 80px);
            font-weight: 900;
            text-transform: uppercase;
            line-height: 0.9;
        }

        /* Botão Customizado */
        .btn-zajno {
            background: transparent !important;
            border: 1px solid #ffffff !important;
            color: #ffffff !important;
            border-radius: 0 !important;
            padding: 15px 40px !important;
            text-transform: uppercase !important;
            font-size: 12px !important;
            font-weight: 700 !important;
            letter-spacing: 2px !important;
            transition: 0.3s !important;
            cursor: pointer !important;
            font-family: 'Inter', sans-serif !important;
            text-decoration: none !important;
        }
        
        .btn-zajno:hover {
            background: #ffffff !important;
            color: #0b0b0b !important;
            text-decoration: none !important;
        }

        .btn-zajno:visited {
            color: #ffffff !important;
            text-decoration: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 1: NAVEGAÇÃO ==========
    # ❌ NÃO ALTERE: Estrutura de navegação fixa
    # ✅ ALTERE: Logo e textos de navegação
    st.markdown("""
    <div class="nav-zajno">
        <div>Zajno / Motion</div>
        <div style="display: flex; gap: 40px;">
            <a href="#trabalhos" class="nav-link" style="text-decoration: none; color: #ffffff;">Trabalhos</a>
            <a href="#estudio" class="nav-link" style="text-decoration: none; color: #ffffff;">Estúdio</a>
            <a href="#contato" class="nav-link" style="text-decoration: none; color: #ffffff;">Contato</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 2: HERO SECTION ==========
    # ✅ ALTERE: Conteúdo principal do hero
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">
            MOVIMENTO<br>É A NOSSA<br>LINGUAGEM
        </div>
        <div style="max-width: 500px; color: #888; font-size: 16px; line-height: 1.6;">
            Somos um estúdio de design focado em criar experiências digitais que ganham vida através do movimento e da tecnologia de ponta.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 3: SHOWCASE DE PROJETOS (GRID DUPLO) ==========
    # ❌ NÃO ALTERE: Estrutura de grid
    st.markdown('<div id="trabalhos" class="project-grid">', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.markdown("""
        <div class="project-item">
            <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800" class="project-thumb">
            <div class="project-meta">
                <p class="project-category">Motion Graphics / 2024</p>
                <h3 style="font-size: 30px; font-weight: 900; text-transform: uppercase;">Cyber Identity</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)  # ✅ ALTERE: Categoria, ano, título e imagem do projeto 1
        
        st.markdown("""
        <div class="project-item">
            <img src="https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=800" class="project-thumb">
            <div class="project-meta">
                <p class="project-category">Interface Design / 2023</p>
                <h3 style="font-size: 30px; font-weight: 900; text-transform: uppercase;">Liquid UI</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)  # ✅ ALTERE: Categoria, ano, título e imagem do projeto 2

    with col2:
        st.markdown("""
        <div class="project-item">
            <img src="https://images.unsplash.com/photo-1633167606207-d840b5070fc2?w=800" class="project-thumb">
            <div class="project-meta">
                <p class="project-category">Art Direction / 2024</p>
                <h3 style="font-size: 30px; font-weight: 900; text-transform: uppercase;">Astro Forms</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)  # ✅ ALTERE: Categoria, ano, título e imagem do projeto 3
        
        st.markdown("""
        <div class="project-item">
            <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800" class="project-thumb">
            <div class="project-meta">
                <p class="project-category">3D Animation / 2024</p>
                <h3 style="font-size: 30px; font-weight: 900; text-transform: uppercase;">Glass Echo</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)  # ✅ ALTERE: Categoria, ano, título e imagem do projeto 4

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 4: SEÇÃO DE TEXTO MANIFESTO ==========
    # ✅ ALTERE: Conteúdo do manifesto
    st.markdown("""
    <div id="estudio" style="padding: 150px 60px; border-bottom: 1px solid #1a1a1a;">
        <div style="max-width: 900px;">
            <h2 style="font-size: 50px; font-weight: 900; text-transform: uppercase; line-height: 1;">
                Nós não apenas movemos pixels. Nós contamos histórias que definem o futuro das marcas.
            </h2>
            <p style="margin-top: 40px; color: #888; font-size: 20px;">
                Trabalhamos com marcas audaciosas para transformar ideias complexas em interações digitais simples, memoráveis e impactantes.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 5: FOOTER (CALL TO ACTION) ==========
    # ✅ ALTERE: Conteúdo do footer
    st.markdown("""
    <div id="contato" class="footer-zajno">
        <div>
            <p style="color: #888; text-transform: uppercase; font-size: 10px; letter-spacing: 2px; margin-bottom: 20px;">Pronto para elevar sua marca?</p>
            <div class="big-footer-text">VAMOS<br>CRIAR JUNTOS</div>
        </div>
        <div style="text-align: right;">
            <p style="margin-bottom: 30px; color: #888;">studio@zajno.com</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="padding-left: 60px; padding-bottom: 100px;">', unsafe_allow_html=True)
    # ✅ ALTERE: Texto do botão e URL de destino
    st.markdown('''
    <a href="https://www.google.com/" target="_blank" class="btn-zajno" style="display: inline-block; text-decoration: none;">
        Iniciar Projeto
    </a>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 6: COPYRIGHT ==========
    # ✅ ALTERE: Informações de copyright
    st.markdown("""
    <div style="padding: 40px 60px; font-size: 10px; color: #444; border-top: 1px solid #1a1a1a; text-transform: uppercase; letter-spacing: 1px;">
        © 2026 Zajno Studio — São Francisco / Remoto
    </div>
    """, unsafe_allow_html=True)

    # ========== FIM DO TEMPLATE ==========
    # Lembre-se: Altere apenas o que tem ✅ ALTERE
    # Não mexa no que tem ❌ NÃO ALTERE

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template22" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

