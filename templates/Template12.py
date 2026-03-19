import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

def render():
    """Renderiza o template 12 - Crehana Clone"""
    
    # ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
    # ❌ NÃO ALTERE: Define as configurações básicas da página
    st.set_page_config(
        page_title="Crehana Clone | Cursos Online",  # ✅ ALTERE: Título que aparece na aba do navegador
        page_icon="🎓",  # ✅ ALTERE: Emoji que aparece na aba do navegador
        layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
    )

    # ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
    # ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
    # Alterar aqui pode quebrar completamente o design da página
    st.markdown("""
    <style>
        /* ❌ NÃO ALTERE: Importa a fonte do Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

        /* ❌ NÃO ALTERE: Tipografia padrão */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;  /* Fonte moderna */
            color: #1b1c1e;  /* Texto preto */
        }

        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { 
            display: none;  /* Oculta o header */
        }

        /* ❌ NÃO ALTERE: Header estilo app */
        .header-crehana {
            display: flex;  /* Layout flexível */
            justify-content: space-between;  /* Espaça itens nas extremidades */
            align-items: center;  /* Alinha itens no centro verticalmente */
            padding: 10px 0px;  /* Espaçamento interno */
            background-color: white;  /* Fundo branco */
            border-bottom: 1px solid #e0e0e0;  /* Borda inferior cinza clara */
            margin-bottom: 30px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Estilo do logo */
        .logo {
            font-size: 24px;  /* Tamanho grande */
            font-weight: 800;  /* Peso muito pesado */
            color: #4b22b4;  /* Roxo Crehana */
        }

        /* ❌ NÃO ALTERE: Estilo do título do hero */
        .hero-title {
            font-size: 42px;  /* Tamanho grande */
            font-weight: 800;  /* Peso muito pesado */
            line-height: 1.1;  /* Altura da linha compacta */
            margin-bottom: 20px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Destaque em roxo */
        .highlight {
            color: #4b22b4;  /* Roxo Crehana */
        }

        /* ❌ NÃO ALTERE: Estilo dos botões nativos do Streamlit */
        .stButton > button {
            border-radius: 8px;  /* Arredondamento suave */
            font-weight: 600;  /* Peso pesado */
            transition: all 0.2s;  /* Animação suave */
            border: none;  /* Sem borda */
        }
        
        /* ❌ NÃO ALTERE: Botão principal (roxo) */
        div.stButton > button {
            background-color: #4b22b4;  /* Fundo roxo */
            color: white;  /* Texto branco */
        }

        /* ❌ NÃO ALTERE: Cards de cursos */
        .course-card {
            background: white;  /* Fundo branco */
            border-radius: 12px;  /* Arredondamento suave */
            overflow: hidden;  /* Oculta conteúdo que sai da área */
            border: 1px solid #efefef;  /* Borda cinza clara */
            transition: transform 0.3s;  /* Animação suave */
            margin-bottom: 20px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos cards */
        .course-card:hover {
            transform: translateY(-5px);  /* Levanta o card */
            box-shadow: 0 10px 20px rgba(0,0,0,0.05);  /* Sombra aumentada */
        }
        
        /* ❌ NÃO ALTERE: Tag de categoria */
        .category-tag {
            font-size: 11px;  /* Tamanho muito pequeno */
            font-weight: 700;  /* Peso pesado */
            text-transform: uppercase;  /* Maiúsculas */
            color: #888;  /* Cor cinza */
            margin-bottom: 5px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Título do curso */
        .course-title {
            font-weight: 600;  /* Peso pesado */
            font-size: 16px;  /* Tamanho médio */
            margin-bottom: 8px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Avaliação do curso */
        .rating {
            color: #ffb400;  /* Cor amarela (estrela) */
            font-size: 14px;  /* Tamanho pequeno */
            font-weight: bold;  /* Peso pesado */
        }

        /* ❌ NÃO ALTERE: Estilo dos botões em links */
        .action-button {
            display: inline-block !important;  /* Exibe como bloco inline */
            background-color: #4b22b4 !important;  /* Fundo roxo */
            color: white !important;  /* Texto branco */
            border: none !important;  /* Sem borda */
            border-radius: 8px !important;  /* Arredondamento suave */
            padding: 12px 30px !important;  /* Espaçamento interno */
            font-weight: 600 !important;  /* Peso pesado */
            font-size: 14px !important;  /* Tamanho pequeno */
            text-transform: uppercase !important;  /* Maiúsculas */
            letter-spacing: 0.5px !important;  /* Espaçamento entre letras */
            transition: 0.3s !important;  /* Animação suave */
            text-decoration: none !important;  /* Remove sublinhado */
            cursor: pointer !important;  /* Cursor de clique */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
        .action-button:hover {
            background-color: #3a1a8a !important;  /* Fundo roxo escuro */
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
    col_l, col_m, col_r = st.columns([1, 2, 2])

    with col_l:
        # ✅ ALTERE: Nome da plataforma
        st.markdown('<div class="logo">crehana</div>', unsafe_allow_html=True)

    with col_m:
        # ✅ ALTERE: Menu de navegação
        st.markdown("""
        <div style="display: flex; gap: 20px; padding-top: 10px;">
            <a href="#categories" style="font-weight:600; font-size:14px; color: #1b1c1e; text-decoration: none; cursor: pointer;">Categorias</a>  <!-- ✅ ALTERE: Texto do menu -->
            <a href="#business" style="font-weight:600; font-size:14px; color: #1b1c1e; text-decoration: none; cursor: pointer;">Para Empresas</a>  <!-- ✅ ALTERE: Texto do menu -->
        </div>
        """, unsafe_allow_html=True)

    # ========== SEÇÃO 4: HERO SECTION ==========
    # ✅ ALTERE: Título, descrição, imagem e botão
    c_hero1, c_hero2 = st.columns([1, 1])

    with c_hero1:
        # ✅ ALTERE: Texto de destaque
        st.markdown('<p style="color:#4b22b4; font-weight:700;">MAIS DE 1000 CURSOS ONLINE</p>', unsafe_allow_html=True)
        
        # ✅ ALTERE: Título principal (com destaque em roxo)
        st.markdown('<h1 class="hero-title">Aumente suas <span class="highlight">oportunidades</span> profissionais</h1>', unsafe_allow_html=True)
        
        # ✅ ALTERE: Descrição
        st.write("Aprenda com especialistas as habilidades mais demandadas no mercado digital. Do zero ao avançado.")
        st.write("")
        
        # ✅ ALTERE: Texto do botão e URL
        st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">🎯 Explorar cursos agora</a>', unsafe_allow_html=True)

    with c_hero2:
        # ✅ ALTERE: URL da imagem do hero
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80", use_container_width=True)

    # ========== SEÇÃO 5: PERGUNTA ENGAJADORA ==========
    # ✅ ALTERE: Texto da pergunta
    st.write("### O que você quer estudar hoje?")

    # ========== SEÇÃO 6: CURSOS (GRID) ==========
    # ❌ NÃO ALTERE: Função que renderiza os cursos
    def course_item(col, img, category, title, rating, students):
        # ❌ NÃO ALTERE: Função que cria os cards de curso
        with col:
            st.markdown(f"""
            <div class="course-card">
                <!-- ✅ ALTERE: URL da imagem do curso -->
                <img src="{img}" style="width:100%; height:150px; object-fit:cover;">
                <!-- ✅ ALTERE: Categoria, título e avaliação -->
                <div style="padding: 15px;">
                    <div class="category-tag">{category}</div>  <!-- ✅ ALTERE: Categoria -->
                    <div class="course-title">{title}</div>  <!-- ✅ ALTERE: Título do curso -->
                    <div class="rating">★ {rating} <span style="color:#888; font-weight:400; font-size:12px;">({students})</span></div>  <!-- ✅ ALTERE: Avaliação e alunos -->
                </div>
            </div>
            """, unsafe_allow_html=True)
            # ✅ ALTERE: Texto do botão e URL
            st.markdown(f'<a href="https://www.google.com/" target="_blank" class="action-button" style="width: 100%; text-align: center; display: block;">Ver detalhes</a>', unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Primeira linha de cursos (4 colunas)
    col1, col2, col3, col4 = st.columns(4)

    course_item(col1, 
                "https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&w=400&q=80",
                "Marketing Digital",  # ✅ ALTERE: Categoria
                "Facebook Ads: Domine o Gerenciador",  # ✅ ALTERE: Título do curso
                "4.8",  # ✅ ALTERE: Avaliação
                "12k alunos")  # ✅ ALTERE: Número de alunos

    course_item(col2, 
                "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=400&q=80",
                "Design",  # ✅ ALTERE: Categoria
                "Adobe Illustrator: Ilustração Vetorial",  # ✅ ALTERE: Título do curso
                "4.9",  # ✅ ALTERE: Avaliação
                "45k alunos")  # ✅ ALTERE: Número de alunos

    course_item(col3, 
                "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=400&q=80",
                "Tecnologia",  # ✅ ALTERE: Categoria
                "Introdução ao Desenvolvimento Web",  # ✅ ALTERE: Título do curso
                "4.7",  # ✅ ALTERE: Avaliação
                "30k alunos")  # ✅ ALTERE: Número de alunos

    course_item(col4, 
                "https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&w=400&q=80",
                "Dados",  # ✅ ALTERE: Categoria
                "Excel para Negócios: Avançado",  # ✅ ALTERE: Título do curso
                "4.9",  # ✅ ALTERE: Avaliação
                "18k alunos")  # ✅ ALTERE: Número de alunos

    # ========== SEÇÃO 7: CREHANA PARA EMPRESAS ==========
    # ✅ ALTERE: Título, descrição, imagem e botão
    st.write("")
    st.write("---")

    with st.container():
        # ❌ NÃO ALTERE: Estrutura de 2 colunas
        ce1, ce2 = st.columns([1, 1])
        
        with ce1:
            # ✅ ALTERE: URL da imagem
            st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80", use_container_width=True)
        
        with ce2:
            # ✅ ALTERE: Título da seção
            st.markdown("## Treine sua equipe com a Crehana")
            
            # ✅ ALTERE: Descrição
            st.write("Soluções de SaaS e conteúdo para fechar a lacuna de habilidades na sua empresa.")
            
            # ✅ ALTERE: Features/benefícios
            st.write("✅ Planos de aprendizado personalizados")
            st.write("✅ Painel de controle para o RH")
            
            # ✅ ALTERE: Texto do botão e URL
            st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">🚀 Solicitar Demo</a>', unsafe_allow_html=True)

    # ========== SEÇÃO 8: FOOTER (RODAPÉ) ==========
    # ✅ ALTERE: Logo, descrição e copyright
    st.markdown("""
    <div style="background-color: #1b1c1e; color: white; padding: 60px 20px; margin-top: 50px; text-align: center;">
        <!-- ✅ ALTERE: Nome da plataforma -->
        <div style="font-size: 24px; font-weight: 800; margin-bottom: 20px;">crehana</div>
        <!-- ✅ ALTERE: Descrição e copyright -->
        <div style="color: #888; font-size: 14px;">
            Transformando o futuro através da educação. <br>
            © 2026 Crehana Inc. Todos os direitos reservados.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== FIM DO TEMPLATE ==========
    # Lembre-se: Altere apenas o que tem ✅ ALTERE
    # Não mexa no que tem ❌ NÃO ALTERE

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template12" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

