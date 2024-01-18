export default function createReportObject(employeesList) {
  const ret = {
    allEmployees: employeesList,
    getNumberOfDepartments(object) {
      return Object.keys(object).length;
    },
  };
  return ret;
}
