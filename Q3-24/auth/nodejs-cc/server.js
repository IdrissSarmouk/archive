import http from 'http';
import fs from 'fs/promises';
import url from 'url';
import path from 'path';


const PORT = 8000;


const __filename = url.fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

console.log(__filename, __dirname);

const server = http.createServer(async(req, res)=>{
    try {
        if (req.method == 'GET' ) {  
        let filePath;       
        if(req.url==='/') {
            filePath = path.join(__dirname,'public','index.html'); 
        } else if (req.url === '/about') {
            filePath = path.join(__dirname,'public','about.html'); 
        } else {
            throw new Error('Not Found');
        }

        const data = await fs.readFile(filePath);
        res.setHeader('Content-Type','text/html');
        res.write(data);
        res.end();

        } else {
            throw new Error('Method Not Allowed');
        }
    } catch(error) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('<h1>Server Error</h1>');

    }

});


server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
})