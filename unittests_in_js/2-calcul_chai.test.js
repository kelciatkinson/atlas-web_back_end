const assert = require("assert");
const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require("./2-calcul_chai");

describe("calculateNumber", function () {
    describe("SUM", function () {
        it("returns the sum of two rounded numbers", function () {
            expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
            expect(calculateNumber('SUM', 1.6, 3.2)).to.equal(5);
            expect(calculateNumber('SUM', -1.4, -4.5)).to.equal(-5);
        });
    });

    describe("SUBTRACT", function () {
        it("returns the subtraction of two rounded numbers", function () {
            expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
            expect(calculateNumber('SUBTRACT', 3.7, 1.2)).to.equal(3);
            expect(calculateNumber('SUBTRACT', -2.8, -1.1)).to.equal(-2);
        });
    });

    describe("DIVIDE", function () {
        it("returns the division of two rounded numbers", function () {
            expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
            expect(calculateNumber('DIVIDE', 4.8, 2.2)).to.equal(2.5);
        });

        it("returns'Error' when dividing by zero", function () {
            expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
            expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
        });
    });

    describe("Invalid type", function () {
        it("throws error for invalid operation type", function () {
            expect(() => calculateNumber('MULTIPLY', 1.4, 4.5).to.throw('Invalid operation'));
        });
    });
});
