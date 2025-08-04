import { NextPage } from 'next';
import Head from 'next/head';
import Link from 'next/link';

const Home: NextPage = () => {
  return (
    <>
      <Head>
        <title>gTok-Tok Codex Platform - Home</title>
        <meta name="description" content="Welcome to the gTok-Tok AfroAsiatic Futuristic Language Codex Platform" />
      </Head>

      <main className="home-container">
        <div className="hero-section">
          <h1>gTok-Tok Chat Mandar</h1>
          <h2>AfroAsiatic Futuristic Language Codex Platform</h2>
          <p className="hero-description">
            Experience the future of multilingual communication through our advanced 
            codex-powered chat platform, seamlessly integrating AfroAsiatic languages 
            with futuristic linguistic technologies.
          </p>
        </div>

        <div className="features-grid">
          <div className="feature-card">
            <h3>🌍 Multi-Language Support</h3>
            <p>Advanced support for AfroAsiatic language families with futuristic enhancements</p>
          </div>
          
          <div className="feature-card">
            <h3>🚀 Codex Technology</h3>
            <p>Revolutionary language processing through our proprietary codex system</p>
          </div>
          
          <div className="feature-card">
            <h3>💬 Interactive Chat</h3>
            <p>Real-time multilingual conversations with intelligent translation</p>
          </div>
          
          <div className="feature-card">
            <h3>🔮 Futuristic Interface</h3>
            <p>Cutting-edge UI/UX designed for the next generation of communication</p>
          </div>
        </div>

        <div className="action-section">
          <Link href="/launch" className="launch-link">
            <button className="launch-home-button">
              Enter Launch Portal
            </button>
          </Link>
          
          <div className="quick-links">
            <a href="/vault/digestive_capsule_summary.md" target="_blank" rel="noopener noreferrer">
              📚 View Documentation
            </a>
            <a href="https://github.com/gTek-Keys/gTok-Tok-Chat-Mandar-n-AfroAsiaticFuturistic-Language-Codex-Platform-" target="_blank" rel="noopener noreferrer">
              🔗 GitHub Repository
            </a>
          </div>
        </div>

        <footer className="home-footer">
          <p>&copy; 2025 gTek-Keys. All rights reserved.</p>
          <p>Powered by Next.js, TypeScript, and the Codex Engine</p>
        </footer>
      </main>

      <style jsx>{`
        .home-container {
          min-height: 100vh;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          color: white;
          display: flex;
          flex-direction: column;
          align-items: center;
          padding: 20px;
        }

        .hero-section {
          text-align: center;
          max-width: 800px;
          margin: 60px 0 80px 0;
        }

        .hero-section h1 {
          font-size: 3.5rem;
          margin-bottom: 15px;
          text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
          background: linear-gradient(45deg, #ffeb3b, #ff9800);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
        }

        .hero-section h2 {
          font-size: 1.8rem;
          margin-bottom: 30px;
          opacity: 0.9;
          font-weight: 300;
        }

        .hero-description {
          font-size: 1.2rem;
          line-height: 1.6;
          opacity: 0.8;
          max-width: 600px;
          margin: 0 auto;
        }

        .features-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
          gap: 30px;
          max-width: 1200px;
          width: 100%;
          margin-bottom: 60px;
        }

        .feature-card {
          background: rgba(255,255,255,0.1);
          padding: 30px;
          border-radius: 15px;
          backdrop-filter: blur(10px);
          border: 1px solid rgba(255,255,255,0.2);
          transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .feature-card:hover {
          transform: translateY(-5px);
          box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .feature-card h3 {
          font-size: 1.3rem;
          margin-bottom: 15px;
          color: #ffeb3b;
        }

        .feature-card p {
          line-height: 1.5;
          opacity: 0.9;
        }

        .action-section {
          text-align: center;
          margin-bottom: 60px;
        }

        .launch-link {
          display: inline-block;
          margin-bottom: 30px;
        }

        .launch-home-button {
          background: linear-gradient(45deg, #ff6b6b, #ee5a24);
          border: none;
          color: white;
          padding: 18px 50px;
          font-size: 1.3rem;
          border-radius: 30px;
          cursor: pointer;
          transition: all 0.3s ease;
          box-shadow: 0 6px 20px rgba(0,0,0,0.2);
          font-weight: 600;
        }

        .launch-home-button:hover {
          transform: translateY(-3px);
          box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        .quick-links {
          display: flex;
          gap: 30px;
          justify-content: center;
          flex-wrap: wrap;
        }

        .quick-links a {
          color: #ffeb3b;
          text-decoration: none;
          padding: 10px 20px;
          border: 1px solid #ffeb3b;
          border-radius: 25px;
          transition: all 0.3s ease;
          background: rgba(255,235,59,0.1);
        }

        .quick-links a:hover {
          background: #ffeb3b;
          color: #333;
          transform: translateY(-2px);
        }

        .home-footer {
          text-align: center;
          opacity: 0.7;
          border-top: 1px solid rgba(255,255,255,0.2);
          padding-top: 30px;
          margin-top: auto;
        }

        .home-footer p {
          margin: 5px 0;
        }

        @media (max-width: 768px) {
          .hero-section {
            margin: 40px 0 60px 0;
          }
          
          .hero-section h1 {
            font-size: 2.5rem;
          }
          
          .hero-section h2 {
            font-size: 1.4rem;
          }
          
          .hero-description {
            font-size: 1rem;
          }
          
          .features-grid {
            grid-template-columns: 1fr;
            gap: 20px;
          }
          
          .quick-links {
            flex-direction: column;
            align-items: center;
          }
        }
      `}</style>
    </>
  );
};

export default Home;
