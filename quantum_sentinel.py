import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Quantum Tensor Anomaly Sentinel",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #030712; color: #38bdf8; }
    .stSidebar { background-color: #0f172a; }
    h1, h2, h3 { color: #38bdf8; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Quantum Tensor Anomaly & Outlier Sentinel")
st.markdown("---")

st.sidebar.header("🎛️ Quantum Tensor Controls")
signal_frequency = st.sidebar.slider("Signal Frequency (Hz)", 10, 100, 50, 5)
contamination_rate = st.sidebar.slider("Anomaly Contamination Rate", 0.01, 0.20, 0.05, 0.01)
z_threshold = st.sidebar.slider("Z-Score Outlier Threshold", 1.5, 4.0, 2.5, 0.25)

try:
    np.random.seed(42)
    time_steps = np.linspace(0, 20, 300)
    base_signal = np.sin(signal_frequency * time_steps / 10) + np.random.normal(0, 0.3, 300)
    
    anomaly_count = int(300 * contamination_rate)
    anomaly_indices = np.random.choice(300, anomaly_count, replace=False)
    base_signal[anomaly_indices] += np.random.choice([-1, 1], anomaly_count) * np.random.uniform(4.0, 7.0, anomaly_count)
    
    mean_val = np.mean(base_signal)
    std_val = np.std(base_signal)
    z_scores = np.abs((base_signal - mean_val) / std_val)
    outlier_mask = z_scores > z_threshold
    
    df_sentinel = pd.DataFrame({
        "Time_Step": time_steps,
        "Tensor_Signal": base_signal,
        "Z_Score": z_scores,
        "Is_Anomaly": outlier_mask
    })

    st.subheader("📊 Quantum Telemetry & Real-Time Threat Analysis")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="🚨 Detected Anomalies", value=f"{np.sum(outlier_mask)} Outliers", delta="Critical Alert")
    with col2:
        st.metric(label="⚡ Standard Deviation", value=f"{std_val:.4f}σ", delta="Volatile")
    with col3:
        st.metric(label="🛡️ Sentinel Core Status", value="Secured / Active", delta="100% Shielded")
        
    st.markdown(f"**Mathematical Threshold Rule:** `|Z-Score| > {z_threshold}` (Isolating extreme standard deviations)")
    st.markdown("---")

    fig, ax = plt.subplots(figsize=(10, 4.5))
    fig.patch.set_facecolor('#030712')
    ax.set_facecolor('#0f172a')
    
    normal_data = df_sentinel[~df_sentinel['Is_Anomaly']]
    anomaly_data = df_sentinel[df_sentinel['Is_Anomaly']]
    
    ax.plot(normal_data['Time_Step'], normal_data['Tensor_Signal'], color='#38bdf8', linewidth=1.5, label='Normal Quantum Stream')
    ax.scatter(anomaly_data['Time_Step'], anomaly_data['Tensor_Signal'], color='#ef4444', s=40, zorder=5, label='Isolated Anomalies')
    
    ax.set_title("Real-Time Tensor Signal & Outlier Isolation Stream", color='#38bdf8', fontsize=12, fontfamily='monospace')
    ax.tick_params(colors='#38bdf8')
    ax.legend(facecolor='#0f172a', edgecolor='#38bdf8', labelcolor='#38bdf8')
    
    for spine in ax.spines.values():
        spine.set_edgecolor('#38bdf8')
        
    st.pyplot(fig)

except Exception as e:
    st.error(f"⚠️ Quantum Anomaly Exception Caught: {e}")
    st.info("The sentinel pipeline remains online. Please re-adjust your parameters.")
