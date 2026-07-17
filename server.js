const express = require('express');
const basicAuth = require('express-basic-auth');
const path = require('path');

const app = express();

// ─── CREDENCIALES ──────────────────────────────────────────────────────────────
// Definir en Render: Environment → Add Environment Variable
// Variables: USER_1, PASS_1, USER_2, PASS_2, USER_3, PASS_3, USER_4, PASS_4
const users = {};
for (let i = 1; i <= 4; i++) {
  const u = process.env[`USER_${i}`];
  const p = process.env[`PASS_${i}`];
  if (u && p) users[u] = p;
}

if (Object.keys(users).length === 0) {
  console.warn('⚠️  Sin credenciales. Configurar USER_1/PASS_1 ... USER_4/PASS_4 en Render.');
}

app.use(basicAuth({
  users,
  challenge: true,
  realm: 'PBA Hub Campaña'
}));

// ─── ARCHIVOS ESTÁTICOS ─────────────────────────────────────────────────────────
app.use(express.static(__dirname, {
  dotfiles: 'deny',
  index: false
}));

// Raíz → hub principal
app.get('/', (_req, res) => {
  res.redirect('/PBA_Maestro_2026.html');
});

// ─── SERVIDOR ──────────────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`PBA Hub Campaña corriendo en puerto ${PORT}`));
