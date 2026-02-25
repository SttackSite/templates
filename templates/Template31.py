import streamlit as st

def render():
    # --- STATEMENT DESIGN SYSTEM ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

        :root {
            --st-bg: #e7f2e8; /* Pistachio Soft */
            --st-black: #000000;
            --st-border: rgba(0, 0, 0, 0.1);
        }

        .stApp { background-color: var(--st-bg); color: var(--st-black); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { 
            font-family: 'Inter', sans-serif; 
            -webkit-font-smoothing: antialiased;
        }

        /* --- GRID LAYOUT --- */
        .st-grid-container {
            border-top: 1px solid var(--st-black);
            display: grid;
            grid-template-columns: 1fr 1fr;
        }

        .st-grid-item {
            border-right: 1px solid var(--st-black);
            border-bottom: 1px solid var(--st-black);
            padding: 60px 8%;
        }

        /* --- TYPOGRAPHY --- */
        .st-h1 {
            font-size: clamp(50px, 10vw, 140px);
            font-weight: 900;
            line-height: 0.85;
            letter-spacing: -0.06em;
            margin-bottom: 60px;
            text-transform: uppercase;
        }

        .st-h2 {
            font-size: 42px;
            font-weight: 700;
            line-height: 1;
            letter-spacing: -0.04em;
        }

        /* --- BUTTON (SOLID & SHARP) --- */
        div.stButton > button {
            background-color: var(--st-black) !important;
            color: white !important;
            border: none !important;
            padding: 20px 40px !important;
            font-weight: 700 !important;
            border-radius: 0px !important; /* Totalmente quadrado */
            transition: 0.2s !important;
            font-size: 14px !important;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            width: 100% !important;
        }

        div.stButton > button:hover {
            background-color: #333 !important;
            transform: translate(4px, -4px);
            box-shadow: -4px 4px 0px var(--st-black);
        }

        /* --- NAV --- */
        .st-nav {
            padding: 30px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--st-black);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAVBAR ---
    st.markdown("""
    <div class="st-nav">
        <div style="font-weight: 900; font-size: 24px; letter-spacing: -1px;">STATEMENT</div>
        <div style="display: flex; gap: 40px; font-size: 12px; font-weight: 700; text-transform: uppercase;">
            <span>Works</span>
            <span>About</span>
            <span>Journal</span>
            <span style="background: var(--st-black); color: white; padding: 5px 10px;">Contact</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown('<div style="padding: 100px 5% 60px 5%;">', unsafe_allow_html=True)
    st.markdown('<h1 class="st-h1">MAKING A<br>STATEMENT.</h1>', unsafe_allow_html=True)
    
    col_h1, col_h2 = st.columns([1.5, 1])
    with col_h1:
        st.markdown("""
            <p style="font-size: 24px; font-weight: 400; line-height: 1.3; max-width: 600px;">
                We are a creative studio helping brands define their voice in a noisy world through radical clarity and intentional design.
            </p>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- GRID DE CONTEÚDO (ESTILO BENTO) ---
    st.markdown('<div class="st-grid-container">', unsafe_allow_html=True)
    
    # Item 1
    st.markdown('<div class="st-grid-item">', unsafe_allow_html=True)
    st.markdown('<div style="background:#000; height:300px; margin-bottom:30px;"><img src="https://images.unsplash.com/photo-1558655146-d09347e92766?w=800" style="width:100%; height:100%; object-fit:cover; filter:grayscale(1);"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="st-h2">Digital Strategy</h2>', unsafe_allow_html=True)
    st.markdown('<p style="margin: 20px 0;">Beyond the surface. We build foundations that last.</p>', unsafe_allow_html=True)
    st.button("View Details", key="btn1")
    st.markdown('</div>', unsafe_allow_html=True)

    # Item 2
    st.markdown('<div class="st-grid-item" style="border-right:none">', unsafe_allow_html=True)
    st.markdown('<div style="background:#000; height:300px; margin-bottom:30px;"><img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800" style="width:100%; height:100%; object-fit:cover; filter:grayscale(1);"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="st-h2">Visual Identity</h2>', unsafe_allow_html=True)
    st.markdown('<p style="margin: 20px 0;">Identity is not a logo. It is a feeling and a promise.</p>', unsafe_allow_html=True)
    st.button("Explore Work", key="btn2")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
    <div style="padding: 100px 5%; background: var(--st-black); color: var(--st-bg);">
        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
            <div>
                <h1 style="color: var(--st-bg); font-size: 80px; font-weight: 900; margin-bottom: 40px; letter-spacing: -4px;">HI.</h1>
                <p style="font-size: 18px; opacity: 0.8;">Berlin / Worldwide</p>
            </div>
            <div style="text-align: right; font-weight: 700; text-transform: uppercase; font-size: 14px;">
                Instagram<br>LinkedIn<br>Twitter<br><br>
                © 2026 STATEMENT STUDIO
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Statement | Creative Studio")
    render()
