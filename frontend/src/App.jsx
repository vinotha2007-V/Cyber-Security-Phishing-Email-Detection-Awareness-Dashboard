
import { useState } from 'react'
import './App.css'

const API_URL = 'http://127.0.0.1:5000'

function App() {
  const [email, setEmail] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function analyzeEmail(e) {
    e.preventDefault()
    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await fetch(`${API_URL}/api/analyze`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || 'Unable to analyze email.')
      }

      setResult(data)
    } catch {
      setError(
        'Cannot connect to the backend. Make sure python app.py is running on port 5000.'
      )
    } finally {
      setLoading(false)
    }
  }

  function clearForm() {
    setEmail('')
    setResult(null)
    setError('')
  }

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-icon">🛡️</div>
          <div>
            <h2>PhishGuard</h2>
            <span>SECURITY CENTER</span>
          </div>
        </div>

        <p className="nav-label">WORKSPACE</p>
        <a className="nav-item active" href="#dashboard">▦ Dashboard</a>
        <a className="nav-item" href="#analyzer">⌕ Email Analyzer</a>
        <a className="nav-item" href="#awareness">◈ Awareness Center</a>

        <div className="sidebar-bottom">
          <div className="shield-art">🔐</div>
          <h3>Stay one step ahead</h3>
          <p>Think before you click. Protect your digital identity.</p>
          <span className="security-status">● Demo protection active</span>
        </div>
      </aside>

      <main className="main" id="dashboard">
        <header className="topbar">
          <div>
            <p className="eyebrow">CYBERSECURITY / EMAIL PROTECTION</p>
            <h1>Phishing Awareness Dashboard</h1>
          </div>
          <div className="top-status"><span /> API Demo</div>
        </header>

        <section className="welcome">
          <div>
            <span className="welcome-tag">YOUR DIGITAL SAFETY MATTERS</span>
            <h2>Spot the bait. <span>Stay secure.</span></h2>
            <p>
              Check suspicious email text, identify common warning signs,
              and learn how to respond safely.
            </p>
            <a className="primary-link" href="#analyzer">Analyze an email ↘</a>
          </div>
          <div className="welcome-art" aria-hidden="true">
            <div className="orbit orbit-one" />
            <div className="orbit orbit-two" />
            <div className="big-shield">🛡️</div>
            <span className="floating-icon lock">🔒</span>
            <span className="floating-icon mail">✉️</span>
            <span className="floating-icon check">✓</span>
          </div>
        </section>

        <section className="stats-grid">
          <article className="stat-card">
            <div className="stat-icon purple">⌕</div>
            <p>Analysis mode</p>
            <h3>Rule-based</h3>
            <span className="stat-note">Demo detection engine</span>
          </article>
          <article className="stat-card">
            <div className="stat-icon green">✓</div>
            <p>API status</p>
            <h3>Connected on analysis</h3>
            <span className="stat-note">Flask · Port 5000</span>
          </article>
          <article className="stat-card">
            <div className="stat-icon orange">⚠</div>
            <p>What gets checked</p>
            <h3>4 warning patterns</h3>
            <span className="stat-note">Links, urgency, sensitive data, prizes</span>
          </article>
        </section>

        <section className="content-grid" id="analyzer">
          <article className="panel analyzer-panel">
            <div className="panel-heading">
              <div>
                <span className="section-kicker">EMAIL SCANNER</span>
                <h2>Analyze an email</h2>
                <p>Paste the email text below. Do not include real passwords or OTPs.</p>
              </div>
              <div className="scanner-icon">✉</div>
            </div>

            <form onSubmit={analyzeEmail}>
              <label htmlFor="email-text">EMAIL CONTENT</label>
              <textarea
                id="email-text"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder={'Example: URGENT! Your account is suspended. Verify now at https://example.com'}
                maxLength={20000}
                required
              />
              <div className="input-footer">
                <span>{email.length}/20,000 characters</span>
                <button type="button" className="text-button" onClick={clearForm}>
                  Clear
                </button>
              </div>
              <button className="analyze-button" type="submit" disabled={loading}>
                {loading ? 'Analyzing email...' : '⌕  Analyze email'}
              </button>
            </form>

            {error && <div className="error-message" role="alert">{error}</div>}

            {result && (
              <section className="result-card" aria-live="polite">
                <div className="result-top">
                  <div>
                    <span className="section-kicker">ANALYSIS RESULT</span>
                    <h3>{result.verdict}</h3>
                  </div>
                  <div className={`risk-badge ${result.risk_score >= 50 ? 'high' : result.risk_score > 0 ? 'medium' : 'low'}`}>
                    {result.risk_score}% risk indicator
                  </div>
                </div>

                <div className="risk-track">
                  <div
                    className={`risk-fill ${result.risk_score >= 50 ? 'high' : result.risk_score > 0 ? 'medium' : 'low'}`}
                    style={{ width: `${result.risk_score}%` }}
                  />
                </div>

                <h4>Warning signs found</h4>
                {result.warning_signs.length ? (
                  <ul className="warning-list">
                    {result.warning_signs.map((warning) => (
                      <li key={warning}>⚠ {warning}</li>
                    ))}
                  </ul>
                ) : (
                  <p className="safe-note">No warning patterns from this demo's rule list were detected.</p>
                )}

                <div className="advice-box">
                  <strong>Recommended action</strong>
                  <p>{result.advice}</p>
                </div>
                <p className="disclaimer">{result.disclaimer}</p>
              </section>
            )}
          </article>

          <aside className="panel tips-panel" id="awareness">
            <span className="section-kicker">SECURITY GUIDE</span>
            <h2>Think before you click</h2>
            <p className="tips-intro">Four things to check when an email feels suspicious.</p>

            <div className="tip">
              <span className="tip-icon red">!</span>
              <div><h3>Check urgency</h3><p>Threats, pressure, and countdowns can push you into mistakes.</p></div>
            </div>
            <div className="tip">
              <span className="tip-icon blue">↗</span>
              <div><h3>Inspect links</h3><p>Check the real destination before opening a link. Avoid unexpected attachments.</p></div>
            </div>
            <div className="tip">
              <span className="tip-icon orange">⌑</span>
              <div><h3>Protect your details</h3><p>Never share passwords, OTPs, or bank details through suspicious messages.</p></div>
            </div>
            <div className="tip">
              <span className="tip-icon green">✓</span>
              <div><h3>Verify the sender</h3><p>Contact the organisation through its official website or phone number.</p></div>
            </div>

            <div className="golden-rule">
              <span>✦ GOLDEN RULE</span>
              <p>When in doubt, don't click. Verify independently.</p>
            </div>
          </aside>
        </section>

        <footer>
          <span>PhishGuard · Cybersecurity Awareness Project</span>
          <span>Educational demo · Not a guarantee of email safety</span>
        </footer>
      </main>
    </div>
  )
}

export default App