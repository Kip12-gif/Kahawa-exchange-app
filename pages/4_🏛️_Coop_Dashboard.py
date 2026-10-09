import streamlit as st

st.set_page_config(
    page_title="Coop Dashboard | KahawaExchange",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ Cooperative Management Portal")
st.caption("Manage inventory, submit cupping sheets, and view real-time Direct Settlement System (DSS) disbursements.")

st.divider()

# Overview Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Registered Farmers", "1,240 Members", "+12 this month")
col2.metric("Total Volume Listed", "140 Bags", "Harvest Season 2026")
col3.metric("Pending Payouts", "$19,044 USD", "DSS Vault Escrow")

st.divider()

tab1, tab2 = st.tabs(["➕ List New Coffee Lot", "📊 Cooperative Earnings"])

with tab1:
    st.subheader("Register New Micro-Lot for Export")
    
    with st.form("new_lot_form"):
        f_coop = st.text_input("Cooperative Name", "Nyeri Hill Farmers Co-op")
        f_grade = st.selectbox("Grade", ["AA", "AB", "PB (Peaberry)", "C", "E"])
        f_bags = st.number_input("Number of 60kg Bags Available", min_value=1, value=20)
        f_score = st.slider("SCA Cupping Score (Certified Miller)", 80.0, 95.0, 87.5, 0.1)
        f_notes = st.text_input("Cupping Notes (comma separated)", "Blackcurrant, Floral, High Acidity")
        f_price = st.number_input("Target FOB Price (USD per lb)", min_value=2.0, value=4.50, step=0.10)
        
        submitted = st.form_submit_button("Submit Lot to KahwaExchange")
        if submitted:
            st.success(f"Successfully listed {f_bags} bags of Grade {f_grade} for {f_coop}!")

with tab2:
    st.subheader("Direct Settlement System (DSS) Payout History")
    
    payout_data = [
        {"date": "2026-09-15", "lot": "LOT-TEK-044", "amount_usd": 27116.00, "status": "Disbursed to Co-op Bank"},
        {"date": "2026-08-01", "lot": "LOT-NYE-088", "amount_usd": 14200.00, "status": "Disbursed to Co-op Bank"}
    ]
    
    st.dataframe(payout_data, use_container_width=True)
