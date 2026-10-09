import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="KahawaExchange | B2B Specialty Coffee Marketplace",
    page_icon="☕",
    layout="wide",
)

# ==============================================================================
# 🎨 HIGH-CONTRAST LIGHT TEXT & STYLING
# ==============================================================================
BACKGROUND_IMAGE_URL = "https://images.unsplash.com/photo-1447933601403-0c6688de566e?q=80&w=1920&auto=format&fit=crop"

custom_css = f"""
<style>
/* Full Page Background Image with Dark Gradient Overlay */
.stApp {{
    background: linear-gradient(rgba(12, 8, 6, 0.88), rgba(12, 8, 6, 0.92)),
                url("{BACKGROUND_IMAGE_URL}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Force Bright White / High-Legibility Light Text for all Elements */
html, body, [class*="css"], .stMarkdown, p, span, label, h1, h2, h3, h4, h5, h6 {{
    color: #FFFFFF !important;
}}

/* Subtitles, Captions & Secondary Labels */
.stCaption, small, [data-testid="stCaptionContainer"] p {{
    color: #E2D8D0 !important;
}}

/* Metric Card Values & Titles */
[data-testid="stMetricValue"] {{
    color: #F2A93B !important;
    font-size: 2.2rem !important;
    font-weight: 700 !important;
}}

[data-testid="stMetricLabel"] p {{
    color: #E2D8D0 !important;
    font-weight: 600 !important;
}}

/* Translucent Glassmorphism Cards with Crisp Golden Borders */
div[data-testid="stBlock"] {{
    background-color: rgba(26, 18, 14, 0.82) !important;
    border-radius: 12px;
    border: 1px solid rgba(242, 169, 59, 0.3);
    backdrop-filter: blur(10px);
}}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==============================================================================
# ☕ APP CONTENT
# ==============================================================================
st.title("☕ KahwaExchange")
st.subheader("Direct-Trade Kenyan Specialty Coffee Marketplace & DSS Escrow")
st.caption(
    "Connecting International Specialty Roasters directly with Kenya's finest"
    " Coffee Cooperatives."
)

st.divider()

# Market Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric(
    label="Avg. Cupping Score", value="86.8 SCA", delta="Top Grade AA/AB"
)
col2.metric(
    label="Available Lots", value="142 Bags", delta="Nyeri, Kirinyaga, Kiambu"
)
col3.metric(
    label="Active Escrow Volume", value="$184,500", delta="Multi-Currency Vault"
)
col4.metric(
    label="EUDR Traceability Pass", value="100% Compliant", delta="GIS Verified"
)

st.divider()

# Analytics Visualizations
left_col, right_col = st.columns([2, 1])

with left_col:
  st.markdown("### 📊 Active Coffee Lots by Grade & Price")
  data = {
      "Cooperative": [
          "Nyeri Hill Co-op",
          "Tekangu FCS",
          "Othaya Farmers",
          "Gakundu Estate",
          "Kiambu Union",
      ],
      "Grade": ["AA", "AB", "PB", "AA", "AB"],
      "SCA Score": [88.5, 86.5, 87.0, 89.0, 85.5],
      "Price (USD/lb)": [4.80, 4.10, 4.35, 5.20, 3.90],
      "Bags Available": [40, 60, 25, 15, 80],
  }
  fig = px.scatter(
      data,
      x="SCA Score",
      y="Price (USD/lb)",
      size="Bags Available",
      color="Grade",
      hover_name="Cooperative",
      title="Price vs. Quality Matrix (FOB Mombasa)",
      template="plotly_dark",
  )
  fig.update_layout(
      paper_bgcolor="rgba(0,0,0,0)",
      plot_bgcolor="rgba(0,0,0,0)",
      font=dict(color="#FFFFFF"),
  )
  st.plotly_chart(fig, use_container_width=True)

with right_col:
  st.markdown("### 🚀 Quick Navigation")
  st.info(
      "**International Roaster?** Use the sidebar on the left to explore the"
      " **Sample Catalog** and order green coffee tasting jars."
  )
  st.success(
      "**Kenyan Co-op / Miller?** Access the **Coop Dashboard** to list new"
      " harvest lots."
  )
  st.warning(
      "**EU Imports:** Access **Farm Traceability** to download automated EUDR"
      " GIS certificates."
  )
