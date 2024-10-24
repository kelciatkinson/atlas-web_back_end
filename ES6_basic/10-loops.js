export default function appendToEachArrayValue(array, appendString) {
  for (const element of array) {
    const value = array[element];
    array = [];
    array = appendString + value;
  }

  return array;
}
