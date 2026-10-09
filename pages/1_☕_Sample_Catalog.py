import streamlit as st

st.set_page_config(
    page_title="Sample Catalog | KahawaExchange",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Specialty Micro-Lot & Sample Catalog")
st.caption("Discover high-scoring Kenyan Arabica and order express tasting samples directly from registered cooperatives.")

st.divider()

# Sample Inventory Data
MOCK_LOTS = [
    {
        "id": "LOT-NYE-001",
        "coop": "Nyeri Hill Farmers Co-op",
        "grade": "AA",
        "score": 88.5,
        "process": "Washed",
        "price_fob": 4.80,
        "notes": ["Blackcurrant", "Citrus", "Floral"],
        "altitude": "1,850 m.a.s.l",
        "bags_left": 40
    },
    {
        "id": "LOT-TEK-044",
        "coop": "Tekangu Farmers Co-op",
        "grade": "AB",
        "score": 86.5,
        "process": "Washed",
        "price_fob": 4.10,
        "notes": ["Grapefruit", "Cane Sugar", "Bright Acidity"],
        "altitude": "1,720 m.a.s.l",
        "bags_left": 60
    },
    {
        "id": "LOT-OTH-012",
        "coop": "Othaya Farmers Society",
        "grade": "PB (Peaberry)",
        "score": 87.2,
        "process": "Natural",
        "price_fob": 4.35,
        "notes": ["Winey", "Dark Berry", "Full Body"],
        "altitude": "1,800 m.a.s.l",
        "bags_left": 25
    },
    {
        "id": "LOT-GAK-009",
        "coop": "Gakundu Estate",
        "grade": "AA",
        "score": 89.0,
        "process": "Washed",
        "price_fob": 5.20,
        "notes": ["Jasmine", "Bergamot", "Complex Acidity"],
        "altitude": "1,900 m.a.s.l",
        "bags_left": 15
    }
]

# Initialize Session State for Sample Cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Sidebar Filters
st.sidebar.header("🔍 Filter Coffee Lots")
min_score = st.sidebar.slider("Minimum SCA Cupping Score", 80.0, 90.0, 85.0, 0.5)
selected_grade = st.sidebar.multiselect("Coffee Grade", ["AA", "AB", "PB (Peaberry)"], default=["AA", "AB", "PB (Peaberry)"])

# Main Grid View
filtered_lots = [
    lot for lot in MOCK_LOTS 
    if lot["score"] >= min_score and lot["grade"] in selected_grade
]

cols = st.columns(2)

for idx, lot in enumerate(filtered_lots):
    col = cols[idx % 2]
    with col:
        with st.container(border=True):
            st.markdown(f"### {lot['coop']} ({lot['grade']})")
            st.caption(f"**Lot Ref:** `{lot['id']}` | **Altitude:** {lot['altitude']}")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("SCA Score", f"{lot['score']} pts")
            c2.metric("Process", lot['process'])
            c3.metric("FOB Price", f"${lot['price_fob']:.2f}/lb")
            
            st.markdown("**Flavor Profile:** " + ", ".join([f"`{n}`" for n in lot['notes']]))
            st.markdown(f"**Available Volume:** {lot['bags_left']} Bags (60kg each)")
            
            btn_col1, btn_col2 = st.columns(2)
            if btn_col1.button("Order 200g Sample ($35)", key=f"sample_{lot['id']}"):
                if lot['id'] not in st.session_state.cart:
                    st.session_state.cart.append(lot)
                    st.success(f"Added {lot['id']} sample to cart!")
                else:
                    st.info("Sample already in cart.")

st.divider()

# Cart Sidebar Summary
st.sidebar.divider()
st.sidebar.subheader("🛒 Sample Order Cart")
if st.session_state.cart:
    total_cost = len(st.session_state.cart) * 35.0
    for item in st.session_state.cart:
        st.sidebar.text(f"• {item['id']} ({item['coop']})")
    st.sidebar.markdown(f"**Total Express Shipping Cost:** `${total_cost:.2f}`")
    if st.sidebar.button("Proceed to Sample Checkout"):
        st.sidebar.success("Sample order placed! Tracking code sent via email.")
        st.session_state.cart = []
else:
    st.sidebar.caption("No samples in cart.")
