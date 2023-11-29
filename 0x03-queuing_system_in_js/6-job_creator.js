const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData);

job.save((err) => {
  if (err) {
    console.error(`Error creating notification job: ${err}`);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }

//   queue.process('push_notification_code', (job, done) => {
//     setTimeout(() => {
//       // For demonstration purposes, let's assume the job is successful
//       // In a real-world scenario, you would perform the actual job/task here
//       console.log(`Processing job ${job.id}: Sending notification to ${job.data.phoneNumber} - Message: ${job.data.message}`);
//       done();
//     }, 2000);
//   });


  job.on('complete', () => {
    console.log('Notification job completed');
    process.exit(0);
  });

  // When the job is failing
  job.on('failed', (err) => {
    console.error(`Notification job failed`);
    process.exit(1);
  });
});
