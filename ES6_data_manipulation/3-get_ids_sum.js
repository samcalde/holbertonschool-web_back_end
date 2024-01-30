export default function getStudentIdsSum(stList) {
  return stList.reduce((sum, student) => sum + student.id, 0);
}
