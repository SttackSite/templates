# -*- coding: utf-8 -*-
"""
Elite Portfolio - Landing Page Premium em Streamlit


✅ ALTERE: Títulos, descrições, números, emails, links
❌ NÃO ALTERE: CSS, estrutura HTML, configurações do Streamlit
"""

import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit

def render():
    """Renderiza o template 7 - Elite Portfolio"""
    
    # ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
    # ❌ NÃO ALTERE: Define as configurações básicas da página
    st.set_page_config(
        page_title="Portfolio Premium - Profissional de Elite",  # ✅ ALTERE: Título da aba
        page_icon="✨",  # ✅ ALTERE: Emoji da aba
        layout="wide",  # ❌ NÃO ALTERE: Layout em largura total
        initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Oculta a barra lateral
    )

    # ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
    # ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
    # Alterar aqui pode quebrar completamente o design da página
    custom_css = """
<style>
    /* ❌ NÃO ALTERE: Importação de fontes do Google */
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Inter:wght@400;500;600;700&display=swap');
    
    /* ❌ NÃO ALTERE: Reset de estilos padrão */
    * {
        margin: 0;  /* Remove margem padrão */
        padding: 0;  /* Remove preenchimento padrão */
        box-sizing: border-box;  /* Inclui borda no tamanho total */
    }
    
    /* ❌ NÃO ALTERE: Estilos do body */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);  /* Gradiente de fundo */
        font-family: 'Inter', sans-serif;  /* Fonte padrão */
        color: #ffffff;  /* Cor de texto branco */
        overflow-x: hidden;  /* Oculta scroll horizontal */
    }
    
    /* ❌ NÃO ALTERE: Remove decorações padrão */
    [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; background: transparent; }
    
    /* ❌ NÃO ALTERE: ANIMAÇÕES */
    @keyframes textReveal {
        0% { clip-path: inset(0 100% 0 0); }  /* Texto oculto à direita */
        100% { clip-path: inset(0 0 0 0); }  /* Texto visível */
    }
    
    @keyframes numberCounter {
        0% { transform: translateY(30px); opacity: 0; }  /* Começa abaixo e invisível */
        100% { transform: translateY(0); opacity: 1; }  /* Sobe e fica visível */
    }
    
    @keyframes floatSoft {
        0%, 100% { transform: translateY(0px); }  /* Posição normal */
        50% { transform: translateY(-20px); }  /* Sobe 20px no meio */
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }  /* Posição inicial */
        50% { background-position: 100% 50%; }  /* Posição do meio */
        100% { background-position: 0% 50%; }  /* Volta à posição inicial */
    }
    
    @keyframes borderGlowCycle {
        0%, 100% { border-color: rgba(100, 200, 255, 0.3); }  /* Borda fraca */
        50% { border-color: rgba(100, 200, 255, 0.8); }  /* Borda forte */
    }
    
    @keyframes slideFromLeft {
        0% { transform: translateX(-100px); opacity: 0; }  /* Começa à esquerda e invisível */
        100% { transform: translateX(0); opacity: 1; }  /* Desliza para a direita e fica visível */
    }
    
    @keyframes slideFromRight {
        0% { transform: translateX(100px); opacity: 0; }  /* Começa à direita e invisível */
        100% { transform: translateX(0); opacity: 1; }  /* Desliza para a esquerda e fica visível */
    }
    
    @keyframes scaleInCenter {
        0% { transform: scale(0.8); opacity: 0; }  /* Começa pequeno e invisível */
        100% { transform: scale(1); opacity: 1; }  /* Cresce e fica visível */
    }
    
    /* ❌ NÃO ALTERE: NAVBAR */
    .navbar {
        background: rgba(10, 14, 39, 0.95);  /* Fundo semi-transparente */
        backdrop-filter: blur(30px);  /* Blur de fundo */
        padding: 20px 80px;  /* Espaçamento interno */
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaço entre logo e nav */
        align-items: center;  /* Centraliza verticalmente */
        border-bottom: 1px solid rgba(100, 200, 255, 0.15);  /* Borda inferior ciano */
        position: sticky;  /* Fica fixo ao rolar */
        top: 0;  /* No topo */
        z-index: 100;  /* Acima de tudo */
    }
    
    /* ❌ NÃO ALTERE: Logo da navbar */
    .navbar-logo {
        font-size: 24px;  /* Tamanho grande */
        font-weight: 800;  /* Peso muito pesado */
        background: linear-gradient(90deg, #64c8ff 0%, #0099ff 100%);  /* Gradiente ciano */
        -webkit-background-clip: text;  /* Aplica gradiente ao texto (webkit) */
        -webkit-text-fill-color: transparent;  /* Texto transparente (webkit) */
        background-clip: text;  /* Aplica gradiente ao texto */
        font-family: 'Syne', sans-serif;  /* Fonte especial */
        letter-spacing: 2px;  /* Espaçamento entre letras */
    }
    
    /* ❌ NÃO ALTERE: Container de navegação */
    .navbar-nav {
        display: flex;  /* Layout flexível */
        gap: 60px;  /* Espaçamento entre itens */
    }
    
    /* ✅ ALTERE: Links de navegação (estilo) */
    .nav-link {
        color: #a0b0d0;  /* Cor cinza-azul */
        text-decoration: none !important;  /* Remove sublinhado */
        font-size: 13px;  /* Tamanho pequeno */
        font-weight: 600;  /* Peso pesado */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1.5px;  /* Espaçamento entre letras */
        transition: all 0.3s ease;  /* Animação suave */
        position: relative;  /* Posicionamento relativo */
    }
    
    /* ❌ NÃO ALTERE: Underline animado do link */
    .nav-link::after {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        bottom: -5px;  /* Abaixo do texto */
        left: 0;  /* À esquerda */
        width: 0;  /* Largura inicial zero */
        height: 2px;  /* Altura da linha */
        background: linear-gradient(90deg, #64c8ff, #0099ff);  /* Gradiente ciano */
        transition: width 0.3s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no link */
    .nav-link:hover::after { width: 100%; }  /* Underline cresce */
    .nav-link:hover { color: #64c8ff; }  /* Texto fica ciano */
    
    /* ❌ NÃO ALTERE: HERO SECTION */
    .hero {
        min-height: 100vh;  /* Altura mínima da tela */
        display: flex;  /* Layout flexível */
        align-items: center;  /* Centraliza verticalmente */
        justify-content: center;  /* Centraliza horizontalmente */
        padding: 100px 80px;  /* Espaçamento interno */
        position: relative;  /* Posicionamento relativo */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
    }
    
    /* ❌ NÃO ALTERE: Efeito de fundo do hero (círculo superior direito) */
    .hero::before {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        width: 800px;  /* Largura */
        height: 800px;  /* Altura */
        background: radial-gradient(circle, rgba(100, 200, 255, 0.08) 0%, transparent 70%);  /* Gradiente radial */
        border-radius: 50%;  /* Círculo */
        top: -300px;  /* Acima da tela */
        right: -300px;  /* À direita da tela */
        animation: floatSoft 8s ease-in-out infinite;  /* Animação de flutuação */
    }
    
    /* ❌ NÃO ALTERE: Efeito de fundo do hero (círculo inferior esquerdo) */
    .hero::after {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        width: 600px;  /* Largura */
        height: 600px;  /* Altura */
        background: radial-gradient(circle, rgba(0, 153, 255, 0.05) 0%, transparent 70%);  /* Gradiente radial */
        border-radius: 50%;  /* Círculo */
        bottom: -200px;  /* Abaixo da tela */
        left: -200px;  /* À esquerda da tela */
        animation: floatSoft 10s ease-in-out infinite reverse;  /* Animação de flutuação reversa */
    }
    
    /* ❌ NÃO ALTERE: Container do hero */
    .hero-container {
        max-width: 1000px;  /* Largura máxima */
        text-align: center;  /* Texto centralizado */
        position: relative;  /* Posicionamento relativo */
        z-index: 2;  /* Acima dos efeitos de fundo */
    }
    
    /* ✅ ALTERE: Label do hero */
    .hero-label {
        font-size: 14px;  /* Tamanho pequeno */
        color: #64c8ff;  /* Cor ciano */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 2px;  /* Espaçamento entre letras */
        margin-bottom: 20px;  /* Espaçamento inferior */
        font-weight: 700;  /* Peso pesado */
    }
    
    /* ✅ ALTERE: Título do hero */
    .hero-title {
        font-size: 92px;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        line-height: 1;  /* Altura da linha mínima */
        margin-bottom: 30px;  /* Espaçamento inferior */
        font-family: 'Syne', sans-serif;  /* Fonte especial */
        letter-spacing: -2px;  /* Espaçamento negativo entre letras */
        animation: textReveal 1.2s ease-out;  /* Animação de revelação */
    }
    
    /* ❌ NÃO ALTERE: Span do título (gradiente animado) */
    .hero-title span {
        background: linear-gradient(135deg, #64c8ff 0%, #0099ff 50%, #64c8ff 100%);  /* Gradiente ciano */
        -webkit-background-clip: text;  /* Aplica gradiente ao texto (webkit) */
        -webkit-text-fill-color: transparent;  /* Texto transparente (webkit) */
        background-clip: text;  /* Aplica gradiente ao texto */
        background-size: 200% 200%;  /* Tamanho do gradiente */
        animation: gradientFlow 4s ease infinite;  /* Animação de fluxo */
    }
    
    /* ✅ ALTERE: Descrição do hero */
    .hero-desc {
        font-size: 18px;  /* Tamanho grande */
        color: #a0b0d0;  /* Cor cinza-azul */
        max-width: 600px;  /* Largura máxima */
        margin: 0 auto 60px;  /* Centraliza e espaçamento inferior */
        line-height: 1.8;  /* Altura da linha generosa */
        font-weight: 400;  /* Peso normal */
    }
    
    /* ❌ NÃO ALTERE: Container de CTA do hero */
    .hero-cta {
        display: flex;  /* Layout flexível */
        gap: 20px;  /* Espaçamento entre botões */
        justify-content: center;  /* Centraliza horizontalmente */
        flex-wrap: wrap;  /* Quebra em múltiplas linhas */
    }
    
    /* ❌ NÃO ALTERE: Botão primário */
    .btn-primary {
        background: linear-gradient(135deg, #64c8ff 0%, #0099ff 100%);  /* Gradiente ciano */
        color: #0a0e27;  /* Texto escuro */
        padding: 16px 50px;  /* Espaçamento interno */
        border: none;  /* Sem borda */
        border-radius: 4px;  /* Arredondamento suave */
        font-weight: 700;  /* Peso pesado */
        font-size: 14px;  /* Tamanho pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        cursor: pointer;  /* Cursor de clique */
        transition: all 0.3s ease;  /* Animação suave */
        box-shadow: 0 0 30px rgba(100, 200, 255, 0.3);  /* Sombra ciano */
        text-decoration: none !important;  /* Remove sublinhado */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão primário */
    .btn-primary:hover {
        transform: translateY(-5px);  /* Levanta o botão */
        box-shadow: 0 0 50px rgba(100, 200, 255, 0.6);  /* Sombra aumentada */
    }
    
    /* ❌ NÃO ALTERE: Botão secundário */
    .btn-secondary {
        background: transparent;  /* Fundo transparente */
        color: #64c8ff;  /* Texto ciano */
        padding: 16px 50px;  /* Espaçamento interno */
        border: 2px solid #64c8ff;  /* Borda ciano */
        border-radius: 4px;  /* Arredondamento suave */
        font-weight: 700;  /* Peso pesado */
        font-size: 14px;  /* Tamanho pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        cursor: pointer;  /* Cursor de clique */
        transition: all 0.3s ease;  /* Animação suave */
        text-decoration: none !important;  /* Remove sublinhado */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão secundário */
    .btn-secondary:hover {
        background: rgba(100, 200, 255, 0.1);  /* Fundo semi-transparente */
        box-shadow: 0 0 30px rgba(100, 200, 255, 0.3);  /* Sombra ciano */
    }
    
    /* ❌ NÃO ALTERE: STATS SECTION */
    .stats-section {
        padding: 120px 80px;  /* Espaçamento interno */
        background: linear-gradient(135deg, #1a1f3a 0%, #0a0e27 100%);  /* Gradiente de fundo */
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(4, 1fr);  /* 4 colunas */
        gap: 40px;  /* Espaçamento entre itens */
        max-width: 1400px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }
    
    /* ❌ NÃO ALTERE: Box de estatística */
    .stat-box {
        text-align: center;  /* Texto centralizado */
        padding: 40px;  /* Espaçamento interno */
        border-left: 4px solid #64c8ff;  /* Borda esquerda ciano */
        animation: slideFromLeft 0.8s ease-out;  /* Animação de deslize */
        animation-fill-mode: both;  /* Mantém estado final */
    }
    
    /* ❌ NÃO ALTERE: Delays de animação */
    .stat-box:nth-child(1) { animation-delay: 0.1s; }
    .stat-box:nth-child(2) { animation-delay: 0.2s; }
    .stat-box:nth-child(3) { animation-delay: 0.3s; }
    .stat-box:nth-child(4) { animation-delay: 0.4s; }
    
    /* ✅ ALTERE: Número da estatística */
    .stat-number {
        font-size: 56px;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        background: linear-gradient(135deg, #64c8ff, #0099ff);  /* Gradiente ciano */
        -webkit-background-clip: text;  /* Aplica gradiente ao texto (webkit) */
        -webkit-text-fill-color: transparent;  /* Texto transparente (webkit) */
        background-clip: text;  /* Aplica gradiente ao texto */
        margin-bottom: 10px;  /* Espaçamento inferior */
        font-family: 'Syne', sans-serif;  /* Fonte especial */
    }
    
    /* ✅ ALTERE: Label da estatística */
    .stat-label {
        font-size: 14px;  /* Tamanho pequeno */
        color: #a0b0d0;  /* Cor cinza-azul */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        font-weight: 600;  /* Peso pesado */
    }
    
    /* ❌ NÃO ALTERE: EXPERTISE SECTION */
    .expertise-section {
        padding: 120px 80px;  /* Espaçamento interno */
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);  /* Gradiente de fundo */
    }
    
    /* ✅ ALTERE: Título da seção */
    .section-title {
        font-size: 56px;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        text-align: center;  /* Texto centralizado */
        margin-bottom: 100px;  /* Espaçamento inferior */
        font-family: 'Syne', sans-serif;  /* Fonte especial */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
    }
    
    /* ❌ NÃO ALTERE: Grid de expertise */
    .expertise-grid {
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(2, 1fr);  /* 2 colunas */
        gap: 50px;  /* Espaçamento entre itens */
        max-width: 1200px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }
    
    /* ❌ NÃO ALTERE: Item de expertise */
    .expertise-item {
        padding: 50px;  /* Espaçamento interno */
        border: 1px solid rgba(100, 200, 255, 0.2);  /* Borda ciano semi-transparente */
        border-radius: 8px;  /* Arredondamento */
        background: linear-gradient(135deg, rgba(100, 200, 255, 0.05), rgba(0, 153, 255, 0.02));  /* Gradiente de fundo */
        transition: all 0.4s ease;  /* Animação suave */
        animation: scaleInCenter 0.8s ease-out;  /* Animação de escala */
        animation-fill-mode: both;  /* Mantém estado final */
        position: relative;  /* Posicionamento relativo */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
    }
    
    /* ❌ NÃO ALTERE: Delays de animação */
    .expertise-item:nth-child(1) { animation-delay: 0.1s; }
    .expertise-item:nth-child(2) { animation-delay: 0.2s; }
    .expertise-item:nth-child(3) { animation-delay: 0.3s; }
    .expertise-item:nth-child(4) { animation-delay: 0.4s; }
    
    /* ❌ NÃO ALTERE: Efeito shine no item */
    .expertise-item::before {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        top: 0;  /* No topo */
        left: -100%;  /* À esquerda da área */
        width: 100%;  /* Largura total */
        height: 100%;  /* Altura total */
        background: linear-gradient(90deg, transparent, rgba(100, 200, 255, 0.1), transparent);  /* Gradiente */
        transition: left 0.6s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no item */
    .expertise-item:hover::before { left: 100%; }  /* Shine desliza */
    
    .expertise-item:hover {
        transform: translateY(-10px);  /* Levanta o item */
        border-color: #64c8ff;  /* Borda fica ciano */
        box-shadow: 0 0 40px rgba(100, 200, 255, 0.2);  /* Sombra ciano */
    }
    
    /* ✅ ALTERE: Número do item */
    .expertise-number {
        font-size: 48px;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        color: #64c8ff;  /* Cor ciano */
        margin-bottom: 20px;  /* Espaçamento inferior */
        font-family: 'Syne', sans-serif;  /* Fonte especial */
    }
    
    /* ✅ ALTERE: Título do item */
    .expertise-title {
        font-size: 24px;  /* Tamanho grande */
        font-weight: 700;  /* Peso pesado */
        margin-bottom: 15px;  /* Espaçamento inferior */
        color: #ffffff;  /* Cor branca */
    }
    
    /* ✅ ALTERE: Descrição do item */
    .expertise-desc {
        font-size: 15px;  /* Tamanho pequeno */
        color: #a0b0d0;  /* Cor cinza-azul */
        line-height: 1.8;  /* Altura da linha generosa */
    }
    
    /* ❌ NÃO ALTERE: WORK SECTION */
    .work-section {
        padding: 120px 80px;  /* Espaçamento interno */
        background: linear-gradient(135deg, #1a1f3a 0%, #0a0e27 100%);  /* Gradiente de fundo */
    }
    
    /* ❌ NÃO ALTERE: Grid de trabalhos */
    .work-grid {
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(3, 1fr);  /* 3 colunas */
        gap: 40px;  /* Espaçamento entre itens */
        max-width: 1400px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }
    
    /* ❌ NÃO ALTERE: Item de trabalho */
    .work-item {
        position: relative;  /* Posicionamento relativo */
        height: 400px;  /* Altura */
        border-radius: 8px;  /* Arredondamento */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
        background: linear-gradient(135deg, rgba(100, 200, 255, 0.1), rgba(0, 153, 255, 0.05));  /* Gradiente de fundo */
        border: 1px solid rgba(100, 200, 255, 0.2);  /* Borda ciano semi-transparente */
        cursor: pointer;  /* Cursor de clique */
        transition: all 0.4s ease;  /* Animação suave */
        animation: slideFromRight 0.8s ease-out;  /* Animação de deslize */
        animation-fill-mode: both;  /* Mantém estado final */
    }
    
    /* ❌ NÃO ALTERE: Delays de animação */
    .work-item:nth-child(1) { animation-delay: 0.1s; }
    .work-item:nth-child(2) { animation-delay: 0.2s; }
    .work-item:nth-child(3) { animation-delay: 0.3s; }
    
    /* ❌ NÃO ALTERE: Efeito hover no item */
    .work-item:hover {
        transform: translateY(-15px);  /* Levanta o item */
        border-color: #64c8ff;  /* Borda fica ciano */
        box-shadow: 0 0 50px rgba(100, 200, 255, 0.3);  /* Sombra ciano */
    }
    
    /* ❌ NÃO ALTERE: Conteúdo do item */
    .work-content {
        position: absolute;  /* Posicionamento absoluto */
        bottom: 0;  /* No fundo */
        left: 0;  /* À esquerda */
        right: 0;  /* À direita */
        padding: 40px;  /* Espaçamento interno */
        background: linear-gradient(180deg, transparent 0%, rgba(10, 14, 39, 0.95) 100%);  /* Gradiente de fundo */
        transform: translateY(50px);  /* Começa abaixo */
        transition: transform 0.4s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no conteúdo */
    .work-item:hover .work-content {
        transform: translateY(0);  /* Sobe para a posição normal */
    }
    
    /* ✅ ALTERE: Título do trabalho */
    .work-title {
        font-size: 20px;  /* Tamanho grande */
        font-weight: 700;  /* Peso pesado */
        color: #ffffff;  /* Cor branca */
        margin-bottom: 10px;  /* Espaçamento inferior */
    }
    
    /* ✅ ALTERE: Descrição do trabalho */
    .work-desc {
        font-size: 14px;  /* Tamanho pequeno */
        color: #a0b0d0;  /* Cor cinza-azul */
    }
    
    /* ❌ NÃO ALTERE: CTA SECTION */
    .cta-section {
        padding: 150px 80px;  /* Espaçamento interno */
        background: linear-gradient(135deg, #64c8ff 0%, #0099ff 100%);  /* Gradiente ciano */
        text-align: center;  /* Texto centralizado */
        position: relative;  /* Posicionamento relativo */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
    }
    
    /* ❌ NÃO ALTERE: Overlay do CTA */
    .cta-section::before {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        top: 0;  /* No topo */
        left: 0;  /* À esquerda */
        right: 0;  /* À direita */
        bottom: 0;  /* No fundo */
        background: rgba(10, 14, 39, 0.1);  /* Overlay escuro */
    }
    
    /* ❌ NÃO ALTERE: Conteúdo do CTA */
    .cta-content {
        position: relative;  /* Posicionamento relativo */
        z-index: 2;  /* Acima do overlay */
    }
    
    /* ✅ ALTERE: Título do CTA */
    .cta-title {
        font-size: 56px;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        color: #0a0e27;  /* Cor escura */
        margin-bottom: 30px;  /* Espaçamento inferior */
        font-family: 'Syne', sans-serif;  /* Fonte especial */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
    }
    
    /* ✅ ALTERE: Descrição do CTA */
    .cta-desc {
        font-size: 18px;  /* Tamanho grande */
        color: rgba(10, 14, 39, 0.9);  /* Cor escura semi-transparente */
        max-width: 600px;  /* Largura máxima */
        margin: 0 auto 50px;  /* Centraliza e espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Botão do CTA */
    .cta-btn {
        background: #0a0e27;  /* Fundo escuro */
        color: #64c8ff;  /* Texto ciano */
        padding: 18px 60px;  /* Espaçamento interno */
        border: 2px solid #0a0e27;  /* Borda escura */
        border-radius: 4px;  /* Arredondamento suave */
        font-weight: 700;  /* Peso pesado */
        font-size: 14px;  /* Tamanho pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        cursor: pointer;  /* Cursor de clique */
        transition: all 0.3s ease;  /* Animação suave */
        text-decoration: none !important;  /* Remove sublinhado */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão */
    .cta-btn:hover {
        transform: translateY(-5px);  /* Levanta o botão */
        box-shadow: 0 8px 30px rgba(10, 14, 39, 0.3);  /* Sombra */
    }
    
    /* ❌ NÃO ALTERE: FOOTER */
    .footer {
        background: #0a0e27;  /* Fundo escuro */
        color: #a0b0d0;  /* Cor cinza-azul */
        padding: 80px;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
        border-top: 1px solid rgba(100, 200, 255, 0.15);  /* Borda superior ciano */
    }
    
    /* ✅ ALTERE: Texto do footer */
    .footer-text {
        font-size: 14px;  /* Tamanho pequeno */
        margin-bottom: 15px;  /* Espaçamento inferior */
    }
    
    /* ✅ ALTERE: Copyright do footer */
    .footer-copyright {
        border-top: 1px solid rgba(100, 200, 255, 0.15);  /* Borda superior */
        padding-top: 40px;  /* Espaçamento superior */
        margin-top: 40px;  /* Espaçamento superior */
        font-size: 12px;  /* Tamanho muito pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 2px;  /* Espaçamento entre letras */
    }
    
    /* ❌ NÃO ALTERE: Responsividade */
    @media (max-width: 768px) {
        .navbar { padding: 15px 20px; flex-direction: column; gap: 15px; }
        .navbar-nav { gap: 20px; }
        .hero { padding: 50px 20px; min-height: auto; }
        .hero-title { font-size: 48px; }
        .stats-section { grid-template-columns: repeat(2, 1fr); padding: 80px 20px; }
        .expertise-grid { grid-template-columns: 1fr; gap: 30px; }
        .work-grid { grid-template-columns: 1fr; }
        .cta-section { padding: 100px 20px; }
        .cta-title { font-size: 36px; }
    }
    
    /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
    [data-testid="stHeader"] { 
        display: none;  /* Oculta o header */
    }
</style>
"""

    # ❌ NÃO ALTERE: Renderiza o CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # ========== SEÇÃO 3: NAVBAR ==========
    # ✅ ALTERE: Logo, textos dos links e URLs
    navbar_html = '''<div class="navbar">
    <!-- ✅ ALTERE: Logo -->
    <div class="navbar-logo">ELITE</div>
    <div class="navbar-nav">
        <!-- ✅ ALTERE: Links de navegação (texto e URL) -->
        <a href="#sobre" class="nav-link">Sobre</a>
        <a href="#expertise" class="nav-link">Expertise</a>
        <a href="#trabalhos" class="nav-link">Trabalhos</a>
        <a href="#contato" class="nav-link">Contato</a>
    </div>
</div>'''
    st.markdown(navbar_html, unsafe_allow_html=True)

    # ========== SEÇÃO 4: HERO ===========
    # ✅ ALTERE: Label, título, descrição e botões
    hero_html = '''<div class="hero" id="sobre">
    <div class="hero-container">
        <!-- ✅ ALTERE: Label -->
        <div class="hero-label">Bem-vindo</div>
        <!-- ✅ ALTERE: Título (span é para gradiente) -->
        <div class="hero-title">Transformando <span>Visões</span> em Realidade</div>
        <!-- ✅ ALTERE: Descrição -->
        <div class="hero-desc">Especialista em criar soluções de impacto com design sofisticado e estratégia de negócio.</div>
        <div class="hero-cta">
            <!-- ✅ ALTERE: Texto do botão e URL -->
            <a href="https://www.google.com/" target="_blank" class="btn-primary">Iniciar Projeto</a>
            <!-- ✅ ALTERE: Texto do botão e URL -->
            <a href="https://www.google.com/" target="_blank" class="btn-secondary">Explorar Trabalhos</a>
        </div>
    </div>
</div>'''
    st.markdown(hero_html, unsafe_allow_html=True)

    # ========== SEÇÃO 5: STATS ===========
    # ✅ ALTERE: Números e labels
    stats_html = '''<div class="stats-section">
    <div class="stat-box">
        <!-- ✅ ALTERE: Número e label -->
        <div class="stat-number">150+</div>
        <div class="stat-label">Projetos Entregues</div>
    </div>
    <div class="stat-box">
        <!-- ✅ ALTERE: Número e label -->
        <div class="stat-number">98%</div>
        <div class="stat-label">Satisfação Clientes</div>
    </div>
    <div class="stat-box">
        <!-- ✅ ALTERE: Número e label -->
        <div class="stat-number">12+</div>
        <div class="stat-label">Anos Experiência</div>
    </div>
    <div class="stat-box">
        <!-- ✅ ALTERE: Número e label -->
        <div class="stat-number">50M+</div>
        <div class="stat-label">Impacto Gerado</div>
    </div>
</div>'''
    st.markdown(stats_html, unsafe_allow_html=True)

    # ========== SEÇÃO 6: EXPERTISE ===========
    # ✅ ALTERE: Título da seção, números, títulos e descrições
    expertise_html = '''<div class="expertise-section" id="expertise">
    <!-- ✅ ALTERE: Título da seção -->
    <div class="section-title">Expertise</div>
    <div class="expertise-grid">
        <div class="expertise-item">
            <!-- ✅ ALTERE: Número, título e descrição -->
            <div class="expertise-number">01</div>
            <div class="expertise-title">Estratégia Digital</div>
            <div class="expertise-desc">Desenvolvimento de estratégias robustas que transformam objetivos em resultados mensuráveis e crescimento sustentável.</div>
        </div>
        <div class="expertise-item">
            <!-- ✅ ALTERE: Número, título e descrição -->
            <div class="expertise-number">02</div>
            <div class="expertise-title">Design Premium</div>
            <div class="expertise-desc">Criação de interfaces sofisticadas que combinam estética com funcionalidade, elevando a experiência do usuário.</div>
        </div>
        <div class="expertise-item">
            <!-- ✅ ALTERE: Número, título e descrição -->
            <div class="expertise-number">03</div>
            <div class="expertise-title">Desenvolvimento</div>
            <div class="expertise-desc">Implementação de soluções técnicas escaláveis e performáticas usando tecnologias de ponta do mercado.</div>
        </div>
        <div class="expertise-item">
            <!-- ✅ ALTERE: Número, título e descrição -->
            <div class="expertise-number">04</div>
            <div class="expertise-title">Consultoria</div>
            <div class="expertise-desc">Orientação estratégica para empresas que buscam inovação, transformação digital e posicionamento de mercado.</div>
        </div>
    </div>
</div>'''
    st.markdown(expertise_html, unsafe_allow_html=True)

    # ========== SEÇÃO 7: WORK ==============
    # ✅ ALTERE: Títulos, descrições e emojis
    work_html = '''<div class="work-section" id="trabalhos">
    <!-- ✅ ALTERE: Título da seção -->
    <div class="section-title">Trabalhos em Destaque</div>
    <div class="work-grid">
        <div class="work-item">
            <!-- ✅ ALTERE: Emoji -->
            <div style="font-size: 120px; display: flex; align-items: center; justify-content: center; height: 100%;">🚀</div>
            <div class="work-content">
                <!-- ✅ ALTERE: Título e descrição -->
                <div class="work-title">Plataforma SaaS</div>
                <div class="work-desc">Solução completa de gestão empresarial com impacto em 10K+ usuários.</div>
            </div>
        </div>
        <div class="work-item">
            <!-- ✅ ALTERE: Emoji -->
            <div style="font-size: 120px; display: flex; align-items: center; justify-content: center; height: 100%;">💎</div>
            <div class="work-content">
                <!-- ✅ ALTERE: Título e descrição -->
                <div class="work-title">Marca Luxury</div>
                <div class="work-desc">Rebranding completo para marca premium com presença global.</div>
            </div>
        </div>
        <div class="work-item">
            <!-- ✅ ALTERE: Emoji -->
            <div style="font-size: 120px; display: flex; align-items: center; justify-content: center; height: 100%;">📊</div>
            <div class="work-content">
                <!-- ✅ ALTERE: Título e descrição -->
                <div class="work-title">Analytics Platform</div>
                <div class="work-desc">Dashboard inteligente para análise de dados em tempo real.</div>
            </div>
        </div>
    </div>
</div>'''
    st.markdown(work_html, unsafe_allow_html=True)

    # ========== SEÇÃO 8: CTA FINAL ===========
    # ✅ ALTERE: Título, descrição e botão
    cta_html = '''<div class="cta-section" id="contato">
    <div class="cta-content">
        <!-- ✅ ALTERE: Título -->
        <div class="cta-title">Pronto para Crescer?</div>
        <!-- ✅ ALTERE: Descrição -->
        <div class="cta-desc">Vamos transformar sua visão em uma solução que gera resultados reais e impacto mensurável.</div>
        <!-- ✅ ALTERE: Texto do botão e URL -->
        <a href="https://www.google.com/" target="_blank" class="cta-btn">Conversar Agora</a>
    </div>
</div>'''
    st.markdown(cta_html, unsafe_allow_html=True)

    # ========== SEÇÃO 9: FOOTER ===========
    # ✅ ALTERE: Email, telefone, links e copyright
    footer_html = '''<div class="footer">
    <!-- ✅ ALTERE: Email e telefone -->
    <div class="footer-text">Email: contato@elite.com | Telefone: +55 (99) 99999-9999</div>
    <!-- ✅ ALTERE: Links -->
    <div class="footer-text">LinkedIn: linkedin.com/in/seu-perfil | Portfólio: seu-site.com</div>
    <!-- ✅ ALTERE: Copyright -->
    <div class="footer-copyright">© 2025 Elite Portfolio. Todos os direitos reservados.</div>
</div>'''
    st.markdown(footer_html, unsafe_allow_html=True)

    # ========== BOTÃO EDITAR TEMPLATE ==========
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 50px; background: #f8f9ff;">
        <a href="https://sttackedit.streamlit.app/?template=template7" target="_blank"
           style="display:inline-block; background:#7b2cbf; color:white; text-decoration:none;
                  padding:22px 60px; font-size:18px; font-weight:700; border-radius:6px;
                  letter-spacing:1px; text-transform:uppercase; font-family:Inter,sans-serif;
                  box-shadow: 0 4px 20px rgba(123,44,191,0.4);">
            ✏️ Editar este Template
        </a>
    </div>
    """, unsafe_allow_html=True)

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
