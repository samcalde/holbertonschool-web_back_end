export default function appendToEachArrayValue(array, appendString) {
  const array = [];
  for (const item of array) {
    array.push(appendString + item);
  }
  return array;
}
