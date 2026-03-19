import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

def render():
    """Renderiza o template 11 - Pura Vida Brackets"""
    
    # ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
    # ❌ NÃO ALTERE: Define as configurações básicas da página
    st.set_page_config(
        page_title="Pura Vida Brackets | Estilo de Vida",  # ✅ ALTERE: Título que aparece na aba do navegador
        page_icon="🌸",  # ✅ ALTERE: Emoji que aparece na aba do navegador
        layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
    )

    # ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
    # ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
    # Alterar aqui pode quebrar completamente o design da página
    st.markdown("""
    <style>
        /* ❌ NÃO ALTERE: Importa as fontes do Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Pacifico&display=swap');

        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { 
            display: none;  /* Oculta o header */
        }

        /* ❌ NÃO ALTERE: Barra de anúncio no topo */
        .announcement-bar {
            background-color: #ffb6c1;  /* Fundo rosa claro */
            color: white;  /* Texto branco */
            text-align: center;  /* Texto centralizado */
            padding: 8px;  /* Espaçamento interno */
            font-size: 13px;  /* Tamanho pequeno */
            font-weight: bold;  /* Peso pesado */
            letter-spacing: 1px;  /* Espaçamento entre letras */
            margin: -5rem -5rem 2rem -5rem;  /* Margem negativa para ocupar tela toda */
        }

        /* ❌ NÃO ALTERE: Container do logo */
        .logo-container {
            text-align: center;  /* Texto centralizado */
            font-family: 'Pacifico', cursive;  /* Fonte cursiva elegante */
            font-size: 45px;  /* Tamanho grande */
            color: #333;  /* Cor cinza escuro */
            margin-bottom: 20px;  /* Espaçamento inferior */
        }

        /* ❌ NÃO ALTERE: Menu de navegação */
        .nav-links {
            display: flex;  /* Layout flexível */
            justify-content: center;  /* Centraliza horizontalmente */
            gap: 30px;  /* Espaçamento entre itens */
            border-bottom: 1px solid #eee;  /* Borda inferior cinza clara */
            padding-bottom: 15px;  /* Espaçamento interno inferior */
            margin-bottom: 30px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Estilo dos links do menu */
        .nav-links a {
            text-decoration: none;  /* Remove sublinhado */
            color: #555;  /* Cor cinza */
            font-weight: 600;  /* Peso pesado */
            font-size: 14px;  /* Tamanho pequeno */
            text-transform: uppercase;  /* Maiúsculas */
        }

        /* ❌ NÃO ALTERE: Box do hero */
        .hero-box {
            position: relative;  /* Posicionamento relativo */
            text-align: center;  /* Texto centralizado */
            color: white;  /* Texto branco */
            margin-bottom: 40px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Texto do hero */
        .hero-text {
            position: absolute;  /* Posicionamento absoluto */
            top: 50%;  /* Posição no meio verticalmente */
            left: 50%;  /* Posição no meio horizontalmente */
            transform: translate(-50%, -50%);  /* Centraliza o elemento */
            background: rgba(255, 255, 255, 0.8);  /* Fundo branco semi-transparente */
            padding: 30px;  /* Espaçamento interno */
            border-radius: 5px;  /* Arredondamento suave */
            color: #333;  /* Texto cinza escuro */
        }

        /* ❌ NÃO ALTERE: Box do produto */
        .product-box {
            text-align: center;  /* Texto centralizado */
            margin-bottom: 30px;  /* Espaçamento inferior */
        }
        
        /* ❌ NÃO ALTERE: Preço do produto */
        .product-price {
            color: #ff69b4;  /* Cor rosa quente */
            font-weight: bold;  /* Peso pesado */
        }
        
        /* ❌ NÃO ALTERE: Estilo dos botões nativos do Streamlit */
        div.stButton > button {
            background-color: #333;  /* Fundo cinza escuro */
            color: white;  /* Texto branco */
            border-radius: 0px;  /* Sem arredondamento */
            padding: 10px 20px;  /* Espaçamento interno */
            width: 100%;  /* Largura total */
            border: none;  /* Sem borda */
            text-transform: uppercase;  /* Maiúsculas */
            letter-spacing: 1px;  /* Espaçamento entre letras */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos botões */
        div.stButton > button:hover {
            background-color: #ffb6c1;  /* Fundo rosa claro */
            color: white;  /* Texto branco */
        }

        /* ❌ NÃO ALTERE: Estilo dos botões em links */
        .action-button {
            display: inline-block !important;  /* Exibe como bloco inline */
            background-color: #333 !important;  /* Fundo cinza escuro */
            color: white !important;  /* Texto branco */
            border: none !important;  /* Sem borda */
            border-radius: 0px !important;  /* Sem arredondamento */
            padding: 12px 30px !important;  /* Espaçamento interno */
            font-weight: 600 !important;  /* Peso pesado */
            font-size: 13px !important;  /* Tamanho pequeno */
            text-transform: uppercase !important;  /* Maiúsculas */
            letter-spacing: 1px !important;  /* Espaçamento entre letras */
            transition: 0.3s !important;  /* Animação suave */
            text-decoration: none !important;  /* Remove sublinhado */
            cursor: pointer !important;  /* Cursor de clique */
        }
        
        /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
        .action-button:hover {
            background-color: #ffb6c1 !important;  /* Fundo rosa claro */
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

    # ========== SEÇÃO 3: BARRA DE ANÚNCIO ==========
    # ✅ ALTERE: Texto do anúncio
    st.markdown('<div class="announcement-bar">FRETE GRÁTIS EM PEDIDOS ACIMA DE R$ 150! 🌴</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 4: LOGO E MENU ==========
    # ✅ ALTERE: Nome da marca
    st.markdown('<div class="logo-container">Pura Vida</div>', unsafe_allow_html=True)

    # ✅ ALTERE: Menu de navegação
    st.markdown("""
    <div class="nav-links">
        <a href="#bracelets" style="color: #555; text-decoration: none; cursor: pointer;">Pulseiras</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#jewelry" style="color: #555; text-decoration: none; cursor: pointer;">Joias</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#collections" style="color: #555; text-decoration: none; cursor: pointer;">Coleções</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#sale" style="color: #555; text-decoration: none; cursor: pointer;">Sale</a>  <!-- ✅ ALTERE: Texto do menu -->
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 5: HERO BANNER ==========
    # ✅ ALTERE: URL da imagem do hero
    hero_img = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1500&q=80"
    st.image(hero_img, use_container_width=True)

    # ✅ ALTERE: Título e descrição do hero
    st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <!-- ✅ ALTERE: Título principal -->
        <h1 style="font-family: 'Montserrat'; font-weight: 300;">VIVA O MOMENTO</h1>
        <!-- ✅ ALTERE: Descrição -->
        <p style="color: #777; max-width: 600px; margin: auto;">
            Nossas peças são feitas à mão por artesãos ao redor do mundo, espalhando a energia "Pura Vida".
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 6: GRID DE PRODUTOS ==========
    # ✅ ALTERE: Título da seção
    st.markdown('<div id="bracelets"></div>', unsafe_allow_html=True)  # ❌ NÃO ALTERE: ID para navegação
    st.subheader("Novidades")

    # ❌ NÃO ALTERE: Estrutura de 4 colunas
    col1, col2, col3, col4 = st.columns(4)

    # ❌ NÃO ALTERE: Função que renderiza os produtos
    def product_item(col, name, price, img_url):
        # ❌ NÃO ALTERE: Função que cria os cards de produto
        with col:
            # ✅ ALTERE: URL da imagem do produto
            st.image(img_url, use_container_width=True)
            # ✅ ALTERE: Nome do produto
            st.markdown(f"**{name}**")
            # ✅ ALTERE: Preço do produto
            st.markdown(f'<p class="product-price">R$ {price}</p>', unsafe_allow_html=True)
            # ✅ ALTERE: Texto do botão e URL
            st.markdown(f'<a href="https://www.google.com/" target="_blank" class="action-button" style="width: 100%; text-align: center; display: block;">Adicionar</a>', unsafe_allow_html=True)

    # ✅ ALTERE: Produto 1 - Imagem, nome e preço
    product_item(col1, "Pack Shoreline", "45,00", "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?auto=format&fit=crop&w=400&q=80")

    # ✅ ALTERE: Produto 2 - Imagem, nome e preço
    product_item(col2, "Ocean Blue", "32,00", "https://images.unsplash.com/photo-1573408301185-9146fe634ad0?auto=format&fit=crop&w=400&q=80")

    # ✅ ALTERE: Produto 3 - Imagem, nome e preço
    product_item(col3, "Sunset Vibes", "38,00", "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=400&q=80")

    # ✅ ALTERE: Produto 4 - Imagem, nome e preço
    product_item(col4, "Sand & Salt", "29,00", "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=400&q=80")

    st.write("---")

    # ========== SEÇÃO 7: IMPACTO SOCIAL ==========
    # ✅ ALTERE: Título, descrição, imagem e botão
    c1, c2 = st.columns([1, 1])

    with c1:
        # ✅ ALTERE: URL da imagem
        st.image("https://images.unsplash.com/photo-1484820540004-14229fe36ca4?auto=format&fit=crop&w=800&q=80")

    with c2:
        # ✅ ALTERE: Título da seção
        st.markdown("### Retribuindo ao Planeta")
        
        # ✅ ALTERE: Descrição
        st.write("Cada compra ajuda a apoiar causas ambientais e artesãos locais. Já doamos mais de R$ 4 milhões para instituições de caridade através de vocês.")
        
        # ✅ ALTERE: Texto do botão e URL
        st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">Saiba Mais</a>', unsafe_allow_html=True)

    # ========== SEÇÃO 8: FOOTER (RODAPÉ) ==========
    # ✅ ALTERE: Logo, descrição e copyright
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 50px; margin-top: 50px; text-align: center; border-top: 1px solid #eee;">
        <!-- ✅ ALTERE: Nome da marca -->
        <div style="font-family: 'Pacifico'; font-size: 24px; color: #333; margin-bottom: 20px;">Pura Vida</div>
        <!-- ✅ ALTERE: Copyright e redes sociais -->
        <p style="color: #999; font-size: 12px;">© 2026 Pura Vida Brackets. Siga-nos no Instagram <a href="https://www.google.com/" target="_blank" style="color: #999; text-decoration: none;">@puravida</a></p>
    </div>
    """, unsafe_allow_html=True)

    # ========== FIM DO TEMPLATE ==========
    # Lembre-se: Altere apenas o que tem ✅ ALTERE
    # Não mexa no que tem ❌ NÃO ALTERE

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template11" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

