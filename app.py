import streamlit as st

# --- CONFIGURATION ---
# Set the page configuration for a wide, clean, and educational focus
st.set_page_config(
    page_title="Treasury Transformation: Data Science for the Treasury Professional", 
    page_icon="🤖",  # Robot icon for automation and efficiency
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CAMPBELL TARTAN COLOR PALETTE (Refined + Gold Accent) ---
NAVY_BLUE = "#012169"    # Primary - Deep Corporate Navy Blue
DEEP_GREEN = "#1E423C"   # Secondary - Rich Green (Headers/Buttons)
TEAL_ACCENT = "#00A0A0"  # Tertiary - Bright Teal (Borders/Alerts)
GOLD_ACCENT = "#D4AF37"  # New - Rich Gold metallic color for opulence
BACKGROUND = "#FFFFFF"   # Clean White background for professionalism

# Define advanced CSS styles for a professional, segmented look
css = f"""
/* Font and Base Styles */
html, body {{
    font-family: 'Georgia', serif; /* Changed font to Serif for a more formal, academic feel */
    color: #333333;
}}
.stApp {{
    background-color: {BACKGROUND};
}}

/* Sidebar Styling - Makes the color encompass the entire left side */
.stSidebar > div:first-child {{
    background-color: {NAVY_BLUE}; /* Entire sidebar background is Navy Blue */
    color: white; 
}}
/* Override default text colors for elements inside the sidebar */
.stSidebar .stMarkdown, .stSidebar .stTitle, .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar .stText {{
    color: white !important;
}}
/* Style sidebar links to be Gold */
.stSidebar a {{
    color: {GOLD_ACCENT} !important;
    font-weight: 600;
}}

/* Main Header Style */
h1 {{
    color: {NAVY_BLUE}; 
    font-weight: 800;
    font-size: 2.5em;
    padding-bottom: 10px;
}}
/* Subheader Style - Used for section titles */
h3 {{
    color: {DEEP_GREEN}; 
    border-bottom: 3px solid {GOLD_ACCENT}; /* Gold under-bar for richness */
    padding-bottom: 8px;
    margin-top: 40px;
    margin-bottom: 25px;
    font-weight: 700;
}}
/* Card/Info Box Styling for Learning Paths */
.stAlert {{
    border-left: 5px solid {TEAL_ACCENT} !important; 
    border-radius: 10px; 
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); 
    padding: 20px;
}}
/* Separator (Gold Line) */
.divider {{
    border-top: 1px solid {GOLD_ACCENT}; /* Rich gold divider */
    margin-top: 40px;
    margin-bottom: 40px;
}}
/* Button style - Primary Deep Campbell Green */
.stButton>button {{
    background-color: {DEEP_GREEN}; 
    color: white;
    border-radius: 8px;
    padding: 10px 25px;
    font-weight: 600;
    transition: background-color 0.3s, transform 0.2s;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border: 2px solid {GOLD_ACCENT}; /* Gold border on button */
}}
.stButton>button:hover {{
    background-color: {NAVY_BLUE}; /* Navy hover for contrast */
    transform: translateY(-2px);
}}
/* Sidebar Image Styling */
.sidebar-img img {{
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5); 
    margin-bottom: 20px;
}}
/* Footer styling for rich gold text */
.stMarkdown p[data-testid="stMarkdownContainer"] > p:last-child {{
    text-align: center; 
    color: {GOLD_ACCENT} !important; 
    font-weight: bold;
    font-style: italic;
}}
"""
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


# --- SIDEBAR CONTENT: NAVIGATION, IMAGE & RESOURCES ---
with st.sidebar:
    # 1. Professional Sidebar Image (Replaces main body image)
    st.markdown('<div class="sidebar-img">', unsafe_allow_html=True)
    # Placeholder for a professional, abstract tech image
    st.image(
        "https://images.pexels.com/photos/3861958/pexels-photo-3861958.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        caption="Data Driven Treasury",
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # TreasuryC Logo with Gold text
    st.image(f"https://placehold.co/150x50/{NAVY_BLUE.replace('#', '')}/{GOLD_ACCENT.replace('#', '')}?text=TreasuryC", width=150)
    st.title("Navigation")
    st.markdown('<div style="border-top: 1px solid white;"></div>', unsafe_allow_html=True) # White separator on dark background
    
    st.markdown("##### 🧭 Learning Paths")
    st.markdown("- Excel Mastery (Power Query)")
    st.markdown("- Power Platforms (Automation)")
    st.markdown("- TMS Integration & Optimization")
    st.markdown('<div style="border-top: 1px solid white;"></div>', unsafe_allow_html=True)
    
    st.markdown("##### 📚 Resources")
    st.markdown("- [Power BI Report Templates](#)")
    st.markdown("- [Power Automate Templates](#)")
    st.markdown("- [XML Templates for TMS Import](#)")
    st.markdown('<div style="border-top: 1px solid white;"></div>', unsafe_allow_html=True)
    st.markdown("Connect with Jamie on [LinkedIn](https://www.linkedin.com/)")


# --- MAIN PAGE CONTENT: HEADER & MISSION ---

st.header("Treasury Transformation: Data Efficiency and the Power Platform")

# 1. MISSION STATEMENT SECTION (Now Full Width on the Left)
st.subheader("Empowering Treasury Teams through Data Mastery and Automation")
st.write(
    """
    The financial landscape demands more than traditional treasury skill—it requires **data fluency** and **process automation**. 
    This platform provides targeted training for front and back office professionals, focusing on practical application 
    of the Power Platforms, Advanced Excel, and TMS integration techniques.

    Our goal is simple: to eliminate cumbersome manual work, significantly accelerate financial closings, and 
    foster a truly data-driven approach to liquidity and risk management.
    
    **Stop manipulating data; start analyzing it.**
    """
)
st.button("Start Your Treasury Journey")


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# 2. KEY LEARNING PATHS SECTION
st.markdown("### Key Learning Paths for Treasury Professionals")

path_col1, path_col2, path_col3 = st.columns(3)

with path_col1:
    st.info("##### 🛠️ Data Manipulation & Cleanup")
    st.markdown(
        """
        - **Advanced Excel:** Using Power Query for dynamic data ingestion and transformation.
        - **Python/Pandas:** Foundational scripting for large-scale data cleansing and reconciliation.
        - **Data Governance:** Standardizing static data, counterparty names, and transaction codes.
        """
    )

with path_col2:
    st.info("##### ⚙️ Process Automation (Power Automate)")
    st.markdown(
        """
        - **RPA for Back Office:** Automating daily liquidity reporting and TMS data entry.
        - **Workflow Design:** Building secure approval flows for payments and guarantee requests.
        - **Email Handling:** Automatically extracting payment confirmations and saving them to SharePoint.
        """
    )

with path_col3:
    st.info("##### 📊 Insightful Reporting (Power BI)")
    st.markdown(
        """
        - **Dashboard Design:** Creating intuitive, drill-down dashboards for cash visibility.
        - **DAX Measures:** Implementing custom measures for calculating risk and yield metrics.
        - **System Checks:** Building dashboards for continuous monitoring of TMS data integrity.
        """
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# 3. GET IN TOUCH / CALL TO ACTION
st.markdown("### Ready to Transform Your Treasury Role?")
st.write("Have specific questions about Power Platform implementation or data governance? Reach out to schedule a consultation.")

# Simple contact form simulation (Streamlit form functionality)
with st.form(key='contact_form'):
    st.markdown("#### Schedule a Consultation")
    user_name = st.text_input("Your Name", placeholder="Jamie")
    user_email = st.text_input("Your Professional Email", placeholder="jamie@example.com")
    message = st.text_area("Your Specific Automation/Data Query", placeholder="I need help automating my monthly debt schedule...")
    submit_button = st.form_submit_button(label='Request Consultation')

    if submit_button:
        # Placeholder success message (integration needed for a real email service)
        st.success(f"Thank you, {user_name}! Your consultation request has been received and we will be in touch shortly.")

st.markdown('---')
st.markdown(f'<p style="text-align: center; color: #666;">A Treasury Resource (2025) | Powered by Streamlit</p>', unsafe_allow_html=True)




