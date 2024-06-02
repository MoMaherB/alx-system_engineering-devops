0x09. Web infrastructure design

0-simple_web_stack

### Combined Explanation Organized with Numbers

1. Server:
   - A server is a physical or virtual machine typically located in a data center, running an OS to manage hardware resources and host components necessary for the website to function, including the web server, application server, and database.

2. Domain Name
   - foobar.com is a human-readable address that maps to an IP address, allowing users to access the website without needing to remember numerical IP addresses; DNS translates this domain name into an IP address that computers use to identify each other on the network.

3. DNS Record:
   - The www in www.foobar.com is a Name record pointing to the root domain (foobar.com), which then points to the IP address 8.8.8.8; the DNS record for www.foobar.com is an A record mapping the domain name to its corresponding IP address (8.8.8.8).

4. Web Server (Nginx):
   - The web server handles incoming HTTP requests from users' browsers, serves static content, and forwards dynamic requests to the application server, providing web pages to users who request them.

5. Application Server:
   - The application server runs the application code (PHP, Python, Node.js, etc.), processing business logic and dynamically generating content based on the request.

6. Database (MySQL):
   - The database stores and manages data, providing the application server with efficient data retrieval and storage capabilities.

7. Communication:
   - The server uses the HTTP/HTTPS protocol to communicate with the user's browser over a network using TCP/IP protocols, handling data transmission and routing.

Issues with This Infrastructure

Single Point of Failure (SPOF):
   - Since all components are hosted on a single server, if the server fails, the entire website becomes unavailable, as there is no redundancy in this setup.

Downtime for Maintenance:
   - Performing maintenance or deploying new code requires restarting services, causing temporary downtime for the website.

Scalability:
   - A single server can only handle a limited amount of traffic; as traffic increases, performance degrades and the server may become overwhelmed, making the infrastructure incapable of scaling beyond the server's capacity.


=============================================================================================================

1-distributed_web_infrastructure

1. Load Balancer (HAProxy):
   - Purpose: Distributes incoming traffic across multiple servers to ensure no single server is overwhelmed.
   - Distribution Algorithm: Round Robin, where each incoming request is distributed to the next server in line, ensuring an even load distribution.
   - Configuration: Configured in an Active-Active setup, where both servers handle traffic simultaneously, balancing the load across them. In contrast, an Active-Passive setup would have one server active and handling traffic while the other remains on standby.
   - Issue: The load balancer is still a single point of failure (SPOF). If it fails, the entire system becomes inaccessible. This can be mitigated by using redundant load balancers.

2. Web Servers (Nginx):
   - **Purpose**: Handle HTTP requests, serve static content, and forward dynamic content requests to application servers.
   - **Addition**: Adding a second web server improves redundancy and load handling.
   - **Configuration**: Each server contains a web server (Nginx), ensuring redundancy and load distribution.

3. Application Servers:
   - Purpose: Execute the application code, process business logic, and generate dynamic content.
   - Addition: Having multiple application servers ensures that if one fails, the others can handle the traffic.
   - Configuration: Each server contains an application server , ensuring redundancy and load distribution.

4. Database (MySQL):
   - Primary-Replica Setup:
     - Primary (Master) Node: Handles all write operations.
     - Replica (Slave) Node: Copies data from the primary node and handles read operations, improving read performance and providing redundancy.
     - How it works: The primary node processes all data modification requests (INSERT, UPDATE, DELETE), and these changes are replicated to the replica node to ensure data consistency.
     - Configuration: Each server contains a database (MySQL), with a primary node handling write operations and replica nodes handling read operations.
     - Issue: If the primary database fails, write operations cannot be processed. This can be mitigated by implementing a failover strategy where the replica can be promoted to primary.

Issues with This Infrastructure

Single Point of Failure (SPOF):
   - Load Balancer: If the load balancer fails, the entire system becomes inaccessible. This can be mitigated by using redundant load balancers.
   - Primary Database: If the primary database fails, write operations cannot be processed. This can be mitigated by implementing a failover strategy where the replica can be promoted to primary.

7. Security Issues:
   - No Firewall: Without a firewall, the servers are vulnerable to unauthorized access and attacks.
   - No HTTPS: Without HTTPS, data transmitted between users and the server is not encrypted, making it susceptible to interception.

8. No Monitoring:
   - Issue: Without monitoring, issues such as high load, server failures, or security breaches may go unnoticed until they cause significant problems.
   - Solution: Implementing monitoring tools like Nagios, Prometheus, or Grafana can help detect and respond to issues proactively.

Improvements for Robustness

- Redundant Load Balancers: Use multiple load balancers to eliminate the load balancer as a SPOF.
- Firewalls: Implement firewalls to protect the infrastructure from unauthorized access.
- HTTPS: Enable HTTPS to secure communication between users and the web server.
- Monitoring Tools: Use monitoring tools to keep track of server health, load, and security incidents.

============================================================================================================


2-secured_and_monitored_web_infrastructure

Load Balancer (HAProxy):
   - Purpose: Distributes incoming traffic across multiple servers to ensure no single server is overwhelmed.
Balances load and provides redundancy.

Firewalls:
   - Purpose: Protect each component from unauthorized access and attacks by controlling incoming and outgoing traffic.
   Enhance security by controlling network traffic to and from each server.

SSL Certificate:
   - Purpose: Encrypts traffic between the user's browser and the web server, ensuring data privacy and integrity.
   Ensures data privacy and integrity by using HTTPS.

Monitoring Clients:
   Purpose: Collects metrics and logs for monitoring and alerting.
   Provides visibility into the infrastructure's performance and health.
   Monitoring clients collect data such as CPU usage, memory usage, QPS (queries per second), and error rates, sending it to a centralized     monitoring service like Sumologic.

Security and Monitoring Updates

- Firewalls: Control access to each server, blocking unauthorized access and protecting against attacks.
- Monitoring: Ensures the infrastructure is functioning correctly and efficiently. Monitoring clients collect performance metrics and logs, sending them to a monitoring service for analysis and alerting.
  
Issues with This Infrastructure

SSL Termination at Load Balancer:
   Terminating SSL at the load balancer means traffic between the load balancer and the web servers is unencrypted.
   - Solution: Use end-to-end encryption by also configuring SSL between the load balancer and web servers.
===================================================================================================================

3-scale_up

Updates for this design:

Additional Servers: Split the web server, application server, and database into their own dedicated servers to improve performance, scalability, and maintainability. Each component is placed on a separate server to isolate its functionality and optimize resource usage.

Additional Load Balancer: Purpose: To provide high availability and failover capabilities. If one load balancer fails, the other can take over.

