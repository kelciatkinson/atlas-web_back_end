/**
 * 
 *
 */

function calculateNumber(type, a, b) {
    const firstNum = Math.round(a);
    const secondNum = Math.round(b); 
    if (type === 'SUM') {
        return firstNum + secondNum;
    }

    if (type === 'SUBTRACT') {
        return firstNum - secondNum;
    }

    if (type === 'DIVIDE') {
        if (secondNum === 0) {
            return 'Error';
        }
        return firstNum / secondNum;
    }

    throw new Error('Invalid operation type');
}

module.exports = calculateNumber;