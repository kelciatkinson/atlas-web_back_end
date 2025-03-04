const Utils = {
    calculateNumber: function (type, a, b) {
    const numA = Math.round(a);
    const numB = Math.round(b);
  
    if (type === 'SUM') {
        return numA + numB;
    }
    if (type === 'SUBTRACT') {
        return numA - numB;
    }
    if (type === 'DIVIDE') {
        if (numB === 0) {
            return 'Error';
        }
        return numA / numB;
    }
    throw new Error('Invalid operation type');
    },
};

module.exports = Utils;
