export default function getStudentsByLocation(stList, city) {
  return stList.filter((student) => student.location == city);
};
