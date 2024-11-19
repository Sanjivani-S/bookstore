# bookstore
books webstore deployed on kubernetes
I have developed a bookstore web service leveraging Django, PostgreSQL, and Docker Desktop, deployed on a local Kubernetes cluster. The application consists of two microservices: `books-service` and `orders-service`. These services are responsible for enabling users to view available books and place orders, respectively.  
The PostgreSQL database operates as a dedicated pod within the cluster and is exclusively accessed by the `books-service` and `orders-service` for enhanced security. It employs persistent storage, ensuring data retention even in the event of system disruptions.  
Both microservices are accessible externally via a web browser on `localhost` for GET requests, such as viewing books or retrieving orders. For operations requiring POST requests, tools like Postman are used.  
Currently, each microservice is configured to run with two replicas to ensure high availability and load distribution. This scalability can be adjusted to meet future demand. The architecture follows cloud-native principles, ensuring modularity, resilience, and seamless deployment in the Kubernetes environment.

Software Architecture Design
The architecture of the bookstore web service follows a  microservices-based architecture  deployed on Kubernetes. It includes two independent microservices (`books-service` and `orders-service`) and a PostgreSQL database, each running in separate containers. The architecture adheres to cloud-native design principles, ensuring scalability, resilience, and separation of concerns.

   Component Roles and Responsibilities 
1.  Books-Service 
   -  Responsibility:   
This service provides functionality to view available books in the inventory.  
Implements a REST API for GET requests (`/books`) to fetch book details from the database.
   -  Interaction:   
Communicates with the PostgreSQL database to retrieve book information. Accessible externally via a browser or API testing tools like Postman.
2.  Orders-Service 
   -  Responsibility:   
    	This service handles user orders.  
Implements a REST API for POST requests (`/orders`) to place an order and GET  requests (`/orders`) to retrieve order details.
   -  Interaction:   
Connects with the PostgreSQL database to store and retrieve order data. It handles API requests through tools like Postman since POST requests cannot be sent via a browser.

3.  Database (PostgreSQL) 
   -  Responsibility:   
Stores persistent data for the application, including book inventory and order details. It runs as a separate Kubernetes pod with persistent storage.
   -  Interaction:   
- Directly accessed by `books-service` and `orders-service`.  
- Not exposed to the outside world for security reasons.

