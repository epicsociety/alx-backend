const kue = require('kue');

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0);

  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    console.error(errorMessage);
    job.log(errorMessage);
    done(new Error(errorMessage));
  } else {
    job.progress(50);

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    setTimeout(() => {
      job.progress(100);
      done();
    }, 1000);
  }
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

queue.on('job enqueue', (id, type) => {
  console.log(`Job #${id} of type ${type} is in the queue.`);
});

queue.on('error', (err) => {
  console.error(`Error in the queue: ${err}`);
  process.exit(1);
});
