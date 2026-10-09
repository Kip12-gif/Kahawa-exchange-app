import json
import folium
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(
    page_title="EUDR Farm Traceability | KahawaExchange",
    page_icon="🌱",
    layout="wide",
)

st.title("🌱 EUDR Farm Boundary & Geo-Traceability Pass")
st.caption(
    "Verify deforestation-free compliance (EU Regulation 2023/1115) with"
    " standard GIS polygons."
)

st.divider()

# Sample Farm Polygon Dataset
MOCK_FARMS = {
    "Nyeri Hill Farm Lot #102": {
        "coop": "Nyeri Hill Farmers Co-op",
        "farmer": "Joseph Mwangi",
        "altitude": "1,850 m.a.s.l",
        "hectares": 2.4,
        "center": [-0.4250, 36.9510],
        "coordinates": [
            [-0.4240, 36.9500],
            [-0.4240, 36.9520],
            [-0.4260, 36.9525],
            [-0.4260, 36.9505],
        ],
    },
    "Tekangu FCS Plot #44": {
        "coop": "Tekangu FCS",
        "farmer": "Mary Wambui",
        "altitude": "1,720 m.a.s.l",
        "hectares": 1.8,
        "center": [-0.5120, 37.0450],
        "coordinates": [
            [-0.5110, 37.0440],
            [-0.5110, 37.0460],
            [-0.5130, 37.0465],
            [-0.5130, 37.0445],
        ],
    },
}

st.sidebar.header("🗺️ Select Coffee Lot")
selected_farm_name = st.sidebar.selectbox(
    "Choose Registered Estate / Plot", list(MOCK_FARMS.keys())
)
farm_info = MOCK_FARMS[selected_farm_name]

col1, col2 = st.columns([1, 2])

with col1:
  st.subheader("📋 Plot Verification Data")
  st.markdown(f"**Cooperative:** {farm_info['coop']}")
  st.markdown(f"**Farmer:** {farm_info['farmer']}")
  st.markdown(f"**Altitude:** {farm_info['altitude']}")
  st.markdown(f"**Calculated Area:** {farm_info['hectares']} Hectares")

  st.divider()

  st.success("✅ **EUDR Status: COMPLIANT**")
  st.info(
      "• Polygon Boundary verified\n• Post-2020 Forest Change: 0%\n• Verified"
      " via Open Satellite Layers"
  )

  dds_json = {
      "eudr_certificate_id": (
          f"EUDR-KE-2026-{selected_farm_name[:4].upper()}"
      ),
      "plot_name": selected_farm_name,
      "coordinates_geojson": farm_info["coordinates"],
      "deforestation_free": True,
      "cutoff_date_verified": "2020-12-31",
  }

  st.download_button(
      label="📄 Download EUDR Compliance Certificate (JSON)",
      data=json.dumps(dds_json, indent=2),
      file_name=f"{selected_farm_name}_EUDR_Pass.json",
      mime="application/json",
  )

with col2:
  st.subheader("📡 Satellite Polygon Boundary View")

  m = folium.Map(
      location=farm_info["center"],
      zoom_start=16,
      tiles=(
          "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
      ),
      attr="Esri World Imagery",
  )

  folium.Polygon(
      locations=farm_info["coordinates"],
      color="#2E8B57",
      weight=3,
      fill=True,
      fill_color="#32CD32",
      fill_opacity=0.35,
      popup=f"<b>{selected_farm_name}</b><br>Area: {farm_info['hectares']} ha",
  ).add_to(m)

  folium.Marker(
      location=farm_info["center"],
      popup=f"{selected_farm_name} Center Point",
      icon=folium.Icon(color="green", icon="leaf"),
  ).add_to(m)

  st_folium(m, width="100%", height=500)