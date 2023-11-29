import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();
const queue = kue.createQueue();

// Promisify Redis functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Initialize the number of available seats to 50
const initialAvailableSeats = 50;
let numberOfAvailableSeats = initialAvailableSeats;

// Initialize reservationEnabled to true
let reservationEnabled = true;

// Function to reserve a seat
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

// Function to get the current available seats
const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return availableSeats ? parseInt(availableSeats) : 0;
};

// Route to get the number of available seats
app.get('/available_seats', (req, res) => {
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  // Create and queue a job in the reserve_seat queue
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }

    res.json({ status: 'Reservation in process' });
  });

  // Listen for job completion
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  // Listen for job failure
  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route to process the queue and reserve a seat
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Process the reserve_seat queue
  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();

    if (currentAvailableSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      numberOfAvailableSeats -= 1;
      await reserveSeat(numberOfAvailableSeats);

      if (numberOfAvailableSeats === 0) {
        reservationEnabled = false;
      }

      done();
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
