import redis from 'redis';

const client = redis.createClient({
    host: '127.0.0.1',
    port: 6379,
});

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function(err) {
    console.log(`Redis client not connected to the server: ${err}`);
});
