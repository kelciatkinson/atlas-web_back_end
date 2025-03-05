const sinon = require("sinon");
const chai = require("chai");
const expect = chai.expect;
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe("sendPaymentRequestToApi", function () {
    let spy, stub;

    beforeEach(() => {
        stub = sinon.stub(Utils, "calculateNumber").returns(10);
        spy = sinon.spy(console, "log");
    });

    it("should call Utils.calculateNumber with 'SUM', 100, 20", function () {
        sendPaymentRequestToApi(100, 20);
        expect(stub.calledOnce).to.be.true;

        expect(stub.calledOnce).to.be.true;
        expect(stub.calledWithExactly("SUM", 100, 20)).to.be.true;
        expect(spy.calledOnceWithExactly("The total is: 10")).to.be.true;
    });

    afterEach(() => {
        stub.restore();
        spy.restore();
    });
});
