const fs = require('fs');

if (fs.existsSync('/home/escartii')) {
  console.log('The file or directory exists');
} else {
  console.log('The file or directory does not exist');
}
