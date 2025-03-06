import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient({
    host: '127.0.0.1',
    port: 6379,
});

client.get
const getAsync = promisify(client.get).bind(client);

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    try {
        const reply = await getAsync(schoolName);
        console.log(reply);
    } catch (err) {
        console.error(err);
    }
}

client.on('error', function(err) {
    console.log(`Redis client not connected to the server: ${err}`);
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
