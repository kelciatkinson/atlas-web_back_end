export default function createEmployeesObject(departmentName, employees) {
  const department = `{${departmentName}}: `;
  let employee = '';
  employees.forEach((value) => {
    employee += `'${value}',`;
  });
  return `${department}[${employee}]`;
}
