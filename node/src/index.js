const express = require('express');
const fs = require('fs');
const path = require('path');
const { Pool } = require('pg');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
app.use(express.json());

// let pool;
// try {
//     const dbHost = process.env.DB_HOST;
//     const dbDatabase = process.env.DB_DATABASE;
//     const dbUser = process.env.DB_USER;
//     const dbPassword = fs.readFileSync('/run/secrets/pg-password', 'utf-8').trim();
//
//     pool = new Pool({
//         host: dbHost,
//         database: dbDatabase,
//         user: dbUser,
//         password: dbPassword,
//     });
//
//     pool.connect(async (err, client, release) => {
//         if (err) {
//             console.error('Failed to connect to the database:', err);
//             throw err;
//         }
//
//         console.info('Successfully connected to the database.');
//
//         await client.query(`
//             CREATE TABLE IF NOT EXISTS records (
//                 id SERIAL PRIMARY KEY,
//                 content TEXT NOT NULL
//             )
//         `);
//         release();
//     });
// } catch (err) {
//     console.error('Database connection error:', err);
// }


app.get('/healthz', (req, res) => {
    res.status(200).json({ healthz: 'Application is running!!!' });
});

app.route('/volumes')
    .get((req, res) => {
        const filename = '/data/test';

        try {
            const content = fs.readFileSync(filename, 'utf-8');
            res.status(200).send(content);
        } catch (err) {
            res.status(404).send('File not found');
        }
    })
    .post((req, res) => {
        const filename = '/data/test';

        try {
            fs.mkdirSync(path.dirname(filename), { recursive: true });
            fs.writeFileSync(filename, 'Customer record');
            res.status(201).send('Saved!');
        } catch (err) {
            res.status(500).send('Failed to save file');
        }
    });

app.get('/environment', (req, res) => {
    res.status(200).json({
        'env-1': process.env.ENV_VALUE,
        'env-2': process.env.ENV_TOKEN,
    });
});

// app.route('/records')
//     .get(async (req, res) => {
//         try {
//             const result = await pool.query('SELECT id, content FROM records');
//             res.status(200).json(result.rows);
//         } catch (err) {
//             console.error('Error fetching records:', err);
//             res.status(500).json({ error: 'Internal Server Error' });
//         }
//     })
//     .post(async (req, res) => {
//         const { content } = req.body;
//         if (!content) {
//             return res.status(400).json({ error: 'Content is required' });
//         }
//
//         try {
//             const result = await pool.query(
//                 'INSERT INTO records (content) VALUES ($1) RETURNING id',
//                 [content]
//             );
//             res.status(201).json({ message: 'Record inserted successfully', id: result.rows[0].id });
//         } catch (err) {
//             console.error('Error inserting record:', err);
//             res.status(500).json({ error: 'Internal Server Error' });
//         }
//     });

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.info(`Server is running on port ${PORT}`);
});

