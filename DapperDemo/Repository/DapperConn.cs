using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Dapper;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using DapperDemo.Models;


namespace DapperDemo.Repository
{
    public class DapperConn
    {
        public IEnumerable<MasterDetails> GetMasterDetails()
        {
            IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["employeesConnection"].ConnectionString);

            var objDetails = db.QueryMultiple("multiplerecord_1", commandType: CommandType.StoredProcedure);
            MasterDetails objMaster = new MasterDetails();

            objMaster.EmpPersonal = objDetails.Read<Employee>().ToList();
            objMaster.StudPersonal = objDetails.Read<student>().ToList();

            List<MasterDetails> CustomerObj = new List<MasterDetails>();
            CustomerObj.Add(objMaster);



            return CustomerObj;
        }
    }
}