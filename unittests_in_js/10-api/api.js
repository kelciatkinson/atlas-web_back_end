const express = require('express');
const app = express();
const PORT = 7865;


// Add middleware to parse JSON bodies - this needs to be before the routes
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.get('/', (req, res) => {
    res.send("Welcome to the payment system");
});

app.get('/cart/:id(\\d+)', (req, res) => {
    const id = req.params.id;
    res.send(`Payment methods for cart ${id}`);
});

app.get('/available_payments', (req, res) => {
    const paymentMethods = {
        credit_cards: true,
        paypal: false
    };
    res.json(paymentMethods);
});

app.post('/login', (req, res) => {
    const username = req.body.username;
    res.send(`Welcome ${username}`);
});

app.listen(PORT, () => {
    console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;
