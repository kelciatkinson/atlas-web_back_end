export default function getListStudentIds() {
  if (Array.isArray(arguments[0])) {
    return arguments[0].map((obj) => obj.id);
  }
  return [];
}
