import streamlit as st

st.set_page_config(
    page_title="Contracts & Escrow | KahawaExchange",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Trade Contracts & DSS Escrow Vault")
st.caption("Secure multi-currency escrow holding and Central Bank-regulated Direct Settlement System (DSS) automated disbursements.")

st.divider()

# Active Contracts Simulation
st.subheader("🔒 Active Trade Contracts")

contracts = [
    {
        "id": "CTR-2026-0891",
        "roaster": "Berlin Coffee Roasters (Germany)",
        "coop": "Nyeri Hill Farmers Co-op",
        "volume": "30 Bags (1,800 kg)",
        "value_usd": 19044.00,
        "status": "Escrow Funded (Awaiting Port Clearance)",
        "dss_status": "Locked in Vault",
        "progress": 0.60
    },
    {
        "id": "CTR-2026-0742",
        "roaster": "Tokyo Craft Coffee (Japan)",
        "coop": "Tekangu Farmers Co-op",
        "volume": "50 Bags (3,000 kg)",
        "value_usd": 27116.00,
        "status": "Delivered & Accepted",
        "dss_status": "Disbursed to Co-op Account",
        "progress": 1.00
    }
]

for ctr in contracts:
    with st.container(border=True):
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.markdown(f"### Contract `{ctr['id']}`")
            st.markdown(f"**Buyer:** {ctr['roaster']}")
            st.markdown(f"**Seller:** {ctr['coop']}")
            st.markdown(f"**Lot Volume:** {ctr['volume']}")
            
        with col2:
            st.metric("Contract Value", f"${ctr['value_usd']:,.2f} USD")
            st.markdown(f"**Vault Status:** `{ctr['status']}`")
            
        with col3:
            st.markdown(f"**DSS Payout Rail:**")
            if ctr['progress'] == 1.00:
                st.success(f"✅ {ctr['dss_status']}")
            else:
                st.warning(f"⏳ {ctr['dss_status']}")
                if st.button("Simulate Port Acceptance", key=ctr['id']):
                    st.success("Delivery Confirmed! Triggering DSS automated API payout...")
        
        st.progress(ctr['progress'])

st.divider()

st.subheader("🏛️ CMA Direct Settlement System (DSS) Flow")
st.info("""
1. **Fund Placement:** International buyer wires USD/EUR into the KahwaExchange Escrow Vault.
2. **Bill of Lading Handshake:** Export documents are verified upon vessel loading in Mombasa.
3. **Automated Settlement:** Buyer confirms lot inspection $\rightarrow$ DSS API releases funds straight to Cooperative Bank Accounts & Farmer Mobile Wallets.
""")
