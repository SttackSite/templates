import streamlit as st

def render():
    # --- SISTEMA DE DESIGN AURA CREATIVE (PINK TEMPLATE) ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --aura-bg: #FFF5F7; /* Rosa muito suave, quase branco */
            --aura-pink-dark: #C6788B; /* Rosa queimado / Rosa Antigo */
            --aura-pink-light: #F7DEDF; /* Rosa claro para detalhes */
            --aura-purple: #8C56A3; /* Lavanda suave */
            --aura-text: #3D2C3F; /* Um marrom arroxeado para contraste */
            --aura-border: rgba(200, 150, 160, 0.2); /* Borda suave */
            --aura-glass: rgba(255, 255, 255, 0.6);
            --aura-glow-start: rgba(200, 100, 150, 0.1);
            --aura-glow-end: rgba(150, 80, 200, 0.1);
        }

        .stApp { 
            background-color: var(--aura-bg); 
            color: var(--aura-text);
            /* Gradientes de fundo para um efeito etéreo */
            background-image: 
                radial-gradient(at 0% 100%, var(--aura-glow-start) 0px, transparent 60%),
                radial-gradient(at 100% 0%, var(--aura-glow-end) 0px, transparent 60%);
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        /* --- TYPOGRAPHY --- */
        .aura-serif { font-family: 'Playfair Display', serif; }
        
        .aura-h1 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(45px, 9vw, 120px);
            font-weight: 700;
            line-height: 0.95;
            letter-spacing: -0.03em;
            margin-bottom: 40px;
            text-align: center;
            color: var(--aura-text);
        }

        .aura-h2 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(30px, 5vw, 60px);
            font-weight: 400;
            line-height: 1.1;
            margin-bottom: 30px;
            color: var(--aura-text);
        }

        .aura-label {
            font-size: 13px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--aura-pink-dark);
            margin-bottom: 20px;
            display: block;
            text-align: center;
        }

        /* --- NAVEGAÇÃO CHIC --- */
        .aura-nav {
            padding: 25px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            background: rgba(255, 245, 247, 0.9); /* BG mais transparente */
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--aura-border);
        }
        .aura-nav-link {
            font-size: 14px;
            font-weight: 500;
            letter-spacing: 0.05em;
            color: var(--aura-text);
            transition: color 0.3s;
        }
        .aura-nav-link:hover { color: var(--aura-pink-dark); }


        /* --- BOTÕES ORGÂNICOS --- */
        div.stButton > button {
            background: linear-gradient(135deg, var(--aura-pink-dark), var(--aura-purple)) !important;
            color: white !important;
            border: none !important;
            padding: 16px 45px !important;
            border-radius: 100px !important;
            font-size: 15px !important;
            font-weight: 600 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            box-shadow: 0 10px 20px rgba(198, 120, 139, 0.2);
        }

        div.stButton > button:hover {
            transform: translateY(-5px) scale(1.03);
            box-shadow: 0 15px 30px rgba(198, 120, 139, 0.3);
            filter: brightness(1.1);
        }

        /* --- CARDS DE PROJETOS (FLUID GLASS) --- */
        .aura-card {
            background: var(--aura-glass);
            backdrop-filter: blur(15px);
            border: 1px solid var(--aura-border);
            border-radius: 20px;
            padding: 40px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.4s ease;
            box-shadow: 0 8px 16px rgba(0,0,0,0.05);
        }
        .aura-card:hover {
            transform: translateY(-8px);
            border-color: var(--aura-pink-dark);
            box-shadow: 0 15px 25px rgba(198, 120, 139, 0.1);
        }

        .card-image-placeholder {
            width: 100%;
            height: 250px;
            background: var(--aura-pink-light);
            border-radius: 12px;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            color: var(--aura-pink-dark);
            font-weight: 600;
            overflow: hidden;
        }
        .card-image-placeholder img {
            width: 100%; height: 100%; object-fit: cover;
            transition: transform 0.5s ease;
        }
        .aura-card:hover .card-image-placeholder img { transform: scale(1.05); }

        /* --- SEÇÕES --- */
        .aura-section { padding: 120px 8%; }
        .text-center { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div class="aura-nav">
        <div class="aura-serif" style="font-weight: 700; font-size: 26px; letter-spacing: 1px; color: var(--aura-pink-dark);">Aura Creative</div>
        <div style="display: flex; gap: 40px;">
            <a href="#home" class="aura-nav-link">Home</a>
            <a href="#portfolio" class="aura-nav-link">Portfólio</a>
            <a href="#servicos" class="aura-nav-link">Serviços</a>
            <a href="#sobre" class="aura-nav-link">Sobre Mim</a>
            <a href="#contato" class="aura-nav-link" style="color: white; background: var(--aura-pink-dark); padding: 8px 20px; border-radius: 100px; margin-top: -8px;">Contato</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown('<div id="home" class="aura-section">', unsafe_allow_html=True)
    st.markdown('<span class="aura-label">Inspire. Crie. Transforme.</span>', unsafe_allow_html=True)
    st.markdown('<h1 class="aura-h1">Construa sua visão<br>com uma <span class="aura-serif" style="font-style:italic; color: var(--aura-purple);">Aura Única.</span></h1>', unsafe_allow_html=True)
    
    col_h1, col_h2, col_h3 = st.columns([1, 0.8, 1])
    with col_h2:
        st.button("MINHA JORNADA CRIATIVA")
    
    st.markdown("""
        <div style="margin-top: 80px; width: 100%; height: 60vh; border-radius: 30px; overflow: hidden; position: relative; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
            <img src="https://images.unsplash.com/photo-1579783900882-c0d3db7df3f2?w=1600" style="width: 100%; height: 100%; object-fit: cover;">
            <div style="position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); background: rgba(255,255,255,0.8); backdrop-filter: blur(8px); padding: 15px 30px; border-radius: 100px; font-weight: 500; color: var(--aura-text);">
                Design | Fotografia | Arte Digital
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PORTFÓLIO (GRID COM DETALHES) ---
    st.markdown('<div id="portfolio" class="aura-section" style="background: var(--aura-pink-light);">', unsafe_allow_html=True)
    st.markdown('<span class="aura-label">Meus Últimos Projetos</span>', unsafe_allow_html=True)
    st.markdown('<h2 class="aura-h2 text-center">Onde a visão ganha vida.</h2>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2, gap="large")
    
    with c1:
        st.markdown("""
        <div class="aura-card">
            <div>
                <div class="card-image-placeholder"><img src="https://images.unsplash.com/photo-1554988944-12e0222f281e?w=800"></div>
                <h3 class="aura-serif" style="font-size: 28px; margin-bottom: 10px;">Campanha "Florescer"</h3>
                <p style="color: var(--aura-text); font-size: 14px;">Identidade visual e estratégia digital para uma marca de beleza orgânica.</p>
            </div>
            <div style="text-align: right; margin-top: 30px;"><span style="color: var(--aura-purple); font-weight: 600;">Ver Projeto →</span></div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="aura-card">
            <div>
                <div class="card-image-placeholder"><img src="https://images.unsplash.com/photo-1520633458694-1a87752a7b1d?w=800"></div>
                <h3 class="aura-serif" style="font-size: 28px; margin-bottom: 10px;">Reimagining Webflow</h3>
                <p style="color: var(--aura-text); font-size: 14px;">Desenvolvimento de websites elegantes e funcionais para criativos.</p>
            </div>
            <div style="text-align: right; margin-top: 30px;"><span style="color: var(--aura-purple); font-weight: 600;">Explorar →</span></div>
        </div>
        """, unsafe_allow_html=True)

    # --- SEÇÃO DE SERVIÇOS (COM ÍCONES) ---
    st.markdown('<div id="servicos" class="aura-section">', unsafe_allow_html=True)
    st.markdown('<span class="aura-label">Como posso te ajudar?</span>', unsafe_allow_html=True)
    st.markdown('<h2 class="aura-h2 text-center">Serviços para sua marca brilhar.</h2>', unsafe_allow_html=True)
    
    col_s1, col_s2, col_s3 = st.columns(3, gap="large")
    
    def render_service_card(col, icon, title, desc):
        with col:
            st.markdown(f"""
            <div class="aura-card" style="text-align: center;">
                <div style="font-size: 40px; margin-bottom: 20px; color: var(--aura-purple);">✨</div>
                <h3 class="aura-serif" style="font-size: 26px; margin-bottom: 15px;">{title}</h3>
                <p style="color: var(--aura-text); font-size: 15px; line-height: 1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            
    render_service_card(col_s1, "✨", "Identidade Visual", "Criação de marcas autênticas que ressoam com seu público e sua essência.")
    render_service_card(col_s2, "📸", "Fotografia Profissional", "Imagens que contam histórias e elevam a percepção de valor do seu produto ou serviço.")
    render_service_card(col_s3, "💻", "Web Design Personalizado", "Websites intuitivos e esteticamente impecáveis, que convertem visitantes em clientes.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SOBRE MIM (NARRATIVA) ---
    st.markdown('<div id="sobre" class="aura-section" style="background: var(--aura-pink-light);">', unsafe_allow_html=True)
    c_about1, c_about2 = st.columns([1, 1], gap="large")
    with c_about1:
        st.markdown('<div style="height: 500px; background-image: url(\'https://images.unsplash.com/photo-1589148725841-e40d040a4555?w=800\'); background-size: cover; background-position: center; border-radius: 40px 10px 40px 10px;"></div>', unsafe_allow_html=True)
    with c_about2:
        st.markdown('<div style="padding-top: 50px;">', unsafe_allow_html=True)
        st.markdown('<span class="aura-label" style="text-align:left;">Minha História</span>', unsafe_allow_html=True)
        st.markdown('<h2 class="aura-h2">A paixão por criar,<br>em cada detalhe.</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 18px; line-height: 1.7; margin-bottom: 25px; color: var(--aura-text);">
            Desde pequena, soube que minha vida seria dedicada à arte e à beleza. Minha jornada no design começou com um lápis e um sonho, evoluindo para o mundo digital onde transformo ideias em experiências visuais cativantes.
        </p>
        <p style="font-size: 18px; line-height: 1.7; color: var(--aura-text);">
            Acredito no poder da estética para comunicar, inspirar e conectar.
        </p>
        """, unsafe_allow_html=True)
        st.button("CONHEÇA MAIS SOBRE MIM")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CTA FINAL ---
    st.markdown('<div class="aura-section text-center">', unsafe_allow_html=True)
    st.markdown('<h2 class="aura-h2">Pronta para elevar sua marca?</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 20px; margin-bottom: 40px; color: var(--aura-text);">Vamos criar algo mágico juntas. Sua história merece ser contada com design que inspira.</p>', unsafe_allow_html=True)
    st.button("AGENDE UMA CONSULTA GRATUITA")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div id="contato" style="background: var(--aura-text); color: white; padding: 100px 8% 50px 8%;">
        <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 60px; margin-bottom: 80px;">
            <div>
                <h3 class="aura-serif" style="font-size: 32px; margin-bottom: 20px;">Aura Creative.</h3>
                <p style="opacity: 0.7; max-width: 300px;">Transformando ideias em arte, com uma pitada de magia e muito profissionalismo.</p>
            </div>
            <div>
                <p style="font-weight: 600; margin-bottom: 25px;">NAVEGAR</p>
                <ul style="list-style: none; padding: 0; opacity: 0.6; line-height: 2.5; font-size: 14px;">
                    <li>Home</li>
                    <li>Portfólio</li>
                    <li>Serviços</li>
                    <li>Blog</li>
                </ul>
            </div>
            <div>
                <p style="font-weight: 600; margin-bottom: 25px;">CONECTAR</p>
                <ul style="list-style: none; padding: 0; opacity: 0.6; line-height: 2.5; font-size: 14px;">
                    <li>Instagram</li>
                    <li>Behance</li>
                    <li>LinkedIn</li>
                    <li>Email</li>
                </ul>
            </div>
        </div>
        <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 40px; display: flex; justify-content: space-between; font-size: 12px; opacity: 0.4;">
            <span>© 2026 AURA CREATIVE. TODOS OS DIREITOS RESERVADOS.</span>
            <span>POLÍTICA DE PRIVACIDADE | TERMOS DE SERVIÇO</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Aura Creative | Design & Arte")
    render()
