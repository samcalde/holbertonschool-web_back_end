export default function returnHowManyArguments(...argv) {
  var i = 0;
  for (const argument of argv) {
    i++;
  }
  return i;
}
