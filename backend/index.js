const express = require('express');
const { Pool } = require('pg');
const app = express();
const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASS,
  port: 5432
});

app.get('/', async (req, res) => {
  const result = await pool.query('SELECT NOW()');
  res.send(`Database time is: ${result.rows[0].now}`);
});

app.listen(5000, () => console.log('Backend running on port 5000'));
