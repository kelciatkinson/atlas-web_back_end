/**
 * Returns a resolved promis with the object when success is true
 */

function getPaymentTokenFromAPI(success) {
    if (success) {
        return Promise.resolve({data: 'Successful response from the API' });
    }
}

module.exports = getPaymentTokenFromAPI;
