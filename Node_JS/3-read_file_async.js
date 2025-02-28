const fs = require('fs').promises;

/**
 * Counts students in each field from a CSV file.
 *
 */

async function countStudents(path) {
    try {
        const data = await fs.readFile(path, 'utf-8');
    
        if (!data) {
          throw new Error('Cannot load the database');
        }
    
        const lines = data.split('\n');
        
        // Removes header row
        const students = lines.slice(1);
        
        console.log(`Number of students: ${students.length}`);
    
        // Creates object to store counts and names by fieldb
        const studentsByField = {};
        
        students.forEach((student) => {
          const [firstname, , , field] = student.split(',');
          if (!studentsByField[field]) {
            studentsByField[field] = [];
          }
          studentsByField[field].push(firstname);
        });
    
        // Prints results for each field
        for (const [field, students] of Object.entries(studentsByField)) {
            console.log(
              `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`
            );
        }
        return Promise.resolve();
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;