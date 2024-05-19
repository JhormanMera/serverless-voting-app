var funker = require('funker');
var pg = require('pg');

function processVote(args) {
  return new Promise((resolve, reject) => {
    var client = new pg.Client('postgres://postgres:postgres@database.default.svc.cluster.local:5432/postgres');
    client.connect();
    client.query("CREATE TABLE IF NOT EXISTS votes (id SERIAL PRIMARY KEY, vote VARCHAR(255) NOT NULL)")
      .then(() => {
        return client.query("INSERT INTO votes (vote) VALUES ($1)", [args.vote]);
      })
      .then(() => {
        client.end();
        resolve();
      })
      .catch(err => {
        reject(err);
      });
  });
}

funker.handle(function(args, callback) {
  // Return immediately so this function runs in the background
  callback();

  console.log("Processing vote for", args.vote);

  processVote(args)
    .then(() => console.log("Vote processed successfully"))
    .catch(err => console.error("Error processing vote:", err));
});