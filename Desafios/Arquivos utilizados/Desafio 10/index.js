const http = require('http');

const PORT = 3000;

const server = http.createServer((req, res) => {
  res.end('Sucesso!');
});

server.listen(PORT);