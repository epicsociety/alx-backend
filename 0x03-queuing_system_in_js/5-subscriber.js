const redis = require("redis");
const client = redis.createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");

    client.subscribe("holberton school channel");
});

client.on("error", (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
});

client.on("message", (channel, message) => {
    console.log(`Message received on channel ${channel}: ${message}`);

    if (message === "KILL_SERVER") {
        client.unsubscribe();
        client.quit();
    }
});
