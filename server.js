const readline = require('readline').createInterface({   //module to take input from the user
    input: process.stdin,
    output: process.stdout
  });

  
const fs = require("fs");             //module to write the command in the commands.txt file
  readline.question('Enter Command:', command => {
      fs.writeFileSync("commands.txt", command)
      readline.close();
    });
