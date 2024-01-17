export default function returnHowManyArguments(...arguments) {
  var i = 0;
  for (argument in arguments) {
    i++;
  }
  return i;
}