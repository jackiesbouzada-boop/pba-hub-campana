const express = require('express');
const session = require('express-session');

const app = express();

// ─── CREDENCIALES ──────────────────────────────────────────────────────────────
const users = {};
for (let i = 1; i <= 4; i++) {
  const u = process.env[`USER_${i}`];
  const p = process.env[`PASS_${i}`];
  if (u && p) users[u] = p;
}

// ─── MIDDLEWARE ────────────────────────────────────────────────────────────────
app.use(express.urlencoded({ extended: true }));
app.use(session({
  secret: process.env.SESSION_SECRET || 'pba-hub-secret-2026',
  resave: false,
  saveUninitialized: false,
  cookie: { maxAge: 8 * 60 * 60 * 1000 } // 8 horas
}));

// ─── LOGIN PAGE ────────────────────────────────────────────────────────────────
const loginPage = (error = '') => `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PBA Hub Campaña — Acceso</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    min-height: 100vh;
    background: #0a1628;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background-image:
      radial-gradient(ellipse at 20% 50%, rgba(26,58,92,0.4) 0%, transparent 60%),
      radial-gradient(ellipse at 80% 20%, rgba(37,99,235,0.15) 0%, transparent 50%);
  }
  .card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 48px 40px;
    width: 100%;
    max-width: 400px;
    backdrop-filter: blur(12px);
    box-shadow: 0 24px 64px rgba(0,0,0,0.4);
  }
  .logo {
    text-align: center;
    margin-bottom: 36px;
  }
  .logo-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 56px;
    height: 56px;
    background: linear-gradient(135deg, #1a3a5c, #2563eb);
    border-radius: 14px;
    font-size: 24px;
    margin-bottom: 16px;
    box-shadow: 0 8px 24px rgba(37,99,235,0.3);
  }
  .logo h1 {
    font-size: 20px;
    font-weight: 700;
    color: #fff;
    letter-spacing: -0.3px;
  }
  .logo p {
    font-size: 13px;
    color: rgba(255,255,255,0.4);
    margin-top: 4px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  .field {
    margin-bottom: 16px;
  }
  label {
    display: block;
    font-size: 12px;
    font-weight: 600;
    color: rgba(255,255,255,0.5);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 8px;
  }
  input {
    width: 100%;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 15px;
    color: #fff;
    outline: none;
    transition: border-color 0.2s, background 0.2s;
  }
  input::placeholder { color: rgba(255,255,255,0.25); }
  input:focus {
    border-color: #2563eb;
    background: rgba(37,99,235,0.08);
  }
  .error {
    background: rgba(239,68,68,0.12);
    border: 1px solid rgba(239,68,68,0.3);
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13px;
    color: #fca5a5;
    margin-bottom: 18px;
    text-align: center;
  }
  button {
    width: 100%;
    background: linear-gradient(135deg, #1d4ed8, #2563eb);
    border: none;
    border-radius: 8px;
    padding: 13px;
    font-size: 15px;
    font-weight: 600;
    color: #fff;
    cursor: pointer;
    margin-top: 8px;
    transition: opacity 0.2s, transform 0.1s;
    letter-spacing: 0.3px;
  }
  button:hover { opacity: 0.92; }
  button:active { transform: scale(0.99); }
  .footer {
    text-align: center;
    margin-top: 28px;
    font-size: 12px;
    color: rgba(255,255,255,0.2);
  }
</style>
</head>
<body>
<div class="card">
  <div class="logo">
    <div class="logo-badge">🗺️</div>
    <h1>PBA Hub Campaña</h1>
    <p>Acceso restringido · 2026</p>
  </div>
  ${error ? `<div class="error">⚠️ ${error}</div>` : ''}
  <form method="POST" action="/login">
    <div class="field">
      <label>Usuario</label>
      <input type="text" name="username" placeholder="Ingresá tu usuario" autocomplete="username" autofocus required>
    </div>
    <div class="field">
      <label>Contraseña</label>
      <input type="password" name="password" placeholder="••••••••" autocomplete="current-password" required>
    </div>
    <button type="submit">Ingresar →</button>
  </form>
  <div class="footer">Provincia de Buenos Aires · Uso interno</div>
</div>
</body>
</html>`;

// ─── RUTAS DE AUTH ─────────────────────────────────────────────────────────────
app.get('/login', (req, res) => {
  if (req.session.authenticated) return res.redirect('/');
  res.send(loginPage());
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  if (users[username] && users[username] === password) {
    req.session.authenticated = true;
    req.session.username = username;
    res.redirect('/');
  } else {
    res.send(loginPage('Usuario o contraseña incorrectos'));
  }
});

app.get('/logout', (req, res) => {
  req.session.destroy();
  res.redirect('/login');
});

// ─── PROTECCIÓN ────────────────────────────────────────────────────────────────
app.use((req, res, next) => {
  if (req.session.authenticated) return next();
  res.redirect('/login');
});

// ─── ARCHIVOS ESTÁTICOS ─────────────────────────────────────────────────────────
app.use(express.static(__dirname, {
  dotfiles: 'deny',
  index: false
}));

app.get('/', (_req, res) => {
  res.redirect('/PBA_Maestro_2026.html');
});

// ─── SERVIDOR ──────────────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`PBA Hub Campaña corriendo en puerto ${PORT}`));
