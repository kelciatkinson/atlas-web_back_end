const sinon = require("sinon");
const chai = require("chai");
const expect = chai.expect;
const sendPaymentRequestToApi = require("./3-payment");

describe("sendPaymentRequestToApi", function () {
    let spy;

    beforeEach(() => {
        spy = sinon.spy(console, "log");
    });

    it("should call Utils.calculateNumber with 'SUM', 100, 20", function () {
        sendPaymentRequestToApi(100, 20);
        expect(spy.calledOnce).to.be.true;
        expect(spy.calledOnceWithExactly("The total is: 120")).to.be.true;
    });

    it("log The total is: 20 once when called with (10, 10)"), function () {
        sendPaymentRequestToApi(10, 10);
        expect(spy.calledOnce).to.be.true;
        expect(spy.calledOnceWithExactly("The total is: 20")).to.be.true;

    }
    afterEach(() => {
        spy.restore();
    });
});
