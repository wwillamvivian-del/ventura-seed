from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- UI/UX DESIGN (THE TECH NOIR AESTHETIC) ---
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ventura Seed | Africa’s Precision Agri-Capital Leader</title>
    <style>
        :root {
            --bg-black: #000000;
            --card-grey: #0a0a0a;
            --text-main: #ffffff;
            --text-dim: #888888;
            --border: #222222;
            --accent-green: #a3e635;
        }
        html { scroll-behavior: smooth; font-size: 16px; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", sans-serif; 
            margin: 0; background-color: var(--bg-black); color: var(--text-main); 
            display: flex; flex-direction: column; align-items: center;
        }
        nav {
            width: 100%; max-width: 1100px; padding: 25px 20px;
            display: flex; justify-content: space-between; align-items: center; box-sizing: border-box;
            position: sticky; top: 0; background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); z-index: 100;
        }
        .logo { font-weight: 800; font-size: 1.3rem; display: flex; align-items: center; gap: 10px; }
        .logo-sq { width: 18px; height: 18px; background: white; border-radius: 2px; }
        
        .hero { text-align: center; padding: 120px 24px 80px; max-width: 800px; }
        .hero h1 { font-size: 3.5rem; font-weight: 700; line-height: 1.1; margin: 0 0 25px; letter-spacing: -2px; }
        .hero p { color: var(--text-dim); font-size: 1.25rem; margin-bottom: 40px; }

        .btn-primary { background: white; color: black; padding: 16px 32px; border-radius: 6px; font-weight: 600; text-decoration: none; display: inline-block; }
        .btn-secondary { background: #222; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-size: 0.9rem; border: 1px solid #333; }

        /* ORBIT SECTION */
        .orbit-container {
            width: 100%; max-width: 1100px; padding: 100px 20px;
            display: flex; flex-direction: column; align-items: center;
            background-image: radial-gradient(var(--border) 1px, transparent 1px);
            background-size: 24px 24px; border-top: 1px solid var(--border); box-sizing: border-box;
        }
        .orbit-wrap {
            position: relative; width: 320px; height: 320px;
            display: flex; justify-content: center; align-items: center; margin-bottom: 60px;
        }
        .v-center {
            position: absolute; width: 90px; height: 90px; background: white; border-radius: 18px;
            display: flex; justify-content: center; align-items: center; z-index: 10;
            box-shadow: 0 0 40px rgba(255,255,255,0.15);
        }
        .orbit-ring {
            position: absolute; width: 100%; height: 100%; border: 1px solid var(--border); border-radius: 50%;
            animation: rotateOrbit 50s linear infinite;
        }
        @keyframes rotateOrbit { to { transform: rotate(360deg); } }
        .orbit-partner {
            position: absolute; background: var(--card-grey); padding: 12px;
            border-radius: 50%; border: 1px solid #1a1a1a; font-weight: bold; font-size: 0.65rem; color: var(--text-dim);
        }
        .orbit-partner:nth-child(1) { top: 0%; left: 50%; transform: translate(-50%, -50%); }
        .orbit-partner:nth-child(2) { top: 50%; right: 0%; transform: translate(50%, -50%); }
        .orbit-partner:nth-child(3) { bottom: 0%; left: 50%; transform: translate(-50%, 50%); }
        .orbit-partner:nth-child(4) { top: 50%; left: 0%; transform: translate(-50%, -50%); }

        /* SPOTLIGHT */
        .spotlight {
            width: 100%; max-width: 1000px; padding: 120px 20px; text-align: center;
            border-top: 1px solid var(--border);
        }
        .spotlight h2 { font-size: 2.2rem; font-weight: 600; margin-bottom: 20px; letter-spacing: -1px; }
        .spotlight p { color: var(--text-dim); max-width: 550px; margin: 0 auto 40px; line-height: 1.6; font-size: 1.1rem; }

        /* FORM */
        .form-section {
            width: 90%; max-width: 500px; background: var(--card-grey); 
            padding: 50px; border-radius: 24px; border: 1px solid var(--border);
            box-sizing: border-box; margin: 60px 0 120px;
        }
        input, textarea { width: 100%; background: transparent; border: none; border-bottom: 1px solid #333; color: white; padding: 18px 0; margin-bottom: 25px; outline: none; font-size: 1rem; }
        .submit-btn { width: 100%; background: white; color: black; border: none; padding: 20px; border-radius: 8px; font-weight: 700; cursor: pointer; transition: 0.2s; }
        .submit-btn:active { transform: scale(0.98); }

        /* --- THE NEW SITEMAP FOOTER --- */
        footer {
            width: 100%; background: var(--bg-black); border-top: 1px solid var(--border);
            padding: 80px 20px 40px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center;
        }
        .footer-grid {
            width: 100%; max-width: 1100px; display: grid;
            grid-template-columns: repeat(2, 1fr); gap: 40px; margin-bottom: 80px;
        }
        @media (min-width: 768px) { .footer-grid { grid-template-columns: repeat(4, 1fr); } }
        
        .footer-col h4 { font-size: 0.9rem; margin-bottom: 25px; font-weight: 600; color: var(--text-main); }
        .footer-col ul { list-style: none; padding: 0; margin: 0; }
        .footer-col li { margin-bottom: 15px; }
        .footer-col a { color: var(--text-dim); text-decoration: none; font-size: 0.9rem; transition: 0.2s; }
        .footer-col a:hover { color: white; }
        
        .footer-bottom {
            width: 100%; max-width: 1100px; display: flex; justify-content: space-between;
            align-items: center; border-top: 1px solid var(--border); padding-top: 40px;
            color: #444; font-size: 0.8rem;
        }
    </style>
</head>
<body>
    <nav>
        <div class="logo"><div class="logo-sq"></div> VENTURA SEED</div>
        <div style="background:white; color:black; padding: 8px 18px; border-radius: 6px; font-size: 0.85rem; font-weight:bold;">Get a Demo</div>
    </nav>

    <section class="hero">
        <h1>Empower Every Farm to Own Their Future.</h1>
        <p>Strategic seed capital and precision infrastructure for Africa’s most ambitious Agri-Innovators.</p>
        <a href="#portal" class="btn-primary">Apply for Funding</a>
    </section>

    <section class="orbit-container">
        <h2 style="font-size: 2.2rem; margin-bottom: 60px; font-weight: 500;">The Precision Agri-Capital leader</h2>
        <div class="orbit-wrap">
            <div class="orbit-ring">
                <div class="orbit-partner">K-AI</div>
                <div class="orbit-partner">LOG</div>
                <div class="orbit-partner">AGR</div>
                <div class="orbit-partner">SEED</div>
            </div>
            <div class="v-center">
                <svg width="45" height="45" viewBox="0 0 100 100">
                    <path d="M10,20 L50,90 L90,20" fill="none" stroke="black" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            </div>
        </div>
    </section>

    <section class="spotlight">
        <h2>Track yield performance with ease</h2>
        <p>Understand how weather patterns, soil health, and logistics access impact your farm’s bottom line in real time.</p>
        <a href="#" class="btn-secondary">Learn more</a>
    </section>

    <div id="portal" class="form-section">
        <h2 style="margin-top:0; font-size: 1.8rem; margin-bottom: 30px;">Founder Portal</h2>
        <form method="POST" action="/submit">
            <input type="text" name="company" placeholder="Company Name" required>
            <textarea name="pitch" rows="3" placeholder="Tell us your vision..." required></textarea>
            <button type="submit" class="submit-btn">Submit Application</button>
        </form>
    </div>

    <footer>
        <div class="footer-grid">
            <div class="footer-col">
                <h4>Platform</h4>
                <ul>
                    <li><a href="#">Yield Data</a></li>
                    <li><a href="#">Market Access</a></li>
                    <li><a href="#">Agent Analytics</a></li>
                    <li><a href="#">Logistics Hub</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Resources</h4>
                <ul>
                    <li><a href="#">Farmer Center</a></li>
                    <li><a href="#">Help Hub</a></li>
                    <li><a href="#">Agri-Blog</a></li>
                    <li><a href="#">AEO Reports</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Company</h4>
                <ul>
                    <li><a href="#">Enterprise</a></li>
                    <li><a href="#">Venture Pricing</a></li>
                    <li><a href="#">Careers <span style="background:#222; padding: 2px 6px; border-radius: 10px; font-size: 0.7rem;">12</span></a></li>
                    <li><a href="#">Contact Us</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Solutions</h4>
                <ul>
                    <li><a href="#">Smallholders</a></li>
                    <li><a href="#">Supply Chains</a></li>
                    <li><a href="#">Fintech Teams</a></li>
                    <li><a href="#">Agencies</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <div>&copy; 2026 Ventura Investors Seed. All rights reserved.</div>
            <div style="display:flex; gap:20px;">
                <a href="#" style="color:#444; text-decoration:none;">Privacy</a>
                <a href="#" style="color:#444; text-decoration:none;">Terms</a>
            </div>
        </div>
    </footer>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/submit', methods=['POST'])
def submit():
    company = request.form.get('company')
    return f'<body style="background:black;color:white;text-align:center;padding:100px;font-family:sans-serif;"><h1>Application Received.</h1><p>Thank you, {company}. Our team will review your pitch shortly.</p><br><a href="/" style="color:white;text-decoration:underline;">Return Home</a></body>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
