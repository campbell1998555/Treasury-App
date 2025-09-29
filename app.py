import streamlit as st

# --- CONFIGURATION ---
# Set the page configuration for a wide, clean, and educational focus
st.set_page_config(
    # Updated title to reflect Data Science focus
    page_title="Treasury Transformation: Data Science for the Treasury Professional", 
    page_icon="🤖",  # Robot icon for automation and efficiency
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define basic CSS styles within the Python file for professional, educational look
css = """
/* Font and Base Styles */
html, body {
    font-family: 'Inter', sans-serif;
    color: #333333; /* Black text for readability */
}
.stApp {
    background-color: #FAFAFA; /* Off-White background for clean contrast (Campbell White/Accent) */
}
/* Main Header Style - Deep Campbell Navy Blue */
h1 {
    color: #012169; /* Deep Navy Blue (Campbell Blue) */
    font-weight: 800;
    font-size: 2.5em;
    padding-bottom: 10px;
}
/* Subheader Style - Used for section titles - Deep Campbell Green */
h3 {
    color: #1E423C; /* Deep Campbell Green */
    border-bottom: 3px solid #1E423C; /* Green underline */
    padding-bottom: 8px;
    margin-top: 40px;
    margin-bottom: 25px;
    font-weight: 700;
}
/* Card/Info Box Styling for Learning Paths - Teal/Accent Blue */
.stAlert {
    border-left: 5px solid #00A0A0 !important; /* Teal accent (Modern Campbell Blue/Accent) */
    border-radius: 8px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.05);
}
/* Separator */
.divider {
    border-top: 1px solid #d0d0d0;
    margin-top: 30px;
    margin-bottom: 30px;
}
/* Button style - Primary Deep Campbell Green */
.stButton>button {
    background-color: #1E423C; /* Deep Campbell Green */
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    transition: background-color 0.3s;
}
.stButton>button:hover {
    background-color: #317068; /* Slightly lighter Green on hover */
}
"""
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


# --- SIDEBAR CONTENT: NAVIGATION & RESOURCES ---
with st.sidebar:
    # Updated text to TreasuryC
    st.image("https://placehold.co/150x50/012169/ffffff?text=TreasuryC", width=150)
    st.title("Navigation")
    st.markdown("---")
    st.markdown("##### Learning Paths")
    # Simplified paths as requested
    st.markdown("Excel")
    st.markdown("Power Platforms")
    st.markdown("Treasury Management System")
    st.markdown("---")
    st.markdown("##### Resources")
    # Updated resource links as requested
    st.markdown("- [Power BI Report Templates for Back Office and Front Office](#)")
    st.markdown("- [Power Automate Templates for Treasury Professionals](#)")
    st.markdown("- [XML Templates using Excel for TMS Import](#)")


# --- MAIN PAGE CONTENT: HEADER & MISSION ---

st.header("Treasury Transformation: Data Efficiency and the Power Platform")

# 1. MISSION STATEMENT SECTION
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Empowering Treasury Teams through Data Mastery and Automation")
    st.write(
        """
        This platform is dedicated to teaching front and back office professionals 
        how to leverage tools like the Power Platforms, Excel and the TMS to eliminate manual work, 
        accelerate financial closings, and enhance decision-making.
        """
    )
    # Updated button text
    st.button("Start Your Treasury Journey")

with col2:
    # Imagery of the Bath, Somerset area (e.g., Royal Crescent area)
    st.image(
        "https://images.pexels.com/photos/1018635/pexels-photo-1018635.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        caption="",
        width=300
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# 2. KEY LEARNING PATHS SECTION
st.markdown("### Key Learning Paths for Treasury Professionals")

path_col1, path_col2, path_col3 = st.columns(3)

with path_col1:
    st.info("##### 🐍 Data Manipulation & Cleanup")
    st.markdown(
        """
        - **Advanced Excel:** Using Power Query for dynamic data ingestion and transformation.
        - **Data Cleaning:** Standardizing counterparty names and transaction codes.
        """
    )

with path_col2:
    st.info("##### ⚙️ Process Automation (Power Automate)")
    st.markdown(
        """
        - **RPA for Back Office:** Automating daily liquidity reporting and TMS data entry.
        - **Workflow Design:** Building approval flows for payments and guarantee requests.
        - **Email Handling:** Automatically extracting payment confirmations and saving them to SharePoint.
        """
    )

with path_col3:
    st.info("##### 📊 Insightful Reporting (Power BI)")
    st.markdown(
        """
        - **Dashboard Design:** Creating intuitive, drill-down dashboards for cash visibility.
        - **DAX Measures:** Implementing custom measures for calculating WACC, VaR, and covenant ratios.
        - **Executive Summaries:** Presenting complex risk metrics clearly to management.
        """
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# 3. FEATURED CASE STUDIES (Emphasis on Power Platform)
# REMOVED - This section was removed to streamline the page as requested by the user.

st.markdown('<a name="contact_me_section"></a>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# 4. GET IN TOUCH / CALL TO ACTION
st.markdown("### Ready to Transform Your Treasury Role?")
st.write("Have specific questions about Power Platform implementation or data governance? Reach out to schedule a consultation.")

# Simple contact form simulation (Streamlit form functionality)
with st.form(key='contact_form'):
    user_name = st.text_input("Your Name", placeholder="Jamie")
    user_email = st.text_input("Your Professional Email", placeholder="jamie@example.com")
    message = st.text_area("Your Specific Automation/Data Query", placeholder="I need help automating my monthly debt schedule...")
    submit_button = st.form_submit_button(label='Request Consultation')

    if submit_button:
        # Placeholder success message (integration needed for a real email service)
        st.success(f"Thank you, {user_name}! Your consultation request has been received and we will be in touch shortly.")

st.markdown('---')
st.markdown('A Treasury Resource (2025) | Powered by Streamlit')


