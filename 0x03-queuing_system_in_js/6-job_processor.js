const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

queue.on('job enqueue', (id, type) => {
  console.log(`Job ${id} of type ${type} is in the queue.`);
});

queue.on('error', (err) => {
  console.error(`Error in the queue: ${err}`);
  process.exit(1);
});
