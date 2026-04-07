# import streamlit as st
# import joblib
# import numpy as np

# # load model
# model=joblib.load("regression_model.joblib")

# st.title("🎓 CGPA to Package Predictor")
# st.write("Enter your CGPA to predict the expected package")

# cgpa=st.number_input(
#     "Enter CGPA",
#     min_value=0.0,
#     max_value=10.0,
#     step=0.1
# )

# if st.button("Predict Package"):
#     input_data=np.array([[cgpa]])
#     prediction=model.predict(input_data)

#     # ✅ FIX HERE
#     predicted_package=prediction[0][0]

#     st.success(f"👜 predicted Package: ₹ {predicted_package:.2f} LPA")



import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="CGPA Predictor", page_icon="🎓", layout="centered")

# Load model
model = joblib.load("regression_model.joblib")

# Title Section
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🎓 CGPA to Package Predictor</h1>
    <p style='text-align: center;'>Predict your expected placement package based on CGPA</p>
""", unsafe_allow_html=True)

st.divider()

# Input Section
st.subheader("Enter Details")
cgpa = st.slider("Select your CGPA", 0.0, 10.0, 7.0, 0.1)

# Predict Button
if st.button("Predict Package"):
    input_data = np.array([[cgpa]])
    prediction = model.predict(input_data)

    predicted_package = prediction[0][0]

    # Result Display
    st.success(f"💰 Estimated Package: ₹ {predicted_package:.2f} LPA")

    # Graph Section
    st.subheader("📊 Prediction Visualization")

    # Generate sample CGPA range
    cgpa_range = np.linspace(0, 10, 50)
    predictions = model.predict(cgpa_range.reshape(-1, 1))

    # Plot
    fig, ax = plt.subplots()
    ax.plot(cgpa_range, predictions, label="Predicted Curve")
    ax.scatter(cgpa, predicted_package, label="Your CGPA", marker='o')

    ax.set_xlabel("CGPA")
    ax.set_ylabel("Package (LPA)")
    ax.set_title("CGPA vs Package")
    ax.legend()

    st.pyplot(fig)

st.divider()

# Footer
st.markdown("""
    <p style='text-align: center; font-size: 12px;'>Built with Streamlit | Data Analytics Project</p>
""", unsafe_allow_html=True)

