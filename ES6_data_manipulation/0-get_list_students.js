export default function getListStudents() {
  function createStudent(id, firstName, location) {
    return {
      id,
      firstName,
      location,
    };
  }
  const student1 = createStudent(1, 'Guillaume', 'San Francisco');
  const student2 = createStudent(2, 'James', 'Columbia');
  const student3 = createStudent(5, 'Serena', 'San Francisco');
  const returnArr = [student1, student2, student3];
  return (returnArr);
}
