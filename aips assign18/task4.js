/**
 * Task 4: Data Structures with Functions (JavaScript → Python)
 * Function `printStudents(students)` prints each student name from an array.
 */

function printStudents(students) {
    console.log('Student List:');
    for (let i = 0; i < students.length; i++) {
        console.log(students[i]);
    }
}

// Test the function with sample student names
const students = ['Alice', 'Bob', 'Charlie'];
printStudents(students);
