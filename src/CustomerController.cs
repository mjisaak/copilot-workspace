using Microsoft.AspNetCore.Mvc;

namespace CustomerApp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class CustomerController : ControllerBase
    {
        private readonly CustomerService _customerService;

        public CustomerController(CustomerService customerService)
        {
            _customerService = customerService;
        }

        [HttpPost]
        public IActionResult AddCustomer(Customer customer)
        {
            _customerService.AddCustomer(customer);
            return Ok();
        }

        [HttpGet("{id}")]
        public IActionResult GetCustomer(int id)
        {
            var customer = _customerService.GetCustomer(id);
            if (customer == null)
            {
                return NotFound();
            }
            return Ok(customer);
        }

        [HttpDelete("{id}")]
        public IActionResult RemoveCustomer(int id)
        {
            var customer = _customerService.GetCustomer(id);
            if (customer == null)
            {
                return NotFound();
            }
            _customerService.RemoveCustomer(id);
            return Ok();
        }

        [HttpPost("validate")]
        public IActionResult ValidateCustomer(Customer customer)
        {
            var isValid = _customerService.ValidateCustomer(customer);
            return Ok(isValid);
        }

        [HttpPut("compare")]
        public IActionResult CompareCustomers(Customer customer1, Customer customer2)
        {
            var areEqual = _customerService.CompareCustomers(customer1, customer2);
            return Ok(areEqual);
        }
    }
}
