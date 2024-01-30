export default function getListStudentIds(objectList) {
  if (Array.isArray(objectList)) {
    const idArray = objectList.map((object) => object.id);
    return (idArray);
  }
  return ([]);
}
