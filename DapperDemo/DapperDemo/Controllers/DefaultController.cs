using Dapper;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace DapperDemo.Controllers
{
    public class DefaultController : Controller
    {
        // GET: Default
        public ActionResult Index()
        {
            
            return View();

        }

        public ActionResult GetId()
        {
            return View();
        }

        public ActionResult GetId_1()
        {
            return View();
        }

        public ActionResult GetRecord()
        {
            List<Models.Employee> emp = new List<Models.Employee>();
            try
            {
                using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["employeesConnection"].ConnectionString))
                {
                    emp = db.Query<Models.Employee>("prcEmpShow1", commandType: CommandType.StoredProcedure).ToList();
                }

                return View(emp);
            }
            catch(Exception ex)
            {
                return View("Error", new HandleErrorInfo(ex, "Models.Employee", "GetRecord"));
            }
        }
        

        public ActionResult SearchRecord(int id)
        {
            
            Models.Employee emp = new Models.Employee();
            using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["employeesConnection"].ConnectionString))
            {
                emp = db.QueryFirstOrDefault<Models.Employee>("EmploySearch2", new { EmployeeId = id }, commandType: CommandType.StoredProcedure);
            }
            return View(emp);
        }

        public ViewResult GetName(int id)
        {
            using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["employeesConnection"].ConnectionString))
            {
               ViewBag.name  = db.QueryFirstOrDefault<string>("EmploySearch3", new { EmployeeId = id}, commandType: CommandType.StoredProcedure);
            }

            return View();
        }

        public ActionResult MultipleRecord()
        {
            List<Models.Employee> ord = new List<Models.Employee>();
            using (IDbConnection db = new SqlConnection(ConfigurationManager.ConnectionStrings["employeesConnection"].ConnectionString))
            {
                ord = db.Query<Models.Employee>("getMultipleRecord", commandType: CommandType.StoredProcedure).ToList();
            }
            return View(ord);
        }
    }
}