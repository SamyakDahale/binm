import streamlit as st

st.set_page_config(page_title="Waste Management System", layout="wide")

def main():
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
        <style>
            html, body {
                font-family: 'Poppins', sans-serif;
                scroll-behavior: smooth;
            }

            .hero {
                background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                url('https://images.unsplash.com/photo-1605810230434-7631c5c3edb3?auto=format&fit=crop&w=1950&q=80') no-repeat center center;
                background-size: cover;
                padding: 100px 50px;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 60vh;
                text-align: center;
                animation: fadeIn 2s ease-in-out;
            }

            .hero-content {
                max-width: 800px;
                margin: 0 auto;
            }

            .hero h1 {
                font-size: 60px;
                margin-bottom: 20px;
                font-weight: 700;
            }

            .hero p {
                font-size: 20px;
                margin-bottom: 40px;
                line-height: 1.6;
                font-weight: 300;
            }

            .cta {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
            }

            .cta-button {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 18px;
                border-radius: 25px;
                cursor: pointer;
                transition: 0.3s ease;
                font-weight: bold;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }

            .cta-button:hover {
                background-color: #2ecc71;
                transform: translateY(-3px);
            }

            .features {
                padding: 60px 30px;
                text-align: center;
            }

            .features h2 {
                font-size: 36px;
                font-weight: 600;
                margin-bottom: 40px;
            }

            .feature-grid {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-around;
                gap: 40px;
            }

            .feature {
                max-width: 300px;
                background: #f4f4f4;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 10px 20px rgba(0,0,0,0.1);
                transition: 0.3s ease-in-out;
            }

            .feature:hover {
                transform: scale(1.05);
            }

            .feature img {
                width: 60px;
                margin-bottom: 20px;
            }

            .feature h4 {
                font-size: 22px;
                margin-bottom: 10px;
            }

            .feature p {
                font-size: 16px;
                line-height: 1.5;
                color: #555;
            }

            .vision {
                background: #dff0ea;
                padding: 60px 30px;
                text-align: center;
            }

            .vision h2 {
                font-size: 36px;
                font-weight: 600;
                margin-bottom: 20px;
            }

            .vision p {
                font-size: 18px;
                max-width: 800px;
                margin: auto;
                line-height: 1.7;
            }

            .footer {
                background-color: #2c3e50;
                color: white;
                padding: 40px 20px;
                text-align: center;
            }

            .footer p {
                margin: 5px;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>

        <div class="hero">
            <div class="hero-content">
                <h1>Waste Less. Live More. 🌿</h1>
                <p>
                    Empowering communities to embrace sustainable waste solutions. Join us in building a greener, cleaner future for generations to come.
                </p>
                <div class="cta">
                    <a href="https://binwiseu.streamlit.app" target="_blank">
                        <button class="cta-button">👤 User Portal</button>
                    </a>
                    <a href="https://binad123.streamlit.app" target="_blank">
                        <button class="cta-button">🛠️ Admin Dashboard</button>
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

    # Placeholder for query-based actions (optional logic can go here)
    if st.query_params.get("user"):
        st.success("Redirecting to User Dashboard...")
    if st.query_params.get("admin"):
        st.warning("Redirecting to Admin Panel...")

if __name__ == "__main__":
    main()
