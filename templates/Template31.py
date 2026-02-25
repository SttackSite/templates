import streamlit as st

def render():
    # --- SIDESTAGE DESIGN SYSTEM ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:italic&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --ss-bg: #f9f9f7;
            --ss-black: #1a1a1a;
            --ss-accent: #ff5c35; /* O toque de cor deles */
            --ss-text-muted: #666660;
        }

        .stApp { background-color: var(--ss-bg); color: var(--ss-black); }
        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        /* --- TYPOGRAPHY --- */
        .ss-h1 {
            font-family: 'Inter', sans-serif;
            font-size: clamp(45px, 8vw, 95px);
            font-weight: 400;
            line-height: 0.95;
            letter-spacing: -0.05em;
            margin-bottom: 40px;
        }

        .ss-serif {
            font-family: 'Instrument Serif', serif;
            font-style: italic;
            font-size: 1.1em;
        }

        .ss-sub {
            font-size: 20px;
            color: var(--ss-text-muted);
            max-width: 600px;
            line-height: 1.5;
            margin-bottom: 50px;
        }

        /* --- BUTTON SIDESTAGE (SOFT & ROUND) --- */
        div.stButton > button {
            background-color: var(--ss-black) !important;
            color: white !important;
            border: none !important;
            padding: 14px 32px !important;
            font-weight: 500 !important;
            border-radius: 100px !important;
            transition: all 0.3s ease !important;
            font-size: 16px !important;
        }

        div.stButton > button:hover {
            transform: scale(1.05) !important;
            background-color: #333 !important;
        }

        /* --- PORTFOLIO CARDS --- */
        .portfolio-grid {
            padding: 100px 8%;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .ss-card {
            background: white;
            border-radius: 32px;
            padding: 50px 40px;
            transition: 0.5s cubic-bezier(0.2, 1, 0.2, 1);
            border: 1px solid rgba(0,0,0,0.03);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 400px;
        }

        .ss-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 40px 80px rgba(0,0,0,0.05);
        }

        .ss-card-tag {
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--ss-text-muted);
            margin-bottom: 20px;
        }

        .ss-card-title {
            font-size: 32px;
            font-weight: 400;
            letter-spacing: -0.03em;
            line-height: 1.1;
        }

        /* --- NAVIGATION --- */
        .ss-nav {
            padding: 40px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: transparent;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- NAV ---
    st.markdown("""
    <div class="ss-nav">
        <div style="font-weight: 600; font-size: 20px; letter-spacing: -1px;">sidestage<span style="color:var(--ss-accent)">.</span></div>
        <div style="display: flex; gap: 40px; font-size: 13px; font-weight: 500;">
            <span>Manifesto</span>
            <span>Portfolio</span>
            <span>Team</span>
            <span style="border-bottom: 1px solid var(--ss-black)">Get in touch</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- HERO ---
    st.markdown('<div style="padding: 120px 8% 80px 8%;">', unsafe_allow_html=True)
    st.markdown("""
        <h1 class="ss-h1">
            Backing the <span class="ss-serif">misfits</span><br>
            building the future.
        </h1>
    """, unsafe_allow_html=True)
    
    col_h1, col_h2 = st.columns([1.2, 1])
    with col_h1:
        st.markdown('<p class="ss-sub">Sidestage is a seed-stage venture fund for founders who think differently. We invest in the stage before it becomes obvious.</p>', unsafe_allow_html=True)
        st.button("Partner with us")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- PORTFOLIO SECTION ---
    st.markdown('<div class="portfolio-grid">', unsafe_allow_html=True)
    
    def render_ss_card(title, tag, category):
        st.markdown(f"""
        <div class="ss-card">
            <div>
                <div class="ss-card-tag">{tag}</div>
                <div class="ss-card-title">{title}</div>
            </div>
            <div style="font-size: 13px; color: var(--ss-text-muted); border-top: 1px solid #eee; padding-top: 20px;">
                {category}
            </div>
        </div>
        """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        render_ss_card("Flow State", "Fintech", "Series A — 2026")
    with c2:
        render_ss_card("Nova Intelligence", "AI / Core", "Seed — 2025")
    with c3:
        render_ss_card("Arcane Bio", "Healthtech", "Pre-seed — 2026")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- MANIFESTO SECTION (THE "CREME" PART) ---
    st.markdown("""
    <div style="padding: 150px 8%; background: white; text-align: center; border-radius: 80px 80px 0 0;">
        <span class="ss-card-tag" style="color: var(--ss-accent)">Our Thesis</span>
        <h2 style="font-size: clamp(30px, 4vw, 54px); font-weight: 400; max-width: 900px; margin: 30px auto; line-height: 1.2; letter-spacing: -0.04em;">
            We believe the most <span class="ss-serif">daring ideas</span> often come from those who have been overlooked by the mainstream.
        </h2>
    </div>
    """, unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown(f"""
    <div style="padding: 100px 8%; background: var(--ss-black); color: var(--ss-bg);">
        <div style="display: flex; justify-content: space-between; align-items: flex-end;">
            <div>
                <h1 style="color: white; margin-bottom: 40px; font-size: 40px;">Let's build.</h1>
                <p style="opacity: 0.6;">Berlin / London / San Francisco</p>
            </div>
            <div style="text-align: right; opacity: 0.6; font-size: 13px;">
                © 2026 Sidestage Ventures. <br> Built for the unconventional.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Sidestage Ventures")
    render()
