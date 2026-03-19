import streamlit as st

def render():
    """Renderiza o template 27 - LittleTracks"""
    
    # ❌ NÃO ALTERE: Importações necessárias para o funcionamento do Streamlit
    # Estas linhas carregam as bibliotecas essenciais para a aplicação rodar

    # ✅ ALTERE: Configuração da Página (Título, Ícone, Layout)
    # Você pode mudar o "page_title" para o nome do seu produto
    # Você pode mudar o "page_icon" para o emoji que preferir
    st.set_page_config(
        page_title="LittleTracks | Memórias da Infância",  # ✅ ALTERE: Nome da página (aparece na aba do navegador)
        page_icon="🐾",  # ✅ ALTERE: Emoji do ícone
        layout="wide"  # ❌ NÃO ALTERE: Define o layout da página
    )

    # ❌ NÃO ALTERE: Bloco de CSS (Estilos Visuais)
    # Este bloco define todas as cores, fontes e efeitos visuais da página
    # Alterar aqui pode quebrar o design
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600&family=Quicksand:wght@400;500;700&display=swap');

        :root {
            --tiny-purple: #9d8df1;  /* ✅ ALTERE: Cor roxa principal (títulos, botões) */
            --tiny-blue: #a0d2eb;    /* ✅ ALTERE: Cor azul (seção de depoimentos) */
            --tiny-pink: #ffafcc;    /* ✅ ALTERE: Cor rosa (não usada, mas disponível) */
            --tiny-yellow: #ffee93;  /* ✅ ALTERE: Cor amarela (não usada, mas disponível) */
            --tiny-bg: #fdfcf0;      /* ✅ ALTERE: Cor de fundo principal */
        }

        /* ❌ NÃO ALTERE: Estilo geral da aplicação */
        .stApp {
            background-color: var(--tiny-bg);
            color: #4a4a4a;
        }

        /* ❌ NÃO ALTERE: Tipografia padrão */
        html, body, [class*="css"] {
            font-family: 'Quicksand', sans-serif;
        }

        /* ❌ NÃO ALTERE: Estilos dos títulos */
        h1, h2, h3 {
            font-family: 'Fredoka', sans-serif;
            color: #2d2d2d;
        }

        /* ❌ NÃO ALTERE: Estilo da navegação superior */
        .nav-tiny {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px 8%;
            background: transparent;
        }
        
        /* ❌ NÃO ALTERE: Estilo do logo */
        .logo-tiny {
            font-family: 'Fredoka', sans-serif;
            font-size: 32px;
            color: var(--tiny-purple);
            font-weight: 600;
        }

        /* ❌ NÃO ALTERE: Estilo da seção hero (topo) */
        .hero-tiny {
            padding: 80px 8% 100px 8%;
            text-align: center;
        }
        
        /* ❌ NÃO ALTERE: Estilo do título principal */
        .hero-h1 {
            font-size: clamp(45px, 7vw, 85px);
            line-height: 1.1;
            margin-bottom: 25px;
        }

        /* ❌ NÃO ALTERE: Estilo dos cards (caixas) */
        .card-base {
            background: white;
            border-radius: 40px;
            padding: 40px;
            border: 2px solid #f0f0f0;
            transition: 0.3s;
        }

        /* ❌ NÃO ALTERE: Estilo da timeline (linha do tempo) */
        .timeline-item {
            border-left: 4px dashed var(--tiny-purple);
            padding-left: 30px;
            margin-left: 20px;
            position: relative;
            padding-bottom: 50px;
        }
        
        /* ❌ NÃO ALTERE: Círculos da timeline */
        .timeline-circle {
            position: absolute;
            left: -14px;
            top: 0;
            width: 24px;
            height: 24px;
            background: var(--tiny-purple);
            border-radius: 50%;
            border: 4px solid white;
        }

        /* ❌ NÃO ALTERE: Estilo dos cards de preço */
        .pricing-card {
            text-align: center;
            background: white;
            border-radius: 40px;
            padding: 50px 30px;
            border: 3px solid transparent;
            transition: 0.4s;
        }
        
        /* ❌ NÃO ALTERE: Estilo do card de preço destacado */
        .pricing-card.popular {
            border-color: var(--tiny-purple);
            transform: scale(1.05);
            box-shadow: 0 20px 40px rgba(157,141,241,0.15);
        }

        /* ❌ NÃO ALTERE: Estilo dos botões */
        div.stButton > button {
            background-color: var(--tiny-purple);
            color: white;
            border: none;
            border-radius: 50px;
            padding: 18px 50px;
            font-family: 'Fredoka', sans-serif;
            font-size: 20px;
            font-weight: 500;
            box-shadow: 0 10px 20px rgba(157, 141, 241, 0.3);
            transition: 0.3s;
        }
        
        /* ❌ NÃO ALTERE: Efeito ao passar o mouse nos botões */
        div.stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(157, 141, 241, 0.5);
        }

        /* ❌ NÃO ALTERE: Estilo dos links do rodapé */
        .footer-link {
            color: #777 !important;
            text-decoration: none !important;
            font-weight: 600;
            transition: 0.3s;
            cursor: pointer;
        }

        .footer-link:hover {
            color: var(--tiny-purple) !important;
            text-decoration: none !important;
        }

        .footer-link:visited {
            color: #777 !important;
            text-decoration: none !important;
        }

        /* ❌ NÃO ALTERE: Estilo dos links de navegação */
        .nav-link {
            color: var(--tiny-purple) !important;
            text-decoration: none !important;
            font-weight: 700;
            font-size: 15px;
            transition: 0.3s;
            cursor: pointer;
        }

        .nav-link:hover {
            opacity: 0.7;
            text-decoration: none !important;
        }

        .nav-link:visited {
            color: var(--tiny-purple) !important;
            text-decoration: none !important;
        }

        /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
        [data-testid="stHeader"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 1: NAVEGAÇÃO ==========
    # ✅ ALTERE: Textos da navegação e logo
    st.markdown("""
    <div class="nav-tiny">
        <div class="logo-tiny">🐾 littletracks</div>  <!-- ✅ ALTERE: Logo e nome da marca -->
        <div style="display: flex; gap: 40px;">
            <a href="#hero" class="nav-link">O App</a>  <!-- ✅ ALTERE: Texto e direciona para seção hero -->
            <a href="#funcionalidades" class="nav-link">Funcionalidades</a>  <!-- ✅ ALTERE: Texto e direciona para seção funcionalidades -->
            <a href="#precos" class="nav-link">Preços</a>  <!-- ✅ ALTERE: Texto e direciona para seção preços -->
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 2: HERO (TOPO PRINCIPAL) ==========
    # ✅ ALTERE: Título e descrição principais
    st.markdown('<div id="hero" class="hero-tiny">', unsafe_allow_html=True)  # ❌ NÃO ALTERE: ID necessário para navegação
    st.markdown('<h1 class="hero-h1">Guardar memórias <br><span style="color: #9d8df1;">nunca foi tão doce.</span></h1>', unsafe_allow_html=True)  # ✅ ALTERE: Título principal
    st.markdown('<p style="max-width: 700px; font-size: 20px; color: #777; margin: 0 auto 40px auto; line-height: 1.6;">O diário digital inteligente que organiza os momentos mais preciosos dos seus filhos, para que você possa focar no que realmente importa: viver cada um deles.</p>', unsafe_allow_html=True)  # ✅ ALTERE: Descrição

    # ❌ NÃO ALTERE: Botão com funcionalidade
    # O botão está configurado para direcionar para Google
    st.markdown('<a href="https://www.google.com/" target="_blank" style="display: inline-block; background-color: #9d8df1; color: white; border: none; border-radius: 50px; padding: 18px 50px; font-family: Fredoka, sans-serif; font-size: 20px; font-weight: 500; box-shadow: 0 10px 20px rgba(157, 141, 241, 0.3); text-decoration: none; transition: 0.3s;">Criar Minha Conta Grátis</a>', unsafe_allow_html=True)  # ✅ ALTERE: Texto do botão e URL

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 3: FUNCIONALIDADES (CARDS) ==========
    # ✅ ALTERE: Títulos, descrições e emojis dos cards
    st.markdown('<div id="funcionalidades" style="padding: 0 8% 100px 8%;">', unsafe_allow_html=True)  # ❌ NÃO ALTERE: ID necessário para navegação
    st.markdown('<h2 style="text-align: center; margin-bottom: 60px; font-size: 42px;">Tudo o que você precisa</h2>', unsafe_allow_html=True)  # ✅ ALTERE: Título da seção

    # ❌ NÃO ALTERE: Estrutura de colunas (layout)
    f_col1, f_col2, f_col3 = st.columns(3, gap="large")

    with f_col1:
        st.markdown("""
        <div class="card-base">
            <div style="font-size: 40px; margin-bottom: 20px;">📸</div>  <!-- ✅ ALTERE: Emoji -->
            <h3>Organização Mágica</h3>  <!-- ✅ ALTERE: Título do card -->
            <p style="color: #888; font-size: 16px;">Fotos e vídeos são organizados automaticamente por data e fase do crescimento.</p>  <!-- ✅ ALTERE: Descrição -->
        </div>
        """, unsafe_allow_html=True)

    with f_col2:
        st.markdown("""
        <div class="card-base">
            <div style="font-size: 40px; margin-bottom: 20px;">👨‍👩‍👧‍👦</div>  <!-- ✅ ALTERE: Emoji -->
            <h3>Círculo da Família</h3>  <!-- ✅ ALTERE: Título do card -->
            <p style="color: #888; font-size: 16px;">Compartilhe momentos com avós e tios em um ambiente privado e seguro.</p>  <!-- ✅ ALTERE: Descrição -->
        </div>
        """, unsafe_allow_html=True)

    with f_col3:
        st.markdown("""
        <div class="card-base">
            <div style="font-size: 40px; margin-bottom: 20px;">🎨</div>  <!-- ✅ ALTERE: Emoji -->
            <h3>Livros de Memórias</h3>  <!-- ✅ ALTERE: Título do card -->
            <p style="color: #888; font-size: 16px;">Transforme seu diário digital em um álbum físico impresso com apenas um clique.</p>  <!-- ✅ ALTERE: Descrição -->
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 4: TIMELINE (LINHA DO TEMPO) ==========
    # ✅ ALTERE: Textos da timeline e URL da imagem
    st.markdown("""
    <div style="background-color: white; padding: 100px 8%; border-radius: 80px 80px 0 0;">
        <div style="display: flex; align-items: center; gap: 80px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 300px;">
                <h2 style="font-size: 48px; margin-bottom: 30px;">Uma linha do tempo da vida deles</h2>  <!-- ✅ ALTERE: Título -->
                <div class="timeline-item">
                    <div class="timeline-circle"></div>
                    <h4 style="color: var(--tiny-purple);">Hoje - 2 Anos e 3 Meses</h4>  <!-- ✅ ALTERE: Data/Título -->
                    <p>O primeiro dia na escolinha! Nenhuma lágrima (pelo menos não do Leo).</p>  <!-- ✅ ALTERE: Descrição -->
                </div>
                <div class="timeline-item">
                    <div class="timeline-circle"></div>
                    <h4 style="color: #666;">Há 6 meses</h4>  <!-- ✅ ALTERE: Data/Título -->
                    <p>Primeiros passos no jardim. Foram 4 passos inteiros!</p>  <!-- ✅ ALTERE: Descrição -->
                </div>
                <div class="timeline-item" style="border: none;">
                    <div class="timeline-circle"></div>
                    <h4 style="color: #666;">O Nascimento</h4>  <!-- ✅ ALTERE: Data/Título -->
                    <p>O começo da trilha mais linda de nossas vidas.</p>  <!-- ✅ ALTERE: Descrição -->
                </div>
            </div>
            <div style="flex: 1; min-width: 300px;">
                <img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?w=800" style="width: 100%; border-radius: 40px; box-shadow: 0 30px 60px rgba(0,0,0,0.1);">  <!-- ✅ ALTERE: URL da imagem -->
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 5: DEPOIMENTOS ==========
    # ✅ ALTERE: Textos dos depoimentos e nomes
    st.markdown("""
    <div style="background-color: #a0d2eb; padding: 120px 8%; text-align: center;">
        <h2 style="color: white; font-size: 42px; margin-bottom: 60px;">Amado por mais de 50.000 famílias</h2>  <!-- ✅ ALTERE: Título -->
        <div style="display: flex; gap: 30px; justify-content: center; flex-wrap: wrap;">
            <div style="background: white; padding: 40px; border-radius: 30px; max-width: 350px;">
                <p style="font-style: italic; color: #555;">"O littletracks mudou a forma como guardo as fotos da minha filha. É tão fácil de usar e as sugestões de marcos são incríveis!"</p>  <!-- ✅ ALTERE: Depoimento -->
                <p style="margin-top: 20px; font-weight: 700;">— Mariana S., Mãe da Alice</p>  <!-- ✅ ALTERE: Nome -->
            </div>
            <div style="background: white; padding: 40px; border-radius: 30px; max-width: 350px;">
                <p style="font-style: italic; color: #555;">"Finalmente um lugar seguro para compartilhar fotos com a família sem precisar das redes sociais abertas."</p>  <!-- ✅ ALTERE: Depoimento -->
                <p style="margin-top: 20px; font-weight: 700;">— Ricardo T., Pai do Bento</p>  <!-- ✅ ALTERE: Nome -->
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 6: PREÇOS ==========
    # ✅ ALTERE: Títulos, preços, descrições e features dos planos
    st.markdown('<div id="precos" style="padding: 120px 8%;">', unsafe_allow_html=True)  # ❌ NÃO ALTERE: ID necessário para navegação
    st.markdown('<h2 style="text-align: center; margin-bottom: 20px; font-size: 42px;">Escolha o seu plano</h2>', unsafe_allow_html=True)  # ✅ ALTERE: Título
    st.markdown('<p style="text-align: center; color: #888; margin-bottom: 60px;">Sem taxas escondidas. Cancele quando quiser.</p>', unsafe_allow_html=True)  # ✅ ALTERE: Descrição

    # ❌ NÃO ALTERE: Estrutura de colunas para preços
    p_col1, p_col2, p_col3 = st.columns(3, gap="large")

    # PLANO 1: BÁSICO
    with p_col1:
        st.markdown("""
        <div class="pricing-card">
            <h3>Básico</h3>  <!-- ✅ ALTERE: Nome do plano -->
            <h2 style="font-size: 48px; margin: 20px 0;">Grátis</h2>  <!-- ✅ ALTERE: Preço -->
            <p style="color: #888;">Para começar a trilha</p>  <!-- ✅ ALTERE: Descrição -->
            <ul style="text-align: left; margin: 30px 0; font-size: 14px; line-height: 2;">
                <li>✓ Até 500 fotos</li>  <!-- ✅ ALTERE: Feature -->
                <li>✓ 1 Perfil de criança</li>  <!-- ✅ ALTERE: Feature -->
                <li>✓ Álbum digital básico</li>  <!-- ✅ ALTERE: Feature -->
            </ul>
            <a href="https://www.google.com/" target="_blank" style="display: inline-block; background-color: #9d8df1; color: white; border: none; border-radius: 50px; padding: 18px 50px; font-family: Fredoka, sans-serif; font-size: 20px; font-weight: 500; box-shadow: 0 10px 20px rgba(157, 141, 241, 0.3); text-decoration: none; transition: 0.3s; margin-top: 20px;">Escolher Básico</a>  <!-- ✅ ALTERE: Texto do botão e URL -->
        </div>
        """, unsafe_allow_html=True)

    # PLANO 2: PREMIUM (DESTAQUE)
    with p_col2:
        st.markdown("""
        <div class="pricing-card popular">
            <span style="background: var(--tiny-purple); color: white; padding: 5px 15px; border-radius: 20px; font-size: 12px; font-weight: 700;">MAIS POPULAR</span>  <!-- ✅ ALTERE: Badge -->
            <h3 style="margin-top: 20px;">Premium</h3>  <!-- ✅ ALTERE: Nome do plano -->
            <h2 style="font-size: 48px; margin: 20px 0;">R$ 19<span style="font-size: 18px;">/mês</span></h2>  <!-- ✅ ALTERE: Preço -->
            <p style="color: #888;">Para memórias infinitas</p>  <!-- ✅ ALTERE: Descrição -->
            <ul style="text-align: left; margin: 30px 0; font-size: 14px; line-height: 2;">
                <li>✓ Armazenamento Ilimitado</li>  <!-- ✅ ALTERE: Feature -->
                <li>✓ Vídeos em 4K</li>  <!-- ✅ ALTERE: Feature -->
                <li>✓ Compartilhamento ilimitado</li>  <!-- ✅ ALTERE: Feature -->
                <li>✓ Backup automático</li>  <!-- ✅ ALTERE: Feature -->
            </ul>
            <a href="https://www.google.com/" target="_blank" style="display: inline-block; background-color: #9d8df1; color: white; border: none; border-radius: 50px; padding: 18px 50px; font-family: Fredoka, sans-serif; font-size: 20px; font-weight: 500; box-shadow: 0 10px 20px rgba(157, 141, 241, 0.3); text-decoration: none; transition: 0.3s; margin-top: 20px;">Assinar Premium</a>  <!-- ✅ ALTERE: Texto do botão e URL -->
        </div>
        """, unsafe_allow_html=True)

    # PLANO 3: FAMÍLIA
    with p_col3:
        st.markdown("""
        <div class="pricing-card">
            <h3>Família</h3>  <!-- ✅ ALTERE: Nome do plano -->
            <h2 style="font-size: 48px; margin: 20px 0;">R$ 35<span style="font-size: 18px;">/mês</span></h2>  <!-- ✅ ALTERE: Preço -->
            <p style="color: #888;">Para toda a árvore genealógica</p>  <!-- ✅ ALTERE: Descrição -->
            <ul style="text-align: left; margin: 30px 0; font-size: 14px; line-height: 2;">
                <li>✓ Tudo do Premium</li>  <!-- ✅ ALTERE: Feature -->
                <li>✓ Até 5 perfis de crianças</li>  <!-- ✅ ALTERE: Feature -->
                <li>✓ Acesso de Admin para 4 pessoas</li>  <!-- ✅ ALTERE: Feature -->
            </ul>
            <a href="https://www.google.com/" target="_blank" style="display: inline-block; background-color: #9d8df1; color: white; border: none; border-radius: 50px; padding: 18px 50px; font-family: Fredoka, sans-serif; font-size: 20px; font-weight: 500; box-shadow: 0 10px 20px rgba(157, 141, 241, 0.3); text-decoration: none; transition: 0.3s; margin-top: 20px;">Escolher Família</a>  <!-- ✅ ALTERE: Texto do botão e URL -->
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 7: FAQ (PERGUNTAS FREQUENTES) ==========
    # ✅ ALTERE: Perguntas e respostas
    st.markdown('<div style="background: #f0f9ff; padding: 100px 20%;">', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; margin-bottom: 50px;">Dúvidas Frequentes</h2>', unsafe_allow_html=True)  # ✅ ALTERE: Título

    with st.expander("Meus dados estão seguros?"):  # ✅ ALTERE: Pergunta
        st.write("Sim! Utilizamos criptografia de nível bancário e seus dados nunca são vendidos para terceiros.")  # ✅ ALTERE: Resposta

    with st.expander("Posso imprimir os álbuns no Brasil?"):  # ✅ ALTERE: Pergunta
        st.write("Sim, temos parceiros de impressão locais que entregam em todo o território nacional com acabamento premium.")  # ✅ ALTERE: Resposta

    with st.expander("Como convido os avós?"):  # ✅ ALTERE: Pergunta
        st.write("Basta enviar um link mágico pelo WhatsApp ou e-mail. Eles não precisam criar senhas complicadas.")  # ✅ ALTERE: Resposta

    st.markdown('</div>', unsafe_allow_html=True)

    # ========== SEÇÃO 8: FOOTER (RODAPÉ) ==========
    # ✅ ALTERE: Logo, links e informações do rodapé
    st.markdown("""
    <div style="padding: 100px 8% 50px 8%; text-align: center;">
        <div class="logo-tiny" style="margin-bottom: 30px;">🐾 littletracks</div>  <!-- ✅ ALTERE: Logo e nome -->
        <div style="display: flex; justify-content: center; gap: 50px; margin-bottom: 40px;">
            <a href="https://www.google.com/" target="_blank" class="footer-link">Instagram</a>  <!-- ✅ ALTERE: URL e texto -->
            <a href="https://www.google.com/" target="_blank" class="footer-link">Facebook</a>  <!-- ✅ ALTERE: URL e texto -->
            <a href="https://www.google.com/" target="_blank" class="footer-link">Blog</a>  <!-- ✅ ALTERE: URL e texto -->
            <a href="https://www.google.com/" target="_blank" class="footer-link">Termos de Uso</a>  <!-- ✅ ALTERE: URL e texto -->
        </div>
        <p style="color: #bbb; font-size: 13px;">© 2026 littletracks. Criado com ❤️ para as futuras gerações.</p>  <!-- ✅ ALTERE: Copyright e descrição -->
    </div>
    """, unsafe_allow_html=True)

    # ========== FIM DO TEMPLATE ==========
    # Lembre-se: Altere apenas o que tem ✅ ALTERE
    # Não mexa no que tem ❌ NÃO ALTERE

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template27" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

