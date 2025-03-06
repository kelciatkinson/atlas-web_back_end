const chai = require('chai');
const expect = chai.expect;
const request = require('request');

describe('Index Page', function () {
    it('should return 200 status code', function(done) {
        request('http://localhost:7865', function (error, response, body) {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return the correct message', function(done) {
        request('http://localhost:7865', function (error, response, body) {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    })
});


describe('Cart page', function() {
    it('returns correct status code 200 when id is a numbner', function(done) {
        request('http://localhost:7865/cart/12', function(error, response, body) {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Payment methods for cart 12');
            done();
        });
    });

    it('should return 404 when id is not a number', function(done) {
        request('http://localhost:7865/cart/hello', function(error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});
