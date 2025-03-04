const sinon = require("sinon");
const chai = require("chai");
const expect = chai.expect;
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe("sendPaymentRequestToApi", function () {
    const spy = sinon.spy(Utils, "calculateNumber");

    it("should call Utils.calculateNumber with 'SUM', 100, 20", function () {
        sendPaymentRequestToApi(100, 20);
        expect(spy.calledOnce).to.be.true;
        expect(spy.calledWithExactly("SUM", 100, 20)).to.be.true;
    });

    spy.restore();
});
