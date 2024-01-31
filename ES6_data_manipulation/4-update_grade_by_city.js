export default function updateStudentGradeByCity(stList, city, newGrades) {
  const stInCity = stList.filter((student) => student.location === city);
  const stUpdated = stInCity.map((student) => {
    for (let i = 0; i < newGrades.length; i++) {
      if (student.id === newGrades[i].studentId) {
        student.grade = newGrades[i].grade;
        break;
      } else {
        student.grade = 'N/A';
      }
    }
    return student;
  });
  return stUpdated;
}