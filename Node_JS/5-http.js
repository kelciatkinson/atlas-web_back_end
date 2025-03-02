const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
    res.setHeader('Content-Type', 'text/plain');

    switch (req.url) {
        case '/':
            res.writeHead(200);
            res.end('Hello Holberton School!');
            break;

        case '/students':
            res.writeHead(200);
            try {
                const databasePath = process.argv[2];
                const output = await countStudents(databasePath);
                res.end(`This is the list of our students\n${output}`);
            } catch (error) {
                res.end(`This is the list of our students\n${error.message}`);
            }
            break;

        default:
            res.writeHead(404);
            res.end('Not found');
    }
});

app.listen(1245);

module.exports = app;
