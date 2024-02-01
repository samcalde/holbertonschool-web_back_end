export default function setFromArray(arrArg) {
  const retSet = new Set();
  arrArg.forEach((value) => {
    retSet.add(value);
  });
  return retSet;
}
