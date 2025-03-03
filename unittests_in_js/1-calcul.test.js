const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber", function () {
    describe("SUM", function () {
        it("returns the sum of two rounded numbers", function () {
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
            assert.strictEqual(calculateNumber('SUM', 1.6, 3.2), 5);
            assert.strictEqual(calculateNumber('SUM', -1.4, -4.5), -5);
        });
    });

    describe("SUBTRACT", function () {
        it("returns the subtraction of two rounded numbers", function () {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
            assert.strictEqual(calculateNumber('SUBTRACT', 3.7, 1.2), 3);
            assert.strictEqual(calculateNumber('SUBTRACT', -2.8, -1.1), -2);
        });
    });

    describe("DIVIDE", function () {
        it("returns the division of two rounded numbers", function () {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
            assert.strictEqual(calculateNumber('DIVIDE', 4.8, 2.2), 2.5);
        });

        it("returns'Error' when dividing by zero", function () {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
            assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
        });
    });

    describe("Invalid type", function () {
        it("throws error for invalid operation type", function () {
            assert.throws(() => calculateNumber('MULTIPLY', 1.4, 4.5), /Invalid operation type/);
        });
    });
});
