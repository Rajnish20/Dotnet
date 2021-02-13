using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace DapperDemo.Models
{
    public class Employee
    {
        public int empno { get; set; }

        public string nam { get; set; }

        public string dept { get; set; }
    }

    public class student
    {
        public string nam { get; set; }

        public string Sub2 { get; set; }
    }


    public class MasterDetails
    {
        public List<Employee> EmpPersonal { get; set; }
        public List<student> StudPersonal { get; set; }
    }
}