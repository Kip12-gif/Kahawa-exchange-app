# ☕ KahawaExchange | B2B Specialty Coffee Marketplace & DSS Escrow

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![EUDR Compliant](https://img.shields.io/badge/EUDR-2020%2F2026%20Verified-green.svg)](https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en)

**KahawaExchange** is an end-to-end B2B digital marketplace bridging the structural gap between **Kenyan Specialty Coffee Cooperatives (FCS) / Estates** and **International Specialty Roasters** (Europe, USA, Asia). 

By integrating Kenya's **Direct Settlement System (DSS)** under the Capital Markets Authority (CMA) framework with real-time **EU Deforestation Regulation (EUDR)** GIS farm boundary validation and a **Micro-Lot Sample Logistics Engine**, KahwaExchange removes disintermediation, streamlines export compliance, and guarantees prompt farmer payouts.

---

## 🌟 Key Features & Core Innovations

### 1. 🧪 Digital Cupping Sheets & Micro-Lot Discovery
* Search and filter high-scoring Arabica lots (**AA, AB, PB, E**) based on **SCA Cupping Scores** (85+ points), altitude (m.a.s.l), processing methods (*Washed, Natural, Honey*), and flavor notes.
* **1-Click Sample Catalog:** International roasters can request 200g green coffee sample jars dispatched via express air-freight directly from Nairobi Coffee Exchange (NCE) sample rooms.

### 2. 🛰️ EUDR GIS Farm Traceability Pass
* Generates automated **Due Diligence Statements (DDS)** required for European imports.
* Validates farm plot coordinates (**point GPS** for <4ha; **polygon GIS boundaries** for ≥4ha) against multi-spectral satellite imagery to prove **zero deforestation post-December 31, 2020**.

### 3. 💳 Multi-Currency Escrow & Direct Settlement System (DSS)
* B2B payments (USD/EUR) are held in secure **Multi-Currency Escrow Vaults**.
* Upon buyer delivery confirmation, the platform triggers automated settlement calls to Kenya's **Central Bank-regulated Direct Settlement System (DSS)**, disbursing net proceeds straight to cooperative bank accounts and farmer wallets.

### 4. 📜 Forward Contracts & Direct-Trade Workflows
* Enables international roasters to lock in future harvest micro-lots with a **20% advance deposit**, giving smallholder farmers upfront liquidity for fertilizers and harvest labor.

---

## 📂 Repository Structure

```text
kahwa-exchange/
├── .streamlit/
│   └── config.toml           # UI styling & color palettes
├── pages/
│   ├── 1_☕_Sample_Catalog.py # International Roaster sample ordering & cupping
│   ├── 2_📜_Contracts_Escrow.py# Contract execution & live DSS escrow tracking
│   ├── 3_🌱_Farm_Traceability.py# Interactive GIS farm boundary maps & EUDR reports
│   └── 4_🏛️_Coop_Dashboard.py # Cooperative inventory, warehouse warrants & payouts
├── app.py                     # Main Landing Page & Market Intelligence Overview
├── requirements.txt           # Production dependencies
├── .gitignore                 # Excludes local secrets & bytecode
└── README.md                  # Project documentation