export default function getListStudentIds(objectList) {
  let idArray = []
  for (let i = 0; i < objectList.length; i++) {
    if (objectList[i].id) {
      idArray.push(objectList[i].id);
    }
  }
  return (idArray);
}
