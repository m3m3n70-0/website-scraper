const axios = require('axios');
const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const url = 'https://justinbonhof/saturn';
const baseDir = './downloaded_files';

axios.get(url, { maxRedirects: 5 }) // Follow a maximum of 5 redirects
  .then((response) => {
    const htmlData = response.data;
    const $ = cheerio.load(htmlData);

    // Rest of the parsing and downloading logic remains the same
    // ...

    // For example, downloading the HTML content to a file
    fs.writeFile(path.join(baseDir, 'response.html'), htmlData, (err) => {
      if (err) {
        console.error(`Error writing HTML file: ${err}`);
      } else {
        console.log('HTML response saved in response.html');
      }
    });
  })
  .catch((error) => {
    console.error(`Error fetching data: ${error.message}`);
  });
