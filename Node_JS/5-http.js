const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
    res.setHeader('Content-Type', 'text/plain');

    res.writeHead(200);

    if (req.url === '/') {   
        res.write('Hello Holberton School!');
    } else if (req.url === '/students') {
        try {
            const databasePath = process.argv[2];
            const output = await countStudents(databasePath);
            //console.log(databasePath)
            //console.log(output)
            res.write(`This is the list of our students\n${output}`);
        } catch (error) {
            res.write(`This is the list of our students\n${error.message}`);
        }
    }
    res.end();
});

app.listen(1245);

module.exports = app;
