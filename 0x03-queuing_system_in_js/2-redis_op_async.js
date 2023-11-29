const redis = require("redis");
const client = redis.createClient();
const { promisify } = require("util");
const getAsync = promisify(client.get).bind(client)

client.on("error", (error) => {
    console.error("Redis client not connected to the server: ", error);
});

client.on("connect", (error) => {
    console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, res) => {
        if (err) {
            console.error(err);
        } else {
            redis.print(res);
        }
    });
}

async function displaySchoolValue(schoolName) {
    try {
        const res = await getAsync(schoolName);
        redis.print(res);
    } catch (err) {
        console.error(err);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco')