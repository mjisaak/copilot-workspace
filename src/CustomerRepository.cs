using System.Linq;
using Microsoft.EntityFrameworkCore;

namespace CustomerApp
{
    public class CustomerRepository
    {
        private readonly AppDbContext _context;

        public CustomerRepository(AppDbContext context)
        {
            _context = context;
        }

        public void AddCustomer(Customer customer)
        {
            _context.Customers.Add(customer);
            _context.SaveChanges();
        }

        public Customer GetCustomer(int id)
        {
            return _context.Customers.FirstOrDefault(c => c.Id == id);
        }

        public void RemoveCustomer(int id)
        {
            var customer = _context.Customers.FirstOrDefault(c => c.Id == id);
            if (customer != null)
            {
                _context.Customers.Remove(customer);
                _context.SaveChanges();
            }
        }

        public bool ValidateCustomer(Customer customer)
        {
            // Add validation logic here
            return true;
        }

        public bool CompareCustomers(Customer customer1, Customer customer2)
        {
            // Add comparison logic here
            return customer1.Id == customer2.Id &&
                   customer1.Name == customer2.Name &&
                   customer1.Email == customer2.Email &&
                   customer1.Phone == customer2.Phone;
        }
    }
}
