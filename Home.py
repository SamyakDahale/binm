import streamlit as st

# Set page configuration
st.set_page_config(page_title="Waste Management System", layout="wide")

# Load external CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main function
def main():
    load_css("style.css")

    # Page content using markdown and HTML
    st.markdown("""
        <div class="hero">
            <div class="hero-content">
                <h1>Waste Less. Live More. 🌿</h1>
                <p>
                    Empowering communities to embrace sustainable waste solutions. Join us in building a greener, cleaner future for generations to come.
                </p>
                <div class="cta">
                    <a href="https://binwiseu.streamlit.app/" target="_blank">
                        <button class="cta-button">👤 User Portal</button>
                    </a>
                    <a href="https://binad123.streamlit.app/" target="_blank">
                        <button class="cta-button">🛠️ Admin11 Dashboard</button>
                    </a>
                </div>
            </div>
        </div>

        <div class="features">
            <h2>Why Choose Our System?</h2>
            <div class="feature-grid">
                <div class="feature">
                    <img src="https://cdn-icons-png.flaticon.com/512/3103/3103446.png" />
                    <h4>Smart Tracking</h4>
                    <p>Track waste collection and disposal schedules in real-time.</p>
                </div>
                <div class="feature">
                    <img src="https://cdn-icons-png.flaticon.com/512/1163/1163624.png" />
                    <h4>Eco Education</h4>
                    <p>Spread awareness and educate citizens on proper waste segregation.</p>
                </div>
                <div class="feature">
                    <img src="https://cdn-icons-png.flaticon.com/512/3503/3503769.png" />
                    <h4>Data Insights</h4>
                    <p>Analyze waste trends and optimize waste management strategies.</p>
                </div>
            </div>
        </div>

        <div class="vision">
            <h2>Our Mission</h2>
            <p>
                We envision a world where waste is no longer a problem but a resource. By combining technology and environmental consciousness, our system aims to revolutionize how we manage, track, and reduce waste.
            </p>
        </div>

        <div class="footer">
            <p>🌍 Waste Management System | Built with ❤️ by Sanket</p>
            <p>Contact: info@wasteless.org | Follow us on 🌱 @WasteSmart</p>
        </div>

        <div id="user"></div>
        <div id="admin"></div>
    """, unsafe_allow_html=True)

    # Optional logic for redirecting based on query parameters
    if st.query_params.get("user"):
        st.success("Redirecting to User Dashboard...")

    if st.query_params.get("admin"):
        st.warning("Redirecting to Admin Panel...")

# Run app
if __name__ == "__main__":
    main()
