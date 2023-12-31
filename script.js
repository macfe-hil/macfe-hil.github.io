const fs = require('fs');
const path = require('path');

const reportFolder = 'reports';
const indexFile = 'index.html';

// Get all HTML files in the reports folder
const files = fs.readdirSync(path.join(__dirname, reportFolder)).filter(file => file.endsWith('.html'));

// Sort files by date and time in the filename, newest first
files.sort((a, b) => {
    const dateA = getDateFromFilename(a);
    const dateB = getDateFromFilename(b);
    return dateB.getTime() - dateA.getTime();
});

// Function to extract date from filename
function getDateFromFilename(filename) {
    const match = filename.match(/(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})\.html/);

    if (match) {
        const [year, month, day, hour, minute, second] = match[1].split(/[-_]/);
        return new Date(`${year}-${month}-${day}T${hour}:${minute}:${second}Z`);
    }

    return new Date(0);
}

// Start building the index.html content
let htmlContent = '<html><head><title>Test Reports</title></head><body><h1>Test Reports</h1><ul>';

// Add each report to the list
files.forEach(file => {
    const fileName = path.basename(file);
    const fileDate = getDateFromFilename(file).toISOString();
    htmlContent += `<li><a href="${file}">${fileName}</a> - ${fileDate}</li>`;
});

htmlContent += '</ul></body></html>';

// Write the content to the index.html file
fs.writeFileSync(path.join(__dirname, indexFile), htmlContent);

console.log("Index file generated successfully.");
