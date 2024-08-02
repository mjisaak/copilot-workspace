# Copilot-Workspace Demo

## .NET Application with Customer Management

This repository contains a .NET application with 2 REST methods to add a new customer and add this customer to a SQL Database.

### How to Run the Application

1. Navigate to the `src` directory:
   ```
   cd src
   ```
2. Run the .NET application:
   ```
   dotnet run
   ```

### Configuring the SQL Database Connection String

1. Open the `src/appsettings.json` file.
2. Update the `DefaultConnection` string with your SQL Database connection details:
   ```json
   {
     "ConnectionStrings": {
       "DefaultConnection": "Server=YOUR_SERVER;Database=CustomerAppDb;Trusted_Connection=True;MultipleActiveResultSets=true"
     },
     "Logging": {
       "LogLevel": {
         "Default": "Information",
         "Microsoft": "Warning",
         "Microsoft.Hosting.Lifetime": "Information"
       }
     },
     "AllowedHosts": "*"
   }
   ```

### Example REST API Requests

#### Add a New Customer

```
POST /api/customer
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "123-456-7890"
}
```

#### Get a Customer by ID

```
GET /api/customer/{id}
```
