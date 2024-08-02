using System.Collections.Generic;

namespace CustomerApp
{
    public class CustomerService
    {
        private readonly CustomerRepository _customerRepository;

        public CustomerService(CustomerRepository customerRepository)
        {
            _customerRepository = customerRepository;
        }

        public void AddCustomer(Customer customer)
        {
            _customerRepository.AddCustomer(customer);
        }

        public Customer GetCustomer(int id)
        {
            return _customerRepository.GetCustomer(id);
        }

        public void RemoveCustomer(int id)
        {
            _customerRepository.RemoveCustomer(id);
        }

        public bool ValidateCustomer(Customer customer)
        {
            // Check for a valid email
            if (string.IsNullOrEmpty(customer.Email) || !customer.Email.Contains("@"))
            {
                return false;
            }
            return true;
        }

        public bool CompareCustomers(Customer customer1, Customer customer2)
        {
            return customer1.Id == customer2.Id &&
                   customer1.Name == customer2.Name &&
                   customer1.Email == customer2.Email &&
                   customer1.Phone == customer2.Phone;
        }
    }
}
