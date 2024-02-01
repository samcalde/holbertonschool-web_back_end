export default function setFromArray(arrArg) {
  let retSet = new Set();
  arrArg.forEach(value => {
    retSet.add(value);
  });
  return retSet;
}