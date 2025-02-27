/**
 * Displays a message to STDOUT
 *
 */

function displayMessage(message) {
    process.stdout.write(message + `\n`);
}

module.exports = displayMessage;
