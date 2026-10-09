import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="KahawaExchange | B2B Specialty Coffee Marketplace",
    page_icon="☕",
    layout="wide",
)

# Header Section
st.title("☕ KahawaExchange")
st.subheader("Direct-Trade Kenyan Specialty Coffee Marketplace & DSS Escrow")
st.markdown(
    "Connecting International Specialty Roasters with Verified Kenyan"
    " Cooperatives."
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

# Sample Data Visualizations
left_col, right_col = st.columns([2, 1])

with left_col:
  st.markdown("### 📊 Active Coffee Lots by Grade & Price")
  # Mock lot inventory dataset
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
  )
  st.plotly_chart(fig, use_container_width=True)

with right_col:
  st.markdown("### 🚀 Quick Actions")
  st.info(
      "**International Roaster?** Navigate to **Sample Catalog** in the sidebar"
      " to order green coffee tasting jars."
  )
  st.success(
      "**Kenyan Co-op / Miller?** Use the **Coop Dashboard** to upload new"
      " cupping sheets & warehouse warrants."
  )
  st.warning(
      "**EU Customs Verification:** View **Farm Traceability** for automated"
      " EUDR boundary polygons."
  )