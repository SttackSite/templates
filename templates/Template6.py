import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Site Pro | Excellence in Design",
    page_icon="⚖️",
    layout="wide"
)

# --- CSS DE PRESTÍGIO (ESTILO LOCATELLI ADV) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

    :root {
        --primary-gold: #c5a059;
        --navy-dark: #0a1128;
        --soft-white: #fcfcfc;
        --text-gray: #4a4a4a;
    }

    .stApp {
        background-color: var(--soft-white);
        color: var(--text-gray);
    }
    
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* Tipografia de Prestígio */
    h1, h2, .title-font {
        font-family: 'Cinzel', serif;
        color: var(--navy-dark);
        letter-spacing: 2px;
        font-weight: 400;
    }

    .serif-body {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 22px;
    }

    /* 1 & 2. HERO - O MANIFESTO */
    .hero-luxury {
        height: 85vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), 
                    url('https://www.transparenttextures.com/patterns/white-diamond.png');
        border-bottom: 1px solid rgba(197, 160, 89, 0.3);
        padding: 0 10%;
    }

    .hero-h1 { font-size: clamp(35px, 5vw, 65px); margin-bottom: 30px; line-height: 1.2; }
    .hero-line { width: 80px; height: 2px; background: var(--primary-gold); margin-bottom: 30px; }

    /* 3 & 4. TEMPLATES - COLEÇÃO EXCLUSIVA */
    .exclusive-card {
        padding: 0;
        background: white;
        border: 1px solid #eee;
        transition: 0.5s ease;
    }
    .exclusive-card:hover {
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        border-color: var(--primary-gold);
    }
    .card-meta {
        padding: 30px;
        text-align: center;
    }

    /* 6. É PARA VOCÊ QUE - PILARES */
    .pillar-box {
        text-align: center;
        padding: 40px;
        border-right: 1px solid #eee;
    }
    .pillar-box:last-child { border-right: none; }

    /* 7. PASSO A PASSO - A JORNADA */
    .step-box-luxury {
        border-left: 1px solid var(--primary-gold);
        padding: 0 0 40px 30px;
        margin-left: 20px;
    }

    /* 8. PREÇOS - INVESTIMENTO */
    .price-box {
        background: var(--navy-dark);
        color: white;
        padding: 60px 40px;
        text-align: center;
        border: 1px solid var(--primary-gold);
    }

    /* Botão de Alfaiataria */
    div.stButton > button {
        background: transparent;
        color: var(--navy-dark);
        border: 1px solid var(--navy-dark);
        padding: 12px 35px;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 0;
        transition: 0.4s;
    }
    div.stButton > button:hover {
        background: var(--navy-dark);
        color: var(--primary-gold);
        border-color: var(--navy-dark);
    }
</style>
""", unsafe_allow_html=True)

# --- 1 & 2. HERO SECTION ---
st.markdown("""
<div class="hero-luxury">
    <div class="hero-line"></div>
    <h1 class="hero-h1">A ARTE DA PRESENÇA<br>DIGITAL IMPECÁVEL</h1>
    <p class="serif-body" style="max-width: 850px; color: var(--text-gray); margin-bottom: 40px;">
        Seu site profissional em minutos, com a sofisticação de um projeto feito sob medida. 
        Escolha entre templates de alta conversão e eleve o padrão do seu negócio.
    </p>
""", unsafe_allow_html=True)
st.button("CONHEÇA A COLEÇÃO")
st.markdown("</div>", unsafe_allow_html=True)

# --- 3 & 4. TEMPLATES (SHOWCASE MINIMALISTA) ---
st.markdown('<div style="padding: 100px 10%;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; margin-bottom: 80px;">CURADORIA DE DESIGN</h2>', unsafe_allow_html=True)

t_col1, t_col2, t_col3 = st.columns(3)

def render_luxury_item(col, name, style, img):
    with col:
        st.markdown(f"""
        <div class="exclusive-card">
            <img src="{img}" style="width:100%; height:350px; object-fit:cover; grayscale(100%);">
            <div class="card-meta">
                <p style="font-size: 11px; letter-spacing: 3px; color: var(--primary-gold); font-weight: 600;">{style}</p>
                <h3 style="font-family: 'Cinzel'; margin: 15px 0;">{name}</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"SOLICITAR PREVIEW: {name.split()[0]}", key=name)

render_luxury_item(t_col1, "ESTATES & CO", "MINIMALIST LUXURY", "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600")
render_luxury_item(t_col2, "SILICON VALLEY", "HIGH-TECH CORPORATE", "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600")
render_luxury_item(t_col3, "THE ARTISAN", "EDITORIAL STYLE", "https://images.unsplash.com/photo-1434626881859-194d67b2b86f?w=600")
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PROVA SOCIAL (DISCRETA) ---
st.markdown("""
<div style="padding: 60px 10%; background: #f4f4f4; text-align: center; border-top: 1px solid #eee;">
    <p style="letter-spacing: 4px; font-size: 12px; margin-bottom: 30px;">CONFIADO POR LÍDERES DE MERCADO</p>
    <div style="display: flex; justify-content: center; gap: 60px; opacity: 0.6; grayscale(100%);">
        <span style="font-family: 'Cinzel'; font-size: 20px;">FORBES</span>
        <span style="font-family: 'Cinzel'; font-size: 20px;">VOGUE</span>
        <span style="font-family: 'Cinzel'; font-size: 20px;">TECH CRUNCH</span>
        <span style="font-family: 'Cinzel'; font-size: 20px;">ESTATE</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. É PARA VOCÊ QUE ---
st.markdown('<div style="padding: 100px 10%; background: white;">', unsafe_allow_html=True)
st_col1, st_col2, st_col3 = st.columns(3)

with st_col1:
    st.markdown('<div class="pillar-box"><h3>EXCELÊNCIA</h3><p>Para quem não aceita nada menos que o melhor design do mercado.</p></div>', unsafe_allow_html=True)
with st_col2:
    st.markdown('<div class="pillar-box"><h3>ESCALA</h3><p>Ideal para profissionais que vendem sites de alto valor para clientes exigentes.</p></div>', unsafe_allow_html=True)
with st_col3:
    st.markdown('<div class="pillar-box"><h3>LEGADO</h3><p>Construa uma autoridade digital que dure décadas, não apenas semanas.</p></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 7. PASSO A PASSO (A METODOLOGIA) ---
st.markdown('<div style="padding: 100px 15%;">', unsafe_allow_html=True)
st.markdown('<h2>O PROTOCOLO DE EXCUÇÃO</h2><br><br>', unsafe_allow_html=True)

def render_step_luxury(title, desc):
    st.markdown(f"""
    <div class="step-box-luxury">
        <h4 style="font-family: 'Cinzel'; color: var(--navy-dark);">{title}</h4>
        <p style="font-size: 16px; opacity: 0.8; max-width: 600px;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

render_step_luxury("ADQUIRA SUA LICENÇA", "Acesso imediato à nossa biblioteca restrita de templates de alto padrão.")
render_step_luxury("PERSONALIZAÇÃO GUIADA", "Ajuste cada detalhe para refletir a identidade única da sua marca.")
render_step_luxury("INFRAESTRUTURA DE ELITE", "Te ensinamos a hospedar seu projeto com máxima segurança e velocidade.")
render_step_luxury("LANÇAMENTO ESTRATÉGICO", "Seu site entra no ar como um ativo de prestígio para seu negócio.")
st.markdown('</div>', unsafe_allow_html=True)

# --- 8. PREÇOS (O INVESTIMENTO) ---
st.markdown('<div style="padding: 100px 10%; background: var(--navy-dark); color: white;">', unsafe_allow_html=True)
st.markdown('<h2 style="color: white; text-align: center;">INVESTIMENTO</h2><br><br>', unsafe_allow_html=True)

p1, p2, p3 = st.columns(3)

with p2: # Featured
    st.markdown("""
    <div class="price-box">
        <h3 style="color: var(--primary-gold);">PRESTIGE PASS</h3>
        <h1 style="font-size: 60px; margin: 30px 0; color: white;">R$ 297</h1>
        <p>Acesso Completo à Curadoria</p>
        <p>Suporte Concierge</p>
        <p>Licença de Revenda Premium</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("ADQUIRIR PRESTIGE", key="p2")

with p1:
    st.markdown("""
    <div class="price-box" style="background: transparent; border: 1px solid rgba(255,255,255,0.1);">
        <h3 style="color: white;">ESSENTIAL</h3>
        <h1 style="font-size: 50px; margin: 30px 0; color: white;">R$ 147</h1>
        <p>1 Template Sob Medida</p>
        <p>Guia de Implementação</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("INICIAR ESSENTIAL", key="p1")

with p3:
    st.markdown("""
    <div class="price-box" style="background: transparent; border: 1px solid rgba(255,255,255,0.1);">
        <h3 style="color: white;">FOUNDER</h3>
        <h1 style="font-size: 50px; margin: 30px 0; color: white;">R$ 597</h1>
        <p>Acesso Vitalício</p>
        <p>Mentoria de Branding</p>
        <p>Novos Templates Mensais</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("TORNAR-SE FOUNDER", key="p3")
st.markdown('</div>', unsafe_allow_html=True)

# --- 9. FAQ ---
st.markdown('<div style="padding: 100px 20%;">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center;">QUESTÕES FREQUENTES</h2><br>', unsafe_allow_html=True)

with st.expander("OS TEMPLATES SÃO EXCLUSIVOS?"):
    st.write("Nossa biblioteca é limitada para garantir que seu design mantenha um alto nível de raridade no mercado.")

with st.expander("HÁ SUPORTE PARA INTEGRAÇÃO JURÍDICA/MÉDICA?"):
    st.write("Sim, nossos layouts respeitam as normas de sobriedade e ética exigidas para profissionais liberais de alto padrão.")
st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="padding: 80px 10%; text-align: center; border-top: 1px solid #eee; font-size: 11px; letter-spacing: 3px; color: #999;">
    © 2026 SITE PRO EXCELLENCE // BOUTIQUE DIGITAL // LONDON - SÃO PAULO
</div>
""", unsafe_allow_html=True)
