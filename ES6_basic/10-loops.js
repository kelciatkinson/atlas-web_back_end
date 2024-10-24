export default function appendToEachArrayValue(array, appendString) {
  for (let element of array) {
    var value = array[element];
    array = [];
    array = appendString + value;
  }

  return array;
}
