import streamlit as st

def render():
    # --- WEBFLOW CORE DESIGN SYSTEM ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800&display=swap');

        :root {
            --wf-blue: #4353ff;
            --wf-black: #101010;
            --wf-dark-gray: #1a1a1a;
            --wf-text-muted: #757575;
            --wf-bg: #f5f5f7;
            --wf-accent-gradient: linear-gradient(90deg, #4353ff 0%, #a259ff 100%);
        }

        .stApp { background-color: white; color: var(--wf-black); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        /* --- HERO SECTION: WEBFLOW STYLE --- */
        .wf-hero {
            padding: 140px 10% 80px 10%;
            text-align: center;
            background: radial-gradient(circle at center, #f0f2ff 0%, white 70%);
        }

        .wf-badge {
            background: white;
            border: 1px solid #e1e1e1;
            padding: 8px 16px;
            border-radius: 100px;
            font-size: 13px;
            font-weight: 600;
            color: var(--wf-blue);
            margin-bottom: 30px;
            display: inline-block;
        }

        .wf-h1 {
            font-size: clamp(40px, 7vw, 90px);
            font-weight: 800;
            line-height: 0.95;
            letter-spacing: -0.04em;
            margin-bottom: 32px;
            color: var(--wf-black);
        }

        .wf-sub {
            font-size: 22px;
            color: var(--wf-text-muted);
            max-width: 700px;
            margin: 0 auto 48px auto;
            line-height: 1.4;
        }

        /* --- BOTÃO WEBFLOW (PULSE) --- */
        div.stButton > button {
            background-color: var(--wf-blue) !important;
            color: white !important;
            border: none !important;
            padding: 16px 40px !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            transition: all 0.3s cubic-bezier(0.19, 1, 0.22, 1) !important;
            font-size: 16px !important;
            box-shadow: 0 4px 14px rgba(67, 83, 255, 0.39) !important;
        }

        div.stButton > button:hover {
            transform: translateY(-4px) !important;
            box-shadow: 0 6px 20px rgba(67, 83, 255, 0.5) !important;
            background-color: #3142ff !important;
        }

        /* --- CARDS COM BORDAS GRADIENTES --- */
        .wf-feature-card {
            background: white;
            border-radius: 24px;
            padding: 40px;
            height: 100%;
            position: relative;
            border: 1px solid #eee;
            transition: 0.4s;
            overflow: hidden;
        }

        .wf-feature-card:hover {
            border-color: var(--wf-blue);
            box-shadow: 0 30px 60px rgba(0,0,0,0.05);
        }

        .wf-feature-title { font-size: 28px; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.02em; }
        .wf-feature-desc { font-size: 16px; color: var(--wf-text-muted); line-height: 1.6; }

        /* --- SEÇÃO DARK (COLABORAÇÃO) --- */
        .wf-dark-section {
            background-color: var(--wf-black);
            color: white;
            padding: 120px 10%;
            border-radius: 60px 60px 0 0;
            margin-top: 100px;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVEGAÇÃO ---
    st.markdown("""
    <div style="padding: 20px 10%; display: flex; justify-content: space-between; align-items: center; background: white; border-bottom: 1px solid #f0f0f0; position: sticky; top:0; z-index:999;">
        <div style="font-weight: 800; font-size: 24px;">Webflow</div>
        <div style="display: flex; gap: 40px; font-weight: 500; font-size: 14px; color: #333;">
            <span>Product</span>
            <span>Solutions</span>
            <span>Resources</span>
            <span style="color: var(--wf-blue); font-weight: 700;">Get started — it's free</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO ---
    st.markdown('<div class="wf-hero">', unsafe_allow_html=True)
    st.markdown('<div class="wf-badge">NEW: EDITING MODE</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="wf-h1">Build better,<br>together.</h1>', unsafe_allow_html=True)
    st.markdown('<p class="wf-sub">Transform workflow with powerful collaboration tools that let designers, developers, and content creators work in parallel.</p>', unsafe_allow_html=True)
    
    c_h1, c_h2, c_h3 = st.columns([1, 0.8, 1])
    with c_h2:
        st.button("Start building today")
    
    st.markdown("""
        <div style="margin-top: 80px; background: white; border-radius: 20px; padding: 10px; border: 1px solid #eee; box-shadow: 0 40px 100px rgba(0,0,0,0.08);">
            <img src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=1400" style="width: 100%; border-radius: 12px;">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- FEATURES GRID ---
    st.markdown('<div style="padding: 120px 10%;">', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    def render_wf_card(col, title, desc, tag):
        with col:
            st.markdown(f"""
            <div class="wf-feature-card">
                <p style="color: var(--wf-blue); font-weight: 700; font-size: 12px; margin-bottom: 20px;">{tag}</p>
                <h2 class="wf-feature-title">{title}</h2>
                <p class="wf-feature-desc">{desc}</p>
                <div style="margin-top: 40px; height: 200px; background: #f8f8fa; border-radius: 12px;"></div>
            </div>
            """, unsafe_allow_html=True)

    render_wf_card(col1, "Parallel editing", "Designers can build while editors update content, all without overwriting each other's work.", "SPEED")
    render_wf_card(col2, "Page branching", "Create branches to work on pages in isolation, then merge them back into the main site when ready.", "CONTROL")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- DARK SECTION (THE "WOW" FACTOR) ---
    st.markdown('<div class="wf-dark-section">', unsafe_allow_html=True)
    c_d1, c_d2 = st.columns([1.2, 1])
    with c_d1:
        st.markdown("""
        <h2 style="font-size: 52px; font-weight: 800; letter-spacing: -0.04em; line-height: 1.1;">
            Stop working in silos.<br>
            <span style="background: var(--wf-accent-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Start working in sync.
            </span>
        </h2>
        <p style="font-size: 18px; color: #aaa; margin: 30px 0; line-height: 1.6;">
            Webflow Enterprise gives your large teams the tools they need to maintain brand consistency while moving faster than ever.
        </p>
        """, unsafe_allow_html=True)
        st.button("Contact Enterprise Sales", key="dark_btn")
    
    with c_d2:
        st.markdown("""
        <div style="padding: 40px; background: #111; border: 1px solid #333; border-radius: 24px; text-align: center;">
            <p style="font-size: 14px; color: #666; margin-bottom: 20px;">TRUSTED BY INNOVATORS</p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; opacity: 0.5; filter: grayscale(1);">
                <h3 style="color:white">NYT</h3>
                <h3 style="color:white">TED</h3>
                <h3 style="color:white">DISCORD</h3>
                <h3 style="color:white">REVOLUT</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 100px 10%; background: white;">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 40px;">
            <div>
                <h4 style="font-weight: 800; font-size: 24px; margin-bottom: 20px;">Webflow</h4>
                <p style="color: #777;">Design and build for the web.</p>
            </div>
            <div style="display: flex; gap: 60px;">
                <div><b>Product</b><br><br><span style="color:#777; line-height: 2;">Features<br>CMS<br>Ecommerce</span></div>
                <div><b>Company</b><br><br><span style="color:#777; line-height: 2;">About<br>Careers<br>Manifesto</span></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Webflow Collaboration | Full Power")
    render()
