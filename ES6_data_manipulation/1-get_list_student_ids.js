export default function getListStudentIds(objectList) {
  const idArray = objectList.map((object) {
    if (object.id) {
      return object.id;
    }
  })
  return (idArray);
}
