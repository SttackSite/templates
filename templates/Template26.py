import streamlit as st

def render():
    """Renderiza o template 26 - Dockyard Social"""

    # ❌ NÃO ALTERE: Importações necessárias para o funcionamento do Streamlit

    # ✅ ALTERE: Configuração da Página (Título, Ícone, Layout)
    st.set_page_config(
        page_title="Dockyard Social | Comida, Bebida & Vibe",  # ✅ ALTERE: Nome da página
        page_icon="🍔",    # ✅ ALTERE: Emoji do ícone
        layout="wide"                   # ❌ NÃO ALTERE
    )

    # ❌ NÃO ALTERE: Bloco de CSS
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=Oswald:wght@700&display=swap');

        :root {
            --dock-yellow: #ffcc00;  /* ✅ ALTERE: Cor principal */
            --dock-black: #111111;    /* ✅ ALTERE: Cor escura */
            --dock-white: #f4f4f4;    /* ✅ ALTERE: Cor de fundo */
        }

        .stApp { background-color: var(--dock-white); }

        h1, h2, h3, .impact-font {
            font-family: 'Oswald', sans-serif;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: -1px;
            line-height: 0.9;
        }

        .nav-dock {
            background-color: var(--dock-black);
            color: var(--dock-yellow);
            padding: 15px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .nav-link {
            color: var(--dock-yellow) !important;
            text-decoration: none !important;
            font-weight: bold;
            font-size: 14px;
            transition: 0.3s;
            cursor: pointer;
        }

        .nav-link:hover { opacity: 0.7; text-decoration: none !important; }
        .nav-link:visited { color: var(--dock-yellow) !important; text-decoration: none !important; }

        .hero-dock {
            background-color: var(--dock-yellow);
            padding: 80px 5%;
            border-bottom: 8px solid var(--dock-black);
            text-align: left;
        }

        .hero-h1 {
            font-size: clamp(60px, 12vw, 150px);
            color: var(--dock-black);
        }

        .dock-card {
            background: var(--dock-black);
            color: white;
            padding: 0;
            border-radius: 0px;
            transition: 0.3s;
            height: 100%;
            border: 4px solid var(--dock-black);
        }

        .dock-card:hover {
            transform: rotate(-1deg);
            border-color: var(--dock-yellow);
        }

        .card-content { padding: 25px; }

        div.stButton > button {
            background-color: var(--dock-black);
            color: var(--dock-yellow);
            border-radius: 0;
            padding: 20px 40px;
            font-family: 'Oswald', sans-serif;
            font-size: 24px;
            border: none;
            width: 100%;
            text-transform: uppercase;
            transition: 0.2s;
        }

        div.stButton > button:hover { background-color: #333; color: white; }

        .announcement {
            background: var(--dock-black);
            color: white;
            padding: 10px;
            font-weight: bold;
            text-align: center;
            letter-spacing: 2px;
        }

        .action-button {
            display: inline-block !important;
            background: var(--dock-black) !important;
            color: var(--dock-yellow) !important;
            border: none !important;
            padding: 15px 40px !important;
            font-family: 'Oswald', sans-serif !important;
            font-size: 14px !important;
            text-transform: uppercase !important;
            text-decoration: none !important;
            transition: 0.3s !important;
            cursor: pointer !important;
        }

        .action-button:hover { background-color: #333 !important; color: white !important; text-decoration: none !important; }
        .action-button:visited { color: var(--dock-yellow) !important; text-decoration: none !important; }

        [data-testid="stHeader"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 1: AVISO ==========
    st.markdown('<div class="announcement">ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO</div>', unsafe_allow_html=True)  # ✅ ALTERE: Texto do aviso

    # ========== SEÇÃO 2: NAVEGAÇÃO ==========
    st.markdown("""
    <div class="nav-dock">
        <div style="font-size: 32px; font-family: 'Oswald'; font-weight: 700;">DOCKYARD SOCIAL</div>
        <div style="display: flex; gap: 30px;">
            <a href="#oque-rola" class="nav-link">O QUE ROLA</a>
            <a href="#comida" class="nav-link">COMIDA</a>
            <a href="#bebida" class="nav-link">BEBIDA</a>
            <a href="#reservar" class="nav-link">RESERVAR</a>
        </div>
    </div>
    """, unsafe_allow_html=True)  # ✅ ALTERE: Logo e links de navegação

    # ========== SEÇÃO 3: HERO ==========
    st.markdown('<div class="hero-dock">', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-h1">COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.</h1>', unsafe_allow_html=True)  # ✅ ALTERE: Título principal
    st.markdown('<p style="font-size: 20px; font-weight: 900; color: #111; margin-top: 20px;">O melhor mercado de comida de rua de Glasgow, agora na sua tela.</p>', unsafe_allow_html=True)  # ✅ ALTERE: Subtítulo
    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 4: CARDS ==========
    st.write("")
    col1, col2, col3 = st.columns(3)

    def render_dock_card(col, title, subtitle, img_url, section_id):
        # ❌ NÃO ALTERE: Função que renderiza os cards
        with col:
            st.markdown(f"""
            <div id="{section_id}" class="dock-card">
                <img src="{img_url}" style="width:100%; filter: grayscale(20%);">
                <div class="card-content">
                    <h2 style="font-size: 40px; margin-bottom: 5px;">{title}</h2>
                    <p style="color: var(--dock-yellow); font-weight: bold; letter-spacing: 1px;">{subtitle}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ✅ ALTERE: Títulos, subtítulos e URLs das imagens dos cards
    render_dock_card(col1, "COMIDA", "10+ VENDEDORES", "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600", "section-1")
    render_dock_card(col2, "BEBIDA", "CRAFT BEER & COCKTAILS", "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600", "section-2")
    render_dock_card(col3, "EVENTOS", "MÚSICA AO VIVO", "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600", "section-3")

    # ========== SEÇÃO 5: SOBRE ==========
    st.markdown("""
    <div style="background-color: #111; color: white; padding: 100px 5%; margin-top: 50px;">
        <div style="max-width: 800px;">
            <h2 style="font-size: 60px; color: var(--dock-yellow); margin-bottom: 30px;">MAIS QUE UM MERCADO.</h2>
            <p style="font-size: 24px; line-height: 1.4; font-weight: 300;">A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos. Nós apoiamos talentos locais, reduzimos o desperdício e garantimos que a única coisa quente por aqui (além da comida) seja a hospitalidade.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)  # ✅ ALTERE: Título e parágrafo da seção sobre

    # ========== SEÇÃO 6: RESERVA / CTA ==========
    st.markdown("""
    <div id="reservar" style="background-color: var(--dock-yellow); color: #111; padding: 100px 5%; text-align: center;">
        <h2 style="font-size: 60px; margin-bottom: 30px;">PRONTO PARA VIVER A EXPERIÊNCIA?</h2>
        <p style="font-size: 20px; margin-bottom: 40px;">Garanta seu ingresso agora e venha fazer parte da melhor vibe de Glasgow.</p>
        <a href="https://www.google.com/" target="_blank" class="action-button" style="background: #111; color: var(--dock-yellow);">RESERVAR AGORA</a>
    </div>
    """, unsafe_allow_html=True)  # ✅ ALTERE: Título, descrição e botão de reserva

    # ========== SEÇÃO 7: FOOTER ==========
    st.markdown("""
    <div style="padding: 60px 5%; background: var(--dock-yellow); color: #111;">
        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
            <div>
                <h2 style="font-size: 40px;">DOCKYARD.</h2>
                <p>952 South St, Glasgow G14 0BX</p>
            </div>
            <div style="text-align: right; font-weight: bold;">
                <a href="https://www.google.com/" target="_blank" style="color: #111; text-decoration: none;">INSTAGRAM</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #111; text-decoration: none;">FACEBOOK</a> / 
                <a href="https://www.google.com/" target="_blank" style="color: #111; text-decoration: none;">TIKTOK</a>
                <br><a href="mailto:hello@dockyardsocial.com" style="color: #111; text-decoration: none;">HELLO@DOCKYARDSOCIAL.COM</a>
            </div>
        </div>
        <div style="margin-top: 40px; border-top: 2px solid #111; padding-top: 20px; font-size: 12px; font-weight: bold;">© 2026 DOCKYARD SOCIAL. SEMPRE REAL, NUNCA COPIADO.</div>
    </div>
    """, unsafe_allow_html=True)  # ✅ ALTERE: Endereço, redes sociais e email

    # ========== FIM DO TEMPLATE ==========
    # ✅ ALTERE apenas o que tem esse símbolo
    # ❌ NÃO ALTERE o que tem esse símbolo

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template26" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

