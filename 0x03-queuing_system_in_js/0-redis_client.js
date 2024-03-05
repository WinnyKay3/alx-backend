import redis from 'redis';

const redis_url = process.env.REDIS_URL ?? 'redis://localhost:6379'
const client = redis.createClient(redis_url);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
