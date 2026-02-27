import streamlit as st

def render():
    """Renderiza o template 21 - Feastables"""
    
    # ❌ NÃO ALTERE: Configuração da página (define título, ícone e layout)
    st.set_page_config(
        page_title="Feastables | O Chocolate do Mrmoon",  # ✅ ALTERE: Nome da página
        page_icon="🍫",  # ✅ ALTERE: Emoji do ícone
        layout="wide"  # ❌ NÃO ALTERE: Layout da página
    )

    # ❌ NÃO ALTERE: Bloco CSS - Define todas as cores, fontes e efeitos visuais
    # Alterar aqui pode quebrar completamente o design
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bungee&family=Inter:wght@700;900&display=swap');

        /* ✅ ALTERE: Cores da marca */
        :root {
            --feast-blue: #0047ff;      /* Cor azul principal */
            --feast-pink: #ff00ff;      /* Cor rosa/magenta */
            --feast-yellow: #ffff00;    /* Cor amarela */
        }

        /* ❌ NÃO ALTERE: Fundo da aplicação */
        .stApp {
            background-color: var(--feast-blue);
        }

        /* ❌ NÃO ALTERE: Tipografia dos títulos */
        h1, h2, .font-heavy {
            font-family: 'Inter', sans-serif;
            font-weight: 900;
            text-transform: uppercase;
            color: white;
            letter-spacing: -2px;
        }

        /* ❌ NÃO ALTERE: Banner animado (marquee) */
        .marquee {
            background: var(--feast-yellow);
            color: black;
            padding: 10px 0;
            font-family: 'Inter', sans-serif;
            font-weight: 900;
            white-space: nowrap;
            overflow: hidden;
            display: flex;
            font-size: 20px;
            border-bottom: 4px solid black;
        }

        /* ❌ NÃO ALTERE: Seção hero */
        .hero-feast {
            padding: 60px 5%;
            text-align: center;
        }

        /* ❌ NÃO ALTERE: Cards de produto */
        .product-card {
            background: white;
            border: 4px solid black;
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            transition: transform 0.2s;
            box-shadow: 8px 8px 0px 0px rgba(0,0,0,1);
            margin-bottom: 30px;
        }
        .product-card:hover {
            transform: translate(-4px, -4px);
            box-shadow: 12px 12px 0px 0px rgba(255, 0, 255, 0.8);
        }

        /* ✅ ALTERE: Estilo da tag de preço */
        .price-tag {
            background: var(--feast-pink);
            color: white;
            padding: 5px 15px;
            border-radius: 50px;
            display: inline-block;
            font-weight: 900;
            margin-top: 10px;
        }

        /* ❌ NÃO ALTERE: Estilo dos botões nativos do Streamlit */
        div.stButton > button {
            background-color: var(--feast-yellow);
            color: black;
            border: 4px solid black;
            border-radius: 12px;
            font-weight: 900;
            font-size: 24px;
            padding: 20px 40px;
            box-shadow: 6px 6px 0px 0px rgba(0,0,0,1);
            transition: 0.1s;
            width: 100%;
            text-transform: uppercase;
        }
        div.stButton > button:hover {
            background-color: var(--feast-pink);
            color: white;
            transform: translate(2px, 2px);
            box-shadow: 2px 2px 0px 0px rgba(0,0,0,1);
        }

        /* ❌ NÃO ALTERE: Estilo dos botões em links */
        .action-button {
            display: inline-block !important;
            background-color: var(--feast-yellow) !important;
            color: black !important;
            border: 4px solid black !important;
            border-radius: 12px !important;
            font-weight: 900 !important;
            font-size: 24px !important;
            padding: 20px 40px !important;
            box-shadow: 6px 6px 0px 0px rgba(0,0,0,1) !important;
            transition: 0.1s !important;
            text-transform: uppercase !important;
            text-decoration: none !important;
            cursor: pointer !important;
        }
        .action-button:hover {
            background-color: var(--feast-pink) !important;
            color: white !important;
            transform: translate(2px, 2px) !important;
            box-shadow: 2px 2px 0px 0px rgba(0,0,0,1) !important;
            text-decoration: none !important;
        }
        .action-button:visited {
            color: black !important;
            text-decoration: none !important;
        }

        /* ❌ NÃO ALTERE: Rodapé */
        .footer-feast {
            background: black;
            color: white;
            padding: 60px 5%;
            margin-top: 100px;
        }
        
        /* ❌ NÃO ALTERE: Esconde header padrão do Streamlit */
        [data-testid="stHeader"] { display: none; }
    </style>

    <!-- ❌ NÃO ALTERE: Banner animado (marquee) -->
    <div class="marquee">
        <div style="display: flex; animation: marquee 20s linear infinite;">
            <span style="margin-right: 50px;">MELHOR QUE O SEU CHOCOLATE ATUAL 🔥</span>
            <span style="margin-right: 50px;">INGREDIENTES REAIS 🔥</span>
            <span style="margin-right: 50px;">DO MR MOON 🔥</span>
            <span style="margin-right: 50px;">PROVE A DIFERENÇA 🔥</span>
            <span style="margin-right: 50px;">MELHOR QUE O SEU CHOCOLATE ATUAL 🔥</span>
        </div>
    </div>

    <style>
    @keyframes marquee {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    </style>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 1: HEADER / LOGO ==========
    # ✅ ALTERE: Título principal e texto
    st.markdown("""
    <div style="text-align: center; padding: 40px 0;">
        <h1 style="font-size: 80px; text-shadow: 4px 4px 0px #ff00ff;">FEASTABLES</h1>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 2: HERO IMAGE & CTA ==========
    # ❌ NÃO ALTERE: Estrutura de colunas
    col_hero_1, col_hero_2 = st.columns([1, 1])

    with col_hero_1:
        # ✅ ALTERE: Título e descrição do hero
        st.markdown("""
        <div style="padding-top: 50px;">
            <h2 style="font-size: 60px;">O CHOCOLATE<br>QUE DETONA.</h2>
            <p style="color: white; font-size: 20px; font-weight: 700;">Zero porcaria. Apenas sabor épico.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # ❌ NÃO ALTERE: Botão com funcionalidade
        # Usa link em vez de st.button para ter controle total do estilo
        st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">COMPRE AGORA</a>', unsafe_allow_html=True)  # ✅ ALTERE: Texto do botão e URL

    with col_hero_2:
        # ✅ ALTERE: URL da imagem do hero
        st.image("https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=800", use_container_width=True)

    # ========== SEÇÃO 3: PRODUTOS (LOJA) ==========
    # ✅ ALTERE: Título da seção
    st.markdown("<br><br><h2 style='text-align: center; font-size: 45px;'>ESCOLHA SEU TIME</h2>", unsafe_allow_html=True)

    # ❌ NÃO ALTERE: Estrutura de colunas para produtos
    p1, p2, p3 = st.columns(3)

    def feast_card(col, title, flavor, img_url, price):
        # ❌ NÃO ALTERE: Função que renderiza os cards de produto
        with col:
            st.markdown(f"""
            <div class="product-card">
                <img src="{img_url}" style="width:100%; border-radius:10px;">
                <h3 style="color: black; margin-top: 15px; font-weight: 900; font-size: 24px;">{title}</h3>
                <p style="color: #555; font-weight: 700;">{flavor}</p>
                <div class="price-tag">R$ {price}</div>
            </div>
            """, unsafe_allow_html=True)
            # ✅ ALTERE: Texto do botão e URL
            st.markdown(f'<a href="https://www.google.com/" target="_blank" class="action-button">ADICIONAR {title}</a>', unsafe_allow_html=True)

    # ✅ ALTERE: Títulos, sabores, URLs de imagens e preços dos produtos
    feast_card(p1, "MILK CRUNCH", "Com Arroz Crocante", "https://images.unsplash.com/photo-1548907040-4baa42d10919?w=400", "19,90")
    feast_card(p2, "ORIGINAL MILK", "Clássico e Cremoso", "https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=400", "18,90")
    feast_card(p3, "PEANUT BUTTER", "Manteiga de Amendoim", "https://images.unsplash.com/photo-1581798459219-318e76aecc7b?w=400", "22,90")

    # ========== SEÇÃO 4: SEÇÃO "POR QUE NÓS?" ==========
    # ✅ ALTERE: Título, descrição e ícones
    st.markdown("""
    <div style="background-color: #ff00ff; padding: 100px 10%; margin-top: 80px; border-top: 5px solid black; border-bottom: 5px solid black;">
        <h2 style="color: white; font-size: 50px; text-align: center;">O QUE TEM DENTRO IMPORTA.</h2>
        <div style="display: flex; justify-content: space-around; margin-top: 50px; text-align: center; flex-wrap: wrap;">
            <div style="max-width: 250px;">
                <h1 style="font-size: 60px;">🌾</h1>
                <h3 style="color: white;">SEM GLÚTEN</h3>
            </div>
            <div style="max-width: 250px;">
                <h1 style="font-size: 60px;">🌱</h1>
                <h3 style="color: white;">INGREDIENTES SIMPLES</h3>
            </div>
            <div style="max-width: 250px;">
                <h1 style="font-size: 60px;">👅</h1>
                <h3 style="color: white;">SABOR INCRÍVEL</h3>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 5: FOOTER ==========
    # ✅ ALTERE: Informações do rodapé, links e copyright
    st.markdown("""
    <div class="footer-feast">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
            <div>
                <h2 style="font-size: 32px; text-shadow: 2px 2px 0px #ff00ff;">FEASTABLES</h2>
                <p style="color: #aaa;">Inspirado pelo Mrmoon.</p>
            </div>
            <div style="line-height: 2;">
                <p><strong>RECURSOS</strong></p>
                <a href="https://www.google.com/" target="_blank" style="color: #aaa; text-decoration: none;">Onde Comprar</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #aaa; text-decoration: none;">Perguntas Frequentes</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #aaa; text-decoration: none;">Termos de Uso</a>
            </div>
            <div>
                <p><strong>NOS SIGA</strong></p>
                <a href="https://www.google.com/" target="_blank" style="color: #aaa; text-decoration: none;">TikTok</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #aaa; text-decoration: none;">Instagram</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #aaa; text-decoration: none;">YouTube</a>
            </div>
        </div>
        <div style="margin-top: 50px; border-top: 1px solid #333; padding-top: 20px; font-size: 12px; color: #666; text-align: center;">
            © 2026 FEASTABLES INC. TODOS OS DIREITOS RESERVADOS.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== FIM DO TEMPLATE ==========
    # Lembre-se: Altere apenas o que tem ✅ ALTERE
    # Não mexa no que tem ❌ NÃO ALTERE
