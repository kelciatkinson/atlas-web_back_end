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