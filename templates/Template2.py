import streamlit as st
import datetime

def render():
    """Renderiza a Landing Page de Alta Conversão - Sttack LP"""
    
    st.set_page_config(
        page_title="Projeto Verão: 30 Dias de Transformação",
        page_icon="🔥",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- CSS DE ALTA CONVERSÃO ---
    custom_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Poppins:wght@400;600&display=swap');
        
        /* Esconder elementos desnecessários do Streamlit */
        [data-testid="stHeader"], [data-testid="stDecoration"] { display: none; }
        
        body { background-color: #0f0f0f; color: #ffffff; font-family: 'Poppins', sans-serif; }

        /* NAVBAR SIMPLIFICADA (SEM LINKS) */
        .navbar {
            background: rgba(0,0,0,0.9);
            padding: 15px 5%;
            display: flex;
            justify-content: center; /* Foco Total no Logo */
            border-bottom: 2px solid #FF6B35;
            position: sticky; top: 0; z-index: 1000;
        }
        .navbar-logo { font-size: 24px; font-weight: 900; color: #fff; text-decoration: none; font-family: 'Poppins'; }
        .highlight { color: #FF6B35; }

        /* HERO SECTION FOCO EM RESULTADO */
        .hero {
            padding: 100px 5% 60px;
            text-align: center;
            background: linear-gradient(180deg, #1a1a1a 0%, #0f0f0f 100%);
        }
        .hero h1 { font-size: 52px; font-weight: 900; line-height: 1.1; margin-bottom: 20px; color: #fff; }
        .hero p { font-size: 20px; color: #ccc; max-width: 700px; margin: 0 auto 30px; }

        /* BOTÃO WHATSAPP FLUTUANTE */
        .float-wpp {
            position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px;
            background-color: #25d366; color: #FFF; border-radius: 50px; text-align: center;
            font-size: 30px; box-shadow: 2px 2px 3px #999; z-index: 1000;
            display: flex; align-items: center; justify-content: center; text-decoration: none;
        }

        /* CARD DE URGÊNCIA */
        .urgency-box {
            background: #FF6B35;
            color: white;
            padding: 15px;
            border-radius: 8px;
            display: inline-block;
            font-weight: 700;
            margin-bottom: 20px;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        /* BOTÃO DE AÇÃO PRINCIPAL (CTA) */
        .main-cta {
            background: #FF6B35;
            color: white;
            padding: 22px 50px;
            border-radius: 50px;
            font-size: 20px;
            font-weight: 900;
            text-decoration: none;
            display: inline-block;
            transition: 0.3s;
            box-shadow: 0 10px 20px rgba(255,107,53,0.4);
            text-transform: uppercase;
        }
        .main-cta:hover { background: #e55a25; transform: scale(1.05); }

        /* RESPONSIVIDADE */
        @media (max-width: 768px) {
            .hero h1 { font-size: 32px; }
            .hero p { font-size: 16px; }
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown('<div class="navbar"><a href="#" class="navbar-logo">STTACK<span class="highlight">FIT</span></a></div>', unsafe_allow_html=True)

    # --- BOTÃO WHATSAPP ---
    # Substitua o número abaixo pelo do seu cliente
    st.markdown('<a href="https://wa.me/5511999999999" class="float-wpp" target="_blank">💬</a>', unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown(f'''
    <div class="hero">
        <div class="urgency-box">⚠️ APENAS 7 VAGAS RESTANTES PARA MARÇO</div>
        <h1>Conquiste o corpo que você <span class="highlight">sempre quis</span> em 30 dias</h1>
        <p>Método comprovado para queima de gordura e definição muscular, sem dietas restritivas e sem perder horas na academia.</p>
        <br>
        <a href="https://wa.me/5511999999999" class="main-cta">QUERO MINHA AVALIAÇÃO GRATUITA</a>
    </div>
    ''', unsafe_allow_html=True)

    # --- SEÇÃO DE PROVA SOCIAL (O QUE VENDE) ---
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### ⭐⭐⭐⭐⭐\n**Roberto S.**\n'Perdi 8kg em um mês com o acompanhamento.'")
    with col2:
        st.markdown("### ⭐⭐⭐⭐⭐\n**Juliana C.**\n'O melhor investimento que fiz na minha saúde.'")
    with col3:
        st.markdown("### ⭐⭐⭐⭐⭐\n**Marcus O.**\n'Suporte 24h que faz a diferença.'")

    # --- RODAPÉ SIMPLES ---
    st.markdown(f'''
    <div style="text-align:center; padding: 40px; color: #666; font-size: 12px;">
        © {datetime.datetime.now().year} Sttack Fit - Método de Transformação Acelerada<br>
        CNPJ: 00.000.000/0001-00
    </div>
    ''', unsafe_allow_html=True)

render()
