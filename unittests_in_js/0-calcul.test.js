const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
    it("return the sum of two rounded numbers", function () {
        assert.strictEqual(calculateNumber(1, 3), 4);
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });

    it("handle negative numbers correctly", function () {
        assert.strictEqual(calculateNumber(-1.5, -3.7), -5);
        assert.strictEqual(calculateNumber(-1.4, -3.2), -4);
    });

    it("handle zero correctly", function () {
        assert.strictEqual(calculateNumber(0, 0), 0);
        assert.strictEqual(calculateNumber(0.4, 0.6), 1);
    });
});
