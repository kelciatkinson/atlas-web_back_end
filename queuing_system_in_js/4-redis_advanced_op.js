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

const schoolData = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2,
};

function setHash() {
    for (const [key, value] of Object.entries(schoolData)) {
        client.hset('HolbertonSchools', key, value, redis.print);
    }
}

function displayHash() {
    client.hgetall('HolbertonSchools', function(err, reply) {
        if (err) {
            console.error(err);
        } else {
            console.log(reply);
        }
    });
}

setHash();
displayHash();
