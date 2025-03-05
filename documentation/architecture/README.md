# National Address Database Submission Tool Architecture

### Entry Points

Users can work with the National Address Database Submission Tool by way of:

- **Flask Web Server**: Primary interface for web-based interactions for Data
  Producers and NAD Administrator.
- **CLI**: Command line interface allowing NAD Administrator to perform
  administrative tasks.

### Application Core

Logic concerning business rules, data validation and profiling, and other
application concerns. The core is unaware of how its entry points and its
infrastructure dependencies are implemented.

### Infrastructure Dependencies

The current remote development environment uses [services provided by cloud.gov](https://cloud.gov/docs/services/intro/).

- **Object Storage**: Storage for datasets submitted by users, via
  [S3](https://cloud.gov/docs/services/s3/).
- **Relational Database**: Persistence for application data and data validation
  reports, via [RDS PostgreSQL database](https://cloud.gov/docs/services/relational-database/).
- **Task Queue Broker**: Manages queue of data validation tasks for Celery, via
  [AWS Elasticache Redis](https://cloud.gov/docs/services/aws-elasticache/).

### System diagram

```mermaid
flowchart TB
    %% External Users
    data_provider([Data Provider])
    nad_admin([NAD Administrator])
    
    %% Authentication System
    login[(Login.gov)]
    
    %% CI/CD Pipeline
    cicd[GitHub/GitLab CI/CD]
    
    %% Main System Boundary
    subgraph NAD_SYSTEM ["National Address Database Submission Tool"]
        direction TB
        
        %% Application Layer
        subgraph APP_LAYER ["Application Layer"]
            app[Python/Flask Web Server]
        end
        
        %% Task Processing Layer
        subgraph PROCESSING_LAYER ["Processing Layer"]
            job_runner[Celery Worker]
        end
        
        %% Infrastructure Layer
        subgraph INFRA_LAYER ["Infrastructure Layer"]
            postgres[(PostgreSQL Database)]
            redis[(Redis Queue)]
            s3[(S3 Object Storage)]
        end
        
        %% Internal Connections
        app -->|Store metadata| postgres
        app -->|Queue tasks| redis
        app -->|Store & read files| s3
        
        job_runner -->|Process tasks| redis
        job_runner -->|Read & write data| s3
        job_runner -->|Update status| postgres
    end
    
    %% External Connections
    data_provider -->|Submit GIS data| app
    nad_admin -->|Manage platform| app
    app -->|Authenticate users| login
    cicd -->|Deploy application| NAD_SYSTEM
    
    %% Visual Styling
    classDef external fill:#e6f7ff,stroke:#1890ff,stroke-width:2px
    classDef infrastructure fill:#f9f0ff,stroke:#722ed1,stroke-width:2px
    classDef application fill:#f0fff4,stroke:#52c41a,stroke-width:2px
    classDef processing fill:#fff2e8,stroke:#fa8c16,stroke-width:2px
    classDef system fill:#ffffff,stroke:#434343,stroke-width:2px,stroke-dasharray: 5 5
    
    class data_provider,nad_admin,login,cicd external
    class postgres,redis,s3 infrastructure
    class app application
    class job_runner processing
    class NAD_SYSTEM system
```
