const redis = require("redis");
const client = redis.createClient();

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

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, res) => {
        if (err) {
            console.error(err);
        } else {
            redis.print(res);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');