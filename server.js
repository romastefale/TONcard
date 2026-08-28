import express from 'express';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;
const UPSTREAM = process.env.UPSTREAM || "https://romastefale.github.io/TONcard";

app.get('/health', (req, res) => {
    res.type('text/plain; charset=utf-8').send('OK');
});

const serveIndex = (req, res) => {
    const indexPath = path.join(__dirname, 'index.html');
    if (fs.existsSync(indexPath)) {
        res.sendFile(indexPath);
    } else {
        res.status(404).send('Not Found');
    }
};

app.get(['/', '/index.html', '/TONcard', '/TONcard/'], serveIndex);

app.use(express.static(__dirname));

app.use(async (req, res) => {
    try {
        let fetchPath = req.path;
        if (fetchPath === '/TONcard' || fetchPath === '/TONcard/') {
            fetchPath = '/';
        }
        
        const target = UPSTREAM.replace(/\/$/, '') + fetchPath + (req.url.includes('?') ? req.url.slice(req.url.indexOf('?')) : '');
        
        const response = await fetch(target, {
            headers: { 'User-Agent': 'TONcard-Proxy/1.1' }
        });
        
        const contentType = response.headers.get('content-type') || 'text/html; charset=utf-8';
        res.status(response.status).set('Content-Type', contentType);
        
        const buffer = Buffer.from(await response.arrayBuffer());
        res.send(buffer);
    } catch (err) {
        res.status(502).type('text/plain; charset=utf-8').send(`Upstream error: ${err.message}`);
    }
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Listening on 0.0.0.0:${PORT}`);
});
