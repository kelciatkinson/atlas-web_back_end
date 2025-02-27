/**
 * Displays a message to STDOUT
 * Prompts user for name and outputs it
 * If input is piped, program will display closing message.
 */

process.stdout.write(`Welcome to Holberton School, what is your name?\n`);

process.stdin.on(`data`, (data) => {
    const name = data.toString().trim();
    process.stdout.write(`Your name is: ${name}\n`);
    // Handles process exit based on input method
    if (!process.stdin.isTTY) {
        process.stdout.write(`This important software is now closing\n`);
    }
    process.stdin.pause()
});
