import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue({ disableSearch: true, testMode: true });
  });

  after(() => {
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('simulate processing the jobs', (done) => {
    queue.process('push_notification_code_3', 2, (job, jobDone) => {
      console.log(`Processing job ${job.id}`);

      jobDone();
    });

    setTimeout(done, 500);
  });

  it('validate job completion', () => {
    expect(queue.testMode.jobs[0].state).to.equal('complete');
    expect(queue.testMode.jobs[1].state).to.equal('complete');
  });
});
