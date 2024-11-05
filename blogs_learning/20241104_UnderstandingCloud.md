![Learning](https://img.shields.io/badge/Self_Education-8A2BE2)
![Written by ChatGPT](https://img.shields.io/badge/written_by-ChatGPT-brightgreen)

# Recap of cloud functionalities

Today I am going to write a memo of cloud. Meaning: What is needed when setting up servers, what is common between different cloud providers, what are the things u need?

---

When creating a new server in the cloud, you typically need to configure and consider several resources and settings to ensure the server functions properly and is secure. Here's an overview of the key components:

### 1. **Virtual Network (VNet)**
   - **Purpose**: A VNet (or equivalent) is essential for isolating and securing your server within a defined network space in the cloud.
   - **Configuration Options**: Subnets, address space, network security groups (NSGs), and peering.

### 2. **IP Address**
   - **Public IP**: If the server needs to be accessible over the internet, you'll need a public IP address.
   - **Private IP**: For internal communication within your VNet, you will use a private IP address.

### 3. **Disk Storage**
   - **OS Disk**: This is where the operating system is installed. It usually comes with a default size, but you can adjust it.
   - **Data Disk**: Additional storage for application data, databases, or other files.
   - **Disk Types**: Options typically include standard HDD, standard SSD, and premium SSD, depending on performance and cost requirements.

### 4. **Compute Resources (VM Size)**
   - **CPU & Memory**: Select the appropriate virtual machine size based on your workload (e.g., vCPUs and RAM).
   - **Performance Considerations**: Choose a size that balances cost and performance.

### 5. **Operating System**
   - **Linux/Windows**: Choose the OS image based on the application requirements.
   - **Custom Images**: You may use custom images if specific configurations or software are needed.

### 6. **Network Security**
   - **Network Security Groups (NSG)**: Define rules to control incoming and outgoing traffic to your server.
   - **Firewalls**: You can use firewalls to add another layer of protection.

### 7. **Authentication and Access Control**
   - **SSH Key (for Linux)**: Generate or use an existing SSH key for secure access.
   - **Password/Username (for Windows)**: Configure a secure username and password.
   - **Role-Based Access Control (RBAC)**: Assign permissions to users and groups to manage server access securely.

### 8. **Load Balancer (if applicable)**
   - If you plan to have multiple servers to distribute traffic, set up a load balancer for load distribution.

### 9. **Domain Name System (DNS)**
   - Configure a DNS name if needed for easier access to the server instead of using an IP address.

### 10. **Backup and Recovery**
   - Configure automated backups for your data and OS.
   - Consider options for disaster recovery.

### 11. **Monitoring and Logging**
   - Set up monitoring to track performance metrics (CPU, memory, disk usage).
   - Enable logging for security and troubleshooting purposes.

### 12. **Auto-scaling and Availability**
   - Configure auto-scaling rules to handle varying workloads (if needed).
   - Consider deploying across availability zones for higher availability.

### 13. **Tags**
   - Add tags to manage and organize resources for easier tracking and billing.

### 14. **Software and Configuration Management**
   - Install necessary software and configure it.
   - Use configuration management tools like Ansible, Chef, or Puppet if needed.

---

