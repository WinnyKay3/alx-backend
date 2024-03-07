import redis from 'redis';

const redis_url = process.env.REDIS_URL ?? 'redis://localhost:6379'
const client = redis.createClient(redis_url);

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function(err) {
  console.log('Redis client not connected to the server: ' + err);
});

client.subscribe('holberton school channel');

client.on('message', function(channel, message) {
  console.log('Message received on channel ' + channel + ': ' + message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
