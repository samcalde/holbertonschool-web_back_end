export default function getListStudentIds(objectList) {
  if (Array.isArray(objectList)) {
    const idArray = objectList.map((object) => {
      if (object.id) {
        return object.id;
      }
    });
    return (idArray);
  }
  return ([]);
}
