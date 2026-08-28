# AWS Architect exam

- [1 IAM](#IAM)
  - [IAM Policies](#IAMPolicies)
  - [IAM Entities](#IAMEntities)
  - [IAM Reports](#IAMReports)
  - [IAM Identities](#IAMIdentities)
- [2 EC2](#EC2)
  - [InstanceMetadata](#InstanceMetadata)
  - [UserData](#UserData)
  - [AMI](#AMI)
  - [Instance Types](#InstanceTypes)
  - [IP](#IP)
  - [Log-in to Private instance](#LoginToEC2)
  - [Block Storage](#BlockStorage)
  - [Placement Groups](#PlacementGroups)
  - [NAT](#NAT)
  - [EC2 lifecycle](#Ec2_lifecycle)
  - [Nitro](#Nitro)
  - [EC2 pricing](#Ec2_pricing)
- [3 Auto Scaling](#AutoScaling)
  - [AutoScaling Group](#AutoScalingGroup)
  - [Auto Scaling Timers](#AutoScalingTimers)
  - [Health Checks](#HealthChecks)
  - [Load Balancing](#LoadBalancing)
    - [Load Balancing Security](#LoadBalancingSecurity)
    - [ALB](#ALB)
    - [NLB](#NLB)
    - [GLB](#GLB)
    - [Cross-zone load balancing](#Cross-zone)
  - [Global Accelerator](#GlobalAccelerator)
- [4 Organizations](#Organizations)
- [5 VPC](#VPC)
  - [Security Groups](#SecurityGroups)
  - [Connecting To VPC](#ConnectingToVPC)
  - [VPC Endpoint](#VPCEndpoint)
- [6 S3](#S3)
  - [S3 Storage Classes](#S3StorageClasses)
  - [S3 Access](#S3Access)
  - [S3 Object Lock](#S3S3ObjectLock)    
  - [S3 Transfer Acceleration](#S3StorageClasses)
  - [S3 Encryption](#S3Encryption)
  - [S3 Static Website](#S3StaticWebsite)
  - [S3 CRR](#S3CRR)
- [7 DNS](#DNS)
  - [Route53](#Route53)
  - [CloudFront](#CloudFront)
- [8 Block and File Storage](#Block_File_Storage)
  - [EBS](#EBS)
  - [File Share](#FileShare)
  - [Storage Gateways](#StorageGateways)
- [9 Containers](#Containers)
  - [ECS](#ECS)
  - [EKS](#EKS)
- [10 Serverless](#Serverless)
  - [Lambda](#Lambda)
  - [API Gateway](#APIGateway)
  - [Fargate](#Fargate)
- [11 Database](#Database)
  - [RDS](#RDS)
    - [Aurora](#Aurora)
  - [ElastiCache](#ElastiCache)
  - [DynamoDB](#DynamoDB)
  - [Redshift](#Redshift)
- [12 Analytics](#Analytics)
  - [EMR](#EMR)
  - [Kinesis](#Kinesis)
    - [Kinesis Data Streams](#KinesisDataStreams)
    - [Kinesis Firehose](#KinesisFirehose)
    - [Kinesis Data Analytics](#KinesisDataAnalytics)
  - [Athena](#Athena)
  - [Glue](#Glue)
- [13 Messaging](#Messaging)
  - [SQS](#SQS)
  - [SNS](#SNS)
  - [Step Functions](#StepFunctions)
  - [Event Bridge](#EventBridge)
  - [Simple Workflow](#SWF)
- [14 Deployment](#Deployment)
  - [CloudFormation](#CloudFormation)
  - [Elastic Beanstalk](#ElasticBeanstalk)
  - [SSM Parameter Store](#SSMParameterStore)
  - [AWS Config](#AWSConfig)
  - [Secrets Manager](#SecretsManager)
  - [OpWorks](#OpWorks)
  - [Resource Access Manager](#ResourceAccessManager)
  - [Billing and Cost Management](#Billing)
- [15 Observability](#Observability)
  - [CloudWatch](#CloudWatch)
  - [CloudWatch Alarms](#CloudWatchAlarms)
  - [CloudWatchLogs](#CloudWatchLogs)
  - [CloudTrail](#CloudTrail)
  - [CloudWatch Events](#CloudWatchEvents)
- [16 Security](#Security)
  - [AD](#AD)
  - [Identity Providers](#IdentityProviders)
  - [KMS](#KMS)
  - [HSM](#HSM)
  - [Certificate Manager](#CertificateManager)
  - [WAF](#WAF)
  - [Shield](#Shield)
  - [Cognitio](#Cognitio)
  - [Inspector](#Inspector)
  - [Trusted Advisor](#TrustedAdvisor)
  - [STS = security token service](#STS)
  - [Macie](#Macie)
  - [GuardDuty](#GuardDuty)
- [17 Migration](#Migration)
  - [SMS](#SMS)
  - [DMS](#DMS)
  - [DataSync](#DataSync)
  - [Snowball](#Snowball)
  - [Data Transfer](#DataTransfer)
  - [AppFlow](#AppFlow)
- [18 Reference Architectures](#ReferenceArchitectures)

## IAM <a id="IAM"></a>

IAM is used to securely control individual and group access to AWS resources.

It makes it easy to provide multiple users with access to AWS resources.

And with IAM, you can manage:
- users,
- goups,
- access policies,
- roles
- user credentials
- User password policies
- enable multifactor authentication
- generate API keys for programmatic access to IAM.

By default, all __new users are created with no access to any services__. 
They can only log into AWS, but they can't actually do anything.

Permissions must then be explicitly granted to allow a user to access an AWS service.

IAM users are the individuals who've been granted access to an AWS account.

__IAM is a universal or global service__, so it doesn't apply to specific regions.

__IAM is eventually consistent__.

Authentication methods:
- __console passwords__ for logging into the management console,
- __access keys__ for programmatic access,
- __server certificates__, which can be used for some services as well.

Server certificates and certificate-based authentication:
- provides an authentication experience where you __authenticate once__ and then can access aws resources without re-entering your credentials
- CBA requires a private certificate authority (CA) to create private certificates to identify users.
- Short-lived certificates are used with CBA to reduce the potential impact of a compromised credential.

### IAM Entities <a id="IAMEntities"></a>

__IAM users:__ individuals
- IAM user is an entity that represent a person or a service.
- By default, they cannot access anything in the account.
- The root user credentials are the email address used to create the account, and there's a password associated with that account.
- The __root account has full administrative permissions and they cannot be restricted__.
- IAM users can be created to represent applications, and those are known then as __service accounts__.
- You can have up to 5,000 users per AWS account.
- access:
  - username/password. Use user password policy to enforce strong password
  - access keys id and secret
- add policy (with many permissions)
- __an IAM user can belong to multiple IAM groups__

__IAM groups:__ collection of IAM users (can belong to many groups)
- IAM groups are __collections of users__ and have policies attached to them.
- A group's not an identity in itself, so it can't be identified as a principal in a policy.
- use groups to assign permissions to users.
- Always follow the principal of least privilege when assigning permissions.
- You __can't nest groups__
- __Groups cannot be specified in the policy document__. Only users and roles
- add policy (with many permissions)
- AWS Doesn't Allow Roles on Groups: Groups are simply permission containers, while roles require an assume-role action (sts:AssumeRole), which must be granted to identities (users or services) — not groups.

__IAM Roles:__
- Roles are created and then __assumed by trusted entities__.
  - Trusted Entities are:
    - AWS Services (e.g., EC2, Lambda, etc.)
    - IAM Users
    - IAM Roles (for cross-account access)
    - Federated Users (users authenticated via external identity providers, like AWS Cognito, Google, or Active Directory)
    - Accounts (for cross-account role assumption)
- They are a __way of delegating permissions to resources for users and services__.
- __Users and services can assume a role to obtain temporary security credentials. And those are issued by the Security Token Service, the STS service__.
- you __can share IAM roles between AWS accounts__ using cross-account IAM role assumption. 
- you __cannot directly transfer or share IAM users or groups across AWS accounts__, __you can share IAM permissions__ (through roles and policies) between AWS accounts by using cross-account access.

__IAM Policies__:
- Policies are documents that define the permissions and they can be applied to users, groups, and roles
- Policy documents are written in JSON and include key value pairs that consist of an attribute and a value.
- __All permissions are implicitly denied by default__.
- The __most restrictive__ policy is applied if there's multiple policies with conflicting statements.
  - it gives you tempoarary credentials
  - delegate access to users, applications, services
  - __attach role to aws service__ (EC2: IAM instance profile)
  - __assume role__: allows an IAM entity to temporarly (1 hour) use permissions of IAM role. Use aws console 'switch role'
    - centralized, auditing
    - can access same aws or different aws account (trusted account)
  - __web identity__ : enables secure access to AWS resources using temporary credentials obtained through external identity provider (IDP) - like github
    - uses OAuth 2.0 (authorization) + OpenID Connect (authentication)
    - uses JWT token to access other web services
  - __SAML 2 federation__: similar to web identity but SAML
    - SAML 2.0 (for AD)
    - Allows SSO: one authentication and access to multiple applications
    - uses XML assertions
  - Custom trust policy: you can create a policy thed defines who can assume the role and under what circumstances
    - example: must have MFA, specific email or department, source IP
    - example:  IAM policy that can be assumed by IAM use with MFA
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::YourAccountID:user/YourIAMUser"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
```

### IAM Policies <a id="IAMPolicies"></a>

- __Identity-Based Policies__: Policies attached to IAM identities: Users, Groups, Roles
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["s3:GetObject"],
        "Resource": "arn:aws:s3:::company-data/*"
      }
    ]
  }
  ```
- __Resource-Based Policies__: Policies attached directly to a resource. They define who can access that resource.
  ```
  {
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::111122223333:root"
    },
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::shared-bucket/*"
  }
  ```
- A __Trust Policy__ is a special policy attached to an IAM Role that defines who (which entities) is allowed to assume the role.
  - It only defines who is trusted to take on the role.
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "ec2.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  }
  ``` 
- __permissions boundaries__. These set the maximum permissions that an identity-based policy can grant to an IAM entity. Created by IAM Administrators or Users with Necessary Permissions
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["s3:*"],
        "Resource": "*"
      }
    ]
  }
  ```
- __Service Control Policies__ aka __organizations service__ control policies. These specify the maximum permissions for an organization or an OU. Can be created by AWS Organizations Administrator or  IAM Users/Roles with Explicit Permissions
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Deny",
        "Action": "s3:DeleteBucket",
        "Resource": "*"
      }
    ]
  }
  ```
- __session policies__ that are used with Assume Role API actions. Temporary policies applied during role sessions.

- Customer Managed Policies:
  - created and managed by users, total control on a permission, fine grained
  - contains many permissions
- Inline policy: 
  - direct association to user, group or role, does not have ARN
  - use it when ou have specific job needs, short term project
- Use IAM Policy Similator to check the policy

### IAM best practices

- __lock__ away your account __root user__ access keys,
- create individual users,
- use __groups__ to assign __permissions to users__,
- grant __least privilege__,
- get started using permissions with AWS managed policies,
- Use customer managed policies instead of inline policies.
- Use __access levels to review__ IAM permissions always bearing in mind that least privilege,
- Configure a strong password policy for your users.
- Enable multi-factor authentication.
- Use roles for applications that run on EC2 instances,
- use __roles__ to __delegate permissions__.
- Do not share access keys. Always keep them to yourself and use them only for your accounts.
- __rotate all credentials__ regularly.
- remove any unnecessary credentials.
- use policy conditions for extra security when you're writing your IAM policies.
- monitor activity in your account to see what's actually happening.


__IAM Root user best practices:__
- never use root user for everyday tasks
- only use root to: close aws account, update email /password, restore IAM permissions, configure aws shield, billing, increase service limits, transfet support plans, GovCloud
- enable MFA
- create admin user
- delete or rotate access keys
- secure email address
- create alias (so account name is not visible in url)

Set a custom password policy on your AWS account to specify complexity requirements and mandatory rotation periods for your IAM users' passwords

The IAM password policy does not apply to the AWS account root user password or IAM user access keys

You must configure permissions to allow an IAM entity (user or role) to view or edit their account password policy:
- iam:GetAccountPasswordPolicy
- iam:DeleteAccountPasswordPolicy
- iam:UpdateAccountPasswordPolicy

Example: Read-Only Access to All S3 Buckets
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::*",
        "arn:aws:s3:::*/*"
      ]
    }
  ]
}
```

### IAM Reports <a id="IAMReports"></a>

- IAM Credential Reports: csv files, overview of IAM user __credentials status__ (password rotation, dates, MFA devices, access keys
- IAM Advisor Reports: aws report, __lists services accessible to given user/group/role__
- IAM Access Analyzer: aws report, improve security of your AWS setup by analyzing __resource permissions__, __see resources shared with external identity__ per region
  - see used and unused findings

### Type of Identities <a id="IAMIdentities"></a>

![ Type of Identities ](./images/Identity_types.jpg)

__Corporate Identity Federation__:
- SAML 2.0 (Security Assertion Mark Up Language) to exchange identity and security information between identity provider and application
- AWS IAM Federation – enables users sign-in to their AWS account with existing corporate credentials
- You can configure IAM Federation with SAML 2.0 without using AWS Directory Service. users can authenticate through a third-party IdP (such as Microsoft Active Directory, Google, Okta, etc.)
- Non-SAML options – AWS Directory Service for Microsoft Active Directory
- AWS Organizations – Use AWS Single Sign On (SSO) to scale to multiple AWS Accounts (centrally manage access)

__Cognito Identity Federation__:
- Users can sign-in to mobile and web apps using social identity providers like Facebook, google, amazon
- Support for corporate identity federation using SAML 2.0
- Open Standards Support - Oauth 2.0, SAML 2.0, OpenID Connect
- Map users to roles and limit access to resources

Example of Principal:

| Principal             | Example
|-----------------------|----------------------------------------------------
| AWS account, root user| "Principal”:{"AWS":"arn:aws:iam::123456789012:root"}
|                       | "Principal”:{"AWS":"123456789012"}
| IAM Users             | "Principal":{"AWS":”arn:aws:iam::123456789012:user/alice"}
| IAM Roles             | "Principal":{"AWS":"arn:aws:iam::123456789012:role/cross-acct"}
| AWS Services          | "Principal":{"Service":"elasticmapreduce.amazonaws.com"}
| Anonymous users       | "Principal": “*”
| Federated Users       | "Principal":{"Federated":"www.amazon.com"}
| Assumed-role sessions | Use the role session name to uniquely identify a session
|                       | when the same role is assumed by different principals or for different reasons
|                       | "Principal":{"AWS":"arn:aws:sts::123456789012:assumed-role/role-name/role-session-name"}

Role Based Access Control (RBAC):
- Traditional authorization model used in IAM is called role-based access control. This is based on a person's job-role. [in AWS context, role refers to IAM-role]
- In RBAC model, you implement different policies for different job functions.
- As best policy, you grant the minimum permissions necessary for the job function. this is known as "granting least privilege".
- The disadvantage of RBAC model is that when employees add new resources, you must update policies to allow access to those resources.

Attribute Based Access Control (ABAC):
- ABAC is an authorization strategy that defines permissions based on attributes (also known as Tags)
- Tags can be attached to IAM Principals (users or roles) and to AWS resources
- With ABAC, policies can be designed to allow operations when the principal's tag matches the resource tag.
- ABAC is useful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome
- With ABAC, permissions scale - it is no longer necessary for administrator to update existing policies.
- ABAC requires fewer policies



### Architecture Patterns

#### select group of users only should be allowed to change their IAM password

Create a group for the users and apply a permissions policy that grants the iam:changePassword API permission.

#### an Amazon EC2 instance must be delegated with permissions to an Amazon DynamoDB table.

Create a role, assign a permissions policy to the role that grants access to the DynamoDB database service.

Create IAM Role for EC2: This trust policy allows EC2 to assume the role defined here:
```
// IAM Role for EC2 - meaning EC2 is allowed to assume this role
resource "aws_iam_role" "ec2_dynamodb_role" {
  name = "ec2-dynamodb-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

// IAM Policy for DynamoDB Access
resource "aws_iam_policy" "dynamodb_access_policy" {
  name = "dynamodb-access-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem",
          "dynamodb:Query",
          "dynamodb:Scan"
        ]
        Resource = "arn:aws:dynamodb:us-east-1:123456789012:table/Orders"
      }
    ]
  })
}

// Attach Policy to Role
resource "aws_iam_role_policy_attachment" "attach_policy" {
  role       = aws_iam_role.ec2_dynamodb_role.name
  policy_arn = aws_iam_policy.dynamodb_access_policy.arn
}

// Create the Instance Profile
resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ec2-dynamodb-profile"
  role = aws_iam_role.ec2_role.name
}

// Attach the Instance Profile to an EC2 Instance
resource "aws_instance" "app_server" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t2.micro"

  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name

  tags = {
    Name = "AppServer"
  }
}
```

for lambda:
```
// Create the IAM Role (Lambda Trust Policy)
resource "aws_iam_role" "lambda_role" {
  name = "lambda-dynamodb-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

// Attach a Policy to the Role (DynamoDB Access)
resource "aws_iam_policy" "lambda_dynamodb_policy" {
  name = "lambda-dynamodb-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem",
          "dynamodb:Query",
          "dynamodb:Scan"
        ]
        Resource = "arn:aws:dynamodb:us-east-1:123456789012:table/Orders"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_lambda_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.lambda_dynamodb_policy.arn
}

// Create the Lambda Function, Attach the role directly to the Lambda function:
resource "aws_lambda_function" "my_lambda" {
  function_name = "my-dynamodb-lambda"
  role          = aws_iam_role.lambda_role.arn
  handler       = "index.handler"
  runtime       = "python3.9"

  filename = "lambda_function.zip"  # Your packaged code

  environment {
    variables = {
      TABLE_NAME = "Orders"
    }
  }
}
```


#### A company has created their first AWS account. They need to assign permissions to users based on job function.

Use the AWS managed policies. And those can be aligned with specific common job functions.

#### A solutions architect needs to restrict access to an AWS service based on the source IP address of the requester.

You can create an IAM permissions policy and use the condition element to control access based on source IP address.

#### A developer needs to make programmatic API calls from the AWS CLI.

In this case, you can instruct the developer to create a set of access keys and use those for any programmatic access.

#### A group of users require full access to all Amazon EC2 API actions.

Create a permissions policy that uses a wildcard for the action element relating to EC2. And that would look like the (ec2:*) action.

```
resource "aws_iam_group" "ec2_full_access_group" {
  name = "ec2-full-access-group"
}
resource "aws_iam_group_policy_attachment" "ec2_full_access_attach" {
  group      = aws_iam_group.ec2_full_access_group.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2FullAccess"
}
resource "aws_iam_user" "user1" {
  name = "user1"
}
resource "aws_iam_user_group_membership" "user1_membership" {
  user   = aws_iam_user.user1.name
  groups = [aws_iam_group.ec2_full_access_group.name]
}
```

#### You would like to revoke programmatic access for an IAM user. What steps do you need to take?

Remove access key credentials

#### You would like to version control your policy changes in IAM so that you have ability to rollback changes. What features can you use to automatically track versions?

Managed Policies are automatically version controlled and maintain previous five versions

#### Can an IAM user belong to more than one IAM Group?

Yes

#### A startup has multiple AWS accounts. Employees play different job-roles and require appropriate access in each account. For example, they have limited privileges in the production account, whereas, in the development account, they have a wide range of privileges. What can be done to streamline access to accounts?

The best option is to use AWS organizations to consolidate all accounts under a master account. 
You can enable single sign-on to manage cross-account access. 
IAM role is the second-best option; however, you need to configure and manage roles manually.

- Centralize identity: Use: IAM Identity Center (recommended) Employees: Log in once
- Use roles per account
  - Create roles like: DevAdminRole (broad access), ProdReadOnlyRole (restricted access)
  - Each role has: Different permissions depending on the account
- Assign roles to users/groups

#### A systems administrator is creating IAM policies and attaching them to IAM identities. After creating the necessary identity-based policies, the administrator is now creating resource-based policies. Which is the only resource-based policy that the IAM service supports?

You manage access in AWS by creating policies and attaching them to IAM identities (users, groups of users, or roles) or AWS resources. A policy is an object in AWS that, when associated with an identity or resource, defines their permissions. Resource-based policies are JSON policy documents that you attach to a resource such as an Amazon S3 bucket. These policies grant the specified principal permission to perform specific actions on that resource and define under what conditions this applies.

Trust policy

Trust policies define which principal entities (accounts, users, roles, and federated users) can assume the role. An IAM role is both an identity and a resource that supports resource-based policies. For this reason, you must attach both a trust policy and an identity-based policy to an IAM role. The IAM service supports only one type of resource-based policy called a role trust policy, which is attached to an IAM role.

#### What is a trust policy? How does it differ from an identity-based policy?

Trust policy: JSON policy attached to an IAM role that defines who can assume the role (principal + sts:AssumeRole).

Identity-based policy: Grants permissions to perform actions after assuming the role.

#### How does AWS evaluate permissions when multiple policies apply (identity-based, resource-based, SCP, boundary, session policy)?

```
Start with all identity-based policies attached to the user or role.
Apply resource-based policies.
Apply permissions boundaries (limits maximum permissions).
Apply SCPs if account is in AWS Organizations.
Apply session policies if using STS temporary credentials.
Explicit Deny overrides everything.
If no explicit allow → access denied by default.
```

#### You have Account A and Account B. You want a user in Account B to access an S3 bucket in Account A. How would you configure this securely?

- Create IAM role in Account A with a trust policy allowing Account B user/group to assume it.
- Attach identity-based policy to the role granting S3 bucket access.
- User in Account B uses STS AssumeRole to assume the role in Account A.

#### What is a permissions boundary? Give a scenario where it’s useful.

Permissions boundary = maximum allowed permissions for an IAM user or role.
It does not grant permissions, it limits them.







## Amazon Elastic Compute Cloud (EC2) <a id="EC2"></a>

__AWS Region__ (36) consists of 2 or more availability zones.

__Availability zone__ = one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region, physically separated by a meaningful distance, 

__Local Zone__ (30+) = data center outside of a region. Its purpose is to run full applicatins closer to users. Supports: EC2, EDB, ECS, EKS, RDS etc.

__Wavelength__: mobile only apps accessing via 5G

__AWS Outpost__: aws hardware installed on private cound that can be managed via aws console

__Edge location__ (400+) = used primarily by Amazon CloudFront but also by AWS Global Accelerator, AWS Shield, and Route 53
- AWS has hundreds of edge locations around the world
- A smaller data center that caches data closer to users, used mainly for content delivery and DNS resolution
- used specifically to deliver content and services with low latency to end users.
- CDN = CloudFront = content from server hosted in internet service provider
- By caching your content in Edge Locations, Amazon CloudFront reduces the load on your Amazon S3 bucket and helps ensure a faster response for your users when they request content. Also, data transfer out for content by using CloudFront is often more cost-effective than serving files directly from Amazon S3, and there is no data transfer fee from Amazon S3 to CloudFront. __You only pay for what is delivered to the internet from Amazon CloudFront, plus request fees__.

__Regional Edge Cache__ = cache content from Origin so Edge location can get it faster

With EC2, you launch virtual server instances on the AWS cloud.

Each virtual server is known as an instance.

With EC2, you get full control at the operating system layer.

Key pairs are then used to securely connect to EC2 instances.

The storage is either Amazon EBS, which is persistent storage, or Instance Store, which is non-persistent storage.

Benefits of Amazon EC2 include:
- __elastic computing__. You can easily launch hundreds to thousands of EC2 instances within minutes.
- You get __complete control__ with full root and administrative access.
- __Flexible__: a choice of instance types, operating system, software packages, the type of storage you're adding, and so on and so forth.
- __Reliable__: EC2 offers very high levels of availability. And instances can be rapidly commissioned and replace where needed.
- __Secure__ It's fully integrated with Amazon VPC and the security features of AWS.
- __Inexpensive__, so it can be very low cost and you only pay for what you use.

Steps to login to your ec2:
- Prerequisites:
  - Key pair (.pem file): You must have the private key (.pem) file that corresponds to the key pair specified when launching the EC2 instance.
  - Security group: Ensure the EC2 instance's security group allows inbound SSH traffic (port 22).
  - Public IP or Elastic IP: Your EC2 instance must have a public IP or Elastic IP if you're connecting from outside AWS.
- Copy the Public IPv4 address from ec2 console
- ssh -i /path/to/your-key.pem ec2-user@<Public-IP-or-DNS>

The default SSH username depends on the OS of the base AMI:
| AMI OS       | Default Username
|--------------|------
| Amazon Linux | ec2-user
| Ubuntu       | ubuntu
| RHEL         | ec2-user or root
| CentOS       | centos
| Debian       | admin or debian
| SUSE         | ec2-user

__Storage__:
- Block
  - Instance Storage: __directly connected storage__ attached to physical host
    - some EC2 types do not support any instance storage (t2micro) or Windows does not support it.
    - price included
  - EBS: __external physical storage__, must be in the same AZ
- File
  - EFS (Unix)
  - FSx (Windows)
- Object (S3)

__EC2 instance endpoint__
- network endpoint that allows communication with an EC2 instance
  - public: This is the instance’s public IP address, which can be used to communicate with the instance over the internet.
  - private: allows communication between EC2 instances within the same VPC or across VPCs using VPC peering
- uses aws username and password
- easy to connect from aws console

### Instance metadata <a id="InstanceMetadata"></a>

__Instance metadata__ is the data about your instance that you can use to configure or manage the running instance. Instance metadata is available at this URL: http://169.254.169.254/latest/meta-data

Example Instance metadata response:
```
curl http://169.254.169.254/latest/meta-data

ami-id
ami-launch-index
ami-manifest-path
instance-id
instance-type
local-ipv4
mac
network/
placement/
profile/
public-ipv4
public-hostname
security-groups

curl http://169.254.169.254/latest/meta-data/instance-id

i-0abcd1234efgh5678
```

### User data <a id="UserData"></a>

__User data__ is data that gets supplied in the form of a script and that runs at system startup. Instance user data is available at this URL: http://169.254.169.254/latest/user-data

User Data is generally used to perform common automated configuration tasks and even __run scripts after the instance starts__. When you launch an instance in Amazon EC2, you can pass two types of user data - shell scripts and cloud-init directives. You can also pass this data into the launch wizard as plain text or as a file.

Scripts entered as __user data__ are executed as the__ root user__, __hence do not need the sudo command in the script__. Any files you create will be owned by root; if you need non-root users to have file access, you should modify the permissions accordingly in the script.

By default, user data scripts and cloud-init directives __run only during the boot cycle when you first launch an instance__. __You can update your configuration to ensure that your user data scripts and cloud-init directives run every time you restart your instance__.

Example User data response:
```
curl http://169.254.169.254/latest/user-data

#!/bin/bash
yum update -y
yum install -y httpd
service httpd start
chkconfig httpd on
```

### AMI <a id="AMI"></a>

An Amazon Machine Image provides the __information required to launch an instance__.

If you create custom AMI then to use it and create new EC2 from it, you need to change the administrator password. Else you will not be able to login to this new EC2.

AMI includes:
- a __template__ for the root volume of the instance,
- __launch permissions__
- a __block device mapping__, which specifies which volume is to attach to the instance.

__AMIs are regional__, so you can only launch an AMI from the region in which it is created.

You can __copy AMIs to other regions__ using the console command line or the API.

AMIs categories:
- community AMIs,
- marketplace AMIs,
- your AMIs, the ones you create yourself.

Steps to create a custom aws AMI:
- Launch an EC2 instance using an existing Amazon-provided AMI
- Install and configure the software, updates, and system settings you want to include in your custom AMI.
- Stop Services (Optional, for consistency): To ensure the disk is in a consistent state, you can stop critical services or the instance itself, though AWS handles this well with modern AMIs.
- Create Image
```
aws ec2 create-image \
    --instance-id i-1234567890abcdef0 \
    --name "MyCustomAMI" \
    --description "AMI with custom software" \
    --no-reboot
```

### Instance types <a id="InstanceTypes"></a>
![ Instance Types ](./images/ec2_instance_types.png)

Burstable T-type instances:
- Low to Moderate CPU utilization with occasional increase
- Burstable Instance - CPU
  - Baseline CPU Performance [5-40%]
  - Instance earns a CPU Credit when usage is less than baseline
  - Performance can burst up to 100% using CPU credits
  - CPU is throttled to baseline performance
- Unlimited Mode [Burstable Instance]
  - no need to worry about throttling
  - Pay for excess capacity consumed

I n s t a n c e _t y p e. g e n e r a t i o n.s i z e

c 5 . 2 x l a r g e = Compute Optimized, 5th generation, 2xlarge (8 vCPUs, 16 GB Memory

Resize instances:
- same type
- .small -> .2xlarge
- Stop-Change-Start
- Check compatibility [OS, Storage, etc.]

Process:
- Map app to instance family
- Pick an appropriate size [small, large, 2xlarge and so forth]
- Run performance tests to right-size

### IP addresses <a id="IP"></a>

public IP address:
- lost when you stop your instance
- used in public subnets
- no charge
- associated with private IP of the instance
- cannot be moved between instances

private IP address:
- retained when the instance is stopped
- Used in public and private subnets

elastic IP address:
- static public IP address,
- charged if not used
- associated with private IP address on the instance
- can move around between instances

### How to Log in to Private instance <a id="LoginToEC2"></a>

1. __Bastion Host__:
- For HA, reassign Elastic IP to new Bastion Host instance
- Client can use existing Elastic IP to connect to new instance
- Issues: extra servers to manage

2. __Systems Manager - Session Manager__:
- Automated patching of servers and Automation of routine administrative tasks
- interactive remote shell for Linux and Windows, macOS
- Agent required: AWS preinstalls in many instances
- Simpler and Safer when compared to Bastion Host
- Close SSH and RDP ports in Security Group
- you can use AWS Systems Manager to __SSH into an EC2 instance without needing to open inbound SSH ports__ (like port 22) on the EC2 instance:
  - EC2 Instance: Your EC2 instance should be running a supported operating system (Linux or Windows).
  - IAM Role: The EC2 instance must be associated with an IAM role that has the necessary SSM permissions.
  - SSM Agent: The SSM Agent must be installed and running on the EC2 instance. Most Amazon Linux 2, Ubuntu, and Windows AMIs have the SSM Agent pre-installed. If you're using custom AMIs, you need to ensure the agent is installed.
  - VPC Configuration: If the EC2 instance is in a private subnet (without a public IP), it should be able to connect to the Systems Manager endpoint. You need to ensure that your EC2 instance can reach the SSM endpoints either via the internet (if your instance has a NAT gateway or public IP) or via a VPC endpoint for Systems Manager.
  - AWS Systems Manager (SSM) offers a Session Manager feature that __allows you to SSH into your private EC2 instances without needing an SSH key__ or direct network access.
- You don’t need a VPN, bastion host, or open SSH ports on the EC2 instance.
- Requirements on your laptop
  - Install AWS CLI (v2 recommended).
  - Install Session Manager plugin for AWS CLI.

3. __VPN or Direct Connect__
- Set Up a VPN Connection: Establish a VPN connection between your on-premises network and your AWS VPC
- Connect to the VPC: your local network will be able to reach the private IP of the EC2 instance within the VPC
- SSH or RDP: From your local machine (now part of the VPN), you can SSH into your EC2 instance

4. __VPC Peering__
- Set up VPC Peering between two VPCs.
- Update route tables in both VPCs to allow routing between them.
- Update Security Groups to allow access to EC2 instances across VPCs.
- SSH to EC2 Instance using its private IP from another EC2 instance in the peered VPC.

### Block Storage for EC2 <a id="BlockStorage"></a>

#### Instance Store

- Highest Performance
- IOPS depends on the instance type and the type:
  - i3.large: 70,000 IOPS
  - i3.16xlarge: 1,000,000 IOPS
  - d2, h1: 3,000 IOPS
- Data persists only for the lifetime of the instance
- Reboot – Data Persists
- Data is lost – when underlying hardware fails, instance stops, or instance terminates
- __Random I/O Workload__ – SSD Preferred. Performance Measured in __IOPS__
- __Sequential I/O Workload__ – Magnetic/HDD Preferred. Performance Measured in __Throughput (MiB/s)__

#### EBS - see 'File Share' section

### Placement groups <a id="PlacementGroups"></a>

- __Cluster placement group__ is designed to keep instances very close for low latency. Think about high performance computing, tightly coupled applications where you've got node to node communication
- __Partition__ will spread your instances across logical partitions so that the groups in one partition don't share the same underlying hardware with other groups of instances. So you can use this for high availability. It's usually used with distributed and replicated workloads. For example, Hadoop, Cassandra and Kafka.
  - When you create a Partition Placement Group, you define the number of partitions. AWS will then ensure that your instances are distributed across the given number of partitions.
  - Each partition is placed on different racks (separate power, networking).
- __Spread placement group__: This will place a small group of instances across distinct underlying hardware to reduce any kind of correlated failures.
  - Each partition is placed on different racks (separate power, networking).

### NAT <a id="NAT"></a>

NAT Gateway = special agent with publicIP that connects to InternetGateway
- __create NAT gateway in each public subnet__
- __define public IP__
- add entry to main route table to NAT Gateway

NAT instances versus NAT gateways:
- The __NAT instance__ is fully managed by you. It's really the old way of doing things.
  - NAT instance can be used as a bastion server
  - Security Groups can be associated with a NAT instance
  - NAT instance supports port forwarding
- __NAT gateway__ is likely to be the best solution in most use cases.    
  - It's fully managed by AWS.
  - You get more scalability over NAT gateway.
  - The only real limitations of the NAT gateway are things like you can't use it as a bastion host, but you should probably separate that into a different instance anyway.
  - There are also __no security groups with a NAT gateway__, whereas there are with a NAT instance.
  - __NAT gateway is deployed inside a subnet with a route from the private subnet and it can scale only inside that subnet in specific AZ__. 
  - For fault tolerance, __it is recommended that you deploy one NAT gateway per availability zone__


### EC2 instance lifecycle <a id="Ec2_lifecycle"></a>

- __Stopping__:
  - Stopping instances works only for EBS-backed instances,
  - no charge for a stopped instance.
  - There is a charge for any EBS volumes in terms of the amount of data that's stored.
  - Data in RAM is lost
  - the instance is migrated to a different host when you start it again.
  - Private IPv4 and IPv6 addresses are retained, public addresses are lost.
  - Any associated elastic IP will, of course, be retained.
- __Hibernation__ applies to on-demand or reserved Linux instances.
  - The contents of RAM get saved to an EBS volume, has to be enabled for hibernation when launched, and specific prerequisites do apply.
  - When you start an instance after hibernation, the root volume is restored to its previous state.
  - The RAM contents are then reloaded and the processes that were previously running on the instance get resumed.
  - Any previously attached volumes are re-attached and the instance retains its instance ID.
  - when you hibernate an EC2 instance, the public IP is typically released, and you will lose it.
- __Rebooting__
  - instances, this is the equivalent to an operating system reboot.
  - The DNS name and IP address gets retained.
  - It doesn't affect billing at all because the instance is still running and it hasn't stopped and started, so it's not a new billing lifecycle.
  - instance storage (also known as ephemeral storage) is lost when you reboot an EC2 instance
- AWS may sometimes __retire__ instances:
  - if there's some irreparable failure of the underlying hardware,
  - when an instance reaches its scheduled retirement date
  - it might be stopped or terminated by AWS. Of course, they'll notify you if that happens.
- __Terminating__ EC2 instances:
  - means deleting the instance.
  - And you can't recover a terminated instance.
  - By default, the root EBS volumes are deleted,
  - Terminated instances cannot be recovered
- __Recovering__ instances:
  - this is where CloudWatch is monitoring the system status and you can recover the instance if required.
  - It applies if the instance becomes impaired due to underlying hardware or platform issues.
  - A recovered instance is __identical to the original instance__ including the __instance ID, private IP addresses, Elastic IP addresses, and all instance metadata__. 
  - If your instance has a public IPv4 address, it __retains the public IPv4 address after recovery__
  - If the impaired instance is in a __placement group__, the recovered instance runs in the placement group.
  - You can create an __Amazon CloudWatch alarm__ to automatically recover the Amazon EC2 instance if it becomes impaired due to an underlying hardware failure
  - data that is in-memory is lost.

You can modify the following attributes of an instance only when it is stopped:
- Instance type.
- User data.
- Kernel.
- RAM disk

You cannot change the instance generation or instance size of an EC2 instance without stopping it.

### Nitro <a id="Nitro"></a>

The __Nitro__ system:
- is the underlying platform for the __newer generation EC2 instances__.
- __Breaks logical functions into specialized hardware__ with a hypervisor.
- The hardware includes the Nitro cards for VPC, EBS, Instance Storage, a card controller, a security chip, and the hypervisor itself.
- Nitro aims to improve performance, security, and innovation.
- The __performance is close to bare metal__, even for virtualized instances.
- It gives you the ENA and the EFA.
  - ENA (Elastic Network Adapter) allows: 200 Gbps / network card etc.
    - To enable EFA: In the Network Interface section of the EC2 launch wizard, you will see an option to enable Elastic Fabric Adapter under the Elastic Network Adapter (ENA) options.
  - EFA (Elastic Fabric Adapter): lower and more consistent latency and higher throughput than the TCP transport traditionally used in cloud-based HPC systems
- You have more available bare metal instance types you can use, and it gives you higher network performance.
- It's also good for HPC because there's more optimizations for high performance computing.
- It can also have dense storage instances as well.
- To create a Nitro-based EC2 instance, you need to use an instance type that is powered by the AWS Nitro System:  It is used by modern EC2 instances such as M5, M5a, C5, C5a, R5, R5a, and others.
- When creating EC2 choose an Instance type that is Nitro-based. For example: M5 (General Purpose), C5 (Compute Optimized), R5 (Memory Optimized)

__Nitro enclaves__:
- are __isolated compute environments__ that run on hardened virtual machines.
- __no persistent storage, interactive access, or external networking__,
- uses cryptographic attestation to ensure only the authorized code is running
- integrates with KMS.
- __good for securing and protecting highly sensitive data like PII__, health care data, financial data, or intellectual property data.

### EC2 pricing <a id="Ec2_pricing"></a>

EC2 pricing options:
- __on-demand__, which is the standard rate, there's no discount, there's no commitment. It's very good for any kind of short-term requirements or unpredictable workloads.
- __reserved__ one or three year commitment, but you get a good discount.
  - Provides a capacity reservation when used in a __specific AZ__,
  - __Can switch AZ within the same region__
  - Can change the instance size within the __same instance type__
- __spot__ instances, you get a very low price because you're essentially using unused capacity. So you can get a large discount, but you can also be terminated at any time.
- __Dedicated instances__ offer physical isolation at the host hardware level from instances belonging to other customers. And you pay per instance. __Hardware dedicated to you__ (account), but you don’t control the physical server.
- __Dedicated host__ is physical servers dedicated for your use, so you get the actual hardware dedicated for you. There's no sharing going on there. You control what EC2 instances run on it
  - visibility into and control over the host (e.g. __sockets, cores__, instance distribution).
  - required for bring-your-own-license (__BYOL__) scenarios
  - You __pay per host__, not per instance.
- __savings plans__ where you can commit to a certain amount of usage for various compute services. You have a one or three-year commitment.
  - With Compute Savings Plan, you can get a __significant discount (up to 66%)__ on any compute services such as __EC2, Lambda, and Fargate__ Containers.
  - So, the compute savings plan applies to both __server-based and serverless computing__. 
  - __Reservation applies only to EC2 instances and does not cover serverless usage.__

If a __spot__ request is persistent, then it is opened again after your Spot Instance is interrupted. A Spot Instance request is either one-time or persistent. If the spot request is persistent, the request is opened again after your Spot Instance is interrupted. If the request is persistent and you stop your Spot Instance, the request only opens after you start your Spot Instance.

__Spot Fleets__ can maintain target capacity by launching replacement instances after Spot Instances in the fleet are terminated

- When you cancel an active spot request, it does not terminate the associated instance. If your Spot Instance request is active and has an associated running Spot Instance, or your Spot Instance request is disabled and has an associated stopped Spot Instance, canceling the request does not terminate the instance; you must terminate the running Spot Instance manually. Moreover, to cancel a persistent Spot request and terminate its Spot Instances, you must cancel the Spot request first and then terminate the Spot Instances.

__Dedicated Instances__ are Amazon EC2 instances that run in a virtual private cloud (VPC) on hardware that's dedicated to a single customer. Dedicated Instances that belong to different AWS accounts are physically isolated at a hardware level, even if those accounts are linked to a single-payer account. However, __Dedicated Instances may share hardware with other instances from the same AWS account that are not Dedicated Instances__.

A __Dedicated Host__ is also a physical server that's dedicated for your use. With a Dedicated Host, you have visibility and __control over how instances are placed on the server__.


### Architecture Patterns

#### A company needs to run a short batch script to configure Amazon EC2 Linux instances after they are launched.

Add the bash script to the user data of the EC2 instances, and then it will run as they boot up, as they launch for the first time.

#### A tightly coupled HPC workload, high performance computing requires low latency between nodes and optimum network performance.

Launch the EC2 instances in a single AZ in a cluster placement group and use an Elastic Fabric Adapter.
And that's a standard pattern for this type of workload that needs very low latency communications between nodes.

#### A line of business application receives weekly bursts of traffic and must scale for short periods, and you need the most cost-effective solution.

Use reserved instances for the minimum required workloads, so that's going to give you a big discount from the standard rates.
And then you can use spot instances for the occasional bursts in traffic because you know those are short-lived. And that means that you can get some cost savings there as well.

#### A single instance application uses a static public IP address. In the event of failure, the address must be remapped to a fail over instance.

Attach an elastic IP address to the instance, and you can remap the IP address in the event of a failure.
And that can be done programmatically, so you might have some kind of automated way of deploying that.

#### A fleet of Amazon EC2 instances run in private subnets across multiple AZs. A company needs a redundant path to the internet.

Use NAT gateways so that your instances in the private subnets have internet access. And you can put them into multiple AZs so you've got that high availability because it does ask for redundancy here. And then you need to update the route tables to point them to the NAT gateway.

#### A team of engineers must administer EC2 instances in private subnets from remote locations using SSH,

Deploy a bastion host to jump to the instances in private subnets.

#### You need to allow remote SSH login to the private EC2 instances from the on-premises network. All requests are sent over the internet

Using the Session Manager (part of the system manager service), authorized employees can log in to their EC2 instances using IAM credentials.
Session Manager does not use SSH or RDP ports

#### An application uses several EC2 instances, the architect must eliminate the risk of correlated hardware failures.

Launch the instances in a spread placement group across distinct underlying hardware.
This means that each of the instances in the application is essentially in a separate rack of servers in the AWS data center with separate power supplies and so on.

#### An application requires enhanced networking capabilities.

Choose an instance type that supports enhanced networking. And you need to ensure that the ENA module is installed and ENA support is enabled.

#### An instance needs close to bare metal performance, EFA, the Elastic Fabric Adapter, and high performance networking

Use an AWS Nitro instance type

#### You are using T2 burstable EC2 instances. You are seeing a sustained load on your application running on these instances. What would be the behavior you would observe?

Burstable instances continuously accumulate CPU credits if usage is below baseline performance.

When there is increased load, it can use the available CPU credits to temporarily boost the performance to fully utilize available CPU capacity.

However, when instances are out of CPU credits, it will fall back to baseline performance and applications may get throttled.

To prevent this situation, you can enable the new “unlimited” mode in burstable types and you will simply be billed an additional hourly charge based on extra CPU capacity consumed

####  You have a fleet of hundreds of EC2 instances. If there are problems with AWS managed items like Physical host, network connectivity to host, and system power, how would you be able to track it?   

System status check would identify AWS infrastructure related issues. Instance status check would also fail if a system status check fails. So, either one can be used

AWS performs two types of status checks for each EC2 instance:
- System status check:	Underlying hardware, network, power, hypervisor, AWS infrastructure issues
- Instance status check: Software and OS on your instance (boot issues, stuck processes, networking)

How to view status checks:
- ec2 console
- AWS CLI
- CloudWatch: EC2 system and instance status checks emit CloudWatch metrics automatically

#### You need to allow remote SSH login to the private EC2 instances from the on-premises network.

Using the Session Manager (part of the system manager service), authorized employees can log in to their EC2 instances using IAM credentials. 
Session Manager does not use SSH or RDP ports. 
Bastion Host is another option – however, this requires additional servers, and you need to keep the SSH port open
- Configure a bastion host within your VPC that can be accessed from your on-premises network, then use that bastion host to connect to the private EC2 instances via SSH
- AWS Session Manager allows remote SSH login to private EC2 instances from an on-premises network, as it establishes a secure tunnel through the AWS infrastructure without requiring any open inbound ports on the EC2 instance or a public IP address, making it ideal for accessing private instances within a VPC; you only need the SSM Agent installed on the EC2 instance and appropriate IAM permissions to connect

Most modern Amazon Linux, Amazon Linux 2, and Ubuntu AWS AMIs have SSM Agent pre-installed.
If not use user-data.

#### When you recover an EC2 instance using CloudWatch Alarm, what happens to the instance?

When an instance is recovered using CloudWatch Alarm Action, a recovered instance is identical to the original instance, including its: Instance ID Public, private, and Elastic IP addresses Instance metadata Placement group Attached EBS volumes Availability Zone

#### Your requirement specifies a single volume with 50 TiB of storage. Which of the following options fulfills this requirement?

Io2 Block Express is the next generation storage solution, delivering unparalleled block storage performance and supporting storage capacities of up to 64 TiB. 
In contrast, all other EBS volume choices are limited to a maximum storage capacity of 16 TiB. 
Historically, when extra storage was required, organizations often relied on attaching multiple EBS volumes to their EC2 instances. Alternatively, configurations like RAID 0 could be employed to combine multiple EBS volumes into a cohesive logical volume.

#### Your security team follows the principle of immutable instances. With this approach, the servers are never patched; instead, the existing servers are replaced with new servers with correct software patches. To speed up the deployment, the security team periodically releases new AMI with all the security patches for known vulnerabilities. The infrastructure is managed using Auto Scaling. How would you replace existing vulnerable instances?

Create a new version of the launch template to use the new AMI, update Auto Scaling Group to use this new version of the template, and then refresh instances

The launch template is immutable, and you need to create a new version with the correct AMI and then configure Auto Scaling Group to use this new version of the launch template. With instance refresh, you can perform a rolling replacement of instances.

#### How does Auto scaling handle spot interruptions?

Auto Scaling automatically handles spot interruptions, deregisters the instance from the load balancer, and initiates steps to launch a replacement instance

In addition, EC2 service publishes a capacity-rebalance early warning event when a spot pool is likely to get interrupted. 
In this case, Auto Scaling can take proactive action to launch a new replacement instance from another spot pool with less likelihood of interruption

#### As part of application configuration step in an EC2 instance, the configuration script needs user data specified when launching the EC2 instance.  What mechanism can the script use to get this data?

Use Metadata query service http://169.254.169.254/latest/user-data

#### An application requires 100 GB of persistent volume storage. The application is expected to perform 600 IOPS. Which of these options meet the requirements cost-effectively?

General Purpose Volume with 200 GB of storage

General purpose volume offers a baseline performance of 3 IOPS per GB. With 200 GB of storage, the baseline performance is 600 IOPS,

Instance store SSD is not the right choice as the question asks for a persistent storage

#### Can I use default password to login to EC2 created from custom AWS AMI ubuntu?

No: you cannot use a default password to log into an EC2 instance launched from a custom AWS AMI based on Ubuntu. 
The default Ubuntu AMI and other custom AMIs typically use SSH key-based authentication for login, not passwords

#### What is aws launch template instance tenancy?

In AWS Launch Templates, the Instance Tenancy setting controls how your EC2 instances are hosted — specifically, whether they run on shared or dedicated hardware.
- default Run on shared hardware alongside instances from other customers (cheapest)
- dedicated Run on dedicated hardware — a physical server fully isolated for your use
- host Use a specific Dedicated Host, giving you control over instance placement (BYOL, compliance)

When you create a Launch Template, the default value for the instance tenancy is shared and the instance tenancy is controlled by the tenancy attribute of the VPC. 
If you set the Launch Template Tenancy to shared (default) and the VPC Tenancy is set to dedicated, then the instances have dedicated tenancy. 
If you set the Launch Template Tenancy to dedicated and the VPC Tenancy is set to default, then again the instances have dedicated tenancy.

#### The engineering team has been seeing recurrent issues wherein the in-flight requests from the ELB to the Amazon EC2 instances are getting dropped when an instance becomes unhealthy. Which of the following features can be used to address this issue?

Connection Draining

To ensure that Elastic Load Balancing stops sending requests to instances that are de-registering or unhealthy while keeping the existing connections open, use connection draining. 
This enables the load balancer to complete in-flight requests made to instances that are de-registering or unhealthy. 
The maximum timeout value can be set between 1 and 3,600 seconds (the default is 300 seconds). 
When the maximum time limit is reached, the load balancer forcibly closes connections to the de-registering instance

#### A medium-sized business has a taxi dispatch application deployed on an Amazon EC2 instance. Because of an unknown bug, the application causes the instance to freeze regularly. Then, the instance has to be manually restarted via the AWS management console. Which of the following is the MOST cost-optimal and resource-efficient way to implement an automated solution until a permanent fix is delivered by the development team?

Setup an Amazon CloudWatch alarm to monitor the health status of the instance. 
In case of an Instance Health Check failure, an EC2 Reboot CloudWatch Alarm Action can be used to reboot the instance

Using Amazon CloudWatch alarm actions, you can create alarms that automatically stop, terminate, reboot, or recover your Amazon EC2 instances. 
You can use the stop or terminate actions to help you save money when you no longer need an instance to be running. 
You can use the reboot and recover actions to automatically reboot those instances or recover them onto new hardware if a system impairment occurs.

You can create an Amazon CloudWatch alarm that monitors an Amazon EC2 instance and automatically reboots the instance. 
The reboot alarm action is recommended for Instance Health Check failures (as opposed to the recover alarm action, which is suited for System Health Check failures).

#### Explain the difference between stopping and terminating an EC2 instance. What happens to the EBS volumes in each case?

| Action    | Instance State | EBS Root Volume                                 | EBS Data Volumes                                             |
| --------- | -------------- | ----------------------------------------------- | ------------------------------------------------------------ |
| Stop      | Stopped        | Persisted (unless `DeleteOnTermination=true`)   | Persisted                                                    |
| Terminate | Terminated     | Deleted by default (`DeleteOnTermination=true`) | Persisted or deleted depending on `DeleteOnTermination` flag |

- Stopping → instance can be restarted later (private IP changes unless using Elastic IP).
- Termination → instance is permanently removed.
- Only EBS-backed instances can be stopped. Instance-store-backed instances cannot be stopped; they are lost on shutdown.
- once an EC2 instance is terminated, you cannot recover it.







## Elastic Load Balancing and Auto Scaling <a id="AutoScaling"></a>

Scaling types:

| Scaling    | Type Description
|------------|------------------------
| Maintain   | Maintain a constant fleet size
| Scheduled  | Time based – add, remove
| Dynamic    | Metrics based – respond to changes to traffic
| Predictive | Machine Learning based – adjust based on predicted traffic

Services with Auto Scaling Support:
- __EC2__ – Adjust EC2 instance capacity based on need
- __EC2 Spot Fleets__ – optimize cost, replace instances that are interrupted due to price or capacity reasons
- __Elastic Container Service__ – adjust tasks based on load, adjust instances in the cluster
- __DynamoDB__ – Adjust provisioned read and write capacity
- __Aurora__ – Adjust the number of read-replicas based on workload

The __Spot Fleet__ selects the Spot Instance pools that meet your needs and launches Spot Instances to meet the target capacity for the fleet. By default, Spot Fleets are set to maintain target capacity by launching replacement instances after Spot Instances in the fleet are terminated.

A __Spot Instance__ is an unused Amazon EC2 instance that is available for less than the On-Demand price. Spot Instances provide great cost efficiency, but we need to select an instance type in advance. In this case, we want to use the most cost-optimal option and leave the selection of the cheapest spot instance to a Spot Fleet request, which can be optimized with the lowestPrice strategy. 

Scaling Policies:
- Dynamic
  - Target tracking
    - Specify a scaling metric and target utilization
    - AWS creates alarm and adjusts server count to maintain target utilization
  - Step scaling
    - You need to create alarm and specify what action to take at each step
  - Simple scaling
    - You need to create alarm and specify what action to take
    - After every scaling action, policy pauses for cooldown period to expire before taking another scaling action
- Maintain
- Scheduled

### Auto Scaling Group <a id="AutoScalingGroup"></a> = to scale EC2
- Auto Scaling __launches and terminates EC2 instance__ is automatically.
- __Scaling is horizontal__, it scales out.
- It provides elasticity and scalability
- __Responds to EC2 status checks and CloudWatch metrics__.
- You can __scale based on demand, performance or on a schedule__.
- __Scaling policies__ will define how to respond to changes in-demand.
- Auto Scaling groups define collections of EC2 instances that are scaled and managed together.
- __auto-scaling group__: allows to manage collection of EC2 as a single unit. Defines VPC and subnet, health check, capacity, max, min, scaling policiies:
  - manual
  - scheduled scaling: runs scaling policy. When you create a scheduled scaling policy, you can define:
    - Start Time (StartTime): The time the action begins.
    - End Time (EndTime): (Optional) The time the action should stop being valid.
  - dynamic scaling: define parameters that control rge auto-scaling process (uncertain workload). __Uses CloudWatch Alarm__
    - simple: single threashold (add 1 ec2 when cpu utilization>50%)
    - step: multiple threasholds
      - Step Scaling uses CloudWatch alarms with scaling steps.
      - different scaling actions depending on how far the metric crosses a threshold:
        - > 60% add 1 instance
        - > 75% add 2 instances
    - target tracking: use metric type (cpu utilization, network bytes out or request count per target) to automatically add capacity. Set __instance warup time__
  - predictive scaling: based on predicted traffic (needs 3 weeks)
  - instance Maintenance policy: after added a new template. Use 'instance refresh' to start:
    - terminate and launch
    - launch before terminating
    - no policy (mixed)
    - custom

Auto scaling monitoring:
- __Group metrics__:
  - data points about the __ASG__.
  - They have __1 minute granularity__
  - there's no charge.
  - they have to be enabled manually.
- __Basic monitoring__ is at the instance level.
  - By default,
  - it has __5-minute granularity__ and there's no charge.
- With __detailed monitoring__ at the instance level:
  - that's __1 minute granularity__
  - charges do apply.

There are some additional scaling settings:
- We've got __cooldowns__, and they're used with simple scaling policies to prevent Auto Scaling from launching or terminating before the effects of a previous activity are visible.
- The termination policy controls which instances to terminate first when a scale in event occurs.
- __Termination protection__ prevents Auto Scaling from terminating the protected instances.
- The __standby state__ is used to put an instance that's in the in-service state into the standby state for updating and troubleshooting.
  - In the EC2 Console, go to the Auto Scaling Groups section. Select the Auto Scaling Group. For Simple Scaling policies, you can set the Cooldown directly in the scaling policy settings.
- __Lifecycle hooks__ can be used to perform custom actions by pausing instances as the ASG launches or terminates them.
  - Use cases:
    - running scripts to download and install software after launching your instance.
    - Pausing an instance to process data before the instance is terminated by a scale in event.

An __ELB distributes incoming traffic across__ multiple targets such as __EC2 instances__, __containers__, and __IP addresses__, and also __Lambda functions__.

It provides fault tolerance for applications.

- __launch template__: standardizes setup of EC2 instances (os, ec2 type, security-group etc.). Can use used with outher aws services (other then auto-scaling group
- you can dynamically changing scaling policies
- instance purchase option: on demand or spot
- allocation strategies: lowest price, price capacity optiized, 
- termination policy: defines what instances are terminated first
  - default: even distribution accross AZ, except if instance is in 'protected' status, oldest template first, closest to next billing hour
  - other: terminate instances based on allocation strategy: spot or on-demand, new instance type
  - custom: total control what instance terminates, __needs lambda__. Use it when:
    - better control what to terminate
    - custom checks (based on labels or some other metric)
    - graceful shutdown of application
    - data backup
    - integration with external systems 
- A Launch Template stores configuration such as:
  - AMI ID (the machine image)
  - Instance type (e.g., t3.micro)
  - Key pair
  - Security groups
  - IAM role
  - User data scripts
  - Block storage configuration (EBS volumes)
  - Network settings
  - Instance purchasing options (On-Demand or Spot)
  
Launch Template vs Launch Configuration:
- Launch Templates are the modern and recommended approach.
- Launch Templates support multiple versions.
- Supports Spot Instances, Mixed Instance Policies, and newer EC2 features.

### Auto-scaling timers <a id="AutoScalingTimers"></a>

- warm-up time: time needed to initialize and ready to handle requests, needs dynamic scaling (metrics)
- cool-down period (default 300s): period before other scaling activity starts
- health-check grace period: amount of time before performing health check on new instances

### Health checks <a id="HealthChecks"></a>

- __EC2 health checks__, which are the EC2 status checks
  - System Status Check: Monitors the physical hardware and network infrastructure in AWS that your EC2 instance runs on. If the system experiences a failure (e.g., hardware failure, AWS infrastructure issues), the instance will be marked as "unhealthy."
  - Instance Status Check: Monitors the health of the EC2 instance itself—including the operating system, software, and any issues that might cause the instance to become unresponsive (e.g., OS crashes, CPU usage spikes, etc.). If the instance is not responsive or cannot be reached, it’s marked as unhealthy.
- __ELB health checks__, which means it's going to use the ELB health checks in addition to the EC2 instance status checks.

The __health check grace period__:
- how long to wait before checking the health status of an instance after it's been launched into an Auto Scaling group.
- Auto Scaling does not act on health checks until the grace period expires.

### AWS Auto Scaling

Automatically increase or decrease the number of resources based on load. It works with several AWS services, mainly compute resources and some databases.
This service is embedded into other services like:
- Containers (ECS): You can scale container services running on Amazon Elastic Container Service
- Kubernetes pods: If you're using Amazon Elastic Kubernetes Service, you can auto scale: pods (Horizontal Pod Autoscaler) or worker nodes
- DynamoDB throughput: Amazon DynamoDB can auto scale its: read capacity or write capacity
- Aurora database replicas: Amazon Aurora can automatically add/remove read replicas.



### Load Balancing <a id="LoadBalancing"></a>

ELBs can distribute incoming traffic into a __single AZ or multiple AZs__.
 
Only __one subnet per AZ__ can be enabled for each ELB.

You need to ensure you have at least a /27 subnet and make sure there's at least 8 IP addresses available for the ELB to scale.

ELBs can be configured as internet facing or internal only.

You cannot directly assign an Elastic IP (EIP) to an AWS Elastic Load Balancer (ELB).  Application Load Balancers (ALB) and Classic Load Balancers (CLB), use DNS names (via AWS Route 53) for routing traffic instead of EIPs. However You can use Elastic IPs with Network Load Balancers (NLB).

Internet facing ELBs:
- the ELB nodes will have public IPs
- they will route traffic to the private addresses of the EC2 instances.
- You need one public subnet in each AZ where the ELB is defined even if you're routing to a private subnet.

Internal only ELB:
- the nodes have private IPs and
- also routes to the private IPS of the instances.

Connection Draining:
- When deregistering instance, allow in-flight requests to complete
- Default wait time is 5 minutes (300 seconds)
- After wait time elapses, instance is deregistered

Sticky Sessions: Route requests from a client to same target

HTTP/2: Multiple requests sent on the same connection

WebSockets:
- Long running TCP Connection
- Bi-directional
- Server to Client Push notification support

Access Logs:
- Elastic Load Balancing provides access logs that capture detailed information about requests sent to your load balancer.
- Each log contains information such as the time the request was received, the client's IP address, latencies, request paths, and server responses.
- You can use these access logs to analyze traffic patterns and troubleshoot issues.

#### Elastic Load Balancing – Security <a id="LoadBalancingSecurity"></a>

- Offload SSL/TLS
- Integrated Certificate Management
- User Authentication – Cognito(Application Load Balancer)
  - Internet Identity Providers
  - SAML
  - OpenID Connect
- LB is in public or private subnet
- EC2s are in private subnets

#### Application Load Balancer <a id="ALB"></a>

- use it with web applications with __layer 7__ routing - http, https, gRPC, WebSockets
- microservices architectures such as Docker containers
- Targets: __EC2, containers, Lambda, on-premises__
- Support for hosting multiple websites (Server Name Indication)
- User Authentication - __Cognito__
- internet-facing or internal: ALB is in public or private subnet
  - select 2 or more subnets in separate AZ for HA
- IPv4 or IPV6
- VPC + public subnet
- Security Group
__ALB will do https decryption__ with the SSL certificate you provide - need to configure it - see below.
- forwards request to __target group__: EC2, lambda, ALB, IP addresses (on-premises)
- can do port translation
- __health check__ (default is port http)
- sticky essions using cookies
- idle connection timeout
- Static IP address __NOT supported__
- can terminate HTTPS and forward traffic as HTTP to your targets
- New connections per second: Tens of thousands to hundreds of thousands, depending on traffic patterns.
- Active connections: ALB can handle millions of concurrent connections.
- ALB uses DNS names (e.g., my-alb-123456.us-east-1.elb.amazonaws.com)

Routing:
- __path-based__ (exampple.com/images or example.com/orders) and __host-based__ routing (images.example.com or orders.example.com)
- Host HTTP header (support for multiple domains)
- Any standard or custom HTTP header
- Query string parameter based
- Source IP based 

ALB – Security Group:
- Allow inbound traffic from clients on listener port
- Allow outbound traffic to instance security group on listener and health check ports

ALB - ACL:
- Allow inbound traffic from clients on listener port
- Allow outbound traffic to client on ephemeral ports
- Allow outbound traffic to instance VPC on listener and health check ports
- Allow inbound traffic from instance VPC on ephemeral ports

#### Network Load Balancer <a id="NLB"></a>

- TCP traffic, extereme performance, millions requests /s, ultra-low latency
- operating at the __TCP__ , __UDP__ , __TLS__ level – __layer 4__
- offers __ultra-low latency__
- Scales to __millions of requests/sec__
- static IP addresses. One Static IP (or Elastic IP) per Availability Zone
- can be used with __VPC endpoint__ services.
- Targets: __EC2, containers, on-premises__
- Preserves Client IP (Source IP)
- __WebSocket__ Support
- sticky essions using cookies
- idle connection timeout
- Static IP address __supported__ (like elastic IP)

Private Link:
- Network LB based Shared Service
- Configure as PrivateLink Powered Service
- Create VPC endpoint for your service in client VPC
- All communication over AWS network

Network Load Balancer does not support Security Group. 
From network perspective, imagine instance interacting with the client directly

NLB - ACL:
- Allow inbound traffic from clients on listener port
- Allow outbound traffic to client on ephemeral ports
- Allow outbound traffic to instance VPC on listener and health check ports
- Allow inbound traffic from instance VPC on ephemeral ports

#### Gateway Load Balancer <a id="GLB"></a>

- This is layer 3 - only packets
- listens for all IP packets across all ports.
- GLP and virtual appliances exchange application traffic using the GENEVE protocol on port 6081.
- Used with virtual appliances such as firewalls, intrusion detection systems, intrusion prevention systems, and deep packet inspection systems.
- Application Server -> Gateway Load Balancer Endpoint -> Gateway Load Balancer -> Security Appliance -YES-> GWLB -> GWLB Endpoint -> Application Server / User
- VPC must use __ingress routing__: inboud or outbound traffic will pass through 3rd party firewall: Integrent Gateway <-> GWLB (with PaloAlto) <-> EC2
  - Simple case: It is EC2 with NIC and firewall software
  - HA case is GWLB instead of EC2
- GWLB does not have url or IP address. It only has endpoint in your VPC
- GWLB should be setup in a separate VPC and you have an endpoint in your VPC
- Typical Use Cases
  - Deploying third-party firewalls (e.g., Palo Alto, Fortinet, Check Point) in AWS.
  - Intrusion detection/prevention for VPC traffic.
  - Centralized deep packet inspection across multiple subnets or VPCs.
  - Traffic mirroring / monitoring for security or compliance.

#### Cross-zone load balancing <a id="Cross-zone"></a>
- when cross-zone load balancing is enabled, each load balancer node will distribute traffic across the register targets in all enabled AZ.
- When it's disabled, each load balancer node distributes traffic only across the registered targets in its availability zone.
- With __Application Load Balancers, cross-zone load balancing is always enabled__.
- With __Network Load Balancers and Gateway Load Balancers, cross-zone load balancing is disabled by default__.
- for both ALB and NLB you must select at least 2 AZs
- for ALB Cross-Zone Load Balancing is always ENABLED
- for NLB Cross-Zone Load Balancing is always DISABLED
- if Cross-Zone Load Balancing = OFF and ALB is in AZ1 then it will send traffic only to EC2 in AZ1

### Global Accelerator <a id="GlobalAccelerator"></a>

Cross-region load balancing

- Global Accelerator decides how to route each application request
- Responds instantaneously to changes in health and traffic conditions
- Clients connect to Edge location
- Request travels in AWS Global network (and not public internet)
- Endpoints can be private (Global Accelerator creates a peering connection)
- DDoS Protection
- AWS Shield Standard and Advanced Protection

AWS Global Accelerator utilizes the Amazon global network, allowing you to improve the performance of your applications by lowering first-byte latency (the round trip time for a packet to go from a client to your endpoint and back again) and jitter (the variation of latency), and __increasing throughput__ (the amount of time it takes to transfer data) as compared to the public internet.

AWS Global Accelerator __improves performance__ for a wide range of applications over TCP or UDP by proxying packets at the edge to applications running in one or more AWS Regions. Global Accelerator is a __good fit for non-HTTP use cases__, such as gaming (UDP), IoT (MQTT), or Voice over IP, as well as for HTTP use cases that specifically require static IP addresses or deterministic, fast regional failover.

![ Global Accelerator ](./images/global_accelerator.jpg)

AWS Global Accelerator creates two IPv4 static IPs when you create an accelerator by default. You can also request one additional IP in the case of needing an extra one for specific use cases like advanced routing or increasing availability and redundancy.

AWS Global Accelerator solves this by providing you with two static IPs that are anycast from our globally distributed edge locations, giving you a single entry point to your application, regardless of how many AWS Regions it’s deployed in. This allows you to add or remove origins, Availability Zones or Regions without reducing your application availability. Your traffic routing is managed manually, or in console with endpoint traffic dials and weights. If your application endpoint has a failure or availability issue, AWS Global Accelerator will automatically redirect your new connections to a healthy endpoint within seconds.

Step by step. Configuring AWS Global Accelerator to route traffic to two ALBs in different regions:
- Create your ALBs
- Create a Global Accelerator
  - You’ll get two static IP addresses automatically (or can bring your own).
  - These static IPs are anycast, meaning traffic will route to the nearest AWS edge location.
- Add Global Accelelator Listeners for the port your application uses (HTTP 80 or HTTPS 443)
- Add Endpoint Groups
  - Endpoint Groups correspond to regions.
  - Add two endpoint groups:
    - Region A → attach ALB in Region A.
    - Region B → attach ALB in Region B.
  - For each group, configure:
    - Traffic dial: percentage of traffic to that region (e.g., 50%-50% or weighted by capacity).
    - Health checks: configure a path (like /health) so Global Accelerator knows which ALB is healthy.

### Auto scaling vs ELB

- ELB automatically routes incoming traffic to all instances in auto-scaling group
- ELB is used to monitor health

### Architectural Patterns

#### HA and Elastic Scalability for web servers

You can use Amazon EC2 Auto Scaling and Application Load Balancers across multiple AZs.

#### Low latency connections are needed over UDP to a pool of EC2 instances running a gaming application.

Use a Network Load Balancer with a UDP listener.

#### Clients needs to white list static IP addresses for a highly available load balanced application and in an AWS region.

Use a Network Load Balancer, you can create static IP addresses in each AZ.
Remember, with an ALB, you don't get static IP addresses, so you wouldn't be able to do that. 
You would know the DNS name, but the IP addresses might change over time.

#### An application on EC2 in an Auto Scaling group requires disaster recovery across regions.

create an ASG in a second region with a capacity set to zero.
That means there's not going to be any instances running so you're not wasting money.
You can take snapshots and copy them across regions.
You might use Lambda to automate that process or data lifecycle manager, DLM.

#### An application on EC2 must scale in larger increments if a big increase in traffic occurs compared to small increases in traffic.

Use Auto Scaling and a step scaling policy. And you configure a larger capacity Increase

#### You need to scale EC2 instances behind an ALB based on the number of requests completed by each instance.

In this case, you can use an Auto Scaling group and a target tracking policy. 
Using the ALBRequestCountPerTarget metric, and that's the number of requests that are outstanding for an individual target.

#### An application runs on EC2 instances behind an ALB, once authenticated, users should not need to reauthenticate if an instance fails.

In this case, you could use a session state store such as DynamoDB or ElastiCache.

#### A company is deploying IDS/IPS. That's an intrusion detection system and intrusion prevention system, and it's using virtual appliances and needs to scale those horizontally.

Use a Gateway Load Balancer in front of the virtual appliances.

#### Your application is expected to receive a lot of traffic after a promotion event. This application has an Elastic Load Balancer for distributing requests to EC2 web servers. What specific steps do you take to ensure internet gateway scales with the traffic?

No action needed. Internet gateway is a managed service and automatically scales, redundant and highly available

Internet Gateway is horizontally scaled, so it can handle very large volumes of traffic.
AWS does not publish a strict bandwidth limit, but performance can be affected by:
- EC2 instance bandwidth
- VPC route table configurations

#### If an instance fails the health check, Elastic Load Balancer would:

- Load Balancer stops new traffic to the instance - Load balancer monitors all registered instances for health. 
- If an instance fails the health check, the load balancer stops new traffic to the instance. 
- ELB continues to perform health checks, even on unhealthy instances. 
- If the instance becomes healthy again, ELB will start using the instance
- Once the instance passes consecutive health checks (healthy threshold), it is marked healthy, and ELB resumes sending traffic.

To handle instances that never recover:
- Attach ELB/ALB target group to an Auto Scaling group
- Auto Scaling monitors instance health using ELB health checks
- When an instance fails health checks for the unhealthy threshold, Auto Scaling terminates it
- Auto Scaling launches a new instance to maintain desired capacity

#### An organization's security policy requires client apps to communicate only with the whitelisted IP Addresses. You need to build a new service on AWS that would be used by client applications. Which of these architectural options would reliably allow whitelisting of the load balancer IP address at the client?

Network Load Balancer assigns a static IP address per availability zone. 
You can use this to configure your client application. 
DNS lookup of Application and Classic Load Balancer Names would return a list of load balancer nodes that are valid at that time; however, this list can change depending on the load on the system. 
So, for application and classic load balancers, you should always refer to it by DNS name.

#### A customer has a hybrid infrastructure consisting of web servers in both on-premises and the AWS cloud. The client request must be distributed across AWS and on-premises servers. Which load balancing product can support this requirement?

Both Application and Network Load Balancers allow you to add targets by IP address. 
You can use this capability to register instances located on-premises and VPC to the same load balancer. 
You need to register private IP of the server for a hybrid load balancer, and on-premises data center should have a VPN connection or a Direct Connect link to AWS (to communicate using private IP)

#### You want to limit access to the load balancer from specific IP ranges. Where can you enforce this policy

Security Groups, are supported by both Classic and Application load balancers. 
You can use the load balancer security group to limit access to the load balancer from specified source IP blocks. 
Network Load Balancer does not support Security Groups. 
You can also restrict access using Network ACL of the load balancer subnets.

#### Which auto scaling group configuration would ensure two running instances when an availability zone is lost? Assume that minimum, maximum, and desired instance count is set to the same value. Pick a choice that is optimized for cost.

We don’t know ahead of time which availability zone will fail. 
When desired instance count is set to 3, and the number of availability zones is set to 3, Auto scaling will deploy one instance in each availability zone.
When an AZ is lost, we would still have two running instances

#### An application consists of an elastic load balancer, a fleet of web servers, and a Relational Database in the multi-AZ configuration. Auto Scaling group dynamically scales the number of web servers based on traffic. Auto Scaling Group uses a load balancer health check. The app team has implemented an in-depth health check that passes only when connectivity to the database is confirmed. The primary database failed, and RDS initiated a failover. How will Auto Scaling respond to this situation?

Auto Scaling would terminate failing web server instances and launch replacement ones. 
In-depth Health checks like these can produce unintended side effects when combined with Auto Scaling. 
With Auto Scaling in the picture, your health check should check only the health of the server and application components. 
An in-depth health check on other dependent services requires careful assessment

#### Which of these options maintains a scaled-down infrastructure in another region and requires only scaling after a disaster?

- __Backup and Restore__ only maintains a backup in another region. After a disaster, we need to restore the data and bring the entire infrastructure up in the second region, so the RTO/RPO is in hours.
- __Pilot light__ maintains a continuously replicated copy of the data in another region; however, the rest of the infrastructure needs to be brought up after the disaster. So, the RTO/RPO is in 10s of minutes.
- __Warm Standby__ maintains a continuously replicated copy of data, and a scaled-down infrastructure is always running for the rest of the components. Warm Standby can meet more stringent RTO/RPO in minutes.
- Multi-site __Active/Active__ is a zero-downtime solution with infrastructure in multiple regions. The application request is routed to any of the regions. This option can meet real-time RTO/RPO requirements.

#### You would like to automatically replace instances that are not healthy due to underlying infrastructure or common guest OS related issues. In order to do so with AutoScaling, you need to

Autoscaling automatically does this for you

#### team wants to use a mix of on-demand and spot instances of various instance types. How would you implement this proposal with Auto Scaling?

Use Auto Scaling Launch Template and specify the on-demand and spot portion of the capacity that the auto scaling group needs to maintain

You can specify a percentage distribution of on-demand and spot instances. 
To maximize the chances of fulfilling spot requests, you can specify a range of values for vCPU and memory configuration. 
Auto Scaling will identify a list of instance families that meet the criteria.

#### The DevOps team at an e-commerce company wants to perform some maintenance work on a specific Amazon EC2 instance that is part of an Auto Scaling group using a step scaling policy. The team is facing a maintenance challenge - every time the team deploys a maintenance patch, the instance health check status shows as out of service for a few minutes. This causes the Auto Scaling group to provision another replacement instance immediately

- Put the instance into the __Standby state__ and then update the instance by applying the maintenance patch. Once the instance is ready, you can exit the Standby state and then return the instance to service
- Suspend the ReplaceUnhealthy process type for the Auto Scaling group and apply the maintenance patch to the instance. Once the instance is ready, you can manually set the instance's health status back to healthy and activate the ReplaceUnhealthy process type again

#### A retail company wants to rollout and test a blue-green deployment for its global application in the next 48 hours. Most of the customers use mobile phones which are prone to Domain Name System (DNS) caching. The company has only two days left for the annual Thanksgiving sale to commence. As a Solutions Architect, which of the following options would you recommend to test the deployment on as many users as possible in the given time frame?

Use AWS Global Accelerator to distribute a portion of traffic to a particular deployment

AWS Global Accelerator is a network layer service that directs traffic to optimal endpoints over the AWS global network, this improves the availability and performance of your internet applications. It provides two static anycast IP addresses that act as a fixed entry point to your application endpoints in a single or multiple AWS Regions, such as your Application Load Balancers, Network Load Balancers, Elastic IP addresses or Amazon EC2 instances, in a single or in multiple AWS regions.

AWS Global Accelerator uses endpoint weights to determine the proportion of traffic that is directed to endpoints in an endpoint group, and traffic dials to control the percentage of traffic that is directed to an endpoint group (an AWS region where your application is deployed).

While relying on the DNS service is a great option for blue/green deployments, it may not fit use-cases that require a fast and controlled transition of the traffic

Elastic Load Balancing (ELB) can distribute traffic across healthy instances. You can also use the Application Load Balancers weighted target groups feature for blue/green deployments as it does not rely on the DNS service. In addition you don’t need to create new ALBs for the green environment. As the use-case refers to a global application, so this option cannot be used for a multi-Region solution which is needed for the given requirement.

How DNS + GA works step by step
- Client queries www.example.com.
- DNS returns the two static GA IP addresses.
- Client connects to the nearest anycast IP.
- AWS Global Accelerator uses health checks to route traffic to the closest healthy endpoint (NLB/ALB/EC2/EIP).
- If an endpoint fails, GA automatically reroutes traffic to another healthy endpoint without the client needing to update DNS.
- Key point: DNS never needs to change during endpoint failover — GA handles routing at the network layer.

#### The engineering team at a logistics company has noticed that the Auto Scaling group (ASG) is not terminating an unhealthy Amazon EC2 instance. As a Solutions Architect, which of the following options would you suggest to troubleshoot the issue? 

- The health check grace period for the instance has not expired
Amazon EC2 Auto Scaling doesn't terminate an instance that came into service based on Amazon EC2 status checks and Elastic Load Balancing (ELB) health checks until the health check grace period expires.
- The instance maybe in Impaired status
Amazon EC2 Auto Scaling does not immediately terminate instances with an Impaired status. Instead, Amazon EC2 Auto Scaling waits a few minutes for the instance to recover. Amazon EC2 Auto Scaling might also delay or not terminate instances that fail to report data for status checks. This usually happens when there is insufficient data for the status check metrics in Amazon CloudWatch.
- The instance has failed the Elastic Load Balancing (ELB) health check status
By default, Amazon EC2 Auto Scaling doesn't use the results of ELB health checks to determine an instance's health status when the group's health check configuration is set to EC2. As a result, Amazon EC2 Auto Scaling doesn't terminate instances that fail ELB health checks. If an instance's status is OutofService on the ELB console, but the instance's status is Healthy on the Amazon EC2 Auto Scaling console, confirm that the health check type is set to ELB.

#### An e-commerce company is using Elastic Load Balancing (ELB) for its fleet of Amazon EC2 instances spread across two Availability Zones (AZs), with one instance as a target in Availability Zone A and four instances as targets in Availability Zone B. The company is doing benchmarking for server performance when cross-zone load balancing is enabled compared to the case when cross-zone load balancing is disabled.

With cross-zone load balancing enabled, one instance in Availability Zone A receives 20% traffic and four instances in Availability Zone B receive 20% traffic each. With cross-zone load balancing disabled, one instance in Availability Zone A receives 50% traffic and four instances in Availability Zone B receive 12.5% traffic each

The nodes for your load balancer distribute requests from clients to registered targets. When cross-zone load balancing is enabled, each load balancer node distributes traffic across the registered targets in all enabled Availability Zones. Therefore, one instance in Availability Zone A receives 20% traffic and four instances in Availability Zone B receive 20% traffic each. When cross-zone load balancing is disabled, each load balancer node distributes traffic only across the registered targets in its Availability Zone. Therefore, one instance in Availability Zone A receives 50% traffic and four instances in Availability Zone B receive 12.5% traffic each.

Consider the following diagrams (the scenario illustrated in the diagrams involves 10 target instances split across 2 AZs) to understand the effect of cross-zone load balancing.

If cross-zone load balancing is enabled, each of the 10 targets receives 10% of the traffic. This is because each load balancer node can route its 50% of the client traffic to all 10 targets.

#### You are working for a software as a service (SaaS) company as a solutions architect and help design solutions for the company's customers. One of the customers is a bank and has a requirement to whitelist a public IP when the bank is accessing external services across the internet. Which architectural choice do you recommend to maintain high availability, support scaling-up to 10 instances and comply with the bank's requirements?

Use a Network Load Balancer with an Auto Scaling Group

Network Load Balancer is best suited for use-cases involving low latency and high throughput workloads that involve scaling to millions of requests per second. Network Load Balancer operates at the connection level (Layer 4), routing connections to targets - Amazon EC2 instances, microservices, and containers – within Amazon Virtual Private Cloud (Amazon VPC) based on IP protocol data. A Network Load Balancer functions at the fourth layer of the Open Systems Interconnection (OSI) model. It can handle millions of requests per second.

Network Load Balancers expose a fixed IP to the public web, therefore allowing your application to be predictably reached using this IP, while allowing you to scale your application behind the Network Load Balancer using an ASG.

Incorrect options:

Classic Load Balancers and Application Load Balancers use the private IP addresses associated with their Elastic network interfaces as the source IP address for requests forwarded to your web servers.

These IP addresses can be used for various purposes, such as allowing the load balancer traffic on the web servers and for request processing. It's a best practice to use security group referencing on the web servers for whitelisting load balancer traffic from Classic Load Balancers or Application Load Balancers.

However, because Network Load Balancers don't support security groups, based on the target group configurations, the IP addresses of the clients or the private IP addresses associated with the Network Load Balancers must be allowed on the web server's security group.

Use a Classic Load Balancer with an Auto Scaling Group - Classic Load Balancer provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. Classic Load Balancer is intended for applications that were built within the Amazon EC2-Classic network.

Use an Application Load Balancer with an Auto Scaling Group - Application Load Balancer operates at the request level (layer 7), routing traffic to targets – Amazon EC2 instances, containers, IP addresses and AWS Lambda functions based on the content of the request. Ideal for advanced load balancing of HTTP and HTTPS traffic, Application Load Balancer provides advanced request routing targeted at the delivery of modern application architectures, including microservices and container-based applications.

Application and Classic Load Balancers expose a fixed DNS (=URL) rather than the IP address. So these are incorrect options for the given use-case.

Use an Auto Scaling Group with Dynamic Elastic IPs attachment - The option "Use an Auto Scaling Group (ASG) with Dynamic Elastic IPs attachment" has been added as a distractor. ASG does not have a dynamic Elastic IPs attachment feature.

#### A CRM web application was written as a monolith in PHP and is facing scaling issues because of performance bottlenecks. The CTO wants to re-engineer towards microservices architecture and expose their application from the same load balancer, linked to different target groups with different URLs: checkout.mycorp.com, www.mycorp.com, yourcorp.com/profile and yourcorp.com/search. The CTO would like to expose all these URLs as HTTPS endpoints for security purposes. As a solutions architect, which of the following would you recommend as a solution that requires MINIMAL configuration effort?

Use Secure Sockets Layer certificate (SSL certificate) with SNI

You can host multiple TLS secured applications, each with its own TLS certificate, behind a single load balancer. To use SNI, all you need to do is bind multiple certificates to the same secure listener on your load balancer. ALB will automatically choose the optimal TLS certificate for each client.

ALB’s smart certificate selection goes beyond SNI. In addition to containing a list of valid domain names, certificates also describe the type of key exchange and cryptography that the server supports, as well as the signature algorithm (SHA2, SHA1, MD5) used to sign the certificate.

With SNI support AWS makes it easy to use more than one certificate with the same ALB. The most common reason you might want to use multiple certificates is to handle different domains with the same load balancer.

#### A streaming solutions company is building a video streaming product by using an Application Load Balancer (ALB) that routes the requests to the underlying Amazon EC2 instances. The engineering team has noticed a peculiar pattern. The Application Load Balancer removes an instance from its pool of healthy instances whenever it is detected as unhealthy but the Auto Scaling group fails to kick-in and provision the replacement instance. What could explain this anomaly?

The Auto Scaling group is using Amazon EC2 based health check and the Application Load Balancer is using ALB based health check

An Auto Scaling group contains a collection of Amazon EC2 instances that are treated as a logical grouping for automatic scaling and management.

Application Load Balancer automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, and AWS Lambda functions. It can handle the varying load of your application traffic in a single Availability Zone or across multiple Availability Zones.

If the Auto Scaling group (ASG) is using EC2 as the health check type and the Application Load Balancer (ALB) is using its in-built health check, there may be a situation where the ALB health check fails because the health check pings fail to receive a response from the instance. At the same time, ASG health check can come back as successful because it is based on EC2 based health check. 

Therefore, in this scenario, the ALB will remove the instance from its inventory, however, the Auto Scaling Group will fail to provide the replacement instance. This can lead to the scaling issues mentioned in the problem statement.

__By default, Auto Scaling does NOT use ALB health checks unless you explicitly configure it. Enable ELB/ALB health checks in Auto Scaling group!__











## AWS Organizations and Control Tower <a id="Organizations"></a>

With __AWS Organizations, you can consolidate multiple AWS accounts__ into an Organization that you create and then centrally manage.

__AWS Organizations__:
- management, billing, compliance enforcement for multiple aws accounts
- define central configuration and __resource sharing__, __consolidated billing__ (volume discounts)
- automated account creation, __service control policies__ (SCP)
  - works at organization level: root, organizational units (OU) or individual accounts
  - can only limit
  - affects only member accounts in the OU. Have no effect on the management account
  - aws evaluates SCPs in conjunction with IAM policies. Action must be allowed in IAM policy and not denied in SCP.
  - The __default FullAWSAccess managed policy__ is attached to all services - it allows all (no restrictions)
  - if SCP is missing (in OU) then it means deny
  - for it to work you send invitation to other aws accounts that must accept invitation
  - SCP is to control permissions, not to add permisions (to User)

It's available in two feature sets:
- __consolidated billing__
- __all features__.

It includes the root account and Organizational Units.

Policies get applied to root accounts or OUs.

Consolidated billing includes:
- a paying account, which is independent and can't access the resources of other accounts
- linked accounts - all linked accounts are also independent of each other.

Consolidated billing:
- __single payment method__ for all the AWS accounts in the Organization.
- __combined view__ of charges incurred by all accounts
- __pricing benefits__ from the aggregated usage.
- There's a limit of 20 linked accounts for consolidated billing by default.
- can help with cost control through the volume discounts.
- __unused reserved instances are applied across the group__
- paying accounts should be used for billing purposes only.

Service Control Policies:
- __manage the maximum available permissions__.
- must have all features enabled in the Organization
- can be applied to accounts or OUs.
- __policies can be assigned at different points in the hierarchy__
- __SCPs affect only IAM users and roles, not resource policies__.
- __SCPs affect the root account in member accounts__.
- SCPs do not affect any action performed by the management accounts.

Different strategies:
- The __deny list strategy__ uses the FullAWSAccess SCP
  - attached to every OU and account
  - overrides the implicit deny.
  - explicitly allows all permissions to flow down from the root, so it grants full access to all permissions.
  - create additional SCPs to explicitly deny permissions anywhere in the hierarchy.
- __allow list strategy__.
  - remove the FullAWSAccess SCP.
  - No APIs are permitted anywhere unless you explicitly allow them.
  - create SCPs to allow all permissions.
  - SCPs must be attached to target accounts and every OU above it including the root.

AWS Organizations – migration
- accounts can be migrated between organizations.
- You must have root or IAM access to both the member and management accounts.
- Use the AWS Organization's console if it's just a few accounts or use the API or CLI if there are many accounts to migrate.

### Architectural Patterns

#### A company needs a method of quickly creating AWS accounts programmatically.

Use the Organization's API to create accounts programmatically.

#### Users in a member account in AWS Organizations should be restricted from making changes in IAM.

Use a Service Control Policy, an SCP to deny access to IAM actions.

#### An AWS account must be moved between Organizations.

Migrate the account using the AWS's Organization's console.
Again, you can do that for a single account.
If you have lots of accounts you want to move, again, you can do that through the API as well.

#### A solutions architect created a new account through the Organization's console and needs to log in to launch resources.

The architect should switch roles to access the new accounts.

#### Multiple member accounts in AWS Organizations require the same permissions to be restricted using SCPs.

Create an OU and add the member accounts and then attached the SCP to the OU.

#### The developers in a company each have their own AWS accounts for testing. The security team wish to enable centralized governance.

Create an AWS Organization and send an invite to each developer's AWS account to join the Organization.

#### You have multiple AWS accounts within a single AWS Region managed by AWS Organizations and you would like to ensure all Amazon EC2 instances in all these accounts can communicate privately. Which of the following solutions provides the capability at the CHEAPEST cost?

Create a virtual private cloud (VPC) in an account and share one or more of its subnets with the other accounts using __Resource Access Manager__

AWS Resource Access Manager (RAM) is a service that enables you to easily and securely share AWS resources with any AWS account or within your AWS Organization. 
You can share AWS Transit Gateways, Subnets, AWS License Manager configurations, and Amazon Route 53 Resolver rules resources with RAM. 
RAM eliminates the need to create duplicate resources in multiple accounts, reducing the operational overhead of managing those resources in every single account you own. 
You can create resources centrally in a multi-account environment, and use RAM to share those resources across accounts in three simple steps: create a Resource Share, specify resources, and specify accounts. RAM is available to you at no additional charge.

A Transit Gateway will work but will be an expensive solution.

```
provider "aws" {
  alias  = "network"
  region = "us-east-1"
}

resource "aws_vpc" "shared_vpc" {
  provider   = aws.network
  cidr_block = "10.0.0.0/16"
}

// shubnet to share
resource "aws_subnet" "shared_subnet" {
  provider          = aws.network
  vpc_id            = aws_vpc.shared_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}

// Create RAM Resource Share
resource "aws_ram_resource_share" "vpc_share" {
  provider                  = aws.network
  name                      = "shared-vpc-subnet"
  allow_external_principals = false
}

// Share Subnet via RAM
resource "aws_ram_resource_association" "subnet_assoc" {
  provider           = aws.network
  resource_arn       = aws_subnet.shared_subnet.arn
  resource_share_arn = aws_ram_resource_share.vpc_share.arn
}

// Share with AWS Organization
resource "aws_ram_principal_association" "org_share" {
  provider           = aws.network
  principal          = "o-xxxxxxxxxx" # Organization ID
  resource_share_arn = aws_ram_resource_share.vpc_share.arn
}

// Accept Share (Optional if auto-enabled)
resource "aws_ram_resource_share_accepter" "accept" {
  provider = aws.app_account
  share_arn = aws_ram_resource_share.vpc_share.arn
}

// Launch EC2 in Shared Subnet (App Account)
provider "aws" {
  alias  = "app_account"
  region = "us-east-1"
}

resource "aws_instance" "app_instance" {
  provider      = aws.app_account
  ami           = "ami-xxxxxxxx"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.shared_subnet.id

  tags = {
    Name = "shared-vpc-instance"
  }
}
```

#### You would like to migrate an AWS account from an AWS Organization A to an AWS Organization B. What are the steps do to it?

To migrate accounts from one organization to another, you must have root or IAM access to both the member and master accounts. 
Here are the steps to follow: 
1. Remove the member account from the old organization 
2. Send an invite to the member account from the new Organization 
3. Accept the invite to the new organization from the member account

#### An AWS Organization is using Service Control Policies (SCPs) for central control over the maximum available permissions for all accounts in their organization. This allows the organization to ensure that all accounts stay within the organization’s access control guidelines. Which of the given scenarios are correct regarding the permissions described below?

If a user or role has an IAM permission policy that grants access to an action that is either not allowed or explicitly denied by the applicable service control policy (SCP), the user or role can't perform that action

Service control policy (SCP) affects all users and roles in the member accounts, including root user of the member accounts

Service control policy (SCP) does not affect service-linked role

Service control policy (SCP) are one type of policy that can be used to manage your organization. Service control policy (SCP) offers central control over the maximum available permissions for all accounts in your organization, allowing you to ensure your accounts stay within your organization’s access control guidelines.

In service control policy (SCP), you can restrict which AWS services, resources, and individual API actions the users and roles in each member account can access. You can also define conditions for when to restrict access to AWS services, resources, and API actions. These restrictions even override the administrators of member accounts in the organization.

Please note the following effects on permissions vis-a-vis the service control policy (SCP):

If a user or role has an IAM permission policy that grants access to an action that is either not allowed or explicitly denied by the applicable service control policy (SCP), the user or role can't perform that action.

Service control policy (SCP) affects all users and roles in the member accounts, including root user of the member accounts.

Service control policy (SCP) does not affect any service-linked role.

#### A company has migrated its application from a monolith architecture to a microservices based architecture. The development team has updated the Amazon Route 53 simple record to point "myapp.mydomain.com" from the old Load Balancer to the new one. The users are still not redirected to the new Load Balancer. What has gone wrong in the configuration?

Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service. 
Amazon Route 53 effectively connects user requests to infrastructure running in AWS – such as Amazon EC2 instances, Elastic Load Balancing load balancers, or Amazon S3 buckets – and can also be used to route users to infrastructure outside of AWS.

You can use Amazon Route 53 to configure DNS health checks to route traffic to healthy endpoints or to independently monitor the health of your application and its endpoints. 
Amazon Route 53 Traffic Flow makes it easy for you to manage traffic globally through a variety of routing types, including Latency Based Routing, Geo DNS, Geoproximity, and Weighted Round Robin—all of which can be combined with DNS Failover to enable a variety of low-latency, fault-tolerant architectures.

The Time To Live (TTL) is still in effect

TTL (time to live), is the amount of time, in seconds, that you want DNS recursive resolvers to cache information about a record. 
If you specify a longer value (for example, 172800 seconds, or two days), you reduce the number of calls that DNS recursive resolvers must make to Amazon Route 53 to get the latest information for the record. 
This has the effect of reducing latency and reducing your bill for Route 53 service.

However, if you specify a longer value for TTL, it takes longer for changes to the record (for example, a new IP address) to take effect because recursive resolvers use the values in their cache for longer periods before they ask Route 53 for the latest information. 
If you're changing settings for a domain or subdomain that's already in use, AWS recommends that you initially specify a shorter value, such as 300 seconds, and increase the value after you confirm that the new settings are correct.

For this use-case, the most likely issue is that the TTL is still in effect so you have to wait until it expires for the new request to perform another DNS query and get the value for the new Load Balancer.

#### You attach an SCP with "Effect": "Allow", "Action": "*" — why might things still fail?

Because SCPs use a deny-by-default model when any SCP is attached:
- If you attach SCPs, you must explicitly allow required services
- Missing services in SCP = implicitly denied

#### Can SCPs restrict the root user of an account?

Yes — SCPs apply to all principals, including root

#### How should you structure Organizational Units (OUs)?

Apply stricter SCPs as you go down toward production

#### What does AWS Control Tower add on top of Organizations?

Control Tower = prebuilt governance + automation layer

| Feature             | Organizations | Control Tower |
| ------------------- | ------------- | ------------- |
| Account management  | ✅             | ✅             |
| SCPs                | ✅             | ✅             |
| Landing zone setup  | ❌             | ✅             |
| Guardrails          | ❌             | ✅             |
| Account vending     | ❌             | ✅             |
| Audit/logging setup | ❌             | ✅             |

#### What are guardrails in Control Tower?

Guardrails = predefined governance rules implemented via:
- SCPs (preventive controls)
- Config rules (detective controls)

#### How does Control Tower handle centralized logging?

- Creates Log Archive account
- Aggregates:
  - CloudTrail logs
  - AWS Config logs









## Amazon VPC <a id="VPC"></a>

Analogous to having your own data center inside AWS.

You get complete control over the virtual networking environment.

VPC is logically isolated from other VPCs on AWS.

__VPCs are region-wide__.

A __default VPC gets created in each region and that always has a subnet in each availability zone__.

By default, you can create up to five VPCs per region.

__Public subnets__ are subnet that have:
- the __auto assigned public IPv4 address__ setting configured to yes, and
- the __subnet route table must have a route to an internet gateway__.

When you create a VPC, you specify a range of IPv4 addresses for the VPC in the form of a CIDR block.

A __VPC will span all availability zones in the region__.

You get full control of who has access to the resources inside the VPC.

The names of availability zones are mapped to different zones for different uses. So, you can __use the AZ ID to identify the actual physical zone__.

__Components of a VPC__:
- __subnet__: segments of a VPC's IP range where you can place groups of isolated resources and they map to a single AZ.
  - AWS subnet is always in one AZ
  - Azure subnet can span multiple AZ
  - By default 2 subnets are connected to each other via Route Table and EC2 can communicate with private IP
- __Internet gateway__ is the VPC side of a connection to the public internet.
- A __NAT gateway__ is a highly available managed network address translation service for enabling access to the internet from private instances.
- The __VPC router__ performs all the routing functions in your VPC.
- A __peering connection__ connects you to another VPC using private IP addresses.
- __VPC endpoints__ enable private IP addresses to be used to connect to services in the public zone.
- An egress only Internet gateway is used by IPv6 addresses to access the internet, and it's outbound only.
- For VPN:
  - A __hardware VPN__ connection is a virtual private network that you can connect your VPC to your data center, your home network, or your co-location facility.
  - The __virtual private gateway__ is the VPC side of the VPN connection,
  - the __customer gateway__ is the customer side of VPN connection.

Rules for your IP __CIDR blocks__:
- the __size can vary between /16 and /28__.
- The CIDR block cannot overlap with any existing CIDR block that's associated with the VPC.
- you __cannot increase or decrease the size of an existing CIDR block__.
- max = 5 VPCs per region
- The first four and last IP addresses in a subnet are not available for use.
- AWS recommend you use the RC 1918 ranges.
- Ensure you have enough networks and hosts.
- Bigger CIDR blocks are often better and smaller subnets are usually okay.
- Consider deploying your application tiers into subnets.
- Split your high availability resources across subnets that are assigned to different AZ.
- VPC peering requires non-overlapping CIDR blocks.

__VPC Sharing__:
- VPC sharing (part of Resource Access Manager) allows multiple AWS accounts to create their application resources such as Amazon EC2 instances, Amazon RDS databases, Amazon Redshift clusters, and AWS Lambda functions, into __shared and centrally-managed Amazon Virtual Private Clouds__ (VPCs). 
- To set this up, the account that owns the VPC (owner) __shares one or more subnets with other accounts__ (participants) that belong to the same organization from AWS Organizations. After a subnet is shared, the participants can view, create, modify, and delete their application resources in the subnets shared with them. Participants cannot view, modify, or delete resources that belong to other participants or the VPC owner.
- You can share Amazon VPCs to leverage the implicit routing within a VPC for __applications that require a high degree of interconnectivity__ and are within the same trust boundaries. This reduces the number of VPCs that you create and manage while using separate accounts for billing and access control.
- To allow another AWS account (with which you've shared a subnet in your VPC) to use the RDS endpoint, you need to ensure a few key things:
  - The RDS endpoint is in a shared subnet
  - Update the security group attached to the RDS instance to allow traffic from the EC2 instances in the other account
  - Make sure the EC2 instances in the other account can resolve the RDS endpoint's DNS name
  - If your RDS setup uses IAM authentication, you’ll need to:
    - Grant the other account's IAM users/roles access to the RDS via IAM policies.

### Security Groups <a id="SecurityGroups"></a>

Security Group:
- Default Security Group: Inbound: All, Outbound: All
- Only __Allow rules__, no Deny
- One security group __can protect many EC2__: SG -- n:n -- EC2
- Stateful: do not check 'inbound' if session has been initiated and this is returning traffic
- One security group can protect EC2s in __different AZs__.
- can be attached to __anything with NIC__ (network interface)

Security groups versus network ACLs:
- __Security groups__:
  - operate at the __instance level__.
  - support __allow rules only__.
  - __stateful__ all rules get evaluated
  - apply only to instances that are associated with the group.
- A __network ACL__:
  - operates at the __subnet level__
  - supports __allow and deny rules__,
  - __stateless__,
  - rules get __processed in order__
  - automatically applies to all instances in the subnets that it's associated with.

| Port range | Description           | Example
|------------|-----------------------|-------
| 0-1023     | Well-known ports      | Http (80)
| 1024-49151 | Registered ports      | MySQL (3306)
| 49152-65535| Dynamic/Private ports | random

ACL Ephemeral Ports
![ Ephemeral Ports ](./images/ephemeral_ports.jpg)

Network ACL – Fix Allow Local Traffic
![ Fix Allow Local Traffic ](./images/fix_allow_local_traffic.jpg)

### Connecting to a VPC <a id="ConnectingToVPC"></a>

- AWS __managed VPN__
  - What: an IPSec VPN connection __over the Internet__.
  - When: a quick and easy way to set up a VPN tunnel to a VPC, can be used as a redundant link for some other connection like Direct Connect
  - Pros: supports static routes or BGP peering and routing.
  - Cons: is dependent on an Internet connection.
  - How: create an AWS managed VPN by creating a virtual private gateway, also known as a VWG on AWS and a customer gateway on the on-premises side.
  - Setup:
    - Customer Gateway
    - VPN Gateway, attach to VPC
    - Site-to-site VPN
    - Download and setup configuration file on on-premises router
    - add route in route table in 2 places: aws and on-premises)
  - VPN Site-to-Site , HA AWS-OnPrem:
    - Two Customer Gateway devices preferably in different data centers
    - Two VPN connection from the same VGW but to different CGWs
    - On-premises Connectivity is configured at VPC level
  - VPN using Transit Gateway:
    - Use Transit Gateway to terminate VPN Connection
    - Share the same VPN connection with multiple VPCs

- __Direct Connect__:
  - faster than VPN, no internet
  - What: dedicated network connection over private lines straight into the AWS backbone.
  - When: requires a large network link into AWS. When you have a lot of resources and services being used by corporate users in your data center or your office.
  - Pros: predictable network performance and potential bandwidth cost reduction if you use the right volume of traffic. And you get up to 10 or 100 gigabits per second of provisioned connections. Supports BGP peering and routing.
  - Cons: may require additional telecom and hosting provider relationships and network setups. So, that can take a bit of time and cost to configure.
  - How: work with your data center networking provider to connect into the AWS locations and then you create virtual interfaces for accessing services on AWS.
  - Bypass internet with a dedicated link between on-premises and AWS
  - Cloud is an extension of your datacenter – access using private IP
  - Consistent network performance and throughput
  - For HA, use multiple DX Locations or use a backup VPN over the internet
  - cost of transferring data from aws to data center is significantly lower than transferring data over the public internet
  - __no encryption__
  - Complex setup:
    - AWS has 100+ Direct Connect locations worldwide. Choose the one closest to your data center.
    - Access resources in any of the AWS regions
    - For Critical workloads, use two Direct Connect locations (location or device failure)
- A Direct Connect gateway is a global resource that __allows VPCs in any AWS Region (except China) to connect to Direct Connect via virtual private gateways__ (VGWs). 
- By connecting both Direct Connect links to the same DX gateway and associating the __VGWs of all relevant VPCs, the company can enable transitive routing across Regions and between on-premises locations and VPCs__ — without setting up complex peering or custom VPN appliances.

- __Combine Direct Connect and a VPN connection__: In this case, you're actually using a VPN connection over your Direct Connect link. Why would you do that? Well, you get an encrypted tunnel over your Direct Connect connection. So, it's more secure in theory at least than Direct Connect alone.

- __VPN CloudHub__
  - What: connect your locations in a hub and spoke manner using AWS's Virtual Private Gateway. So, it's VPN connections from multiple office locations or multiple data centers that you might have.
  - When: linking your remote offices for backup or primary WAN access to AWS resources and to each other because it will route between them as well.
  - Pros: reuses existing Internet connections and supports BGP routes to direct traffic.
  - Cons: is dependent on internet connections again and there's no inherent redundancy.
  - How: assign multiple customer gateways to a virtual private gateway, each with their own BGP ASN and unique IP ranges.
- __Software VPN__:
  - What: provide your own VPN endpoints and software.
  - Whan: You have to manage both ends of the connection. It's a software layer.
  - Pros: flexibility and manageability options.
  - Cons: you need to design for any kind of redundancy as well.
  - How: In terms of actually deploying a software VPN, there's lots of different options out there: can also use the marketplace to find an EC2 instance with pre-packaged software.
- __Transit VPC__:
  - What: strategy where you're connecting geographically dispersed VPCs in a hub and spoke manner with AWS managed VPNs. So then you have one VPC that's configured as the network transit center for the other VPCs.
  - When: Locations and VPC-deployed assets across multiple regions that need to communicate with each other.
  - Pros: flexibility and manageability and also AWS-managed VPN hub-and-spoke between VPCs.
  - Cons:  define any redundancy that you need across the whole chain.
  - How: there are some third-party providers (Cisco, Juniper) that also offer equipment that can be used with your VPCs and help you to configure a transit VPC.
- __VPC peering__:
  - What: provide connectivity between VPCs and they need to have that connectivity via private IP addresses.
  - Whan: Multiple VPCs need to communicate.
  - Pros: use the AWS backbone without traversing the Internet
  - Cons: no transitive peering supported.
  - How: VPC peering request created, accepted,
    - you need to create a route
- __VPC Endpoints__:
  - __Interface Endpoint__
    - What: it's an elastic network interface with a private IP.
    - How: It uses DNS entries to redirect traffic. 
    - Interface endpoint __creates a network interface with private IP__
    - Which services: many services including API Gateway CloudFormation and CloudWatch.
    - Security: security groups which you can assign as well, so you can apply your security groups to your interface.
    - Interface endpoints are also known as __PrivateLink__
    - For HA, create an interface endpoint in each AZ
  - __Gateway Endpoint:__
    - What: this is a target for a specific route
    - How: uses prefix lists in the route table to redirect traffic.
    - And this is for Amazon S3 and DynamoDB only.
    - Security: You can't use security groups, but you can use VPC endpoint policies.
- __Flow Logs__:
  - can capture information about the IP traffic going to and from network interfaces in a VPC.
  - The flow log data is stored using CloudWatch logs or Amazon S3 or Kinesis
  - can be created at different levels: The VPC level, subnet level, or the network interface level.

__VPC Transit Gateway__
- can connect many: VPCs, VPNs, Direct Connect, peering connections.
- must be in the same AWS account and region
- multiple regions: setup Transit Gateway in each region
- add transit gateway attachment for each VPC
- add route table entries

The VPC router connects different AZs together and connects the VPC to the Internet Gateway

__Internet Gateways__ (IGW) must be created and then attached to a VPC, be added to a route table, and then associated with the relevant subnet(s)
IGW is horizontally scaled, redundant and HA and performs NAT between private and public IPv4 addresses
Internet Gateway requires public IP. Else not traffic will go in or out.

Public subnet:
- Auto-assign public IPv4 address” set to 'Yes'.
- If your subnet is associated with a route to the Internet

You have to create Route Table
- main route table is created when you create VPC. It is automatically associated with all subnets
- separate route table for public (create new) and private subnets (main route table)
- associate public subnet with public route table and
- add route to Internet Gateway (destination: 0.0.0.0/0; target: InternetGateway)

To enable access to or from the Internet for instances in a VPC subnet, you must do the following:
- Attach an Internet Gateway to your VPC
- Ensure that your subnetʼs route table points to the Internet Gateway
- Ensure that instances in your subnet have a globally unique IP address
- Ensure that your network access control and security group rules allow the relevant traffic to flow to and from your instance

__Managed Prefix List__
- one or more CIDR blocks
- use it in VPC security groups, subnets, transit gateway tables, firewall etc
- use it for outboud traffic
- Example:
  - Instead of allowing 0.0.0.0/0 or manually maintaining all S3 IP ranges, you can do:
  ```
  {
    "IpProtocol": "tcp",
    "FromPort": 443,
    "ToPort": 443,
    "PrefixListId": "pl-63a5400a"
  }
  ```
  - Bad solution:
  ```
  Type: HTTPS
  Protocol: TCP
  Port Range: 443
  Destination: 52.216.0.0/15
  Destination: 54.231.0.0/17
  ...
  ```

### VPC Endpoint <a id="VPCEndpoint"></a>

- powered by PrivateLink: provides private connectivity between VPCs, AWS services and on-premises aapplications using amazon network (not internet)
- Gateway endpoint ( Dynamodb or S3): you need to define route table target in route table
- Interface endpoint: ENI with private IP
- Gateway Load Balancer endpoint:
- Limits to access specific service (through load balancer). VPC Peering - access everything
- Endpoint is always in the same region
- To access endpoint from another region use VPC peering
- Gateway endpoints work through route tables, not the Internet Gateway.

Interface Endpoint:
![ Gateway endpoints ](./images/interface_endpoints.jpg)

Gateway endpoints:
![ Gateway endpoints ](./images/gateway_endpoints.jpg)

DHCP - dynamic host connection protocol
- router provides IP for host
- you can have custom DHCP option set

### Cost Optimization Hub

Use AWS Cost Optimization Hub to get a report of Amazon EC2 instances that are either idle or have low utilization and use AWS Compute Optimizer to look at instance type recommendations

Cost Optimization Hub is an AWS Billing and Cost Management feature that helps you consolidate and prioritize cost optimization recommendations across your AWS accounts and AWS Regions, so that you can get the most out of your AWS spend. You can use Cost Optimization Hub to identify, filter, and aggregate AWS cost optimization recommendations across your AWS accounts and AWS Regions. It makes recommendations on resource rightsizing, idle resource deletion, Savings Plans, and Reserved Instances. With a single dashboard, you avoid having to go to multiple AWS products to identify cost optimization opportunities.

AWS Compute Optimizer provides Amazon EC2 recommendations to help you improve performance, save money, or both. You can use these recommendations to decide whether to change to a new instance type. To make recommendations, Compute Optimizer analyzes your existing instance specifications and utilization metrics. The compiled data is then used to recommend which Amazon EC2 instance types are best able to handle the existing workload.


### Architecture Patterns

#### An Amazon S3 bucket must only allow access from EC2 instances in a private subnet using private IPs.

Create a VPC endpoint and configure a bucket policy that restricts access to the VPC endpoint ID using the condition elements.

#### Malicious traffic is reaching some EC2 instances in a public subnet from a few identified public IP addresses.

Use a network ACL to deny access based on the source IP addresses.

#### A company wants to connect their on-premises data center to AWS and requires consistent performance and encryption.

Create a Direct Connect connection. But you can't get encryption on a Direct Connect connection, so you have to run a site-to-site VPN over the top.

- AWS Direct Connect → for consistent performance
- AWS Site-to-Site VPN → for encryption + backup
- AWS Transit Gateway → for scalable architecture

Direct Connect HA
- Use 2 separate DX connections
- Ideally:
  - Different locations
  - Different providers

VPN HA
- Site-to-Site VPN provides:
  - 2 tunnels automatically
  - Each tunnel to different AWS endpoints

```
                    ┌────────────────────────────┐
                    │     On-Prem Data Center    │
                    │   (Router / Firewall)      │
                    └─────────────┬──────────────┘
                                  │
                     ┌────────────┴────────────┐
                     │                         │
         Primary (Performance)        Encryption + Backup
                     │                         │
                     ▼                         ▼
      ┌────────────────────────┐    ┌────────────────────────┐
      │ Direct Connect Location│    │   Internet (Public)     │
      │   (DX POP Facility)    │    └────────────┬───────────┘
      └────────────┬───────────┘                 │
                   │                             ▼
                   ▼                 ┌────────────────────────┐
        ┌──────────────────────┐     │ Site-to-Site VPN       │
        │ Direct Connect GW    │     │ (IPsec - Encrypted)    │
        └──────────┬───────────┘     └────────────┬───────────┘
                   │                              │
                   └──────────────┬───────────────┘
                                  ▼
                    ┌──────────────────────────┐
                    │   Transit Gateway (TGW)  │
                    │   (Regional, HA)         │
                    └─────────────┬────────────┘
                                  │
                ┌─────────────────┼─────────────────┐
                ▼                 ▼                 ▼
        ┌────────────┐    ┌────────────┐    ┌────────────┐
        │   VPC A    │    │   VPC B    │    │   VPC C    │
        │ (Multi-AZ) │    │ (Multi-AZ) │    │ (Multi-AZ) │
        └────────────┘    └────────────┘    └────────────┘
```

#### A company requires private connectivity between VPCs in different regions with full redundancy.

Create VPC peering connection between the VPCs.

AWS Transit Gateway with Inter-Region Peering

Transit Gateway supports inter-region peering

Enables VPC-to-VPC communication across regions

#### Several remote office locations should be connected to an Amazon VPC and to each other over the internet with full encryption.

Create a VPG and attach multiple remote locations in a hub and spoke topology, and that's an AWS cloud hub topology.

#### Microservices app requires instance level firewall with different rules per application component.

Classic case for security groups for each application component, and you just need to make sure you configure the appropriate rules.

#### A company is using IPv6 addresses with Amazon EC2 and needs to enable outbound internet connectivity.

Rather than an Internet gateway, you need an egress only Internet gateway. That's for IPv6.

#### A subnet must be configured that allows internet connectivity using IPv4 with auto address assignment.

Attach an Internet gateway to the VPC, update the route table so, for the new subnet and then enable the auto assigned public IPv4 setting for the subnet as well.

#### An on-premises data center needs to establish site-to-site VPN connections to several VPCs in a full mesh architecture.

Deploy an AWS transit gateway, attach the VPN connection from the on-premises and then attach it also to each VPC.

#### How would you increase the availability of your VPN setup between on-premises and AWS cloud?

Use a single virtual private gateway (VGW) and two customer gateways (CGW). VGWs are highly available and can tolerate AZ failure

#### What capability can you use for auditing inbound and outbound traffic in your VPC?

VPC Flow Logs capture detailed information about IP traffic going in and out of network interfaces in your VPC.

#### How would you increase the availability of your Direct Connect link between on-premises and AWS Cloud?

To avoid a single point of failure, you need to consider using two different direct connect locations for critical workloads. 
This will protect you from device failures and direct connect location outages

#### When a NAT Gateway is deployed in a VPC, it:

- Resides in a public subnet
- Scales inside one availability zone

#### You are hired to help with migrating a customer's solution to the AWS Cloud. Customer wants to perform a phased migration strategy and they would like to first run couple of webservers on AWS that points to existing on-premises database. Application requests should routed across webservers in AWS as well as webservers located on-premises.  Which load balancing product can be used for this requirement?

Both Application and Network Load Balancers allow you to add targets by IP address. You can use this capability to register instances located on-premises and VPC to the same load balancer.

An AWS Application Load Balancer can route traffic to:
- ✅ On-premises data center (via IP addresses)
- ✅ Auto Scaling group in AWS (via instances)
- BUT they must be in separate target groups.

#### An e-commerce company operates multiple AWS accounts and has interconnected these accounts in a hub-and-spoke style using the AWS Transit Gateway. Amazon Virtual Private Cloud (Amazon VPCs) have been provisioned across these AWS accounts to facilitate network isolation. Which of the following solutions would reduce both the administrative overhead and the costs while providing shared access to services required by workloads in each of the VPCs?

Build a shared services Amazon Virtual Private Cloud (Amazon VPC)

Consider an organization that has built a hub-and-spoke network with AWS Transit Gateway. 
VPCs have been provisioned into multiple AWS accounts, perhaps to facilitate network isolation or to enable delegated network administration. 
When deploying distributed architectures such as this, a popular approach is to build a "shared services VPC, which provides access to services required by workloads in each of the VPCs. 
This might include directory services or VPC endpoints. 
Sharing resources from a central location instead of building them in each VPC may reduce administrative overhead and cost.

A VPC endpoint allows you to privately connect your VPC to supported AWS services without requiring an Internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. 
Endpoints are virtual devices that are horizontally scaled, redundant, and highly available VPC components. 
They allow communication between instances in your VPC and services without imposing availability risks or bandwidth constraints on your network traffic.

A Shared Services VPC is a centralized VPC that hosts services used by multiple VPCs or accounts, such as:
- Directory services (AD)
- DNS resolvers
- Bastion hosts / jump boxes
- Logging / monitoring
- CI/CD tools
- Security appliances

```
                ┌──────────────────────────────┐
                │  Shared Services VPC         │
                │                              │
                │  - AD / Directory            │
                │  - DNS (Route 53 Resolver)   │
                │  - Bastion / Jump Host       │
                │  - Logging / Security Tools  │
                └────────────┬─────────────────┘
                             │
                     Transit Gateway
                             │
     ┌───────────────┬───────────────┬───────────────┐
     ▼               ▼               ▼
 App VPC A      App VPC B      App VPC C
 (Account A)    (Account B)    (Account C)
```

Steps:
- Create Shared Services VPC
  - CIDR: e.g. 10.0.0.0/16
  - Multi-AZ subnets
- Deploy Core Shared Services
  - Bastion host (for admin access)
  - Central logging agents
- Create Transit Gateway (TGW)
  - Attach: Shared Services VPC, All application VPCs
- Connect Application VPCs
- Use AWS Resource Access Manager to share:
  - Subnets
  - Transit Gateway
  - Route 53 rules

#### A national logistics company has a dedicated AWS Direct Connect connection from its corporate data center to AWS. Within its AWS account, the company operates 25 Amazon VPCs in the same Region, each supporting different regional distribution services. The VPCs were configured with non-overlapping CIDR blocks and currently use private VIFs for Direct Connect access to on-premises resources. As the architecture scales, the company wants to enable communication across all VPCs and the on-premises environment. The solution must scale efficiently, support full-mesh connectivity, and reduce the complexity of maintaining separate private VIFs for each VPC. Which combination of solutions will best fulfill these requirements with the least amount of operational overhead?

- Create an AWS Transit Gateway and attach all 25 VPCs to it. Enable route propagation for each attachment to automatically manage inter-VPC routing
Attaching all VPCs to a single AWS Transit Gateway centralizes routing and allows for transitive communication between the VPCs. Enabling route propagation eliminates the need to manually update route tables for every VPC. This design supports scalable, full-mesh VPC connectivity with low operational burden.
- Create a transit virtual interface (VIF) from the Direct Connect connection and associate it with the transit gateway
Using a transit VIF from the Direct Connect connection to the transit gateway enables on-premises-to-VPC connectivity through a single, centralized path. This eliminates the need to maintain multiple private VIFs and simplifies BGP management and route aggregation. Combined with Option A, this forms a highly efficient hub-and-spoke architecture.

#### A retail company is using AWS Site-to-Site VPN connections for secure connectivity to its AWS cloud resources from its on-premises data center. Due to a surge in traffic across the VPN connections to the AWS cloud, users are experiencing slower VPN connectivity. Which of the following options will maximize the VPN throughput?

Create an AWS Transit Gateway with equal cost multipath routing and add additional VPN tunnels

VPN connection is a secure connection between your on-premises equipment and your VPCs. Each VPN connection has two VPN tunnels which you can use for high availability. A VPN tunnel is an encrypted link where data can pass from the customer network to or from AWS. The following diagram shows the high-level connectivity with virtual private gateways.

With AWS Transit Gateway, you can simplify the connectivity between multiple VPCs and also connect to any VPC attached to AWS Transit Gateway with a single VPN connection. AWS Transit Gateway also enables you to scale the IPsec VPN throughput with equal cost multi-path (ECMP) routing support over multiple VPN tunnels. A single VPN tunnel still has a maximum throughput of 1.25 Gbps. If you establish multiple VPN tunnels to an ECMP-enabled transit gateway, it can scale beyond the default maximum limit of 1.25 Gbps. You also must enable the dynamic routing option on your transit gateway to be able to take advantage of ECMP for scalability.

#### When would you use a VPC Endpoint instead of a NAT Gateway?

VPC Endpoint: Private, internal-only access to AWS services (S3, DynamoDB, etc.)
- Traffic never goes to the internet.
- Lower latency and cost for large S3/DynamoDB traffic.

NAT Gateway: Provides internet access for private subnets.
- Charges per GB and per hour.
- All outbound traffic goes via internet → potential exposure.

#### How can you audit all traffic in your VPC? Can VPC Flow Logs capture all packets?

- VPC Flow Logs capture metadata: source/destination IP, port, protocol, accept/reject.
- Cannot capture payloads → for packet inspection, use traffic mirroring.
- Can be published to CloudWatch Logs or S3 for auditing.
- Works per ENI, subnet, or VPC level.












## Amazon Simple Storage Service <a id="S3"></a>

You can store any type of file.

Files can be anywhere from __0 bytes to 50TB__.

There is virtually unlimited storage available.

S3 is a __universal namespace, so bucket names must be unique globally__.

You have to __create your buckets within a specific region__.

There's __no hierarchy__ for objects within a bucket.

S3 delivers __strong read-after-write consistency__.

- HA: 99.99% (standard)
- Max file size 50TB
- Data Consistency: 
  - read-after-write for PUTS of new objects
  - eventual consistency for overwrite PUTs and DELETE
- NOT GOOD for:
  - low latency access
  - many small files
  - frequent updates
  - data transactions

S3 Buckets:
- Files get stored in buckets
- the bucket can be viewed as a container for the objects.
- It's a flat container of objects with no hierarchy
- you can use an object key name or a prefix to mimic folders.
- 100 buckets per account by default as a limit,
- you can store unlimited objects in your buckets.
- cannot create nested buckets, so a bucket will never go inside another bucket.
- globally unique
- 3-63 chars long
- lowercase, numbers, hyphens, dots
- must start with letter or number
- cannot look like IP
- Bucket type: __general purpose__ (choose region) OR __directory__ (choose Region+AZ)

S3 objects:
- Objects are the files that you upload to S3.
- S3 supports any file type.
- each object is stored and retrieved by a unique key.
- Objects remain in the region in which they're stored unless you set up replication.
- Permissions can be defined on objects at any time.
- The storage class is set at the object level.

S3 Lifecycle rules
- automated changing storage class 
- applied to filtered objects: prefix, tags, object size (range)
- you can setup for versioned and not versioned objects

By default __bucket owner__ pays for: storage, data transfer, PUT or GET user requests
__Requester__ if authenticated (must have aws account) can be made to pay for: data transfer and request cost. Requested must have a specific http header. To enable it you must:
- make S3 bucket public
- create bucket policy to everyone to access
- set __'requester pay' option in 'properties'__. It makes the bucket not available to anonymous access.
- requested must use __x-amz-request-payer header__.

__S3 pre-signed url__: __allow access to private S3 objects for limited time__
- downloading and uploading
- create it using:
  - aws sdk
  - aws cli
  - aws console

__S3 MFA delete for bucket__: must aws cli and you must have MFA on for your aws user.

__VPC Gateway Endpoint for S3__
- only S3 and DynamoDB
- no additional cost
- integrates directly into VPC route table (creates entry)

__S3 Access Point__
- Instead of giving every application direct access to the same bucket with complicated policies, you create multiple access points, each with its own permissions and network controls.
- An S3 Access Point is a custom doorway into an S3 bucket with its own permissions and network rules
- you can always use url to s3
- S3 access point help you to control who and how they can access S3 bucket
- Useful if bucket is accessed from many (like 500) applications/users  (doing it in bucket policy will be complex)
- Simplified bucket policy
- ability to restrict access from specific VPC of IP address
- support network based restrictions
- you have to delegate your __bucket policy__ to delegate the management to access point
  - Before access points existed, everything was controlled through one bucket policy.
  - problem:
    - One policy becomes very large and hard to manage
    - Risk of breaking permissions for other apps

__S3 Object Lambda__: Feature: Modify S3 data dynamically before returning it to users.

### Storage classes <a id="S3StorageClasses"></a>

- __Standard__: pay per day
- __Infrequent access__: accessed 1/month, HA 99.9, retrieval fees, >128KB, at least 30 days
- __Intellingenmt tiering:__ unknown access pattern, HA 99.9, 30 days
- __IA One zone__: use for data that can be re-created. HA: 99.5%, retrieval fees, >128KB
- __Express one zone__: high performance, single zone to deliver consistent single-digit millisecond latency. AI. 10* faster then Standard, Requires 'directory' bucket
- __Glacial Instant retrival__: long lived, few times per year fast retrival. >90days. Good for backup
- __Glacier flexible retrival__: rarely accessed: good for archive or backup. >90days. Retrival within min-hours
  - Backup storage: disaster recovery, potentially frequent access, fast retrival speed
- __Glacier Deep Archive:__ rarely accessed, use for archive. retrival in >12 hours, >180 dyas
  - Archive: long term data preservation, infrequent access, slow retrival speed

Data Access Pattern:

| S3 Storage Class  | Standard            | Infrequent Access       | Glacier Deep Archive
|-------------------|---------------------|-------------------------|-------------------------
| Access            | Immediate           | Immediate               | Several hours
| Usage             | Frequently Accessed | Less frequently accessed| Rarely accessed
| Monthly Cost 500GB| USD 11.50           | USD 6.25                | USD 0.50
| Retrieval Fee     | N/A                 | Per GB                  | Per GB
| Redundancy        | 3 AZ                | 3 AZ                    | 3 AZ


![ Storage classes ](./images/s3_storage_classes.png)

![ Storage classes comparison ](./images/s3_comparison.jpg)
 
### Controlling access to AWS S3 Buckets <a id="S3Access"></a>

__IAM Policy__
- applies to all AWS services
- __attached to IAM users, groups, roles__
- IAM policies are identity-based policies.
- The principal is not defined within an IAM policy.
- complex for cross-account access
- cannot deny public access to bucket
- IAM policies if you need to control access to AWS services other than as S3.
- numerous S3 buckets, each with different permissions requirements, IAM policies will turn out to be a lot easier to manage.
- if you prefer to keep access control policies in the IAM environment.
- example custom policy for IAM user:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowFullAccessToTestBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::test-bucket",
        "arn:aws:s3:::test-bucket/*",
        "arn:aws:s3:::my-bucket-name/my-folder/specific-file.txt"
      ]
    }
  ]
}

```

__Bucket Policy__
- used only for S3 resources
- __attached to S3 buckets__
- simple __cross-account access__
- explicit public access control like: Fine-grained IP or condition-based rules
- you have to provide principal
- Bucket policies are resource-based policies.
- Bucket policies, they can only be attached to Amazon S3 buckets.
- you __can assign the same policy to many S3 buckets, but not directly__ by referencing one policy across multiple buckets
- __cannot assign a bucket policy directly to an individual S3 object__.
- Common Uses of Bucket Policies
  - ✅ Public file hosting
  - ✅ Cross-account access
  - ✅ Restrict access by IP
  - ✅ Enforce HTTPS
  - ✅ Allow CloudFront access
- example of bucket policy that will protect S3 bucket:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowReadOnlyToSpecificUser",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/krzysztof"
      },
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::test-bucket",
        "arn:aws:s3:::test-bucket/*",
        "arn:aws:s3:::my-bucket-name/documents/myfile.txt"
      ]
    }
  ]
}
```

| Feature              | Bucket Policy             | IAM Policy           |
| -------------------- | ------------------------- | -------------------- |
| Policy type          | Resource-based            | Identity-based       |
| Attached to          | S3 bucket                 | IAM user/role/group  |
| Controls             | Who can access the bucket | What the user can do |
| Cross-account access | Very common               | Harder               |
| Public access        | Yes                       | No                   |
| Scope                | Single bucket             | Many AWS services    |


__S3 ACL = Access Control Lists__ - disabled by default
- These are a legacy access control mechanism.
- AWS will generally recommend using S3 bucket policies or IAM policies rather than ACLs.
- They can be attached to a bucket or directly to an object,
- limited options for the grantees and the permissions that you can apply.
- Not as good as JSON-based IAM policy.
- provides way to grant access to specific account or authenticated group (created by aws like: everyone or authenticated only)
- cannot be used to grant access to IAM resources
- can be attached to bucket or specific object
- __can setup different owner of S3 bucker and different for S3 object__
- __Applied in the order above__. Access policies must be attached explicitly.
- Use it when:
  - simple way to grant cross account access to S3 without using IAM roles.
  - if your IAM policies are reaching the size limits,
  - you prefer to keep access control policies in S3.

__S3 Versioning__:
- enable in __bucket__ (default disabled) or __object__
- Versioning is a means of keeping multiple variants of an object in the same bucket.
- You use versioning to preserve, retrieve, and restore every version of the object stored in your S3bucket.
- Versioning enabled buckets will enable you to recover objects from accidental deletion or overwrites.

__Lifecycle management__:

![ Lifecycle management ](./images/s3_life_cycle_management.png)

Archive Flow – Intelligent Tiering:

![ Intelligent Tiering ](./images/intelligent_tiering.jpg)
 
__Multi-Factor Authentication Delete__:
- Adds an MFA requirement for bucket owners to the following operations:
  - changing the versioning state of a bucket
  - permanently deleting an object version,
- The x-amz-mfa request header must be included in the above requests.
- The second factor of authentication is generated by a hardware device or software program like an authenticator app such as the Google Authenticator app that we've used in this course. It does require versioning to be enabled on the bucket.
- Versioning can be enabled by:
  - bucket owners,
  - the root account,
  - AWS account that created the bucket,
  - authorized IAM users.
- MFA Delete can be enabled by the bucket owner only.

__Protected API access with MFA__:
- This is used to enforce another authentication factor, an MFA code when accessing resources and not just S3.
- It's enforced using the AWS MultiFactorAuthAge key in a bucket policy.

__Event notifications__:
- this is where S3 sends notifications when an event happens in an S3 bucket.
- The destinations include SNS, SQS, and Lambda.
- created when: object deleted, created, updated
- good for: automated workflows, real-time notification

__Multipart upload__:
- uploads objects in parts, independently, in parallel and in any order
- It's performed using the Multipart upload API
- recommended for objects __above 100 MB__.
- can be used for objects from 5MB up to the maximum file size, which is __50TB__.
- it has to be used for any objects larger than 5GB.
- Multipart upload to Amazon S3 does support __retries__
  - AWS SDK (Java, Python, Node, etc.)
    - Most SDKs automatically retry failed parts using built-in retry logic.
  - AWS CLI: retries automatically.
__S3 Multipart Upload__ (mandatory for files >5GB):
- get uploadId: 
  ```
  aws s3api create-multipart-upload --bucket kjbucket --key kjfilename
  ```
- compress + split file ( 7-zip )
- upload file parts <5MB
  ```
  aws s3api upload-part --bucket kjbucket --key kjfilename --part-number 1 --upload-id <id> --body .\you_file_name_part
  ```
- get ETag to track
- send request with uploadID and ETAGs to assemble file
  ```
  aws s3api complete-multipart-upload --bucket....
  ```

__S3 copy API__:
- you can copy objects __up to 5GB__.
- it can be used to:
  - generate additional copies of objects,
  - rename objects,
  - change the storage class or encryption at rest status,
  - move the objects between AWS locations and regions.
  - You can also change the object metadata.

__Server Access Logging__:
- __summary level__ record of requests in plain text made to S3 bucket
- provides detailed records for the requests that are made to a bucket.
- information that is logged includes the requester, the bucket name, the request time, request action, response status, and the error code.
- It's disabled by default.
- you only pay for the storage space that's actually used.
- You must configure a separate bucket as the destination,
- you can specify a prefix if you want to.
- You must also grant write permission to the Amazon S3 Log Delivery group on the destination bucket.

__Cloud Trail events__: logs in json of all actions on your objects - __all details__ like: requestor, operation

__Cross Account Access Methods:__
- Resource-based policies and IAM policies can be used for programmatic access to S3 bucket objects,
- resource-based ACL and IAM policies for programmatic access to S3 bucket objects as well.
- If you need programmatic and console access, you can use cross account IAM roles.

__Performance optimizations__:
- S3 does support at least 3,500 PUT, COPY, POST, DELETE, or 5,500 GET HEAD requests per second __per prefix__ in a bucket.
  - to reach 10,000 PUT/sec, you simply distribute the requests across multiple prefixes
  - A prefix is the logical path before the object name.
  - Example objects: bucket/logs/a/file1 preffix is: logs/a
- You can increase, read or write performance by parallelizing reads.
  - multiple requests happen at the same time instead of sequentially
- You can use Byte-Range Fetches.
- You can retry requests for latency sensitive applications
- you can combine S3 and EC2 in the same region for better performance.
- you can use Amazon S3 Transfer Acceleration to minimize any latency caused by long distances.

#### Amazon S3 and Glacier

A bucket owner can grant cross-account permissions to another AWS account (or users in an account) to upload objects.
- The AWS account that uploads the objects owns them.
- The bucket owner does not have permissions on objects that other accounts own, however:
  - The bucket owner pays the charges.
  - The bucket owner can deny access to any objects regardless of ownership

You can use the AWS Policy Generator to create a bucket policy for your Amazon S3 bucket.

Bucket and object permissions are independent of each other.

### Transfer acceleration <a id="S3TransferAcceleration"></a>

Amazon S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and your Amazon S3 bucket.

S3 Transfer Acceleration leverages Amazon CloudFrontʼs globally distributed AWS Edge Locations.

Transfer acceleration is as secure as a direct upload to S3

- improving the performance of transfers of files,
- leverages the CloudFront edge locations.
- Used to accelerate uploads of objects over long distances, so you're reducing latency.
- Transfer Acceleration is as secure as a direct upload to S3,
- you're charged only if there's a benefit in the transfer time.
- You need to enable Transfer Acceleration on the S3 bucket. It cannot be disabled after that, but only suspended.
- it is using aws global network and edge locations
- speeds-up 50-500% faster
- enable it and get new url
- you can perform PUT, POST, and DELETE, along with other standard object operations

Must use one of the following endpoints:
- .s3-accelerate.amazonaws.com.
- .s3-accelerate.dualstack.amazonaws.com (dual-stack option)

### S3 encryption <a id="S3Encryption"></a>

S3 encryption:
- SSE-S3, using S3's existing encryption key for AES 256 encryption.
- SSE-C you're uploading your own AES 256 encryption key, which S3 then uses for you.
- SSE-KMS is where you're using KMS keys
  - Amazon S3 Bucket Keys reduce the cost of Amazon S3 server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS). Using a bucket-level key for SSE-KMS can reduce AWS KMS request costs by up to 99 percent by decreasing the request traffic from Amazon S3 to AWS KMS. Enabling S3 Bucket Keys with SSE-KMS allows S3 to generate a unique data key for each object locally using a bucket-level KMS key, which dramatically reduces the number of direct AWS KMS API calls. This approach maintains the same security and compliance properties as SSE-KMS, while reducing request-related costs—especially beneficial for workloads with frequent access or write operations.
- client-side is where you have your own encryption keys and you're managing the encryption as well. There's no encryption happening on AWS you're doing it before you upload your objects.

- uses symmetric encryption
- SSE (server side): happens on server side
  - key management: 
   - aws managed keys (SSE-S3, KMS)
     - SSE-S3 - aws manages the keys , you can change encryption per object, uses AES0256, __automatic key rotation__, no audit logging
     - KMS - aws managed or customer managed key. rotation manual or automatic when you schedule, Auditing using cloud-trail. Objects can be accessed only by user who created/owns KMS key
       - access control: you can add key users
       - custom key rotation
    - Dual layer SSE with KMS: data encrypted twice: S3 + AWS KMS. FIPS requires it.
   - you provide keys (SSE-C): 
     - you manage they keys outside of aws
     - provide keys when uploading/downloading the object
     - create key using OpenSSL: 
      ```
      # create key
      openssl rand 32 > sse-c.key 
      # encode it to base64
      key=$(cat sse-c.key | base64)
      # create md5 hash
      keymd5=$( cat sse-c.key | openssl dgst -md5 -binary | base64)
      ```
      - aws console cannot open this file
- CSE (client side)
  - need to use AWS encryption SDK or OpenSSL or other to encrypt

__S3 Public access:__
- set 'block all public access' on the bucket: account level or bucket level
- set one of:
  - set 'ACL':
    - set 'everyone public access'
  - 'Bucket Policy' (recommended):
    - create bucket policy (see above): PublicReadGetObject, Principal: *

### Static Websites <a id="S3StaticWebsite"></a>

You can use a custom domain name with S3 using a __Route 53 Alias record__.

When using a custom domain name the __bucket name must be the same as the domain name__.

Only supports __GET and HEAD requests__ on objects.

To enable website hosting on a bucket, specify:
- Bucked should be marked __'static website'__
- Bucket - __public read access__ for bucket and all docs
- __disable block public access settings__
- Bucket __permissions__: add an object access control list (ACL) that grants __everyone read access__.
- Define An __index.html__ document (default web page) and optionally error.html document.
- define __DNS entry__
  - __register custom domain name__
  - create 2 buckets:
    - __Domain bucket__ – __example.com__. Configure your root domain bucket for website hosting
    - __Subdomain bucket__ – __www.example.com__. Configure your subdomain bucket for website redirect
  - Add __alias records__ for your domain and subdomain
- __only http__ (no s). if you want https: use cloudFront

- register domain name: krzysztof.pl
- __create S3 bucket__: bucket name: web.krzysztof.pl
- __upload files__: index.html etc.
- S3 bucket: __make s3 bucket public__: 'public access off'
- __create bucket policy__
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```
- S3 bucket: __enable static website hosting__ and specify index.html etc. page
- __change DNS record__ in domain registrar and __change name servers__
- __Create public hosted zone in Route 53 with A or CNAME record__ and point DNS to S3 website endpoint
- Use Amazon __CloudFront for HTTPS support__ 

__AWS S3 Cross-origin resource sharing (CORS)__
- it is a way to request resources from different domain (javascript 'fetch')
- browsers will block it
- with Permissions -> CORS you can still do it by adding CORS rules to the bucket:
```
<CORSConfiguration>
  <CORSRule>
    <AllowedOrigin>https://example.com</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
  </CORSRule>
</CORSConfiguration>
```

CORS with Amazon S3:
- is enabled through setting:
  - the access-control-allow-origin,
  - access-control-allow-methods,
  - access-control-allow-header.
- These settings are defined using rules
- the rules are added using JSON files in Amazon S3.

Example problem without CORS:
- If the browser tries to fetch or upload a file from S3, the request may be blocked by the browser unless the S3 bucket explicitly allows it via CORS configuration
```
Frontend app: https://app.example.com
S3 bucket:    https://mybucket.s3.amazonaws.com
```

### S3 Object Lock <a id="S3ObjectLock"></a>

S3’s Object Lock feature allows you to enforce the “Write Once Read Many” (WORM) paradigm. 
In this paradigm, an object version cannot be modified or deleted; however, it is available for reading.

S3 Object Lock protects your data from accidental and malicious deletion Object Lock needs to be enabled at Bucket Level. 
This feature also automatically enables versioning.

Prevent deletion of objects (even life cycle policy cannot delete it)
- retention mode: rules that define how strictly the object is protected
  - Governance Mode: Protected from most users, but authorized users can override with special permission
  - Compliance Mode: Absolute enforcement — no one, not even the root user, can delete or modify the object until the retention period expires
- retention period
- Legal hold: indefinite time.
- Versioning must be enabled
- one S3 object lock is enabled, it cannot be disabled or versioning cannot be suspended.
- can be set on bucket or individual object
- You can place a __retention period on an object version either explicitly or through a bucket default setting__. When you apply a retention period to an object version explicitly, you specify a Retain Until Date for the object version. Amazon S3 stores the Retain Until Date setting in the object version's metadata and protects the object version until the retention period expires.
- Like all other Object Lock settings, __retention periods apply to individual object versions__. Different versions of a single object can have different retention modes and periods.


Why can’t you enforce the WORM paradigm using IAM policies?
The issue with IAM policies are:
- The root user has full access and can remove objects
- Identity and Resource-based policies may not be sufficient to comply with legal hold notice
- It may not be easy to enforce operationally

There are three ways in which you can use Object Lock:
- __Legal Hold__.
  You can place an object version on legal hold (__s3:PutObjectLegalHold__).
  When a legal hold is in place, the object version cannot be deleted.
  Lifecycle policies cannot delete an object version with a legal hold.
  This feature lets you keep an object version for as __long as needed__
  Once the legal hold is removed, the object version can be deleted.
  To remove a Legal Hold on an object in Amazon S3, you must disable the legal hold status for that specific object version.
- __Retention Period__
  We can also protect an object version from deletion or modification by __specifying a retention period__
  - In __Governance Mode__, anyone with __S3:BypassGovernanceRetention__ permission can override retention configuration and delete the object version
  - In __Compliance Mode__, the __Object version cannot be deleted by anyone__ (including the root user) until the retention period expires.

### AWS S3 Cross-region replication (CRR) <a id="S3CRR"></a>

__Cross Region Replication requires versioning__ to be enabled on the source and destination buckets.

__Replication is 1:1__ (one source bucket, to one destination bucket).
You can configure __separate S3 Lifecycle rules on the source and destination buckets__.

- automatically replicates every object in another region in the __same or different account__
- inserts or updates are replicated
- you __can change storage class__ in the destination
- you must have __versioning enabled__
- must have __IAM role with permissions__ to perform replication (read from source bucket and write to destination bucket)
- __Define rules__ how to do replication
  - __replication time control__: guarantee replication time, include SLA, metrics
  - __replication metrics__: detailed monitoring
  - __delete marker replication__: object will not be deleted (replication marker) in destination - good for backup
  - __replica modification sync__: changes made to replicated copies are sync back to source bucket


### S3 Limits

- Storage Limits:
  - Unlimited Storage: You can store an unlimited amount of data in S3. 
  - Individual Object Size: Objects can range from 0 bytes to 50 TB in size. 
Single PUT Operation: The largest object you can upload in a single PUT operation is 5 GB. 
Multipart Upload: For objects larger than 100 MB, it's recommended to use the Multipart Upload feature for optimal performance. 
Bucket Size: There is no limit on the total size of data stored in a bucket. 
Number of Buckets: Amazon S3 now supports up to 1 million buckets per AWS account. 
Directory Buckets: S3 directory buckets, which only support S3 Express One Zone storage class, can support up to 2 million transactions per second. 

- Request Rate Limits:
  - PUT/COPY/POST/DELETE:  3,500 requests per second per prefix within a bucket, according to Stack Overflow. 
  - GET/HEAD: 5,500 requests per second per prefix within a bucket, according to Stack Overflow. 
- Service Quotas:
  - There are also service-level quotas, and you can request increases to these if needed. 
- 503 Slow Down Errors: When S3 is scaling to higher request rates, you might encounter 503 Slow Down errors. These should resolve as S3 completes scaling. 
- Latency: S3 is not designed for latency-critical workloads, and actual latency can vary. 

### Architecture Patterns

#### A company is concerned about accidental deletion of Amazon S3 objects.

Well, they might want to mitigate this by using S3 Versioning.

1. Enable Versioning
2. Enable MFA Delete
   - Bucket must have versioning enabled
   - Only root account can enable MFA Delete
3. Use S3 Object Lock
   - Compliance Mode – objects cannot be deleted until retention expires, even by root account
   - Governance Mode – privileged users can override if needed
4. Lifecycle Policies: Can prevent premature deletion of important data by setting minimum retention periods.
5. Cross-Region Replication: Protects against regional failures or accidental deletion in the primary bucket.

#### Data stored in S3 is frequently accessed for 30 days, then is rarely accessed, but must be immediately retrievable.

Use a lifecycle policy to transition objects from S3 Standard to S3 Standard Infrequently Accessed after 30 days.

#### A backup of S3 objects within a specific folder in a bucket must be replicated to another region.

Configure cross-region replication and specify the folder name as a prefix.

#### Previous versions of objects in a versioning enabled S3 bucket must be stored long term at the lowest cost.

Create a lifecycle rule that transitions previous versions to S3 Glacier Deep Archive, and that's the cheapest option for storing that long term.

#### A company wishes to manage all encryption of S3 objects through their application with their own encryption keys.

Use client-side encryption with client managed keys.

#### Unencrypted objects in an Amazon S3 buckets must be encrypted.

Re-upload the objects because they're already there and you can't encrypt existing objects. And when you upload them, you can specify the encryption to use and the encryption key.

#### An administrator requires a notification when objects are deleted from an S3 bucket.

Configure an event notification that uses the SNS service.

#### A group of customers without AWS credentials must be granted limited access to a software update that is stored in an S3 bucket.

Generate a __presigned URL__ and the users won't need an AWS account and it will be time limited.

#### Solutions architects require both programmatic and console access across AWS accounts.

For that, you can configure cross account access using IAM roles.

#### You want to put restrictions in an S3 bucket so that only your EC2 instances can access the bucket.

EC2 instances access S3 using Public IP Address and traffic is routed through internet gateway.
If VPC endpoint is used, S3 is accessed using AWS private network. 
In this case, bucket policy can use VPC ID or VPC Endpoint ID to restrict access.

#### You want to distribute content in S3 bucket using CloudFront edge locations. You also want to restrict access to the content to only the users who are authorized by your application.

Configure content to be accessible only using signed URLs or signed cookies
Create CloudFront user and grant read access to S3
Remove permissions for anywone to directly access S3 bucket

| Requirement                         | Solution                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| Distribute content globally         | **Amazon CloudFront** → edge caching for low latency                                  |
| Restrict access to authorized users | **Private S3 bucket + CloudFront signed URLs or signed cookies**                      |
| Prevent direct S3 access            | Use **S3 bucket policy** that allows **only CloudFront Origin Access Identity (OAI)** |

Step-by-Step Implementation
- 1️⃣ Make the S3 bucket private
  - Default bucket access: private
  - Remove public access
- 2️⃣ Create a CloudFront distribution
  - Set Origin as your S3 bucket
  - Enable Origin Access Identity (OAI) → allows CloudFront to access S3
  - Update S3 bucket policy to allow only OAI
-3️⃣ Restrict access to authorized users
  - Signed URLs
    - Generate URL with expiration timestamp and cryptographic signature
    - Only valid URLs can access content
    - Best for per-object access control

```
// S3 Bucket Policy Example (OAI only)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontOAI",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity YOUR-OAI-ID"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

#### An object of size 10 KB is stored in S3 using Standard - IA storage class. How is the pricing computed for this object?

Minimum charge computed for object in Standard-IA is based on 128KB size. 
If object is less than 128KB, it is still charged for 128KB​. There is also a 30 day minimum charge.

#### Account A grants S3 bucket access to Account B. An IAM user belonging to Account B needs access to that bucket. What steps need to be performed for this to work?

Account B can delegate access to its users.

1. Update the bucket policy in Account A (bucket owner)
  - Allow access to IAM principals in Account B
  - Example: allow s3:GetObject or s3:* depending on requirements
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "CrossAccountAccess",
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam::ACCOUNT_B_ID:root"
        },
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::bucket-a/*"
      }
    ]
  }
  ```
2. Ensure IAM user in Account B has a policy allowing S3 access
  - IAM policies cannot override the bucket policy; both must allow the action
  - Example IAM policy for the user:
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "s3:GetObject"
        ],
        "Resource": "arn:aws:s3:::bucket-a/*"
      }
    ]
  }
  ```

#### A social media application needs to store 1000s of objects. The average size of each object is 20 KB size, and it needs to be immediately accessible when needed. The older objects are accessed less frequently. What storage would be suitable for this requirement at the lowest cost?

Object size is 20 KB and needs to be immediately accessible. 
Standard-IA, One Zone-IA, Glacier Instant Retrieval all have a 128 KB minimum charge. 
Standard provides the required performance at the lowest cost for this example

#### A team is currently using the S3 Standard class for all their storage. The data in the bucket are used by different groups in the organization, and there is no clear visibility on the percentage of data accessed. What tool can you use to generate reports on the usage of data automatically?

__Storage Class Analysis__ can continuously monitor your bucket and track how your objects are accessed over time. 
This tool generates detailed reports on the percentage of data retrieved and by age groups. 
You can use this report to manage lifecycle policies. 

#### A game developer is planning to use S3 to store important game statistics for each user. The traffic could reach 1000s of GET and PUT requests per second with millions of users. Which of these key naming conventions would scale to support the traffic?

S3 is a distributed cluster of storage nodes that automatically scales to support the traffic. 
S3 uses the object key to select the node. 
When several objects share the same key prefix, there is a high likelihood of these objects landing in a small set of nodes. 
Among these choices, __/userID/gametitle/stats.txt ensures there is a large number of unique prefixes__.

#### Your department got a legal hold notice from the company's legal department to preserve all the evidence and documents in the S3 bucket. The data should be protected from modification and deletion for three years. All buckets currently have lifecycle policies that automatically purge data at varying intervals. What would you do?

Configure a retention period of three years in __Compliance Mode__ for each object. 
This will ensure current object versions are protected from modification and deletion. 

Governance mode is not the right choice as administrators, and other users with S3:* permission on the bucket would be able to remove the object version. A legal hold may be possible; however, people with s3:PutObjectLegalHold permission can disable the legal hold and then delete the object

#### What feature can you use to protect the data in S3 Data Lake if someone accidentally makes the S3 Bucket public?

With __S3 Server Side Encryption using Customer Master Key__, the user needs permission to access the bucket or object and the customer master key. 
So, even when the bucket is made public, only the users who have access to the customer master key can access the object. 

With default keys, S3 automatically decrypts data for anyone who has permission to access the bucket

#### Your legal department has asked your team to ensure that project documents are not deleted or tampered with.  They have further asked for a three year retention window. Your team is currently using Glacier for storing the project documents.  What option would you pick to enforce this policy?

Configure a retention period of three years in Compliance Mode for each object. This will ensure current object versions are protected from modification and deletion.

Governance mode is not the right choice as administrators, and other users with S3:* permission on the bucket would be able to remove the object version.

A legal hold may be possible; however, people with s3:PutObjectLegalHold permission can disable the legal hold and then delete the object

#### A company is using S3 to store employee files. Employees are requesting files and documents stored in S3 to be presented as a local network drive.  How can you do this?

In the File Gateway mode of the Storage Gateway, you can present an S3 bucket as a network file share to your on-premises systems. Any changes (addition, deletion, updates) that you make to the files are automatically replicated in the S3 bucket.

#### Multiple applications in different accounts within an enterprise upload data to a central S3 bucket. What security configuration would you use for the bucket?

Disable ACL-based permissions management for the bucket and ensure uploads are allowed only for authorized accounts in the organization

ACL is a legacy way of managing permissions and is problematic with cross-account upload scenarios. 
A bucket owner cannot read the object in the bucket unless the uploading account grants permissions using ACL. 
When you disable Object ACL, the bucket owner automatically owns all the objects in the bucket, and permission can be effectively managed using identity-based and resource-based policies

#### You have enabled cross region replication for your S3 bucket. When you delete an object in the source bucket, what is the behavior observed in replicated bucket?

Delete Marker is not replicated

#### Your company uses S3 for storing a variety of documents and files. Your users ask for a feature similar to a trash can or recycle bin. This feature should allow the users to restore any deleted files or objects within 30 days. The deleted files older than 30 days must be removed automatically. How would you accomplish this?

You can use versioning to keep the older version of the objects and life cycle policies can be defined to remove the older version after 30 days

#### For disaster recovery, a customer needs to replicate the content of an existing S3 bucket to another bucket in a different region. Which option would meet the requirements?

Answer:
- __S3 Batch Operations__ is a serverless solution that can inventory and transfer existing objects. For ongoing incremental transfer of changes to existing objects and newly created objects, we can use S3 Replication
Not correct:
- __When you enable S3 Replication, it does not transfer already existing objects. Only new changes are replicated__

Amazon S3 Batch Operations is a managed feature that lets you perform large-scale, repetitive actions on millions or billions of S3 objects with a single request, instead of having to write custom scripts.

```
resource "aws_s3_batch_operations_job" "copy_job" {
  account_id = "123456789012"  # Your AWS account
  role_arn   = aws_iam_role.batch_role.arn

  manifest {
    spec {
      format = "S3BatchOperations_CSV_20180820"
      fields = ["Bucket", "Key"]
    }
    location {
      object_arn = "arn:aws:s3:::manifest-bucket/inventory-manifest.csv"
      etag       = "manifest-etag"  # Replace with actual ETag of CSV
    }
  }

  operation {
    # Copy objects to destination bucket
    s3_put_object_copy {
      target_resource = "arn:aws:s3:::destination-bucket"
      # Optional: storage class, e.g., STANDARD_IA
      metadata_directive = "COPY"
    }
  }

  report {
    bucket  = "arn:aws:s3:::report-bucket"
    format  = "Report_CSV_20180820"
    enabled = true
    prefix  = "batch-copy-reports"
  }

  description = "Batch copy all objects from source to destination bucket in another region"
  priority    = 10
  status      = "Enabled"
}
```

#### Compare storage cost of AWS S3 Standard storage class, provisions an Amazon EBS volume (General Purpose SSD (gp2)) with 100 gigabytes of provisioned storage and  lastly an Amazon EFS Standard Storage filesystem.

Cost of test file storage on Amazon S3 Standard < Cost of test file storage on Amazon EFS < Cost of test file storage on Amazon EBS

With Amazon EBS Elastic Volumes, you pay only for the resources that you use. The Amazon EFS Standard Storage pricing is $0.30 per GB per month. Therefore the cost for storing the test file on EFS is $0.30 for the month.

For Amazon EBS General Purpose SSD (gp2) volumes, the charges are $0.10 per GB-month of provisioned storage. Therefore, for a provisioned storage of 100GB for this use-case, the monthly cost on EBS is $0.10*100 = $10. This cost is irrespective of how much storage is actually consumed by the test file.

For S3 Standard storage, the pricing is $0.023 per GB per month. Therefore, the monthly storage cost on S3 for the test file is $0.023.

#### what is cheapest storage type on aws s3 to access hundreds of Terabytes and should be available with millisecond latency but only 1/year?

S3 Glacier Instant Retrieval:
- S3 Standard ~$0.023 Milliseconds None
- S3 Standard-IA ~$0.0125 Milliseconds Yes (per GB)
- S3 Glacier Instant Retrieval ~$0.004 Milliseconds Yes (per GB)

#### what is the difference between aws s3 global accelarator and aws s3 transfer accelerator

__S3 Transfer Acceleration__
- Purpose: Speeds up uploads and downloads to/from a specific S3 bucket from geographically distant clients.
- How it works:
    - Uses the Amazon CloudFront edge network to route traffic to the closest AWS edge location.
    - Then it forwards data over Amazon's private backbone network to the target S3 bucket.
    - Designed specifically for faster data transfer (e.g., large file uploads) to one S3 bucket.
- Use case examples:
    - Uploading large media files to an S3 bucket from users all over the world.
    - Accelerating backups or data ingestion into a central S3 bucket.

__AWS Global Accelerator (with S3)__
- Purpose: Improves availability and performance of your global applications, not just S3, by providing static IPs and intelligent routing.
- How it works:
    - Routes client traffic to the optimal AWS endpoint (could be a regional S3 endpoint, ALB, EC2, etc.) using the AWS global network.
    - Chooses the fastest path and closest region based on health, geography, and performance.
- For S3:
    - You can use Global Accelerator to route requests to different S3 buckets across multiple AWS Regions.
    - Helps implement multi-region redundancy and latency-based routing for S3 access (e.g., GET requests).
- Use case examples:
    - Building a multi-region S3 application (e.g., read-only content delivery from multiple buckets).
    - Wanting high availability or region-based failover with consistent IPs.

#### A company has historically operated only in the us-east-1 region and stores encrypted data in Amazon S3 using SSE-KMS. As part of enhancing its security posture as well as improving the backup and recovery architecture, the company wants to store the encrypted data in Amazon S3 that is replicated into the us-west-1 AWS region. The security policies mandate that the data must be encrypted and decrypted using the same key in both AWS regions.

- Create a new Amazon S3 bucket in the us-east-1 region with replication enabled from this new bucket into another bucket in us-west-1 region. 
- Enable SSE-KMS encryption on the new bucket in us-east-1 region by using an AWS KMS multi-region key. 
- Copy the existing data from the current Amazon S3 bucket in us-east-1 region into this new Amazon S3 bucket in us-east-1 region
- AWS KMS supports multi-region keys, which are AWS KMS keys in different AWS regions that can be used interchangeably – as though you had the same key in multiple regions. 
- Each set of related multi-region keys has the same key material and key ID, so you can encrypt data in one AWS region and decrypt it in a different AWS region without re-encrypting or making a cross-region call to AWS KMS.

You can use multi-region AWS KMS keys in Amazon S3. 
However, Amazon S3 currently treats multi-region keys as though they were single-region keys, and does not use the multi-region features of the key.
However, you cannot convert an existing single-Region key to a multi-Region key.

#### An e-commerce company has copied 1 petabyte of data from its on-premises data center to an Amazon S3 bucket in the us-west-1 Region using an AWS Direct Connect link. The company now wants to set up a one-time copy of the data to another Amazon S3 bucket in the us-east-1 Region. The on-premises data center does not allow the use of AWS Snowball. As a Solutions Architect, which of the following options can be used to accomplish this goal?

- Copy data from the source bucket to the destination bucket using the aws __S3 sync command__ 
  - The aws S3 sync command uses the CopyObject APIs to copy objects between Amazon S3 buckets. 
  - The sync command lists the source and target buckets to identify objects that are in the source bucket but that aren't in the target bucket.
  - The command also identifies objects in the source bucket that have different LastModified dates than the objects that are in the target bucket. 
  - The sync command on a versioned bucket copies only the current version of the object—previous versions aren't copied.
- Set up Amazon __S3 batch replication__ to copy objects across Amazon S3 buckets in another Region using S3 console and then delete the replication configuration
  - Amazon S3 Batch Replication provides you a way to replicate objects that existed before a replication configuration was in place, objects that have previously been replicated, and objects that have failed replication. 
  - This is done through the use of a Batch Operations job. 
  - You should note that batch replication differs from live replication which continuously and automatically replicates new objects across Amazon S3 buckets. 
  - You cannot directly use the AWS S3 console to configure cross-Region replication for existing objects. 
  - By default, replication only supports copying new Amazon S3 objects after it is enabled using the AWS S3 console. 
  - Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. Buckets that are configured for object replication can be owned by the same AWS account or by different accounts. 
- Amazon S3 Transfer Acceleration (Amazon S3TA) is a bucket-level feature that enables fast, easy, and secure transfers of files over long distances between your client and an Amazon S3 bucket. You cannot use Transfer Acceleration to copy objects across Amazon S3 buckets in different Regions using Amazon S3 console.










## DNS, Caching and Performance Optimization <a id="DNS"></a>

DNS components / architecture:
- DNS resolver: ISP provider, caches entries or forwards
- DNS root server: knows about domain suffixes like ".com" and forwards to TLD server
- TLD server: knows about specific domain suffix like .com and forwards to DNS authoritative server for a given FQDN
- DNS authoritative server: forwards to specific server for FQDN like: facebook.com

### Route 53 <a id="Route53"></a>

- Route 53 gives you:
  - __domain name registry__,
  - __DNS resolution__,
  - __health checking__ of resources.
- It is __located along side edge locations__.
- private hosted zone vs public hosted zone
- Route 53 becomes the authoritative DNS server for registered domains and will create a public hosted zone for you.
- Amazon Route 53 automatically creates the Name Server (NS) and Start of Authority (SOA) records for the hosted zones.
- private DNS, lets you have an authoritative DNS server within your VPCs without exposing your DNS records.
- You can transfer existing domains to Route 53 if the top-level domain is supported.
- You can also transfer domain from Route 53 to another registrar, but you have to contact AWS support.
- You can transfer a domain to another account in AWS, but that doesn't migrate the zone by default.
- You can also have a domain registered in one AWS account and the hosted zone in another AWS account.

Hosted zone:
- is a __collection of records for a specified domain__.
- There are two types:
  - public hosted zone for routing traffic on the internet
  - a private hosted zone for your VPC, which helps to route traffic within your VPC.
- For private hosted zones, you must set the following VPC settings to true:
  - EnableDNSHostname
  - enableDNSSupport.

Health checks:
- check the instances health by connecting to it.
- you can point health checks:
  - endpoints,
  - status of other health checks
  - status of a CloudWatch alarm.
- Endpoints can be IP addresses or domain names.

Two types of DNS record:
- __CNAME__
  - Route 53 charges for queries.
  - You can't create CNAME a record at the top node of DNS namespace,
  - If you have the domain namespace example.com, you can't create a CNAME for example.com, but you can for www.example.com because that's a subdomain. So, not the zone apex.
  - A CNAME can point to any DNS record hosted anywhere.
  - __CNAME cannot be used at the root domain (example.com) — only on subdomains (www.example.com, api.example.com, etc.)__
  - __CNAME records must point to a domain, never to an IP address__
  - Use CNAME for subdomains when you want to point them to another domain name.
  - Great for pointing to CDNs, load balancers, managed services.
  - Example of CNAME use:
    - www.example.com points to another domain: 
    - www.example.com.    IN CNAME    myapp.hostingprovider.com.
  - Things that do not work for Alias but work with CANME:
    - CNAME Points to non-AWS domains (Alias cannot)
    - Supported outside AWS Route 53
- __A__ record:
  - __maps a domain name to an IP address__
  - Example: "google.com" pointing to the IP address "74.125.224.147"
- __AAAA__: name -> IP for IPv6
- __Aliases__:
  - Route 53, doesn't charge for queries to AWS resources.
  - You can create an alias record at the zone apex, which is what you can't do with CNAME, so it's a key difference.
  - An alias record can only point to CloudFront, Elastic Beanstalk, ELB, S3 buckets configured as static websites or to another record in the same hosted zone.
  - allows users to access a page or file at an alternative path. It's similar to having multiple front doors to one location
  - An ALIAS record can be used to point multiple domains to the same site, such as example.com, www.example.com, and blog.example.com all pointing to the same site
  - Alias records work like a CNAME record in that you can map one DNS name (e.g. example.com) to another ‘targetʼ DNS name (e.g. elb1234.elb.amazonaws.com).
  - An Alias record can be used for resolving apex / naked domain names (e.g. example.com rather than sub.example.com).
  - A CNAME record canʼt be used for resolving apex / naked domain names.
  - Examples of Alias use:
    - example.com.    IN ALIAS    myapp.hostingprovider.com.
- __MX__: email
- __PTR__: IP -> name

Routing policies:
- __simple__ routing (only one IP)
- __weighted__ routing policy + health-check
- __geolocation__: create one A record per regions + IP and default. dnschecker.org
  - Use when: You want to serve users in specific countries, continents, or states (U.S. only) from different endpoints.
- __latency__: create many A records in different regions
- __geoproximity__: need to __create traffic policy_- (provide exact geo area coordinates + bias)
  - Use when: You want fine-grained control over traffic distribution based on distance to endpoints.
  - You want to adjust traffic boundaries dynamically using bias
- __failover__: need to __create health-check__ , decrease __TTL__
- __multivalue__: __returns many IP addresses__ in different order (round robin): same A record can have many IP addresses: Used for load balancer. Can add health-check
    - issues: cannot send traffic to private subnet, no https, slow TTL (min 60s)
- __ip based__ routing: different IP depending on source IP

![ Routing policies ](./images/route_53_routing_policies.png)

You can combine Geoproximity Routing with Failover Routing in Amazon Route 53, but only through Route 53 Traffic Flow using policy rules and failover endpoints within the same traffic policy.

- You define geoproximity rules to route users based on their geographic location.
- For each geoproximity location (e.g., us-east-1, eu-west-1), you can specify:
  - A primary endpoint
  - A secondary (failover) endpoint with Failover = Secondary
- If the primary health check fails, Route 53 automatically sends traffic to the secondary

Configure Routte 53 routing policy that routes to closest region and has automatic failover if one region fails:
- With latency routing, failover is handled via health checks, not by specifying a failover region manually.
- if us-east-1 becomes unhealthy, Amazon Route 53 will automatically stop returning that endpoint and send users to the other region (e.g., eu-west-1) as long as health checks are configured
```
api.example.com → latency record → us-east-1 ALB
api.example.com → latency record → eu-west-1 ALB

// US record
Record name: api.example.com
Record type: A
Routing policy: Latency
Region: US East (N. Virginia)
Alias: Yes
Alias target: ALB in us-east-1
Health check: us-east-api
Evaluate target health: Yes

// EU record
Record name: api.example.com
Record type: A
Routing policy: Latency
Region: EU (Ireland)
Alias: Yes
Alias target: ALB in eu-west-1
Health check: eu-west-api
Evaluate target health: Yes
```

### Amazon CloudFront <a id="CloudFront"></a>

To use CloudFront to distribute your website content, create a distribution and specify settings for it.
When you create a distribution, __CloudFront assigns a domain name to the distribution, such as d111111abcdef8.cloudfront.net.__ 
You can use this domain name in the URLs for your content.
Instead of using this provided domain name, you can use an alternate domain name (also known as a CNAME).

Amazon CloudFront __can route to multiple origins based on the content type__: You can configure a single Amazon CloudFront web distribution to serve different types of requests from multiple origins. For example, if you are building a website that serves static content from an Amazon Simple Storage Service (Amazon S3) bucket and dynamic content from a load balancer, you can serve both types of content from a Amazon CloudFront web distribution.

__Failover__:
- Use an origin group with __primary and secondary origins__ to configure Amazon CloudFront for __high-availability and failover__
- You can set up Amazon CloudFront with origin failover for scenarios that require high availability. To get started, you create an origin group with two origins: a primary and a secondary. If the primary origin is unavailable or returns specific HTTP response status codes that indicate a failure, CloudFront automatically switches to the secondary origin.
- To set up origin failover, you must have a distribution with at least two origins. Next, you create an origin group for your distribution that includes two origins, setting one as the primary. Finally, you create or update a cache behavior to use the origin group.

__Field level encryption__:
- Use __field level encryption__ in Amazon CloudFront to protect sensitive data for specific content: Field-level encryption allows you to enable your users to securely upload sensitive information to your web servers. The sensitive information provided by your users is encrypted at the edge, close to the user, and remains encrypted throughout your entire application stack. This encryption ensures that only applications that need the data—and have the credentials to decrypt it—are able to do so.
- To use field-level encryption, when you configure your Amazon CloudFront distribution, specify the set of fields in POST requests that you want to be encrypted, and the public key to use to encrypt them. You can encrypt up to 10 data fields in a request. (You can’t encrypt all of the data in a request with field-level encryption; you must specify individual fields to encrypt.)

TLS (used in HTTPS) encrypts the transport channel between two points.
Typical path with CloudFront:
```
User Browser  --HTTPS-->  CloudFront Edge  --HTTPS-->  Origin Server: decrypts request --HTTP--> ALB
```

| Security Layer           | HTTPS (TLS)                     | Field-Level Encryption (FLE)                                   |
| ------------------------ | ------------------------------- | -------------------------------------------------------------- |
| Encrypts                 | Entire HTTP request/response    | Specific fields within the body (e.g., JSON field, form input) |
| Visibility to CloudFront | Full request visible            | Encrypted fields are unreadable even by CloudFront             |
| Use case                 | Protects data in transit        | Protects sensitive fields end-to-end                           |
| Who can decrypt          | Any system handling the request | Only **specific backend app** with private key                 |

- Cache copies of content close to your users
- CloudFront routes request to nearest edge location

- CDN as we know for __caching content around the world__.
- You __can define a maximum time to live__ and a default TTL for records.
- TTL is defined at the behavior level and CloudFront.
- This can be used to define different TTLs for different file types, so you could have a different time to live for your PNGs versus your JPEGs.
- __After expiration, CloudFront checks the origin for any new requests__.
- __Headers can be used to control the cache__:
  - the Cache-Control max-age in seconds, and that specifies how long before CloudFront gets the objects again from the origin server.
  - Expires: which specifies an expiration time and date.
- You __can also cache based on request headers__: forward headers in the viewer request to the origin.
- CloudFront can then cache multiple versions of an object based on the values in one or more request headers.
- Controlled in a behavior to do one of the following;
  - forward all headers to your origin, which means the objects are not cached.
  - forward a whitelist of headers that you specify.
  - forward only the default headers and then it doesn't cache the objects based on values in the request headers.
- low latency, high transfer
- uses edge locations
- Origin domain: source of the content: s3, ec2, lambda, lb, api gateway
- Origin path
- Custom header: additional header you want to pass to origin (authentication)
- Origin shield: additional layer of caching (edge locations + regional cache already does caching)
  - origin shield adds 3 layer of caching (last one) to reduce the load
- __CloudFront does not internally enable Global Accelerator.__
  - When a user makes a request: User → CloudFront Edge → Origin
  - The edge location closest to the user receives the request.
  - CloudFront then fetches data from the origin (your ALB, EC2, or S3 bucket). __By default it goes though public internet!__ You need global accelerator

__CloudFront setup__:
- setup static website
- create CloundFront Distribution (in CloudFront)
  - origin is the static website
- all edge location as Price class
- use the new CloudFront url

__CloudFront Cache__ behavior:
- path pattern: what content you want to cache (* means all)
- compression
- viewer protocol: HTTP or HTTPS or both
- for __custom domain name__, you need to configure CNAME and setup SSL/TLS certificate:
  - use AWS __Certificate Manager__ to create the SSL/TLS certificate
  - CloudFront needs the certificate in Virginia region
  - Create A-Alias record for your domain in Route53
- to make your website secure, you do not want the user to access it using http from S3
  - __S3 bucket must be private and CloundFront origin access = 'Origin Access Control'__
  - you still have to create bucket policy on your S3
- Use header or cookie to understand request
- Create cache policies, compression, TTL

To __secure Amazon CloudFront__:
- enable HTTPS,
- restrict access with signed URLs/cookies,
- AWS WAF,
- implement field-level encryption,
- consider geographic restrictions,
- leverage CloudFront's security policies

Create a __secure HTTPS website__ and preventing users from accessing the S3 bucket directly 
- Host Website Content on S3 (Private)
  - Create an S3 bucket (e.g., mywebsite.com).
  - Upload your website files (HTML, CSS, JS, etc.).
  - Disable public access to the bucket:
  - Do not enable static website hosting on the bucket directly
- Create CloudFront Distribution
  - Use Amazon CloudFront as the CDN and secure HTTPS entry point.
  - Origin domain: Set it to your S3 bucket’s regional endpoint 
  - Restrict access: Enable Origin Access Control (OAC) or Origin Access Identity (OAI) to let only CloudFront access the S3 bucket.
  - Viewer protocol policy: Set to Redirect HTTP to HTTPS or HTTPS only.
  - Enable custom domain name if using your own domain.
  - Attach an SSL certificate
- Request SSL Certificate (HTTPS)
  - Use AWS Certificate Manager (ACM).
  - Go to ACM and request a public certificate (e.g., www.mywebsite.com, mywebsite.com).
  - Validate domain ownership
- Configure Domain Name (Optional via Route 53)
  - If using your custom domain:
    - Use Route 53 or your domain registrar.
    - Create an A (Alias) record pointing to the CloudFront distribution.
- Secure S3 Bucket (Restrict Direct Access)
  - Use Bucket Policy to allow access only from CloudFront

While CloudFront primarily uses ports 80 (HTTP) and 443 (HTTPS), you can configure it to communicate with your origin server on other ports (1024-65535).

However, CloudFront itself only listens on 80 and 443, and clients connecting to CloudFront must use these standard ports

CloudFront is not a service supported by DNS-Route-53 health checks and it does not return health checks.

With CloudFront’s Origin Failover capability, you can setup two origins for your distributions - primary and secondary, such that your content is served from your secondary origin.
If CloudFront detects that your primary origin is unavailable


CloudFront __Response Headers policy__:
- piece of info sent from web server to web browser
- use it to increase security, protect sensitive data

CloudFront __Function Associations__
- allows you to execute custom code to modify request or response as they pass-through CloudFront
- viewer request, origin request, origin response, viewer response
- url reqrites, redirects, request validation, adding custom headers
- you want to redirect users to different version of your website based on geo-location
- __CloudFront functions__: lightweight, high-performance, javascript, must be in Virginia.
- __Lambda at Edge__: complex, higher latency, many lanuages

__CloudFront Origin groups__
- Primary and secondary origin = automatic failover
- EC2 and S3 failover

__S3 Transfer Acceleration__ leverages Amazon CloudFrontʼs globally distributed AWS Edge Locations

CloudFront __does not support region-specific origins__.

#### Origin

- Dynamic and Static Content
- Restrict access - Signed URLs, Signed Cookies
- Geo Restriction
- Configurable Caching, Invalidation Option
- Personalized – Query String Parameters, HTTP Cookies
- Backup Origin (primary not healthy)
- Security:
  - Origin Access Identity – Limit access to S3 bucket only from CloudFront Identity
  - When configured, CloudFront uses OAI credentials to sign S3 requests

#### Signed URLs and cookies

- With __signed URLs__:
  - these provide more control over access to content.
  - __You can specify the beginning and expiration date and time and IP addresses__ or ranges of IP addresses for users.
- With __signed cookies__, that's similar to signed URLs:
  - can use these when you don't want to change URLs,
  - they can also be used when you want to provide access to __multiple restricted files__, that's a key difference.
  - A signed URL is for a single object, whereas if you want multiple objects to be included, then you should use signed cookies.

Restrict Behavior User Access (for paid content)
- can be activated using __signed url__ or __signed cookies__
- trusted key groups: you need to created public+private keys to create 

#### Lambda@edge

Lambda functions at edge locations.

Customize application behavior – without touching origin systems

- This is where you run Node.js and Python Lambda functions to customize the content that CloudFront delivers,
- it __executes the functions closer to the view__ of a better performance.
- You can run Lambda@edge at the following points:
  - __after CloudFront receives a request__ from a viewer that's called a viewer request, before CloudFront forwards the request to the origin, that's an origin request,
  - __after CloudFront receives the response__ from the origin, origin response,
  - __before CloudFront forwards the response__ to the viewer and that's called the viewer response.

#### Global Accelerator

- improves availability: automatically reroutes traffic to healthy endpoints ensuring your apps stay available
  - can send load balance traffic across different aws regions - __multi-region__
  - weight based routing
- improve performance: uses aws network
- provides 2 public IP addresses that you later used in DNS
- health check
- tcp/udp support
- integrates with security services like WAF
- custom routing: if user x comes from country Y then send it to EC2 in region Z
- supports any static IP address

__Global Accelerator Setup__
- no region selection
- Create the accelerator: you will get 2 static IPs and DNS name that never change
- listener setup: tcp:port or udp:port
- endpoint group: define region and weight, health checks and muliple targets (ALB, NLB, EC2, Elastic IP)
- Add endpoints: Inside each endpoint group you attach: ALB, NLB, EC2 instance, Elastic IP

#### Traffic flow cloudfront, aws route 53 and aws s3

A secure Website is deployed to aws cloudfront, aws route 53 and aws s3. How the interaction between CloudFront and Route 53 looks like?

Components:
- Amazon S3: Hosts your static website files (HTML, CSS, JS, images).
- Amazon CloudFront: CDN that caches and delivers content securely and globally.
- Amazon Route 53: DNS service that maps your domain name to CloudFront.
- Web Browser: Client that accesses the site using your domain (e.g., https://example.com).

Browser --> Route 53 --> CloudFront --> S3 Bucket (origin)

Step-by-Step Breakdown:
- The user types https://example.com in the browser.
- The browser needs to resolve example.com to an IP address
- The browser sends a DNS query (via the OS or a DNS resolver).
- Route 53 responds with the IP address of the CloudFront distribution. This happens because you’ve created an A or CNAME record in Route 53 pointing your domain (e.g., example.com) to the CloudFront distribution domain, like d1234abcd.cloudfront.net.
- the browser makes an HTTPS request to the CloudFront edge location closest to the user.
- CloudFront serves the request. If the content is cached, it serves it from the edge location. If the content is not cached, it fetches it from the origin (S3 in this case).
- CloudFront is configured with S3 as the origin.
- It securely fetches the object from the S3 bucket if it's a cache miss.
- CloudFront caches the object (if caching is enabled).
- Sends the response back to the browser.
- The user sees the website content.

Multi-region replication architectures:
- __Active-Active__ (Globally Distributed): Applications run concurrently in multiple regions, serving local traffic and enabling instantaneous failover. Data is replicated, often requiring specialized, conflict-resolving databases
- __Active-Passive__ (Primary-Secondary): One region handles all writes while others act as read replicas. This offers high consistency (strong) but introduces write latency for users far from the primary region
- __Warm Standby / Pilot Light__: A cost-effective passive approach where the secondary region runs minimal services, scaling up only when a failover occurs, 

### Architecture Patterns

#### An elastic load balancer must be resolvable using a company's public domain name, a Route 53 hosted zone already exists.

Create an __alias__ record that maps the __domain name to the ELB__ (ALB or NLB), and you must use an __alias__ here rather than the CNAME.
A CNAME can be used for a subdomain. But in this case, it's not a sub domain and it's mapping to an ELB.

#### A website runs across two AWS regions. All traffic goes to one region and should be redirected only if the website is unavailable.

Create a failover routing policy in Route 53 and configure health checks on the primary.

#### Websites run in several countries and distribution rights require restricting access to content based on the geographic source of the connection.

use Route 53 geo-location routing and restrict distribution based on geographic location.

#### A CloudFront distribution has multiple S3 origins. Requests should be served from different regions based on file type being requested.

Use a behavior and configure a path pattern. You do that within your distribution.

You can achieve this with Amazon CloudFront by using __cache behaviors and multiple origins__. 
Essentially, CloudFront lets you route requests to different origins based on URL path patterns, which can correspond to your file types.

#### Content is accessed using an application and CloudFront distribution. You need to control access to multiple files on the distribution.

Configure signed cookies and then update the application so it processes those cookies.

To control access to content being served via CloudFront, you have several options to ensure that only authorized users or applications can access specific file:
- __Signed URLs__ (for specific files or paths): Use the private key to generate a signed URL, which gives access to a specific file on CloudFront for a limited time.
- __Signed Cookies__ (for controlling access to multiple files): create a cookie with policies for access, allowing the user to access multiple files for a specified duration
- Restricting Access to CloudFront with S3 (via __Origin Access Identity__): Attach the OAI to your CloudFront Distribution
- __Lambda@Edge__ for Custom Authorization

Signed URLs exmaple:
- Create a CloudFront Key Pair
- Generate a Signed URL for the Specific File: 
  - You'll sign the URL using your CloudFront private key and a __policy document__, which defines access conditions such as expiration time and allowed resources
  - this is done in a python script that runs as lambda or you server backend.
  - Example of:
    - Lambda Function: The Lambda will generate a signed URL for a specific CloudFront resource.
    - You will also need API Gateway: API Gateway will trigger the Lambda function via an HTTP request.
- Distribute the Signed URL

A __normal signed URL__ allows you to grant access to a specific file for a limited period. The URL is signed using your private key and can be used directly to access that file on CloudFront or any other supported AWS service.

A __signed URL with a policy document__ provides more flexibility and control over who can access the file and under what conditions. Instead of just signing the URL with an expiration time and file path, you use a policy document that defines additional parameters, such as the allowed IP addresses, time window, or multiple resources

#### An application runs behind an application load balancer in multiple regions. You need to intelligently route traffic based on latency as well as availability.

- Use AWS Route 53 with latency-based routing and health checks
- Create an AWS global accelerator and add the ALBs
  - global traffic management for your applications by directing traffic to the best-performing endpoints based on user location, health check
  - When you create a Global Accelerator, AWS assigns two static IP addresses for your accelerator. These are used by clients to route traffic to your application.
  - Create Regional Endpoints: For each region you want to route traffic to, you need to create an endpoint group.
    - Choose a regional endpoint: You can choose between Application Load Balancer (ALB), Network Load Balancer (NLB), or EC2 instances
    - Add endpoint groups
    - Set Endpoint Weights
  - Configure Health Checks
  - Traffic Routing

| Feature               | **Route 53**                               | **Global Accelerator**                                                                |
| --------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------- |
| **Traffic Routing**   | Latency-based, Geolocation-based, Weighted | Latency-based, Health-based routing                                                   |
| **Global Static IPs** | No                                         | Yes (2 global static IPs)                                                             |
| **Failover**          | Yes (with health checks)                   | Yes (automatic health checks and failover)                                            |
| **Performance**       | User traffic routed via DNS resolution     | Routes traffic to the region with **lowest latency** and health                       |
| **DNS Caching**       | Yes (TTL based)                            | No (Global Static IPs, no DNS caching)                                                |
| **Complexity**        | Simpler for basic setups                   | Ideal for high-performance, multi-region apps                                         |
| **Cost**              | DNS requests cost, health checks cost      | Pricing based on the number of accelerators and data transfer, but no extra DNS costs |


#### An application uses Geo Location Based Routing on Route 53. Route 53 receives a DNS Query and it is unable to detect requester’s Geo location. How will Route 53 respond in this case?

Default location is returned if it is configured. Otherwise 'no answer' response is returned

#### An application is deployed in multiple AWS regions and Route 53 is configured to route request to the region that offers lowest latency for the client. Due to an unplanned downtime, Application is not available in one of the regions. How will Route 53 handle this scenario?

Health Check needs to be configured for Route 53 to become aware of application down scenarios. 
It will then act on the routing configuration specified

#### Your app is using a third party API for some of the functionality. Requests from your app to the API needs to be digitally signed using keys issued by the third party. You are planning to use CloudFront to reach the global audience for the app, and you would like to call the third party API from CloudFront Edge location directly.  What approach would you use?

With Lambda@Edge, you can run your application logic at Edge locations. 
You can configure CloudFront to invoke the Lambda@Edge function to digitally sign the requests for third party API. 
Deploying third-party integration components of your app in multiple regions is not required as it increases complexity and cost.

#### You would like to point your zone apex to your elastic load balancer. Which record type would you use?

Use Alias record. To point Zone Apex Record (example.com is zone apex. www.example.com is a subdomain) to another AWS supported endpoint, you need to use the Alias record

#### You want to configure all your email servers in Route 53. Which record type would you use?

MX Record is used for specifying mail servers in your domain

#### Your application must be accessible only from certain countries. What routing policy would you use?

Route 53 Geolocation based routing can route based on Continent, Country and for some regions at State level

#### An application uses Geolocation Based Routing on Route 53. Route 53 is unable to pinpoint the originating location of a request. In this case, what will be Route 53's response?

Route 53 uses the caller IP address to determine the location. 
On some occasions, Route 53 may not be able to determine the precise location of the user. 
For these scenarios, you can configure a default record that handles both queries from IP addresses that are not mapped to any location and queries that come from locations that you haven’t created geolocation records for

#### Can you share the same Private DNS Hosted Zone entries with multiple VPCs across different regions?

Yes. You can enable multiple VPCs across the same or different regions in a Private Hosted Zone

#### The latency of a CloudFront application is inconsistent for global users. Some requests are extremely fast, while others are very slow. What could be the cause of this issue?

Requests are going to the origin. 
During a cache-miss, CloudFront route the request to the origin. 
Request response time, in this case, depends on how far the origin is from the user and how long an origin takes to respond. 
CloudFront does not support region-specific origins. 
With anycast routing, the request is routed to the nearest edge location. 
When Geo-restrictions are enabled, CloudFront will simply block requests from countries that are not allowed access.

#### The requests for a web application need to be routed to the webserver close to the user. Which of these options would you use?

Use Route 53 latency-based routing. 
With Route 53, you can configure region-specific endpoints. 
Route 53 will respond with the nearest endpoint address for a DNS query

#### A request needs to be routed to the nearest healthy endpoint. The application needs to respond very quickly to changing health conditions of endpoints.  Which of these options would you use?

The __global accelerator__ automatically routes requests to the nearest endpoint. 
Since the routing decision is made for each request, it can instantly respond to changes in the health conditions of endpoints. 
Route 53 will also work. However, it is based on DNS based endpoint resolution. 
DNS records are cached for the duration specified in the TTL parameter. 
So, a client may attempt to connect an unhealthy, but closest endpoint until new DNS records are fetched.

#### A company wants to minimize disruption during software upgrades. Which of these options would you use?

With __Global Accelerator__, you can control traffic flow to your regional endpoints. 
You can easily perform region-by-region upgrades by reducing traffic-dial to 0 for a region. 
Weight parameter is useful for distributing traffic in-proportion that you specify across multiple endpoints in a single region. 
This is useful for blue-green deployment. There is no need to remove regions from a Global accelerator. 
Route 53 failover routing is used for active-passive failover and Weighted routing is used for routing traffic to resources in proportions that you specify.DNS solution is slow to respond

#### When distributing Private Content with CloudFront, how do you make sure users do not bypass security measures and go directly to custom origin servers and S3 location?

You need to:
- Lockdown S3 with CloudFront Origin Access Identity (OAI) and remove permissions for others
- Configure CloudFront to forward custom headers to your publicly accessible origin server. Verify Custom header and value in your application

CloudFront Origin needs to have a public endpoint. To prevent others from calling your Origin endpoints directly, you need to configure the endpoint to verify if the request is coming from CloudFront.

A common pattern is configuring CloudFront to embed a specific header and value (either static value or dynamic values using Lambda@edge). You can verify the header content in your origin server to allow or deny access.

You can configure CloudFront to embed specific code to a custom header and cross-check the header value in Origin Server.

For S3, CloudFront uses Origin Access Identity (OAI) to access your S3 bucket. In the S3 bucket policy, you need to limit access only to this identity

#### A media company has documents, videos, images and other paid content that is currently hosted in their own datacenter. Content is personalized based on signed-on user. Users are located world wide and they are complaining about timeouts and poor performance. What options do you have to address this situation? (Choose Two)

CloudFront allows you to cache the content closest to your customer using AWS global Edge network. CloudFront Origin can be S3, applications hosted in AWS, and external applications hosted on-premises. CloudFront also supports dynamic content that is personalized based on signed-on user

#### My application uses CloudFront distribution to reach a global audience. The application uses HTTPS to accept payment information (credit card, debit card, bank information) for subscriptions. This payment information must be accessible only for specific billing components in the application and be protected from unauthorized access in other components.

Do this:
- Enable TLS/SSL encryption from CloudFront to your Origin Load Balancer and then from Load Balancer to your Webservers
- Enable Field level encryption in CloudFront to protect sensitive data

Since the application handles sensitive data, you must ensure SSL/TLS is turned on all the way to the web servers. 

If you terminate SSL at the load balancer, communication between the load balancer and the web server is unencrypted, leading to sensitive data access by components other than billing. 

CloudFront supports Field Level Encryption to protect sensitive data. 
With this capability, you can configure CloudFront to encrypt fields using the specified encryption keys. You would then configure the billing component to use the matching keys so that it can decrypt the sensitive data.

#### A popular SaaS application is hosted using an Application Load Balancer (ALB). A big corporate customer of this application is requesting that the application endpoints have a static IP address so that they can configure the firewall to allow traffic to the endpoint. The SaaS application technical team is heavily using ALB's routing features, and it is a non-trivial task to move to a different load balancer type. Which one of these options is most operationally efficient to meet the requirement?

Configure a Global Accelerator in front of an application load balancer.

Global Accelerator endpoint has two static IP addresses. Customer can configure their firewall and application to communicate with the Global Accelerator IP address. The requests are automatically forwarded to Application Load Balancer by Global accelerator. The global accelerator has several benefits like using the AWS edge network to route the request to the nearest endpoint, static IP address, traffic dial to easily shape traffic flow, responding instantaneously to changes in health and traffic conditions, etc.

#### Route 53 geo-location vs geo-proximity:

- Geolocation Routing, you can route traffic based on the requester's location. You can configure route 53 records based on Country and Continent. In the case of the USA, you can even configure it by State.
- Geoproximity Routing – Similar to Geolocation, if you have resources in multiple regions, you can route traffic to the nearest location and, optionally, shift traffic from resources in one location to another. This allows for more complex traffic shaping; however, Geoproximity requires the use of Traffic Flow, and it involves additional monthly costs (USD 50/month)

#### How to combine CloudFront, API Gateway caching, and ElastiCache?

- CloudFront → caches content at edge for global users.
- API Gateway caching → caches API responses in region, reduces Lambda/RDS calls.
- ElastiCache → caches frequently accessed DB queries.

### Combining multiple Route 53 routing policies like latency-based, weighted, and failover

AWS Route 53 allows one routing policy per record, but you can combine policies using nested records and alias records.
- Weighted + Failover: You can combine weighted routing with failover by creating multiple records under a failover setup, each with weighted sub-records.
- Latency + Weighted: You can combine latency-based routing with weighted by creating multiple latency records per region and then applying weighted distribution within the region.

#### A retail company has connected its on-premises data center to the AWS Cloud via AWS Direct Connect. The company wants to be able to resolve Domain Name System (DNS) queries for any resources in the on-premises network from the AWS VPC and also resolve any DNS queries for resources in the AWS VPC from the on-premises network.

Create an inbound endpoint on Amazon Route 53 Resolver and then DNS resolvers on the on-premises network can forward DNS queries to Amazon Route 53 Resolver via this endpoint

Create an outbound endpoint on Amazon Route 53 Resolver and then Amazon Route 53 Resolver can conditionally forward queries to resolvers on the on-premises network via this endpoint

Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service. Amazon Route 53 effectively connects user requests to infrastructure running in AWS – such as Amazon EC2 instances – and can also be used to route users to infrastructure outside of AWS. By default, Amazon Route 53 Resolver automatically answers DNS queries for local VPC domain names for Amazon EC2 instances. You can integrate DNS resolution between Resolver and DNS resolvers on your on-premises network by configuring forwarding rules.

To resolve any DNS queries for resources in the AWS VPC from the on-premises network, you can create an inbound endpoint on Amazon Route 53 Resolver and then DNS resolvers on the on-premises network can forward DNS queries to Amazon Route 53 Resolver via this endpoint.












## Block and File Storage <a id="Block_File_Storage"></a>

### EBS <a id="EBS"></a>
- __volume data persists independently of the life of the EC2 instance__.
- EBS volumes do not need to be attached to an EC2 instance.
- you __can attach multiple EBS volumes__ to an instance.
- You an use __Multi-Attached to attach a volume to multiple instances__ with a few constraints.
- EBS volumes __need to be in the same AZ as the instances__ you're attaching them to.
- the __root EBS volumes are deleted on termination by default__.
- Extra non-boot volumes are not deleted on termination by default.
- Create Amazon Machine Image (AMI) from Snapshots to launch new EC2 instances
  - Snapshot is async and works in the background

EBS volume data is replicated across multiple servers in an AZ

Volume sizes and types can be upgraded without downtime: increase volume size, adjust performance, or change the volume type. 
However, you cannot decrease an EBS volume size.

volume types:
- SSD:
  - __gp__
    - gp2: 3 IOPS/GB, max 16 000 IOPS, burst capacity, throughput: 250 MiB/s
    - gp3: __constant 3000 IOPS__, max 16 000 IOPS, __throughput: 1000 MiB/s__
  - __io__
    - io1: 64 000 IOPS, multi-attach, throughput: 1000MiB/s
    - __io2: 64 000 IOPS + 256 000 with block express__, __multi-attach__, __throughput: 4000 MiB/s__, 99.99% durability

![ SSD ](./images/ebs_ssd_volume_types.png)

- HDD backed:
  - __500 IOPS__, throughput: __500 MiB/s__
  - extremely cheap in comparison to the SSD-backed volumes.
  - Key thing to note here, there's no Multi-Attach enabled and you cannot use these as boot volumes.

![ HDD ](./images/ebs_hdd_volume_types.png)


#### Data Lifecycle Manager:
- automates the creation, retention, and deletion of EBS snapshots and EBS-backed AMIs.
- DLM helps with:
  - __protecting valuable data by enforcing a regular backup schedule__
  - __create standardized AMIs that can be refreshed at regular intervals__,
  - retain backups as you might need for auditors or compliance
  - __reduces storage costs by deleting outdated backups__.
  - create disaster recovery backup policies that backup data to other accounts.

#### EBS versus Instance Store:
- Instance Store volumes are high performance local disks physically attached to the host computer on which your instance is running.
- They are ephemeral, so the data is non-persistent.
- Instance stores are good for temporary storage of information that changes  frequently
- Instance store volume root devices are created from AMI templates stored on S3
- And Instance Store volumes cannot be detached and reattached.

#### AMIs:
- these __provide the information required to launch an instance__.
- AMI includes one or more EBS snapshots or for Instance Store-backed AMIs, a template for the root volume of the instance.
- Launch permissions that control which accounts can use the AMI
- a block device mapping specifying the volumes to attach to the instance.

#### EBS snapshots

- __capture a point in time state__ of an instance.
- cost effective and easy backup strategy.
- __can be used to migrate a system to a new availability zone or region__.
- can also use them to __convert an unencrypted volume to an encrypted volume__.
- Snapshots are __stored on S3__.
- EBS volumes are __AZ specific__, but __snapshots are region specific because they're on S3__.

EBS snapshot: you can:
- restore in different AZ 
- you can create encrypted/unencrypted volume (EBS)
- you can copy snapshot to another region
- snapshot automation

#### RAID with EB
- RAID is a Redundant Array of Independent Disks.
- It's not provided by AWS. It's something you configure in your operating system.
- __RAID 0__,
  - This is __striping data for performance__.
  - You need two or more disks
  - if one disk fails the entire RAID set fails.
- __RAID 1 is mirroring__
  - data across disks for __redundancy and fault tolerance__.
  - If one disk fails, the other disk is still working.
  - data gets sent to two EBS volumes at the same time.

#### EBS encryption:
- you can encrypt both the boot and data volumes of an EC2 instance
- What is encrypted:
  - The data at rest inside the volume,
  - all data moving between the volume and the instance,
  - all snapshots that get created from the volume.
  - all volumes created from those snapshots.
- Encryption is supported by all EBS volume types.
- all instance families support encryption as well.

### File Share <a id="FileShare"></a>

| Service                  |   Purpose
|--------------------------|-----------------
| Elastic File System (EFS)| File share for Linux EC2 instances on AWS
| FSx for Windows          | File share for Windows EC2 instances on AWS
| FSx for Lustre           | File share Optimized for High Performance
|                          | Computing – Linux EC2 instances
|                          | Access S3 as a file share (like Storage Gateway)

- Fully managed – automatically grow and shrink
- High Durability and Availability – Replicated across multiple availability zones in a region
- All these file shares can be used from On-Premises using AWS Direct Connect or VPN

#### Elastic File System (EFS) 

Amazon EFS is a fully managed service for hosting Network File System (__NFS__) filesystems in the cloud.

- File Share for __Linux__ EC2 instances on AWS (NOT Windows).
- fully managed file system solution accessed using the __NFS protocol__ only.
- You get __elastic storage capacity__
- you __pay only for what you use__.
- You get __multi-AZ metadata and data storage__.
- can configure __mount points in one or many AZs__.
- __can mount from on-premises systems, but only if you have a Direct Connect or VPN connection__.
- you can use the AWS Data Sync service to synchronize data into an AWS EFS.
- EFS is elastic and grows and shrinks as you add and remove data.
- can scale up to petabytes.
- can __concurrently connect up to thousands of EC2 instances from multiple AZs within a region__.
- You can choose general purpose or Max I/O Both SSD-backed.
- Data always get stored across __multiple AZs__ within a region
- you get __read-after write consistency__.
- You need to create mount targets and choose the AZs to include
- You can mount an AWS EFS filesystem from on-premises systems ONLY if you are using __AWS Direct Connect or a VPN connection__
- Lifecycle management moves files that have not been accessed for a period of time to the EFS Infrequent Access Storage class
- Encryption in transit is enabled when mounting the file system. Enable encryption at rest in the EFS console or by using the AWS CLI or SDKs.
- EFS is much more __expensive__ than EBS or S3
- managed, scalable, secure, file sharing
- __can be protected with security group__
- __create mounts points to EFS in each AZ__
- __accessible from ec2, ecs, eks or from on premises__
- DR: you can move files to S3 using: DataSync (EFS->EFS or EFS->S3), scripts, or AWS Backup (EFS->S3)

| **Storage Type**   | **Throughput**                                     | **Latency**        | **IOPS**         | **Durability**            | **Scalability**                    | **Use Case**                                      |
| ------------------ | -------------------------------------------------- | ------------------ | ---------------- | ------------------------- | ---------------------------------- | ------------------------------------------------- |
| **Instance Store** | Very High (up to 1 GB/s depending on instance)     | Very Low (< 1 ms)  | Very High        | Low (ephemeral)           | Limited (instance size)            | Temporary storage for caching, scratch space      |
| **EBS**            | 100 MB/s to 16,000 MB/s (depending on volume type) | Low (~1–10 ms)     | 100–64,000 IOPS  | High (99.999%)            | Scalable (up to 64 TiB per volume) | Persistent storage for databases, file systems    |
| **S3**             | High (up to 5 GB/s per request)                    | Higher (1–10 ms)   | Not Applicable   | Very High (99.999999999%) | Virtually Unlimited                | Object storage for backups, media, big data       |
| **EFS**            | Scales up to 10 GB/s                               | Moderate (1–20 ms) | High concurrency | High (99.999999999%)      | Scalable (petabytes)               | Shared file storage for web apps, content systems |


Access control:
- use IAM to control who can administer your file system.
- For controlling access to files and directories, there's a __POSIX compliant user and group level permissions__ that you can apply.
  - POSIX permissions allow you to restrict access from hosts by user and group.
- EFS security groups act as a firewall and the rules you add to find the traffic flow, who's allowed to connect to your file system.

For encryption:
- EFS offers the ability to encrypt data at rest and in transit.
- Encryption at rest must be enabled at file system creation time.
- Encryption keys are managed by AWS KMS.
- Data encryption in transit uses transport layer security.

Data Sync:
- is a service that you can use for transferring data into EFS.
- provides a fast and simple way to securely sync existing file systems into Amazon EFS.
- You can securely and efficiently copy files over the internet or a Direct Connect connection.
- Copies file data and file system metadata such as ownership, timestamps, and access permissions.

Replication:
- You can replicate your EFS file system in an __AWS Region__.
- If you enable replication Amazon EFS __automatically and transparently replicates the data and metadata__ on the source file system to a destination file system.
- Data is transferred based on the __Last synced time__ for the replication.
- To __back up__ EFS data to __S3__, you can use the AWS CLI 'sync'__ command or use AWS Backup for a more managed approach

Mount to mount it on linux
- Use AWS Client VPN: Connect your laptop to the VPC using AWS Client VPN
  - Amazon Elastic File System creates mount targets, and each mount target lives in one subnet inside a Amazon Virtual Private Cloud.
- Install dependencies: sudo yum install -y amazon-efs-utils
- Create a mount directory: sudo mkdir -p /mnt/efs
- Mount the EFS filesystem: sudo mount -t efs fs-12345678:/ /mnt/efs


#### FSx

- provides a fully managed third-party file system.
- extermly high performance >> EFS
- __Linux and Windows__
- supports __SMB__, __NTFS__ and also __Linux__ and __MacOS__
- provides you with two options to choose from:
  - __FSx for Windows File Server__, for Windows based apps 
    - FSx for Windows File Server provides a fully managed native Microsoft Windows File System.
    - get full support for __SMB__, Windows __NTFS__, and __Microsoft AD.__
    - supports Windows Native File System features, ACL, shadow copies, and user quotas, NTFS file systems
    - that can be accessed from up to thousands of computer instances using SMB.
    - replicates data within an AZ. And in terms of Multi-AZ,
    - the file systems include an active and standby file server in separate AZs.
  - __Amazon FSx for Lustre__ for compute intensive workloads.
    - __high-performance file system __optimized for fast processing of workloads such as machine learning, high performance computing, video processing, financial modelling,
    - It works natively with S3, which means you can transparently access your S3 objects as files.
    - S3 objects are presented as files in the file system, and you can write your results back to S3.
    - It also provides a POSIX compliant file system interface.
- accessible from ec2, ecs, eks or from on premises
- supports NFS (Linux), SMB (Windows), NetApp etc. It supports file systems:
  - FSx for NetApp ONTAP: prioprietary OS to manage storage, snapshots, clones, deduplication, compression
  - FSx for OpenZFS: open source on top of Linux, solves data corruption issues, storage pool, snapshot, cloning, transactions, RAID-Z, deduplication, compression, tiered
  - FSx for Windows file server: managed service, scalable, needs Active Directory (authentication service for windows)
  - FSx for Luster (linux cluster): HPC (__high-performance__) = throughput 1000GB/s which is 100 times better then any other, cluster, open source, integrated with S3, only Linux, single AZ

Replication:
- FSx __automatically replicates data__ within the __same AZ__
- You can deploy FSx with a __Multi-AZ architecture__, where data is replicated to a __second AZ__
- To __back up__ data from FSx to __S3__, you can leverage __AWS Backup__ or you can create a Data Repository Association (DRA) to link your FSx file system to an S3 bucket
- In case of a failure, FSx __automatically fails over__ to a standby file server, ensuring minimal downtime and continued operation
    
### Storage gateways <a id="StorageGateways"></a>

- __connects on-premises software appliance with cloud-based storage__
- it is __virtual machine__ image that you install on premises
- Common targets: S3
- Use AWS S3 as a local file share backend
- when you need to access AWS storage locally, with low-latency and caching.

#### Storage gateway – File gateway

- NFS, SMB support, mount shares, shared folders
- This provides an __on-premises file server__.
- You can store and retrieve files as objects in __S3__.
- You can use it with __on-premises applications and EC2-based applications__ that need file storage in S3 for object-based workloads.
- File gateway offers SMB or NFS-based access to data in S3 with local caching.
- local cache
- Windows ACL support
- only changes are transfered
- __files are not all stored locally. Only recently accessed or recently written data is cached locally; the full dataset is stored in Amazon S3__.

#### Storage gateway - volume gateway

- can have cached volume or shared volume (and schedule task to move to S3)
- attach ec2 or VMware to gateway
- features: cache, backup volumes as EBS snapshots, integrates with AWS backup
- This supports __block-based volumes__. So, it's an iSCSI protocol that you use to connect.
- __cached volume mode__ where the __entire data set is stored on S3, and a cache of the most frequently accessed data is on site__.
- __stored volume mode__ means that the __entire data set is stored on site and asynchronously backed up to S3__

#### Storage gateway - tape gateway

- used for back up with popular backup software.
- Each gateway is pre-configured with a media changer and tape drives, all virtual, of course.
- supported by NetBackup, Backup Exec, Veeam and so on.
- When creating virtual tapes, there are various sizes available.
- Annotate gateway can have up to 1,500 virtual tapes with a maximum aggregate capacity of one petabytes.
- All data transferred between the gateway and AWS storage is encrypted using SSL.
- all data stored by Tape Gateway in S3 is encrypted with server-side encryption using Amazon S3 managed encryption keys, SSE-S3
- data is not permanently stored locally; it is __buffered (cached) temporarily and then uploaded to AWS__ (Amazon S3 or S3 Glacier/Deep Archive).

Tape Gateway enables you to replace using physical tapes on-premises with virtual tapes in AWS without changing existing backup workflows. Tape Gateway supports all leading backup applications and caches virtual tapes on-premises for low-latency data access. Tape Gateway encrypts data between the gateway and AWS for secure data transfer and compresses data while transitioning virtual tapes between Amazon S3 and Amazon S3 Glacier, or Amazon S3 Glacier Deep Archive, to minimize storage costs.

Tape Gateway compresses and stores archived virtual tapes in the lowest-cost Amazon S3 storage classes, Amazon S3 Glacier and Amazon S3 Glacier Deep Archive. This makes it feasible for you to retain long-term data in the AWS Cloud at a very low cost. With Tape Gateway, you only pay for what you consume, with no minimum commitments and no upfront fees.

Tape Gateway stores your virtual tapes in S3 buckets managed by the AWS Storage Gateway service, so you don’t have to manage your own Amazon S3 storage. Tape Gateway integrates with all leading backup applications allowing you to start using cloud storage for on-premises backup and archive without any changes to your backup and archive workflows


#### DataSync vs Storage gateway
- data sync
  - to transfer data
  - uses agent (=VM) that is used to read/write data from your storage
- storage gateway 
  - storage system store your data in cloud
  - storage gatway appliance (=VM) 

#### FSx vs Storage gateway file gateway?

| Feature / Service            | **Amazon FSx**                                                        | **AWS Storage Gateway – File Gateway**                         |
| ---------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Type of Storage**          | Fully managed **cloud-native file system**                            | **Hybrid cloud storage**: local access + S3-backed             |
| **Primary Use Case**         | Replace traditional on-prem file servers with AWS-native file systems | Extend on-prem apps to cloud using existing file protocols     |
| **Storage Location**         | **Fully cloud-based** (e.g., FSx for Windows, Lustre, ONTAP)          | Local cache, with data stored in **Amazon S3**                 |
| **Access Protocols**         | SMB, NFS, Lustre, iSCSI (varies by FSx type)                          | NFS or SMB (locally), backed by S3                             |
| **Performance Model**        | High performance, scalable cloud file systems                         | Local disk cache + S3 transfer (latency depends on cache size) |
| **Hardware Needed On-Prem?** | ❌ No                                                                  | ✅ Yes (or a VM/software appliance)                             |
| **Integration with S3**      | ❌ Not native                                                          | ✅ Yes – files stored as S3 objects                             |
| **Supports File Locking**    | ✅ (depending on FSx type)                                             | ❌ Limited / eventual consistency                               |
| **Snapshot/Backup Support**  | ✅ AWS-native snapshots, depending on FSx type                         | ✅ Files backed in S3 (versioning & lifecycle supported)        |

To connect to Amazon FSx from on-premises, you need to ensure network connectivity between your on-prem environment and your Amazon FSx file system:

| Connectivity Option        | Description                                                   |
| -------------------------- | ------------------------------------------------------------- |
| **AWS Direct Connect**     | Low-latency, high-bandwidth private connection to AWS         |
| **AWS Site-to-Site VPN**   | IPSec VPN over internet; easier to set up than Direct Connect |
| **AWS Transit Gateway**    | For large or multi-VPC environments                           |
| **Software VPN appliance** | Third-party VPN in AWS if no hardware VPN available           |


### Architecture Patterns

#### simple method of backing up Amazon EBS volumes and it needs to be fully automated.

Use Data Lifecycle Manager to create a backup schedule.

#### A distributed application has many nodes that each hold a copy of data that is synchronized between them, and you need the best performance for your storage subsystem.
 
?????
use instance stores for storing the data. That would give you great performance, and you don't have to worry about it being ephemeral because the data is synchronized.

#### An application must start out quickly when launched by an ASG, but requires app dependencies and code to be installed.

Create an AMI that includes the application dependencies and code.
That means you don't have to run the installation process when the system starts, when it first launches.

#### Many Linux instances must be attached to a shared file system that scales elastically.

use an EFS file system and mount from each instance.

#### A company requires a managed file system that uses the NTFS file system.

use Amazon FSx for Windows File Server.

#### On-premises servers must be able to attach a block storage system locally, and the data should be backed up to S3 as snapshots.

use a storage gateway, volume gateway that's in stored volume mode.

#### An Amazon EBS volume must be moved between regions.

take a __snapshot__ and copy the snapshot between regions.

#### Root EBS volumes for critical application must not be deleted on termination.

modifying the delete on termination attribute when you launch the instances.

#### On-premises servers use NFS to attach a file system, the file system should be replaced with an AWS service that uses S3 with a local cache.

use a storage gateway, file gateway and that will give you the local cache and it backs onto S3.

#### How can you change the encryption key associated with an EBS volume?

Change the key during snapshot copy process. Another option is: from an EC2 instance, mount a new EBS volume with the desired key and copy data from old volume to new volume

#### A company is evaluating use of AWS for backing up data in the cloud. One important consideration is that data needs to be available even when connection over the internet is down

The Volume Gateway runs in either a cached or stored mode.

In the cached mode, your primary data is written to S3, while retaining your frequently accessed data locally in a cache for low-latency access.

In the stored mode, your primary data is stored locally and your entire dataset is available for low-latency access while asynchronously backed up to AWS

#### An organization has a pool of EC2 Linux and Windows instances running in region us-east-2. A multimedia production workload uses Linux instances for some of the tasks followed by a set of operations in Windows instances. The media files needs to be shared across Linux and Windows instances.

__FSx for windows__ is a file share for __windows__ instances and also now __supports Linux and MacOS__.
EFS is a file share for Linux instances.
FSx for Lustre is a high performance file share and it currently supports only Linux instances. 
FSx for Lustre also supports a link to S3 bucket where the objects can accessed and stored using file system commands

Latest: 
Amazon __Elastic File System (EFS)__ - Best for: Shared file system across Linux and Windows instances.
- Amazon EFS is a fully managed, scalable, and shared file system that can be mounted by both Linux and Windows instances using different mount options.
EFS supports NFS (Network File System) for Linux instances, and for Windows instances, you can use Amazon EFS for Windows via Amazon EFS Mount Helper or SMB (Server Message Block) protocol.

Amazon FSx for Windows File Server: Windows-focused workload with access from Linux.
- If you are looking for a solution that is optimized for Windows but still allows access from Linux, Amazon FSx for Windows File Server is a good option.

#### Your customer is a small business that works with a lot of images. These images need to be backed up in a secure offsite location. Images are accessed very often initially and then rarely accessed after few days. However, when needed, it needs to be accessible as quickly as possible. How can you use AWS Cloud Storage for this?

Use AWS Storage Gateway deployed as a File Gateway

File Gateway configuration can locally cache frequently used data and for data that is not in cache, it can retrieve from AWS. It automatically and securely backsup file to S3. Volume gateway is used as block storage and not suitable for this requirement.

#### A company is in the process of migrating its on-premises SMB file shares to AWS so the company can get out of the business of managing multiple file servers across dozens of offices. The company has 200 terabytes of data in its file servers. The existing on-premises applications and native Windows workloads should continue to have low latency access to this data which needs to be stored on a file system service without any disruptions after the migration. The company also wants any new applications deployed on AWS to have access to this migrated data.

Use Amazon FSx File Gateway to provide low-latency, on-premises access to fully managed file shares in Amazon FSx for Windows File Server. The applications deployed on AWS can access this data directly from Amazon FSx in AWS

#### You would like to mount a network file system on Linux instances, where files will be stored and accessed frequently at first, and then infrequently. What solution is the MOST cost-effective?

Amazon EFS Infrequent Access

Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. Amazon EFS is a regional service storing data within and across multiple Availability Zones (AZs) for high availability and durability.

Amazon EFS Infrequent Access (EFS IA) is a storage class that provides price/performance that is cost-optimized for files, not accessed every day, with storage prices up to 92% lower compared to Amazon EFS Standard. Therefore, this is the correct option.

Amazon FSx for Lustre is a file system better suited for distributed computing for HPC (high-performance computing) and is very expensive

EFS types:
- Amazon EFS Standard (General Purpose)
- Amazon EFS Infrequent Access (EFS IA)
- EFS One Zone Storage Class
- EFS Lifecycle Management (Automatic Transition between Storage Classes)
  - While this is not a storage class in itself, EFS Lifecycle Management enables you to automatically transition files between the EFS Standard and EFS IA storage classes based on their access patterns.

#### A financial services company wants to move the Windows file server clusters out of their datacenters. They are looking for cloud file storage offerings that provide full Windows compatibility. Can you identify the AWS storage services that provide highly reliable file storage that is accessible over the industry-standard Server Message Block (SMB) protocol compatible with Windows systems? 

- Amazon FSx for Windows File Server
Amazon FSx for Windows File Server is a fully managed, highly reliable file storage that is accessible over the industry-standard Server Message Block (SMB) protocol. It is built on Windows Server, delivering a wide range of administrative features such as user quotas, end-user file restore, and Microsoft Active Directory (AD) integration.

- To access Amazon FSx for Windows File Server from your on-premises data center, you can use AWS Direct Connect or a VPN connection

- File Gateway Configuration of AWS Storage Gateway
Depending on the use case, AWS Storage Gateway provides 3 types of storage interfaces for on-premises applications: File, Volume, and Tape. The File Gateway enables you to store and retrieve objects in Amazon S3 using file protocols such as Network File System (NFS) and Server Message Block (SMB).

#### How do you ensure high availability and fault tolerance for Amazon EBS volumes?

To ensure high availability and fault tolerance for Amazon EBS:
- __Multi-AZ Deployments__: Use EBS volumes across different Availability Zones (AZs). This can be done by taking snapshots in one AZ and restoring them to volumes in other AZs in case of an AZ failure.
- __Snapshots__: Regularly back up EBS snapshots to Amazon S3 for disaster recovery. Snapshots can be restored in any AZ or region.
- __Elastic Volumes__: Dynamically scale EBS volumes up or down to meet changing workloads without downtime.
- __Monitoring__: Use CloudWatch to monitor volume health, throughput, and performance. Set alarms for failures and performance degradation.

#### How does Amazon EFS handle file locking and concurrent file access?

Amazon EFS supports file locking and concurrent file access by using NFSv4.1 and NFSv4.2 protocols, which offer file locking mechanisms. The system supports read-write locks that can be used by multiple clients simultaneously to avoid data corruption.

- File Locking: EFS supports NFS file locking to prevent concurrent modifications to the same file
- Concurrency: EFS ensures that multiple EC2 instances or clients can read and write concurrently to the file system with minimal latency

#### What are the trade-offs between using Amazon EFS vs. using Amazon S3 for file storage in terms of performance, cost, and use case suitability?

- EFS provides real-time __file-based access__ (NFS), while S3 is suitable for object storage where data is accessed over __HTTP/S__.
- Use EFS for applications requiring __shared file access__, and use __S3 for cheap storage__ of large datasets, backups, or media files that don’t need constant access.
- S3 High-throughput object storage, but access is not as fast or __low-latency as file systems like EFS__.

#### How would you migrate a large on-premises file system to Amazon EFS with minimal downtime?

- Set up __Amazon EFS__: Deploy an EFS file system within your __VPC__ and create mount targets in the correct subnets.
- __AWS DataSync__: Use AWS DataSync to automate the migration of data from on-premises to EFS. DataSync supports high-speed transfers and can sync data between on-premises storage and Amazon EFS with minimal downtime.
- __Test Migration__: Conduct a pilot test with a subset of the data to verify the migration process before migrating the entire dataset.
- __Cutover Phase__: During the cutover phase, ensure that file system access is directed to EFS and new data writes are directed to the cloud while synchronizing any final changes to EFS.
- __Post-Migration__: Once the migration is complete, continue syncing any changes made during the migration period and verify the application works seamlessly on EFS.













## Docker Containers and ECS <a id="Containers"></a>

Key features of the Elastic Container Service:
- __serverless computing with AWS Fargate__ managed for you and fully scalable.
- __Fully managed container orchestration__. The control plane is managed for you.
- __Docker support__, you can run and manage Docker containers with integration into the Docker compose CLI.
- You also get __Windows Container Support__. ECS supports management of Windows containers.
- You get __Elastic Load Balancer integration__ so you can distribute traffic across containers using either an ALB or an NLB.
- You get Amazon ECS anywhere. It enables the use of the ECS control plane to manage on-premises implementations.

Layers:
| One computer      | VM             | Docker
|-------------------|----------------|---------
| physical          | physical       | physical
| kernel            | __hypervisor__ | kernel
| application layer | kernel *n      | __docker daemon__
| application       | app layer *n   | app layer * n
|                   | application *n | application * n

### ECS components <a id="ECS"></a>

- __Cluster__: It's a __logical grouping of EC2 instances__. you can create IAM policies for your clusters to allow or restrict users access to specific clusters.
- A __container instance__: is an EC2 instance that runs the ECS agent.
- __Container agent__: The container agent __runs on each infrastructure resource on an ECS cluster__. The container agent is included in the Amazon ECS optimized AMI. The container agent is Linux and Windows-based. And for non-Linux instances to be used on AWS, you must manually install the ECS container agent.
- A __task definition__ is a __blueprint that describes how a Docker container should launch__, It's a text file in JSON format that describes one or more containers up to 10. Task definitions use Docker images to launch the actual containers. And you can specify the number of tasks to run.
- __task__ itself is a __running container__ using settings from a task definition.
  - Three ways to run:
    - Batch
      - Scheduled execution of tasks
      - Invoked through EventBridge rules
    - Service
      - Suitable for continuously running tasks
      - Example, global ecommerce site need web, app and data tiers running 24x7
    - Run-task
      - Manually start a task or configure run-task action in response to an event
  - ECS __automatically replaces unhealthy tasks and instances__
- A __service__ is used to define long running tasks, and you can control how many tasks you want to run. You can also use auto scaling and elastic load balancing.
- no setup required
- aws integration (CloudWatch, ALB etc)
- intelligent scheduling
- fargate
- secure, IAM
- Scalable

Building APIs with Docker containers has been gaining momentum over the years. For hosting and exposing these container-based APIs, they need a solution which supports HTTP requests routing, autoscaling, and high availability. In some cases, user authorization is also needed.

For this purpose, many organizations are orchestrating their containerized services with Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS), while hosting their containers on Amazon EC2 or AWS Fargate. Then, they can add scalability and high availability with Service Auto Scaling (in Amazon ECS) or Horizontal Pod Auto Scaler (in Amazon EKS), and they expose the services through load balancers.

When you use Amazon ECS as an orchestrator (with EC2 or Fargate launch type), you also have the option to expose your services with Amazon API Gateway and AWS Cloud Map instead of a load balancer. AWS Cloud Map is used for service discovery: no matter how Amazon ECS tasks scale, AWS Cloud Map service names would point to the right set of Amazon ECS tasks. Then, API Gateway HTTP APIs can be used to define API routes and point them to the corresponding AWS Cloud Map services.

ECS cluster = many docker hosts acting as one + container orchestration
- provides a pool of resources where you can schedule anr run containers
- Infrastructure:
  - Fargate - serverless, fast launch time, per per use (cpu, memory), needs VPC
    - You do NOT pay for EC2 instances at all.
    - You pay per vCPU-second and per GB-second that your container actually runs
    - Fargate task, can access the internet even if it is running in private subnet: you need a NAT Gateway or NAT instance in a public subnet.
  - EC2 instances witch auto-scaling, full control over instances
    - ALB can send traffic directly to containers
    - needs agent on ec2
    - Network mode:
      - host: all container have the same NIC. Containers cannot use same port
      - bridge: one NIC and bridge sends to different containers, one port
        - bridge dynamic port mapping: solves this problem
      - VPC: separate NIC for each container. You can attach security group
- task definition:
  - define containers and resource requirements
  - container image, environment variables, volumes, ports, and networking mode
  - Task placement on EC2: ECS decides where to place tasks based on multiple factors:
    - Resource availability: CPU, memory, ports on each EC2 instance.
    - Placement constraints and strategies: You can use rules like “distinctInstance,” “memberOf” (labels), “binpack,” or “spread.”
    - Custom instance attributes (labels): Only one part of the placement logic.
- service:
  - includes load balancer and auto-scaling
  - Ensures the desired number of task copies are always running (replicas).
  - Can automatically replace failed tasks.
- ECS anywhere: add VMs from your data center. You need to:
  - install SSM agent to register VM with AWS Systems Manager 
  - set IAM role
  - set ECS Agent on this VM
- ECS cluster level encryption: encrypts the data
- ECS storage
  - ephemeral storage: only fargate
  - managed storage: persists beyond task/container lifetime
  - EBS, EFS
- Compute
  - Fargate and Farget stop - always included
  - EC2. AWS will automatically create: auto-scaling group, launch template
    - use ecs optimized AMI else you need to install ESC agent yourself

Launch types: determine the type of infrastructure on which your tasks and services are hosted:
- Amazon __EC2 launch type__
  - explicitly provision EC2 instances,
  - you're responsible for upgrading, patching, and taking care of that pool of instances
  - you handle cluster optimization,
  - you get more granular control over infrastructure.
- __Fargate__
  - the control plane asks for resources and Fargate provisions,
  - it's fully serverless.
  - provisions the compute as needed and handles all cluster optimization.
  - You have limited control as the infrastructure is automated, but also you have less management overhead.

ECS images:
- containers are created from Read-Only templates called an image, which has the instructions for creating a Docker container.
- Images are built from a Docker file.
- only Docker containers are currently supported.
- An image contains the instructions for creating the container.
- Images are stored in a registry such as Docker Hub or the Elastic Container Registry.
- ECR is a managed AWS Docker registry service that is secure, scalable, and reliable, and it's also private.

Deployment Options:

| Location        | Purpose
|-----------------|----------------------------------------------------------
| AWS Local Zones | AWS location closer to large population centers and industries
|                 | Run latency sensitive applications in local zones
| AWS Wavelength  | AWS managed edge infrastructure embedded within 5G communication providers
|                 | Run latency sensitive mobile services
| AWS Outposts    | AWS managed on-premises infrastructure
|                 | Suitable when on-premises systems need low-latency access to AWS services
| ECS Anywhere    | Run containers in customer-managed infrastructure
|                 | On-premises or other cloud providers

Deployment strategies - Upgrade production app with no downtime:
- Rolling Deployment:
  - Small number of new tasks are launched
  - Wait until health check passes
  - Remove old tasks
  - Repeat until all old tasks are replaced with new
- Blue/Green Deployment:
  - Old and new version of software running side-by-side
  - Rapidly respond to issues with new version

Auto scaling for ECS:
- service autoscaling:
  - adjusts the desired task count up or down using the application auto scaling service.
  - supports target tracking, step, and scheduled scaling policies
- cluster auto scaling:
  - uses a capacity provided to scale the number of EC2 cluster instances using EC2 auto scaling.
  - the ASG can automatically scale using managed scaling and managed instance termination protection can be configured as well.

"Container Instance Role" - Agent (EC2) uses this role to:
- Communicate with ECS service
  - EC2 Instance registration, deregistration
  - Launch and terminate tasks
  - Reports status of tasks and server to Cluster
- Download images from private repository
- Retrieve third-party repository credentials stored in Secrets Manager
- Publish Container generated logs to CloudWatch Logs

Data Volumes for Containers:
- EFS File Share' and 'FSx for Windows File Share:
  - All tasks (from a task definition) access the same storage
- EBS Volumes: Private task level storage

Networking Modes:
- Host Mode: Container is directly connected to host networking
- Bridge Mode (static port): Virtual network bridge between host and container. Remap Host port to container port
- Bridge Mode (Dynamic port): Virtual network bridge between host and container. Docker assigns a random host port for container
- AWSVPC Mode: Each Task is assigned a network interface and private IP. Containers can bind to static port

Service Discovery:
- Internal Elastic Load Balancer
- Shared Internal Elastic Load Balancer: Single Load Balancer shared with many services
- Cloud Map: Maintain service domain names in Cloud Map. ECS automatically updates entries
- App Mesh: 
  - Service discovery with ease of managed load balancer
  - Envoy proxy handles load balancing
  - Envoy Proxy can detect failures and retry failed requests

### Elastic Kubernetes Service, EKS <a id="EKS"></a>

- use this when you need to standardize container orchestration across multiple environments using a managed Kubernetes implementation.
- __can have a hybrid deployment__ where you manage Kubernetes clusters and applications across hybrid environments like AWS and on-premises.
- Batch processing where you're using the Kubernetes Jobs API.
- It can be used for machine learning use cases and web applications as well.
- __EKS Anywhere__: Intended for __hybrid environments__.
- __Cluster Federation__ / Multi-cluster Management. Use tools like Amazon EKS Connector, Rancher, or KubeFed to federate or manage on-prem clusters along with EKS.

ECS versus EKS
- So, both are all managed, highly available, highly scalable container platforms.
- ECS, it's AWS specific and supports Docker. It's considered simpler to learn and use and it leverages various AWS services.
- EKS, it's compatible with Kubernetes, so it's easy to lift and shift from other Kubernetes deployments. Kubernetes is considered to be more feature rich and complex and has a steep learning curve.

### Architectural Patterns

#### application will be deployed on Amazon ECS and it must scale based on memory.

Use service auto scaling and use the memory utilization as the metric to follow. Configure auto-scaling policies for your ECS service
- Define Memory Requirements for the Container in __Task Definition__
- Enable ECS Service Auto Scaling: create Auto Scaling Policies for your ECS service
  - CloudWatch alarm to monitor the memory usage of the ECS tasks
  - configure Auto Scaling policies to scale the ECS service up or down based on the alarm.
  - Attach Scaling Policies to the ECS Service

#### An application will run on ECS tasks across multiple hosts and needs access to an S3 bucket.

use a task execution IAM role to provide permissions to the S3 bucket. So remember this is task level, not host level.
- Create an IAM Role for ECS Tasks
- Configure ECS Task Networking
  - If you're using Amazon ECS on __Fargate__, your tasks automatically get internet access. If they are launched in a VPC with a public subnet or through a NAT Gateway in a private subnet.
  - If you're using Amazon ECS with EC2 instances, ensure that your EC2 instances (where ECS tasks run) have:
    - Public IP (if using public subnets) or
    - NAT Gateway (if using private subnets) for outbound internet access.
    - Better: VPC Endpoint for S3
- Configure S3 Bucket Permissions: Ensure that your S3 bucket policy allows access from the ECS task's IAM role.

#### A company requires standard Docker container automation and management service to be used across multiple environments.

use Amazon EKS. If they're looking for industry standards rather

#### A company plans to deploy Docker containers on AWS at the lowest cost.

- use ECS with a cluster of spot instances and enable spot instance draining.
- You might actually find that Fargate is cheaper because you're paying for the tasks themselves rather than the cluster hosts, but it really depends on your workload.
- Use AWS Lambda for Short-Lived Container Jobs

#### A company plans to migrate Docker containers to AWS and does not want to manage operating systems.

use Fargate because it is serverless,

#### Multiple microservices applications running on ECS need to route based on information in the HTTP header.

Use an __ALB__ in front of ESC and use query string parameter-based routing.
- Set Up Your ECS Services: Each of your microservices should be deployed as an ECS service with a specific task definition
- Create an Application Load Balancer (ALB)
  - listeners
  - securty groups
  - target groups for each ECS
- Define Routing Rules in ALB: listeners -> rules

You can also use __Amazon API Gateway__ instead of Application Load Balancer (ALB) to route traffic to multiple microservices running on Amazon ECS based on HTTP headers.

Attention: __ECS Service itself does not directly perform load balancing__, it can work in conjunction with AWS Load Balancers

ECS Service:
- An ECS service ensures that a __specified number of ECS tasks__ (containers) are running at any time.
- It automatically __restarts__ tasks if they fail or stop.
- It also supports __auto-scaling__, where the number of running tasks is increased or decreased based on demand.

If you don't use an Application Load Balancer (ALB), but you have an ECS Service running with 3 ECS Tasks, all three tasks will be running, but only one of them may be directly accessible depending on how you expose the tasks to the outside world.

#### A containerized app runs on Amazon EKS and you need to collect and centrally view metrics and logs including EKS namespaces and EKS services.

use the CloudWatch performance monitoring tool and it has a feature called Container Insights. And you can view that data in the CloudWatch console.

####  Your lambda function needs to access internet and other AWS Service end points: By default, a lambda function is not bounded to a VPC

If you attach the lambda to a VPC, you'll loose internet access, which prevents you from accessing resources such S3 and Dynamo, and from making HTTP requests.

####  Lambda functions, by default, are allowed access to internet resources.

Yes, Lambda functions, by default, are allowed to access internet resources. When a Lambda function is executed, it runs in an environment that has internet access unless explicitly configured otherwise.

To access databases and other resources in your VPC, you need to configure Lambda function to run inside the context of a private subnet in your VPC.
When this is done: your lambda function gets a private IP address and can reach resources in your VPC.
In this mode, it can access internet services only if private subnet has a route to a NAT device

#### What option do you have to monitor the performance characteristics of distributed applications? You need the ability to pinpoint components that are slow or have a high error rate.

AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. 
With X-Ray, you can understand how your application and its underlying services perform to identify and troubleshoot the root cause of performance issues and errors

#### The container images are hosted on a third-party private repository. The image must be privately shared with applications running on an ECS cluster. How would you configure security to allow image access for authorized applications?

Store access credentials in Secrets Manager and configure Task Execution Role with permission to access Secrets Manager. 
The __task execution role__ is assigned to a specific task definition and is used by ECS Container Agent to download images and run the container. 
The __Container Instance Role__ would also work; however, the permissions are assigned to the EC2 instance, and all Tasks running on that instance would get elevated privileges. 
The __task role__ is used for granting permissions to your application code to access other AWS services (like S3, DynamoDB, SQS, and so forth)

#### A distributed application uses many containers to process the pending work. The containers are short-lived, and after completing the work, they stop running. The container logs must be stored in CloudWatch logs to troubleshoot any issues. How would you send the logs to CloudWatch logs?

Docker containers use log drivers to collect containers' standard output and standard error streams and forward the log to the configured destination. 
The __awslogs__ driver publishes the captured logs to the CloudWatch log group. 
This is a straightforward setup to consolidate logs from containers

#### A containerized application sees sustained high CPU and memory utilization. Which of these launch types may optimize the cost?

ECS Cluster with EC2 instance launch type

#### A microservice deployment uses an Elastic Load Balancer to facilitate service-to-service communication. The caller sends the request to a load balancer endpoint, and the load balancer routes the request to healthy containers running in an ECS cluster. However, the drawback of this approach is that every micro service requires a load balancer, which increases the deployment cost. Which options would lower the cost and ensure the requests are forwarded only to healthy containers?

We can minimize the number of load balancers using Application Load Balancer __path-based routing__ capability. 
Here, we create __one target group for each microservice__ and assign a unique path. 
Depending on the path used by the caller, the request is routed to the appropriate microservice. 

Another option is using App Mesh. 
With App Mesh, an envoy sidecar is deployed along with each container. 
App Mesh publishes services and their tasks to Envoy. 
Envoy performs a health check of tasks and routes the request to a healthy target. 
With App Mesh, we don't need an elastic load balancer.

#### You have a docker container that is listening on Port 80. It is part of an ECS Task and managed using ECS. An Elastic Load Balancer routes the requests to the container. You want flexibility to launch multiple instances of this Task in a single EC2 Instance. What Elastic Load Balancer can you use for this?

__Application Load Balancer with Dynamic Port Mapping__

Dynamic Port mapping allows automatic mapping of unused EC2 instance port to container. 
When container is registered with ALB, it automatically tracks the instance and port combination. 
This will allow you to run multiple tasks belonging to same task definition in a single EC2 instance

#### what is the pricing for using Amazon Elastic Container Service (Amazon ECS) with the EC2 launch type compared to the Amazon Elastic Container Service (Amazon ECS) with the Fargate launch type?

- ECS on EC2: Pay for EC2 instances (and related resources like EBS, ALB, etc.)
- Fargate: Pay per vCPU and GB of memory provisioned per second

#### A media company operates a video rendering pipeline on Amazon EKS, where containerized jobs are scheduled using Kubernetes deployments. The application experiences bursty traffic patterns, particularly during peak streaming hours. The platform uses the Kubernetes Horizontal Pod Autoscaler (HPA) to scale pods based on CPU utilization. A solutions architect observes that the total number of EC2 worker nodes remains constant during traffic spikes, even when all nodes are at maximum resource utilization. The company needs a solution that enables automatic scaling of the underlying compute infrastructure when pod demand exceeds cluster capacity. Which solution should the architect implement to resolve this issue with the least operational overhead?

Deploy the Kubernetes Cluster Autoscaler to the EKS cluster. 
Configure it to integrate with the existing EC2 Auto Scaling group to automatically launch or terminate nodes based on pending pod demands

The Kubernetes Cluster Autoscaler is the recommended and most seamless solution to automatically manage the size of an EKS cluster's underlying compute resources. 
It works in tandem with the Kubernetes scheduler and continuously monitors the cluster for unschedulable pods—these are pods that cannot be scheduled due to a lack of available resources (CPU, memory, etc.) on the current set of EC2 nodes.

When the Cluster Autoscaler detects unschedulable pods, it attempts to find an Auto Scaling group (ASG) attached to the EKS cluster that can satisfy the resource requirements of the pending pods. If it finds one, it automatically increases the desired capacity of that ASG, triggering the launch of new EC2 nodes. These new nodes register with the cluster and become available to host the previously unschedulable pods. In the same way, the Cluster Autoscaler also supports scale-in operations: it identifies underutilized nodes and safely drains and terminates them if their workloads can be moved elsewhere—leading to cost savings and higher resource efficiency.

This approach ensures the EKS cluster is highly elastic, cost-effective, and operationally simple, making it the best fit for real-time, variable workloads with minimal administrative overhead.

#### What is the difference between Amazon ECS Task Definitions and Kubernetes Pods?

- ECS Task Definition:
  - It is a blueprint for an ECS task, specifying the Docker images, environment variables, networking settings, resource allocations (CPU, memory), and IAM roles.
  - A Task Definition is more like a deployment specification in ECS, and it describes how containers in a task should run and interact. When you create a service, ECS uses the task definition to launch and manage containers.
  - ECS tasks can restart automatically, similar to Kubernetes Pods, but the mechanics of how they are restarted differ between Amazon ECS and Kubernetes.
- Kubernetes Pod:
  - A Pod is the smallest and simplest Kubernetes object. A pod can contain one or more containers that are deployed together on the same node and share resources (e.g., network namespace, storage).
  - Pods are self-healing, which means if a container in a pod crashes, Kubernetes will automatically restart the container to maintain the desired state.

#### How does ECS handle service discovery for containerized applications, and how is it different from EKS?

- ECS Service Discovery: ECS provides built-in service discovery by integrating with AWS __Cloud Map__. The ECS service discovery allows tasks to discover each other by resolving DNS names without needing static IPs
- EKS Service Discovery: service discovery is provided by CoreDNS

#### How would you implement continuous deployment (CD) for a containerized application using ECS and EKS with github actions

Continuous Deployment to ECS using GitHub Actions:
- checkout
- docker/setup-buildx-action@v1 : GitHub Action that sets up Docker Buildx - creates images for various platforms
- login to Log in to Amazon ECR
- Build and push Docker image to Amazon ECR
- Update ECS service with new image: aws ecs update-service --cluster my-ecs-cluster --service my-ecs-service --forc









## Serverless Applications <a id="Serverless"></a>

Serverless Services:
- no instances to manage.
- don't need supervision hardware
- there's no management of operating systems or software
- capacity provisioning and patching is handled automatically
- it provides automatic scaling and high availability.
- can be very cheap to run serverless services.

Serverless services:

![ Serverless services ](./images/serverless_services.png)

### Lambda <a id="Lambda"></a>

- Lambda runs code as functions.
- Lambda executes the code only when needed and __scales automatically__.
- You __pay only for the compute time you consume__ and you pay nothing when your code is not running.
- You specify the amount of memory you need allocated to your Lambda functions.
- Lambda __allocates CPU power proportional to the memory__ you specify using the same ratio as a general purpose EC2 instance type.
- There is a __maximum execution time out, and that's 15 minutes or 900 seconds. And the default is 3s__.
- Lambda terminates the function at the timeout.
- Lambda is an event-driven compute service.
- An __event source is an AWS service application that produces events that trigger an AWS Lambda function__.
- Event sources are mapped to Lambda functions.
- __For stream-based services Lambda performs the polling e.g. DynamoDB and Kinesis__. So that means Lambda checks with the stream based service rather than the polling coming the other way.
- __Inbound network connections are blocked by AWS Lambda__. However, outbound calls are allowed from Lambda. In this case, we can use an API Gateway to listen and receive inbound requests. The API Gateway would then invoke a Lambda function to process the request
- Benefits of Lambda:
  - there's no service to manage.
  - continuous scaling,
  - millisecond billing,
  - integrates with almost all other AWS services.
- The primary use cases:
  - data processing,
  - real time file processing,
  - real time streaming processing,
  - building serverless backends for various different use cases.
  - Pricing based on memory, and duration (GB-Seconds). Millisecond Metering
- event driven
- pay per execution or usage
- max execution time: 15 min
- cold start
- auto-scaling based on load
- runs on VPC or direct access to internet
- available runtimes: java, python, node.js, 
- lambda_handler(event, content) - in python mandatory function name
- lambda blueprint: edit written lambdas and save them as your own 
- lambda execution role
  - create role that given permission to lambda to do something (write to S3)
  - add role to your lambda
  - you need to do it or create 'default execution role' that given lambda permission to write to CloudWatch log
- Boto3 - library in python to execute aws APIs
- Lambda trigger:  You have to add a trigger to your lambda function
- You can package and deploy AWS Lambda functions as __container images__.

There is an upper limit on number of __concurrent lambda function executions__ for your account in each region.

Lambda support __versioning__ and you can maintain one or more versions of your lambda function. Each lambda function has a unique ARN. By default latest version is executed

Lambda Alias:
- Lambda also supports __Alias__ for each of your functions. 
- Lambda alias is a pointer to a specific lambda function version.
- Alias enables you to promote new lambda function versions to production and if you need to rollback a function, you can simply update the alias to point to the desired version
- allows you to trigger lambda version you want

__Cold start__: to process new request, Lambda must initialize new instances – slowness in response (Cold Start)

For Latency sensitive applications, keep lambda instances always ready! Configured using “__Provisioned concurrency__” setting.

Since AWS Lambda functions can __scale extremely quickly__, this means you __should have controls in place to notify you when you have a spike in concurrency__. A good idea is to deploy an __Amazon CloudWatch Alarm__ that notifies your team when function metrics such as ConcurrentExecutions or Invocations exceeds your threshold. You should create an __AWS Budget__ so you can monitor costs on a daily basis.

Different types of function invocation:
- synchronous
  - CLI, SDK, or API Gateway.
  - result gets returned immediately.
  - Error handling happens on the client side
- Asynchronous:
  - S3, SNS, and CloudWatch events.
  - Lambda will retry up to 3 times,
  - processing needs to be idempotent.
- event source mappings:
  - SQS, Kinesis data streams, and DynamoDB streams
  - Lambda has the mapping to the stream-based service.
  - Lambda does the polling,
  - Records get processed in order except for SQS Standard.

Orchestrate Lambda:
- Use Step Functions for long running workflows
- Build your app using smaller Lambda functions
- Orchestrate using Step Functions

Lambda Scaling:
- Deploys 500 function instances for initial burst!
- Some regions deploy up to 3000 instances
- Additional 500 instances per minute until concurrency limit is reached
- Application Requests Per Second: 
  - Function takes 300 ms to process a request
  - Per second = 3.3 requests [1000/300]
  - With 500 Lambda instances, your app can support 3.3 X 500 = 1,600 requests per second
  - Throttling error when requests exceed concurrency limit

RDS Connection:
- Large number of open connections to database
- Open and Close at a high rate
- Exhaust database resources
- __Use RDS Proxy__: et’s you share database connections across multiple Lambda instances

Lambda netework isolation:

![ Lambda netework isolation ](./images/lambda_network_isolation.jpg)

Synchronous Invocation:
1. Caller waits for function execution to complete
2. Any errors are returned to the caller – invalid permission, invalid data, throttling error and more
3. Retries are handled by the caller
4. Throttling errors – caller must retry using exponential backoff strategy (increase wait time between successive retries)

Asynchronous Invocation:
1. Caller gets a success acknowledgement (that request was added to queue!)
2. Separate Lambda process reads the events and sends them to your function

Error Handling in Asynchronous execution:
1. Function error – Lambda retries two more times
2. Throttling errors – Lambda will retry for up to six hours with exponential backoff
3. Original caller is not aware of errors!
4. Optional – Store failed events in a Dead-Letter Queue
5. Optional – Store send success events to SQS, SNS, EventBridge

Lambda@Edge:
- Customize cached content without routing request to origin
- Improve security by checking for expired or invalid JWT token and redirect to login page

Lambda container images
- Specify container image: any OS
- Specify OS-only Runtime
  - Amazon Linux + install your runtime

Lambda in VPC
- by default lambda runs in amazon managed infrastructure
- use it to access resources from your VPC
  - ENI is created and attached to your subnet. It has private IP
  - add NAT or Internet gateway
  - add security group

Lambda and Amazon Q (AI agent - executes actions on your behalf): use it to write lambdas to start or stop ec2 instances etc

#### AWS Lambda execution environment
- lambda creates execution environment (container) to process the request
- aws creates this environment automatically (allocates compute resources)
- aws loads python runtime 
- function is injected/loaded into container
- first time: latency 100-300 ms
- if started execution environment is busy, aws launches new execution environment (auto-scaling)
- to reduce cold starts: 
  - provisioned concurrency: pre-warmed lambda
  - optimized memory and cpu allocation = faster processing
  - lambda layers - preloaded dependencies
- warm start: reuses started execution environment
- Concurrency: how many lambda instances will run?
  - default concurrency limit for all lambdas: 1000 / region (all lambdas)
  - you can increase concurrency limit or use many regions or use many accounts
  - formula = duration of each request [s] * requests/s 
  - reserved concurrency: reserve for a given function and no other lambda can use it
  - types of concurrency:
    - on demand: automatically spins up environment when request arrives (default), has cold-start problem
    - provisioned concurrency: pre-initializes execution environment (eliminates cold-starts)
      - must have version and alias enabled
      - it creates specified execution environments (no cold start)
      - check throttles metric
      - you pay for min
- lambda layers
  - module: single file containing code
  - library: collection of modules packaged together (python boto3). Must be imported
  - __lambda layers__: allows you to manage common code (modules or libraries) separately from common code
  - you can attach layer in many lambda functions
  - built-in and custom libraries

### Fargate <a id="Fargate"></a>

Fargate Serverless Compute for Containers

Specify CPU and Memory needed

Hourly charge for CPU and Memory

Scheduled Tasks – Pay only when the task is running

Web App - Need to pay even when there is no traffic

"Task Execution Role" - Fargate Agent uses this role to:
- Download images from private repository
- Retrieve third-party repository credentials stored in Secrets Manager
- Publish Container generated Logs to CloudWatch Logs

ECS with Fargate allows you to run containers without managing EC2 infrastructure, and it integrates natively with Amazon EFS to support persistent, shared storage for stateful applications. You __define the EFS volume in the task definition and mount it to the container__, allowing multiple tasks to access shared data. This setup requires __no server or storage lifecycle management__ and aligns perfectly with the company's requirements.

### API Gateway <a id="APIGateway"></a>

All the APIs created with Amazon API Gateway expose HTTPS endpoints only (does not support unencrypted endpoints).

An API can present a certificate to be authenticated by the back end

CloudFront is used as the public endpoint for API Gateway

With API Gateway, you can route requests to private resources in your VPC. Using HTTP APIs, you can
build APIs for services behind private ALBs, private NLBs, and IP-based services registered in AWS Cloud Map, such as ECS tasks

- fully managed service for publishing, maintaining, monitoring and securing APIs
- An API endpoint type refers to the hostname of the API.
- all of the APIs created with __API Gateway expose HTTPS endpoints only__.
- The endpoint type can be __edge-optimized__ if you've got a global user base, regional if your user base is within a region or private if you want to provide access only within a VPC or to computers connected over a Direct Connect connection.
  - they hit a nearby edge location (CloudFront
  - Then AWS routes the request over its private network to your API’s region
- API Gateway also has caching.
- you can add caching to API calls by provisioning the cache and specifying its size in gigabytes. That means you can cache the end points response.
- __Caching__ can reduce the number of API calls to your backend and improve latency.
- __Throttling__ with API Gateway, where you're setting a limit on the steady state rate and the burst of request submissions against the APIs in your account.
- By default, API Gateway limits to steady state requests to __10,000 requests per second__ and the maximum concurrent request is 5,000 across all APIs within the account. If you go over those limits, you get a 429 too many requests error message.
- if those exceptions occur, then you'll need your client application to resubmit the failed requests in a way that doesn't exceed those rate limits again.
- Amazon API Gateway creates RESTful APIs that enable __stateless__ client-server communication and Amazon API Gateway also creates WebSocket APIs that adhere to the __WebSocket__ protocol, which enables stateful, full-duplex communication between client and serve
- API Gateway is a regional service: When you create an API in API Gateway, it exists in a __region__, not in a specific Availability Zone (AZ).

#### API Gateway endpoints

An API endpoint type is a hostname for an API in API Gateway that is deployed to a specific region.
The hostname is of the form {api-id}.execute-api.{region}.amazonaws.com.

The API endpoint type can be:
- __edge-optimized__ for geographically distributed clients. API requests are routed to the nearest CloudFront Point of Presence (POP)
- __regional__ intended for clients in the same region. When a client running on an EC2 instance calls an API in the same region
- __private__ can only be accessed from your Amazon Virtual Private Cloud (VPC) using an interface VPC endpoint, which is an endpoint network interface (ENI) that you create in your VPC

![ Gateway endpoints ](./images/gateway_endpoints.jpg)

#### Caching

You can add caching to API calls by provisioning an Amazon API Gateway cache and specifying its size in gigabytes.

API Gateway caches responses for a specific amount of time (time to live or TTL). The default TTL is 300 seconds

#### API Gateway Scaling

API Gateway sets a limit on a steady-state rate and a burst of request submissions against all APIs in your account.

By default API Gateway limits the steady-state request rate to __10,000 requests per second__.
The maximum concurrent requests is 5,000 requests across all APIs within an AWS account

Default scaling up to 10,000 requests/second
• Throttle requests
• Limit requests/second by API keys
• Usage Plan based on API Keys

Amazon API Gateway caching is a feature that enables you to cache the responses from your API endpoints to improve performance and reduce the number of calls made to your backend services.

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications. API Gateway supports containerized and serverless workloads, as well as web applications.

You can enable Amazon API caching in Amazon API Gateway to cache your endpoint's responses. With caching, you can reduce the number of calls made to your endpoint and also improve the latency of requests to your API. When you enable caching for a stage, API Gateway caches responses from your endpoint for a specified time-to-live (TTL) period, in seconds. Amazon API Gateway then responds to the request by looking up the endpoint response from the cache instead of requesting your endpoint. The default TTL value for API caching is 300 seconds. The maximum TTL value is 3600 seconds. TTL=0 means caching is disabled. Using API Gateway Caching feature is the answer for the use case, as we can accept stale data for about 24 hours.

| Feature                                        | Description                                                                                                     |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Configurable TTL**                           | You can specify how long responses remain cached (in seconds).                                                  |
| **Cache Invalidation**                         | Cache is invalidated automatically after TTL expires; can be manually invalidated by deployment or via SDK/CLI. |
| **Per-Stage Caching**                          | Caching is enabled and configured per API stage (e.g., dev, prod).                                              |
| **Cache Encryption**                           | Cache data can be encrypted at rest for security.                                                               |
| **Cache Size Options**                         | Multiple cache sizes available to balance cost and performance (from 0.5 GB up to 237 GB).                      |
| **Integration with Method Request Parameters** | Cache keys can be based on request parameters, headers, or body to ensure correct cache hits.                   |
| **Cost Savings & Performance**                 | Reduces backend calls and speeds up API responses.                                                              |


#### Usage plans and API keys

A usage plan specifies who can access one or more deployed API stages and methods — and how much and how fast they can access them


### Architecture Patterns

#### an application includes EC2 and RDS and spikes in traffic are causing writes to be dropped by RDS.

You can decouple EC2 and RDS with an SQS queue and you can use Lambda to process the records from the queue.

#### A web app includes a web tier and a processing tier. And it must be decoupled and the processing tier should dynamically scale based on the number of jobs.

decouple the web tier and the processing tier with an SQS queue. You can scale with auto scaling based on the queue length.

#### A Lambda function execution time has increased significantly as the payload size increased.

optimize execution time by increasing the memory available to the function. It will proportionately increase the amount of CPU available to the function as well.

#### Statistical data stored in RDS and will be accessed using a REST API. Demand will range from no traffic to sudden bursts of traffic and it's unpredictable.

create a REST API using API Gateway and integrate with a Lambda function for connecting to the RDS database.

#### A new application processes customer orders and consists of multiple decoupled tiers. Orders must be processed in the order they are received.

you need SQS with a FIFO queue to preserve the record order.

#### An app uses API Gateway and Lambda. During busy periods, many requests fail multiple times before succeeding and no errors are reported in Lambda.

The cause of this could be that the throttle limit is set too low. So, you just need to increase that and that will hopefully resolve the issue.

API Gateway Limits: 
- throttle max 10,000 requests/sec, per account per region
- Per-method: 1000 RPS

AWS Lambda:
- Concurrency limit: 1000 new executions / 10s
- If Lambda exceeds concurrency: Requests are throttled by API Gateway that returns 502 or 429 http status code

You should align: API Gateway throttling ≤ Lambda concurrency capacity

You can configure __reserved concurrency for a Lambda function__:
- ✅ Guarantees capacity: That number of concurrent executions is always available for this function
- ✅ Caps scaling: The function cannot exceed that number

#### EC2 instance processes images using JavaScript code and stores the results in S3. The load is highly variable and you need a more cost-effective solution.

replace EC2 with a Lambda function.

#### An app uses an API Gateway Regional Rest API. It's just gone global and performance has suffered

in that case, they might want to convert the API to an edge-optimized API to optimize for a global user base. And then it will use the CloudFront edge network and improve latency and performance.

- Put Amazon CloudFront in front of your API.
  - Uses global edge locations
  - Caches responses (if possible)
- Switch to Edge-Optimized API Gateway: Edge-optimized endpoint - This automatically uses CloudFront under the hood
- Multi-region deployment (true global): For serious scale:
  - Deploy API + Lambda in multiple regions
  - Route users using: Amazon Route 53 latency-based routing

#### A legacy application uses many batch scripts that process data and pass on to the next script. And it's complex and difficult to maintain.

Use Lambda functions along with step functions for coordinating and orchestrating the application.

#### Objects uploaded to an S3 bucket must be processed by Lambda.

For this, you can create an event source notification to notify Lambda to process the new objects.

#### Your application has a Lambda function that needs access to both internet services and a database hosted in private subnet of your VPC.  What steps are needed to accomplish this?

Lambda functions, by default, are allowed access to internet resources. 
To access databases and other resources in your VPC, you need to configure Lambda function to run inside the context of a private subnet in your VPC. 
When this is done: your lambda function gets a private IP address and can reach resources in your VPC. 
In this mode, it can access internet services only if private subnet has a route to a NAT device

#### You are writing a mini-web server that would listen on the configured port to process requests from users. The code you have is straightforward, and you observe that it can fit nicely as a lambda function. Which of these options would you pick?

AWS Lambda blocks inbound network connections. 
You would need to use a service like API Gateway to receive the requests and configure API Gateway to invoke the appropriate Lambda function

#### A Lambda function is triggered whenever objects are added to the S3 bucket. Function needs to read the object and store the meta-data about the object in a DynamoDB table. What permissions are needed for this scenario?

S3 needs permission to invoke Lambda function; Lambda function needs permission to read S3 Objects and to put items in the DynamoDB table

```
// IAM role for Lambda
// assume_role_policy = This is a trust policy, not a permission policy i.e. “Who is allowed to use (assume) this role?”
resource "aws_iam_role" "lambda_role" {
  name = "lambda_s3_dynamodb_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {                         // The AWS Lambda service is allowed to assume this role
        Service = "lambda.amazonaws.com"
      }
      Action = "sts:AssumeRole"             // This uses AWS Security Token Service: "log in” to this role, get temporary credentials
    }]
  })
}

// IAM policy (permissions)
resource "aws_iam_policy" "lambda_policy" {
  name = "lambda_s3_dynamodb_policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = ["s3:GetObject"]
        Resource = "${aws_s3_bucket.bucket.arn}/*"
      },
      {
        Effect = "Allow"
        Action = ["dynamodb:PutItem"]
        Resource = aws_dynamodb_table.table.arn
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      }
    ]
  })
}

// Attach policy to role
resource "aws_iam_role_policy_attachment" "attach" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}

// Lambda
resource "aws_lambda_function" "fn" {
  function_name = "s3_to_dynamodb"

  role    = aws_iam_role.lambda_role.arn
  handler = "index.handler"
  runtime = "nodejs18.x"

  filename = "lambda.zip"
}

// Allow S3 to invoke Lambda
resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.fn.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.bucket.arn
}

// S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-example-bucket"
}

// Attach a bucket policy (resource-based policy)
resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = aws_s3_bucket.my_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid = "AllowPublicRead"
        Effect = "Allow"
        Principal = "*"
        Action = "s3:GetObject"
        Resource = "${aws_s3_bucket.my_bucket.arn}/*"
      }
    ]
  })
}

// S3 event notification
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.fn.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3]
}
```

#### An S3 bucket is configured to invoke the Lambda function whenever a new object is added to the bucket. The Lambda function transforms the object and uploads the transformed object to the same bucket. Would you approve of this solution?

No. This solution can unintentionally create an infinite loop and accumulate massive charges to your account.

#### Your Lambda function needs access to a private web end point available in your VPC.  What steps do you need to enable such an access?

Configure Lambda to run inside a private subnet of your VPC. 
Lambda function can only access private resources inside your VPC when you configure it to run inside your VPC. 
You need to specify the VPC, private subnets, and Security group as part of the Lambda configuration

#### Your application services are used by several third parties. To ensure quality of service for all customers and to prevent a single customer from consuming all the resources, you want to enforce limits on maximum requests per second that can be made by a single customer.

API Gateway can act as a single point for your third parties to integrate with your services. 
API Gateway allows to throttle requests at specific method level and manage individual API Keys. 
It also allows you to cache the responses so that API Gateway can directly answer certain method calls without invoking your backend services for every request. 
You can configure your API methods to require authorization can support IAM based control, third party identity providers, custom authorizers and so forth.

The best AWS-native way to solve this is using Amazon API Gateway Usage Plans + API Keys:
- Each customer gets a unique API key
  - This key is sent with each request (usually in header: x-api-key)
- You attach that key to a Usage Plan
- The usage plan enforces: Rate limit (requests per second)

Client sends request:
```
GET /orders
x-api-key: <customer-a-key>
```

Terraform:
```
resource "aws_api_gateway_method" "get_orders" {
  rest_api_id   = aws_api_gateway_rest_api.api.id
  resource_id   = aws_api_gateway_resource.resource.id
  http_method   = "GET"
  authorization = "NONE"

  api_key_required = true  # 🔥 IMPORTANT       // enforces usage plans
}

// Create Usage Plan (limits)
resource "aws_api_gateway_usage_plan" "basic_plan" {
  name = "basic-plan"

  throttle_settings {
    rate_limit  = 100   # requests per second
    burst_limit = 200
  }

  quota_settings {
    limit  = 1000000
    period = "DAY"
  }

  api_stages {
    api_id = aws_api_gateway_rest_api.api.id
    stage  = aws_api_gateway_stage.stage.stage_name
  }
}

// Attach API Key to Usage Plan
resource "aws_api_gateway_usage_plan_key" "customer_a_attach" {
  key_id        = aws_api_gateway_api_key.customer_a.id
  key_type      = "API_KEY"
  usage_plan_id = aws_api_gateway_usage_plan.basic_plan.id
}
```

#### Your Lambda function subscribes to an SNS topic, and the Lambda function is invoked asynchronously when a message arrives for that topic. When there is an error while processing a message, you want to ensure that the message is available for your team to troubleshoot. What configuration can you use for this?

Configure Dead Letter Queue for Lambda function

Using Dead Letter configuration, you can direct Lambda to send unprocessed events to SQS queue or SNS topic. 
This can be used for troubleshooting events that were unsuccessful. 
While you can catch errors in a Lambda function and push the events to SQS queue, Lambda does it automatically for you using Dead Letter config. 
SNS Topic itself does not have dead letter configuration. 
SQS has a dead letter option to move messages that were not processed after specified number of retries

1. SNS publishes a message
2. Lambda is invoked asynchronously
3. If Lambda fails: AWS retries automatically (up to 2 times)
4. If it still fails: Message is sent to the DLQ

#### A startup is modernizing its monolithic Python-based analytics application by transitioning to a microservices architecture on AWS. As a pilot, the team wants to refactor one module into a standalone microservice that can handle hundreds of requests per second. They are seeking an AWS-native solution that supports Python, scales automatically with traffic, and requires minimal infrastructure management and operational overhead to build, test, and deploy the service efficiently.

Use AWS Lambda to run the Python-based microservice. 
Integrate it with Amazon API Gateway for HTTP access and enable provisioned concurrency for performance during peak loads

AWS Lambda is a fully managed serverless compute service that natively supports Python runtimes. 
It is ideal for event-driven and API-based microservices. 
Lambda automatically scales based on request volume, requires no server provisioning or patching, and integrates easily with API Gateway for RESTful access. 
The company can also enable provisioned concurrency to reduce cold start latency for high-throughput workloads. 

AWS Fargate is a serverless container service that works with ECS and supports auto scaling, but it requires containerization of the application, Dockerfile management, and more setup complexity than Lambda. 
Although suitable for microservices, it involves more operational overhead, especially during initial development and testing phases.

#### How do you prevent one client from overwhelming your system?

- Use Amazon API Gateway Usage Plans + API keys for per-client throttling
- Add WAF rate limiting for IP-based protection
- Buffer with Amazon SQS to decouple spikes
- Set Lambda reserved concurrency to protect downstream systems

#### How do you avoid duplicate processing with SQS + Lambda?

- Use idempotency keys (e.g., request ID)
- Store processed IDs in:
- Amazon DynamoDB (with TTL):
  - dynamodb is eventually consistent
    - You do NOT rely on reads for correctness
    - Use conditional write: ConditionExpression: "attribute_not_exists(id)"
      - Two Lambdas try to process same message:
        - Both attempt PutItem
        - DynamoDB:
          - First succeeds
          - Second fails with ConditionalCheckFailedException
- Make writes idempotent (e.g., conditional writes)

What if Lambda crashes after write but before processing?
- Store status field:
  - IN_PROGRESS
  - COMPLETED

#### How do you reduce cold starts?

- Use provisioned concurrency for critical paths
- Keep functions small (reduce package size)
- Avoid VPC unless needed
- Use higher memory (faster CPU → faster init)

#### DLQ vs Destinations

Both are used with asynchronous Lambda invocations (like from Amazon SNS, S3, EventBridge).

What should happen AFTER Lambda finishes (success or failure)?

DLQ:
- Original event payload
- ❌ No execution details
- ❌ No error message (minimal context)

Lambda Destinations:
- Works for: Success or Failure
- SNS → Lambda → result → Destination (SQS/SNS/EventBridge/Lambda)
- What gets sent?
  - A rich execution record, including:
  - Request payload
  - Response (if success)
  - Error message (if failure)
  - Function name
  - Timestamp
  - Request ID















## Database <a id="Database"></a>

Different options:
- We can use a database on EC2. We might do that if we need full control over the instance in the database or maybe the third party database engine is not available on RDS.
- RDS is where we need a traditional relational database.
- DynamoDB is a NoSQL database, it gives you in-memory performance, and is useful for where your I/O needs are very high. It also offers dynamic scaling.
- Redshift is more for data warehouses for large volumes of aggregated data.
- ElastiCache is for temporary storage for small amounts of data. It's also in-memory.
- EMR is used for running analytics workloads using Hadoop.

![ Standard features ](./images/database_standard_features.jpg)

### RDS <a id="RDS"></a>

- RDS uses instances, so you have to choose the instance family and type.
- It's a relational database, so it uses SQL.
- RDS is an online transaction processing type of database.
- It's easy to set up, highly available, fault tolerant, and scalable.
- Can encrypt your RDS instances and your snapshots at rest by enabling the encryption option. And you do that when you create the database. Encryption uses KMS keys.
- supports the following engines, SQL, Oracle, MySQL, Postgres, and Aurora and also MariaDB.
- scales up by increasing the instance size for compute and storage.
- Read replicas are an option for read heavy workloads and that scaling out your reads.
- Disaster recovery with the Multi-AZ option.

- Configuration
  - instance classes: db.*: standard, memory optimized and compute optimized
  - pricing

__RDS DB Parameter group__: controls database settings: memory, max_connections, query_cache_size

__RDS Option Group__: add extra features or extensions that are not part of database: oracle OEM plugin, SQL Server transparent data encryption, MySQL MemCached etc.


#### RDS HA
- Single DB Instance: single AZ without replica or auto-failover. You have to do manual restore from backup and failover
- Multi-AZ DB Instance: 2 db instances in 2 AZ in the same region. 
    - __Primary__ and __Standby__ accessible via db endpoint that points to primary. 
    - Uses EBS that is replicated to secondary EBS, __synchronous__, no data loss
    - Failover: Automatic. Standby becomes primary and new secondary is created within 60s
    - No performance gain (standby is down), small latency increase because of sync to secondary
    - No scaling benefit
- Multi-AZ DB Cluster: 3 db instances in 3 AZ: __1 writer+read and 2 read standby__ DB Instances
    - Better performance for read workloads and lower write latency
    - sync process to copy data to read-instance: The transaction is committed only after it has been replicated to at least one standby in another AZ
    - failover time: 10s
    - performance gain and scaling gain, but cannot scale to more nodes
- read replica: read-only, in sync with primary
  - read replica cannot automatically take over during failover event. __Cannot provide failover benefit__
  - __can be created in another region__. 
  - The replication process is always __asynchronous__ (same or different region). There is a replication lag — the replica may be slightly behind the primary
  - __you can promote it to primary manually__.


Multi-AZ versus read replica

![ Multi-AZ versus read replica ](./images/rds_multi-az-vs-replica.png)

Push-button scaling, replication, and redundancy

You cannot have an encrypted Read Replica of an unencrypted DB instance or an unencrypted Read Replica of an encrypted DB instance

RDS supports SSL encryption between applications and RDS DB instances. RDS generates a certificate for the instance.

Enable db encryption without data loss: create snapshot -> encrypted snapshot of db -> encrypted rds db -> DMS to synchronize data

For __multi-AZ__ high availability, RDS uses __synchronous__ replication between primary and standby systems.
If standby is slow, transactions will take longer to complete. 
After failover, DNS is updated to point to new primary

__RDS Read Replica__ on the other hand uses __asynchronous__ replication and any slowness in Read Replica instance would simply cause data lag in the read - replica.
Transactions in primary is not impacted

RDS Maintenance Windows:
- Operating system and database patching can require taking that database offline,
- those tasks take place during a maintenance window
- by default, a weekly maintenance window is configured, but you can choose your own.

Combining Multi-AZ and Read Replicas
- Yes, you can combine Multi-AZ with read replicas
- Multi-AZ Primary:
  - Your RDS instance is configured as Multi-AZ for high availability.
  - It has a synchronous standby in another AZ for failover.
- Read Replicas:
  - You can create read replicas from the primary Multi-AZ instance.
  - Read replicas can be used for read-heavy workloads.
  - These replicas are asynchronously replicated.

#### RDS Security

- __encryption at rest__ can be enabled, and that includes the database storage, backups, read replicas and snapshots.
- You can only enable it when you create the instance, not afterwards.
- DB instances that are encrypted can't be modified to disable encryption,
- it uses AES 256 encryption, which is transparent with minimal performance impacts.
- Oracle and SQL, they also support transparent data encryption, which may have a performance impact.
- __KMS__ is used for managing encryption keys.
- You can't have an encrypted read replica of an unencrypted DB instance or an unencrypted read replica of an encrypted DB instance.
- Read replicas of encrypted primary instances are encrypted and the same __KMS key__ is used if in the same region as the primary, or if it's in a different region, a different KMS key is used.
- You can't restore an unencrypted backup or snapshot to an encrypted DB instance.
- __Network encryption__: to encrypt traffic between ec2 and database - use __certificate authority__  to create __certificate_ and install it in ec2 application server:
  - Enable __SSL__ on the RDS instance
  - Download the AWS RDS SSL Certificate on ec2
  - Connect with SSL/TLS Using JDBC
- __data encryption__: enable during instance creation. 
  - when set, the data is encrypted at rest.
  - it uses __KMS__ to encrypt database, backup, snapshot, replica, db logs
  - to encrypt data in transit: create server certificate (asymmetric key) use SSL/TLS for connections.  
    - Certificate: Contains the public key and is signed by a trusted Certificate Authority (CA).
  - to encrypt an unencrypted database you need to:
    - create unencrypted snapshot
    - copy the snapshot with encryption enabled
    - restore the database from encrypted shapshot

__Authentication and access controls__:
- use __AWS Secrets Manager__ to handle management of master credentials automatically. It automatically rotates credentials (and updates db credentials)
  ```
  aws secretsmanager create-secret \
    --name prod/myapp/db \
    --description "RDS credentials for myapp" \
    --secret-string '{"username":"app_user","password":"StrongPassword123!"}' \
    --tags Key=Environment,Value=Production

  // later  
  AWSSecretsManager client = AWSSecretsManagerClientBuilder.defaultClient();
  GetSecretValueRequest request = new GetSecretValueRequest().withSecretId("my-db-credentials");
  GetSecretValueResult result = client.getSecretValue(request);
  String json = result.getSecretString();  // contains username/password
  ```
- __environment variables__ - Good for containers/EC2. Store credentials as environment variables injected at deployment time
- __AWS Systems Manager Parameter Store__ (with encryption): store the credentials as SecureString parameters.
  ```
  AWSSimpleSystemsManagement ssm = AWSSimpleSystemsManagementClientBuilder.defaultClient();
  GetParameterRequest request = new GetParameterRequest().withName("/my/db/password").withWithDecryption(true);
  String password = ssm.getParameter(request).getParameter().getValue();
  ```
- __IAM Authentication for RDS__ (Best for short-lived access): Use temporary IAM tokens instead of passwords to connect. Only works with RDS MySQL and PostgreSQL.
  ```
  {
    "Effect": "Allow",
    "Action": "rds-db:connect",
    "Resource": "arn:aws:rds-db:us-east-1:123456789012:dbuser:db-ABCDEFGHIJ/app_user"
  }

  // later
  String token = RdsIamTokenGenerator.generate(...);
  String jdbcUrl = "jdbc:mysql://mydb.cluster-xyz.rds.amazonaws.com:3306/mydb";
  Connection conn = DriverManager.getConnection(jdbcUrl, "iam_user", token);
  ```
- password __Kerberos authentication__ - when using AD


Recomendations:
- Deploy RDS in __Private Subnet__ (unless your requirement is a publicly accessible RDS instance)
- __Configure RDS Security Group__ to allow access from Web Server or Application Server Security Groups
- Assign a __subnet in all Availability Zones__ to the DB Subnet Group

#### RDS backups are snapshots

Automated backups and patching are applied in customer- defined maintenance windows.

By default, Amazon RDS creates and saves automated backups of your DB instance securely in Amazon S3 for a user-specified retention period. 

- automated backups: daily, incremental shanpshhots. First backup is full snapshot. Sored in S3 in the same region as db. Retention period:1-35 days (default 7)
  - backup window - to minimize performance impact
  - backup replication - in another region
  - cost: free up to rdb allocated size
  - use manual if you want to  keep backups for longer than 35 days or do it when you want.
- snapshots
- restoring from backups/snapshots: use RDS console
  - restoring to latest backup
  - restore to Point-in-time (PTR)
  - restore from S3: instead of creating database and importing the data, you can do it in one step. Only restores exported .dump file) = offline migration
  - to migrate life database use AWS DMS

Automated Backups:
- they backup the __entire DB instance, not just individual databases__.
- backup occurs during a daily user-configurable 30 minute period known as the backup window
- For __single AZ DB instances, there's a brief suspension in I/O__.
- For __multi-AZ SQL, I/O activity is briefly suspended on the primary__.
- backup your databases and transaction logs
- You can restore your DB instance to any specific time during the backup retention period, creating a new DB instance
- The first snapshot of a DB instance contains the data for the full database. Subsequent snapshots of the same database are incremental, which means that only the data that has changed after your most recent snapshot is saved.
- In addition to the daily automated backup, RDS archives database change logs. This __enables recovery of the database to any point in time during__ the backup retention period, __up to the last five minutes__ of database usage

In addition, you can create snapshots, which are user-initiated backups of your instance that are kept until you explicitly delete them. 

Snapshots:
- For Multi-AZ, MariaDB, MySQL, Oracle, and Postgres, the snapshot gets taken from the standby.
- Snapshots do not expire. There's no retention period.
- you can share a manual DB snapshot or DB cluster snapshot with other AWS accounts.

#### RDS Scaling

You can only scale RDS up (compute and storage).
You cannot decrease the allocated storage for an RDS instance.
You can scale storage and change the storage type for all DB engines except MS SQL.

RDS now supports Storage Auto Scaling

Scaling compute will cause downtime.

#### Multi-AZ and Read Replicas

Multi-AZ:
- Multi-AZ RDS creates a __standby replica__ in another AZ and synchronously replicates to it (DR only)
- During failover RDS automatically updates configuration (including DNS endpoint) to use the second node.
- It is recommended to implement DB connection retries in your application
- The secondary DB in a multi-AZ configuration cannot be used as an independent read node (read or write).

Read Replica Support for Multi-AZ:
- Amazon RDS Read Replicas for MySQL, MariaDB, PostgreSQL, and Oracle support Multi-AZ deployments
- A Read Replica in a different region than the source database can be used as a standby database and promoted

Read Replicas:
- Read replicas are used for read-heavy DBs and replication is __asynchronous__.
- Read replicas provide read-only DR.
- Read replicas are created from a snapshot of the master instance.
- Read replicas are available for MySQL, PostgreSQL, MariaDB, Oracle, Aurora, and SQL Server.
- In a multi-AZ failover the read replicas are switched to the new primary.

#### RDS Storage

  - uses EBS
  - storage types: gp2, gp3 (general purpose), io1, io2 (provisioned), magnetic. Max storage is 65TB depending of database enging and storage type)
  - RDS data stiping: improves performance of reads and writes. Configured automatically
  - Storage Auto-scaling: scales beyond 'allocated storage'. Storage increased afher threashold is reached. Not available for Multi-AZ Cluster or for read-replica.

#### RDS Performance and monitoring

- __Performance Insights__: tool in RDS to understand how db engine is workng: top sql quesries, wait events, database load, user sessions, load by query type etc. Real-time
- __Enhanced Monitoring__: of OS like: cpu usage, memory usage, disk IO, file system usage, network throughput, 1s granularity, connect to CloudWatch Logs
- __CloudWatch__: general monitoring for AWS. Combines data from database angine and OS. 1-5 min delay. Can set alarms, automatic response, track logs
- RDS __Log Exports__: contains database activity (error logs, audit logs, slow query log, general log). You can store them only in AWS CloudWatch Logs (from database server)
  - for long term retention you can export these logs from CloudWatch Logs to S3
  - You need a IAM role. It will be created automatically.

#### Maintenance: security pathces, minor upgrades (5.4.3->5.4.4)

- you need to enable it
- you can select maintenance window
- major upgrades (5.4.3->5.5.1) are manual
- the maintenance depends on deployoemt type: Single AZ - there will be downtime.. Multi-AZ - has failover, Cluster - no downtime
- deletion prodection - use it for prod databases

#### Blue-Green deployment (blue: current, green: duplicate of prod, staging, test schema changes, test engine major upgrades)

- use it for major database upgrades
- one green is fully tested, traffic will switch from blue to green
- if green fails then rollback

#### RDS Proxy

- manages database connections - connection pooling
- improves failover handling
- especially useful for __aws lambda__: solves connection overload 
- makes db more secure and simple: RDS Proxy uses __AWS Secrets manager__ and you do not need to add db credentials in EC2 or Lambda
- RDS Proxy runs in __multiple AZs__ simultaneously
- Scalability: RDS Proxy automatically adjusts capacity to accommodate changes

#### RDS Zero-ETL Integration

- automatically replicates data __from RDS to Redshift__
- near real-time
- now only MySQL

#### ElastiCache Cluster for RDS

- shard: logical partition of your database, consists of one primary and multiple replica nodes, can do reads
- cluster mode: define number of shards and number of replicas, supported my redis not memcached
- if cluster mode disabled = 1 shard, fixed replicas, all data in one shard, supported by redis and memcached
- __redis supports: geospatial indexing, real-time notifications (pub-sub), sorted sets for leaderboards, persistence, multi-az, auto-failover, auth token, encryption__
- __memcached__: simple cases, one shard, one az, does not have redis features above
- __replication group__ = primary node + replica nodes = cluster
- Cache strategies:
  - __read-through cache__: cache automatically fetches the data on cache misss
  - __cache-aside cachine (lazy loading)__: application checks cache and in miss then gets the data and updates cache
  - __write-Though caching__: update cache all the time the data is written to db

#### Connect to RDS from java application on EC2

- Your RDS security group allows inbound access from EC2 on the correct port
- Get RDS Connection Details
  - Endpoint: e.g., mydb.abc123xyz.us-east-1.rds.amazonaws.com
  - Port: based on the DB engine
  - Username/password: from RDS configuration
  - Database name
- Include JDBC Driver in Your Java App
- Connect Using JDBC in Your Java Code


#### Aurora <a id="Aurora"></a>

Separation of compute and storage

Storage Subsystem that automatically maintains __6 copies__ of data across __3 availability zones__

- This is an AWS database offering in the RDS family.
- Aurora is a MySQL and Postgres compatible relational database built for the cloud.
- Aurora is __up to 5 times faster than standard MySQL and 3 times faster than Postgres__.
- Aurora features a distributed fault tolerant, self-healing storage system that scales up to 128 terabytes per database instance.
- key features of Aurora:
  - Gives you high performance self-healing storage up to 128 terabytes.
  - Point-in-time recovery and continuous back up to S3
  - compatible with MySQL and Postgres databases.
  - in-region read scaling __failover target with up to 15 Aurora replicas__
  - __cross-region scaling with failover targets with MySQL replicas__.
  - Global database is a cross-region cluster with read scaling and it gives you fast replication and low latency reads. And you can remove the secondary and promote it if you need to.
  - __Multi-master scales out writes within a region__
  - __serverless__ is an on-demand auto scaling configuration for Aurora. Does not support read replicas or public IPs.

Aurora endpoints:
- Cluster endpoint: Points to Current Primary Instance
- Reader endpoint: Points to Read Replicas
- Instance endpoint: Points to Individual Aurora Instance

![ Aurora replica ](./images/aurora_replica.png)

When should you not use RDS?
- Any time you have a DB type other than the supported database engines.
- you need root access to the operating system. You won't be able to do that on RDS.
- for large binary objects, S3,
- automated scalability, name/value data structures or data that's not well structured or is unpredictable. Those would be better on DynamoDB.

2 copies of data are kept in each AZ with a minimum of 3 AZʼs (6 copies)

Can handle the loss of up to two copies of data without affecting DB write availability and up to three copies without affecting read availability.

__Aurora Auto Scaling__ enables your Aurora DB cluster to handle sudden increases in connectivity or workload.
Aurora Auto Scaling dynamically adjusts the number of Aurora Replicas (reader DB instances) provisioned for an Aurora DB cluster.
Aurora Auto Scaling enables your Aurora DB cluster to handle sudden increases in connectivity or workload.
When the connectivity or workload decreases, Aurora Auto Scaling removes unnecessary Aurora Replicas so that you don't pay for unused provisioned DB instances.
The scaling policy defines the minimum and maximum number of Aurora Replicas that Aurora Auto Scaling can manage

Amazon Auroraʼs backup capability enables point-in-time recovery for your instance.
Allows you to restore your database to any second during your retention period

Aurora Replicas:
- __Aurora Replica__
  - up to 15 replicas
  - in-region
  - automated failover
  - asynchronous
- __MySQL Replica__
  - up to 5 replicas
  - cross-region
  - manual failover
  - asynchronous

Cross-Region Read Replicas:
- available ONLY for __Amazon Aurora with MySQL compatibility__


##### Aurora global databases:

An __Aurora global database__ consists of a:
- __primary Aurora DB cluster__ in one AWS Region, where your data is __written__,
- up to 5 __read-only secondary DB clusters__ in up to five other AWS Regions.

You issue __write__ operations directly to the __primary__ DB cluster in the primary AWS Region.
Aurora replicates data to the secondary AWS Regions using dedicated infrastructure, with latency typically under 1 second.

A database in a secondary region can be __promoted to full read/write__ capabilities in less than 1 minute

##### Multi-Master

Amazon Aurora Multi-Master is a feature of the __Aurora MySQL-compatible__ edition that adds the ability to
__scale out write performance__ across multiple Availability Zones, allowing applications to direct read/write workloads to multiple
instances in a database cluster and operate with higher availability.

designed to achieve high availability and __ACID transactions across a cluster of database nodes__ with configurable __read after write consistency__

- Maximum writer nodes: 16 writer instances per cluster. 
- You can also have additional read replicas (up to 15 per cluster in Aurora MySQL).
- All writer nodes share a single, distributed storage layer.
- Writes from any node go to the same underlying table.
- Aurora handles conflict detection at the storage layer.
- application-level conflicts may still happen if multiple writers update the same row simultaneously

##### Aurora Serverless

On-demand, auto-scaling configuration for Amazon Aurora.

Available for MySQL-compatible and PostgreSQL-compatible editions.

You only pay for database storage and the database capacity and I/O your database consumes while it is active. 
Pay on a per-second basis for the database capacity you use when the database is active.

Storage and Processing are separate – scale down to zero processing and pay only for storage

Automatic Pause and Resume – Configurable period of inactivity after which DB Cluster is Paused

Rapid scaling: uses a pool of warm resources

#### Migrate database from datacenter to RDS using DMS

Use the AWS __Database Migration Service__ (AWS DMS), which allows you to transfer data between on-premises databases and cloud-based RDS instances with minimal downtime

steps involved in migrating a database to RDS using AWS DMS:
- Create AWS resources
- Configure source database
- Create replication instance in DMS
- Set up data providers
- Create migration project
- Perform schema conversion (if needed)
- Start migration
- Test and switch over

#### Migrate database from RDS without DMS

- Take a full backup of the database on the on-premises DB instance.
- Upload the backup file to Amazon S3.
- Download the backup file from S3 to your RDS Custom for SQL Server DB instance.
- Restore a database using the downloaded backup file on the RDS Custom for SQL Server DB instance.

Importing RDS MySQL → Aurora MySQL:
- Using a Snapshot: Supported if Aurora MySQL version >= the RDS MySQL version
- Using Logical Backup (mysqldump)

### ElastiCache <a id="ElastiCache"></a>

- fully managed implementation of Redis and Memcached.
- It's a key value store
- an in-memory database with great performance and low latency.
- You can put it in front of databases such as RDS and DynamoDB.
- nodes run on EC2 instances,

![ Elasticache ](./images/elasticache.png)

Push-button scalability for memory, writes and reads.

ElastiCache EC2 nodes cannot be accessed from the Internet, nor can they be accessed by EC2 instances in other VPCs.

Memcached:
- Does not support multi-AZ failover or replication.
- Does not support snapshots.
- You can place nodes in different AZs.
- multi-threaded
- no HA (replication)

Redis:
- Supports master / slave replication and multi-AZ for cross-AZ redundancy
- Supports automatic and manual snapshots (S3)
- Data is persistent and it can be used as a datastore.
- Redis is not multi-threaded
- Supports more complex data structures: sorted sets and lists.
- Replication from the primary node is asynchronous

Multi-AZ failover:
- ElastiCache automatically promotes the replica that has the lowest replica lag
 
### DynamoDB <a id="DynamoDB"></a>

- It's a fully managed NoSQL database service.
- It's a key value store and a document store.
- It's fully serverless and you get push button scaling.
- you can achieve ACID compliance with DynamoDB transactions.
- Data is synchronously replicated across three facilities in a region.
- DynamoDB is schema-less.
- it can be used for storing session state data.
- It provides two read models, eventually consistent reads and strongly consistent reads.
- two pricing models:
  - on-demand capacity where DynamoDB charges you for the data reads and writes your application actually performs.
  - Provisioned capacity mode means that you specify the number of reads and writes, and you'll pay whenever it's used or not.
- We can define a TTL, so the items in our table will expire after a period of time.
- key features a DynamoDB:
  - It's serverless, fully managed, and fault tolerant.
  - It's highly available with great availability, even better with global tables.
  - It's a NoSQL type of database with a name/value structure, so good when you need a flexible schema.
  - It gives you horizontal scaling with push button scaling and auto-scaling options.
  - Transaction options are strongly consistent or eventually consistent reads as well as support for ACID transactions.
  - Backup is point in time recovery down to the last second in the last 35 days
  - on-demand backup and restore as well.
  - Global Tables is a multi-region multi-master solution.
- Point-in-Time Recovery – Automated Continuous Backup (35 days retention)
- On-Demand Backup/Snapshot for long term retention
- Automatic deletion of expired items – Time To Live
- Limits - Item size cannot exceed 400 KB
- cost based on: data storage, read/write operations

Data is synchronously __replicated across 3 AZs in a region__

Multi-AZ redundancy and Cross-Region Replication option.

DynamoDB stores and retrieves data based on a __Primary key__. There are 2 types of primary key:
- __Partition key__ - unique attribute. Value of the Partition key is input to an internal hash function which determines the partition or physical location on which the data is stored
- __Composite key__ - combination of __primary key and sort key__. All items with the same Partition key are stored together, then sorted according to the Sort key value.

If your access pattern exceeds 3000 RCU or 1000 WCU for a single partition key value, your requests might be throttled.

DynamoDB supports:
- __eventually consistent reads__: When you read data from a DynamoDB table, the response might not reflect the results of a recently completed write
- __strongly consistent reads__: response with the most up-to-date data, reflecting the updates from all prior write operations that were successful
  - may have higher latency than eventually consistent reads.
  - are not supported on global secondary indexes.
  - use more throughput capacity than eventually consistent reads.

#### DynamoDB Storage Architecture

- split data into multiple units called __partitions based on Hash(Partition key)__
- Each partition is small, manageable
- partitions are distributed across multiple nodes (servers): leader server and replica nodes in many AZ
- __Leader node__ handles writes, strongly consisted reads
- __Replica nodes__ handle eventually consistent reads

#### Read Consistency

- eventually consistent, 
- strongly consistent read (3 items - 3 queries), 
- transactional read (3 items - 1 query)
- __RCU__ (read capacity unit): how much data can you read per s
  - item size: block = 4KB
  - read consistency type: eventual: 0.5, strongly_consistent: 1, transactional: 2 
  - __RCU formula = ceil(item_size_KB/4) * reads_per_s__ / consistency_type

#### Write Consistency: standard, transactional (2 updates in 1 request)

- __WRC__ (Write Capacity Unit): how much data can we write /s
  - item size: block = 1 KB
  - write consistency type: standard: 1, transactional: 2 
  - number of writes / s
  - __RCU formula = ceil(item_size_KB) * writes_per_s * consistncy_type__

#### Capacity Mode

- On-Demand: you do not need to setup RCU,WRC. Automated elastic scaling. Can set max capacity.
- Provisioned: must set RCU and WCU. You pay for allocated capacity. Traffic will be throttled. Autoscaling: min, max, utilization
- Warm Throughput: scale capacity without throtteling or delay
- there can be a significant cost benefit to using Provisioned Capacity Mode in Amazon DynamoDB if your workload is predictable and stable: 
  - Provisioned: cost of 1 month of 100 read requests/s of eventual RCU: 4.68 USD
  - On Demand: cost of 1 month of 100 read requests/s of eventual RCU: 64.8 USD

#### Table Settings

- table class: standard vs standard-IA (infrequent access): define how storage cost is calculated:
  - standard: frequent access, storage cost: higher, request cost: lower
  - standard-IA: infrequent access, storage cost: lower, request cost: higher
  - you can change the class at will
- capacity mode:
- max read capacity units:
- max write capacity units:
- local secondary indexes
- global secondary indexes:

#### How to Connect Java App to DynamoDB from EC2

- Add AWS SDK to Your Java Project
- Assign IAM Role to EC2
- Write Java Code to Connect
```
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.model.*;

public class DynamoExample {
    public static void main(String[] args) {
        // Set the AWS Region
        Region region = Region.US_EAST_1; // change if needed

        // Create DynamoDB client (uses EC2 instance role credentials automatically)
        DynamoDbClient ddb = DynamoDbClient.builder()
                .region(region)
                .build();

        // List tables example
        ListTablesResponse response = ddb.listTables();
        System.out.println("Tables: " + response.tableNames());

        ddb.close();
    }
}
```

#### DynamoDB streams

- captures a time mode sequence of item level modifications in your table,
- stores them in a log file for up to 24 hours,
- you can process that data.
- you can configure what data is actually written. Keys only, new image, old image, or new and old images.
- data added, updated, deleted - creates event available for 24 hours. Streams captures changes, who and when, cost included in DynamoDB
- Integrates with: AWS Lambda, Kinesis Client Library, Kinesis Data Firehose, Amazon OpenSearch, S3, Amazon Redshift, Step Functions, EventBridge 

__DynamoDB Trigger__: action triggered by a stream and connects to AWS Lambda

__DynamoDB Kinesis Data Stream:__ integrates with many aws services, separate cost, retention up to 365 days, supports advanced processing like aggregation, windows

      
#### DAX = DynamoDB Accelerator

- fully managed in-memory cache for DynamoDB,
- will reduce latency from milliseconds to microseconds.
- can be both a read-through cache and a write-through cache.
- DAX is updated only if DynamoDB is successfully updated first.
- you don't need to modify any application logic, DAX is fully compatible with the DynamoDB APIs.
- can improve reads up to 10 times: millisecond -> microsecond
- read-through cache
- write to DAX: write to DynamoDB and update cache
- Setup:
  - node family = compute
  - cluster size = number of nodes
  - VPC, subnet
  - Security Group
  - AZ
  - Permissions to access DynamoDB
- Each table has endpoint
- Clients use DAX client (or DynamoDB client) and uses 'table' endpoint
- When using Amazon DynamoDB Accelerator (DAX): you create a DAX cluster made up of nodes. 
  - Recommended production setup continas 3 nodes: 1 primary node + 2 replica nodes
  - nodes run inside your VPC, specifically in subnets you choose
- Your application does NOT connect directly to nodes. Instead it connects to a single DAX cluster endpoint

#### DynamoDB Transactions

Transactions provide atomicity, consistency, isolation, and durability (ACID) in DynamoDB.

Enables reading and writing of __multiple items across multiple tables__ as an all or nothing operation

Example:

```
    Collection<TransactWriteItem> actions = Arrays.asList(
        new TransactWriteItem().withConditionCheck(checkCustomerValid),
        new TransactWriteItem().withUpdate(markItemSold),
        new TransactWriteItem().withPut(createOrder));

    TransactWriteItemsRequest placeOrderTransaction = new TransactWriteItemsRequest()
        .withTransactItems(actions)
        .withReturnConsumedCapacity(ReturnConsumedCapacity.TOTAL);

    // Run the transaction and process the result.
    try {
        client.transactWriteItems(placeOrderTransaction);
        System.out.println("Transaction Successful");

    } catch (ResourceNotFoundException rnf) {
        System.err.println("One of the table involved in the transaction is not found" + rnf.getMessage());
    } catch (InternalServerErrorException ise) {
        System.err.println("Internal Server Error" + ise.getMessage());
    } catch (TransactionCanceledException tce) {
        System.out.println("Transaction Canceled " + tce.getMessage());
    }
```

#### Scan and Query API calls

Scan:
- returns one or more items and item attributes by accessing every item in a table or a secondary index.
- reads up to the maximum number of items set (if using the Limit parameter) or a maximum of 1 MB.
- A filter expression is applied after a Scan finishes but before the results are returned

Query:
- finds items in your table based on the primary key attribute and a distinct value to search for.
- You can use an optional sort key name and value to refine the results.
- Results are always sorted by the sort key

#### Indexes

An index is a data structure which allows you to perform fast queries on specific columns in a table.

You select columns that you want included in the index and run your searches on the index instead of the entire dataset.

2 types of indexes:
- Local Secondary Index
  - alternative sort key to use for scans and queries.
  - You can have up to five LSIs per table.
  - The sort key consists of exactly one scalar attribute
  - must be created at table creation time
  - benefit of an LSI is that you can query on additional values in the table other than the partition key / sort key
- Global Secondary Index
  - You can create when you create your table or at any time later.
  - A GSI has a different partition key as well as a different sort key

__DynamoDB Global vs Local Indexes__:
- GSI:
  - new partition and sork keys
  - replicates data from main table
  - no sharing storage with main table.
  - dedicated capacify without affecting main table
  - can be created long after table was created
  - eventually consistent
- LSI
  - same partition key but different sort key
  - uses capacity of main table
  - must be created at table creation time
  - updated at the same time as main table. no delay. always strongly consistent

#### Global Tables

Provide a fully managed solution for deploying a __multi-region__, __multi-master__ database.

Global tables provide automatic multi-master replication to AWS regions world-wide

A __global table__ is a collection of one or more __replica tables__, all owned by a single AWS account.

Each replica table stores the same set of data items.

An application can read and write data to any replica table.
If your application only uses eventually consistent reads, and only issues reads against one AWS region, then it will work without any modification.

If your application requires strongly consistent reads, then it must perform all its strongly consistent reads and writes in the same region. DynamoDB does not support
strongly consistent reads across AWS regions.

Conflicts can arise if applications update the same item in different Regions at about the same time. To help ensure eventual consistency, DynamoDB global tables use a “last writer wins” method to reconcile between concurrent updates.

- data is replicated from one region to another
- 2 way replication
- HA: if 1 region is down, customers who connect to other regions are fine
- Global Table uses 'DynamoDB Streams'
- Conflict resolution: last writer wins based on timestamps


#### DynamoDB Encryption

- at rest: automatic, 
  - key management: KMS, 
  - owned by: 
    - DynamoDB, 
    - AWS Managed Key (stored in your KMS in your account): limited audit logs
    - Customer Managed key (you create it in KMS): you define rotation, see audit logs, monitoring, strict compliance requirements
- in transit 

#### DynamoDB Resource Policies:
- defines who (aws account, user, services) can access your table/index and pwrform what operations (getItem, PutItem, Query)
- Extra rules: specific IP or time range

#### DynamoDB Backup

- backup saves: table data, indexes, settings
- does not affect performance of DynamoDB
- PITR (point in time recovery): continuous, automated, up to 35 days back, stored for 35 days, DR
- On Demand backups: manual, point-in-time, archival, migration

__DynamoDB Export to S3__: you want to analyze it  or share data
- no performance impact
- PITR must be on
- Full Export: all data as is or up to 35 days back
- Incremental Export: export data that has changed within specific time period
- file format: __dynamodb json__ (contains data type, better if you want to import it back) or __Amazon Ion__ (better if you want to analyze the data: glue, athena)



### Redshift <a id="Redshift"></a>

- This is a SQL-based data warehouse used for analytics.
- You get to analyze data using standard SQL and business intelligence tools.
- it's a relational database used for OLAP use cases.
- Redshift uses EC2 instances, so you have to choose the instance family and type.
- it always keeps free copies of your data and provides continuous and incremental backups.
- Use cases are where you need to perform complex queries or massive collections of structured and semi structured data with great performance, frequently access data that needs a consistent, highly structured format.
- You can use Spectrum for direct access of S3 objects in a data lake.
- it's a managed data warehouse solution with automated provisioning, configuration and patching, data durability with continuous backup to S3 and it scales with simple API calls.
- It also offers exabyte scale query capability.
- Redshift has a serverless option

Option to query directly from data __files on S3 via Amazon RedShift Spectrum__

Amazon RedShift can store huge amounts of data but __cannot ingest huge amounts of data in real time__.

__Only available in one AZ__ but you can restore snapshots into another AZ.
Alternatively, you can run data warehouse clusters in multiple AZʼs by loading data into two Amazon RedShift data warehouse clusters in separate AZs from the same set of Amazon S3 input files.

Amazon RedShift does not support Multi-AZ deployments.

Amazon RedShift always keeps three copies of your data:
- The original.
- A replica of compute nodes (within the cluster).
- A backup copy on S3.

How to optimize redshift queries:
- Distribution Styles: Use the right distribution style for your tables to minimize data movement during joins:
  - KEY – distribute rows based on a join key.
  - EVEN – default; distributes rows evenly across nodes.
  - ALL – small dimension tables replicated to all nodes for faster joins.
- Sort Keys:
  - Define sort keys on columns frequently used in WHERE clauses, joins, or aggregations.
  - Redshift stores data physically sorted by these keys, speeding up range-restricted scans.
- Compression Encodings:
  - Apply column compression (like ZSTD or LZO) to reduce I/O and improve query performance.
  - Use ANALYZE COMPRESSION to automatically suggest optimal encodings.
- Vacuum & Analyze:
  - Regularly run VACUUM to reclaim space from deleted rows.
  - Run ANALYZE to update table statistics so the query planner makes optimal decisions.
- Query Optimization:
  - Avoid SELECT *; select only required columns.
  - Push filters early in the query to reduce scanned data.
  - Break complex queries into staging tables if needed for large joins.
- Workload Management (WLM):
  - Configure queues and concurrency limits to prioritize critical queries and avoid resource contention.
- Partitioning & Indexing?
  - Redshift does NOT support traditional indexes like OLTP databases.
  - Instead, you rely on sort keys, distribution keys, and interleaved sort keys to achieve similar performance benefits.

Amazon Redshift has two deployment modes:
- Provisioned Redshift (classic):
  - You provision clusters with fixed node types and sizes.
  - You manage scaling manually (or with Elastic Resize for limited adjustments).
  - Not serverless—you pay for cluster uptime, even if queries aren’t running.
- Redshift Serverless:
  - AWS introduced Redshift Serverless, which automatically scales compute capacity based on workload.
  - You don’t manage clusters; you only pay for the compute you use and storage.
  - Ideal for sporadic or unpredictable workloads.

Redshift Serverless – Use when:
- Workloads are sporadic, unpredictable, or highly variable.
- You don’t want to manage clusters or worry about resizing nodes.
- You want pay-per-use pricing based on actual query compute time.
- Good for ad-hoc analytics, development, testing, or small-to-medium production workloads.

Provisioned Redshift (Cluster-based) – Use when:
- Workloads are steady, predictable, or very high-volume.
- You need maximum performance and full control over node types, distribution, and concurrency.
- You are running large-scale ETL, complex joins, or heavy BI workloads.
- Can optimize costs via Reserved Instances for long-term, predictable usage.

### Architectural Patterns

#### Each Read Capacity Unit provisioned in a DynamoDB table translates to

A unit of Read Capacity enables you to perform one strongly consistent read per second or two eventually consistent reads per second. 
Each read can transfer up to 4KB.
Each Read Capacity Unit provisioned in a DynamoDB table translates to one strongly consistent read per second or two eventually consistent reads per second

#### An organization has several RDS databases, DynamoDB tables, and EFS file shares. The data needs to be backed up automatically, and a copy must be maintained in the disaster recovery region. Which solution would you use?

Use AWS Backup to set up backup policies, automate the process, and maintain a copy in the DR site

We can centrally manage the backup policies and automate the process using the AWS Backup service. In addition, AWS Backup can also maintain a copy of the backup in a disaster recovery region.

AWS Backup is a fully-managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud, and on premises. Using this service, you can configure backup policies and monitor activity for your AWS resources in one place.

#### You have configured an Aurora database with five read replicas.  What is the recommended mechanism for clients to connect to read replicas?

Use Aurora database reader endpoint.

If there is more than one Aurora Replica, the reader endpoint directs each connection request to one of the Aurora Replicas.

#### Your RDS instance was upgraded to most current major and minor database version. Legal requirement calls for a 10 year retention of your database backups and some of the backup were created on database versions that are no longer supported by RDS. What will happen when you restore an unsupported database version?

Older version when restored from snapshot will be automatically upgraded to currently supported database engine version

#### In a multi-AZ RDS Deployment, automatic failover will not happen under this condition

Primary Instance Deadlock and Query Timeouts

#### Your DynamoDB application stores and retrieves Items that are 8KB in size. The application reads 10 items per second in eventually consistent mode The application also writes 10 items per second. How much capacity would you need to provision?

10 Read Capacity Units and 80 Write capacity units

- A read capacity unit represents one strongly consistent read per second, or two eventually consistent reads per second, for an item up to 4 KB in size.  Item size is rounded to the next 4KB boundary.  
- A write capacity unit represents one write per second, for an item up to 1 KB in size.  Item size is rounded to the next 1KB boundary.

####  A DynamoDB table is provisioned with 20 Read Units and 20 Write Units. If items are 4KB in size, what is the net throughput that can be achieved?

A read capacity unit represents one strongly consistent read per second, or two eventually consistent reads per second, for an item up to 4 KB in size. Item size is rounded to the next 4KB boundary. For example: if item size is 4.5KB, DynamoDB would round it to 8KB for Read Capacity Unit calculation. A write capacity unit represents one write per second, for an item up to 1 KB in size. Item size is rounded to the next 1KB boundary. For example: if item size is 4.5KB, DynamoDB would round it to 5KB for Write Capacity Unit calculation

#### A healthcare company uses its on-premises infrastructure to run legacy applications that require specialized customizations to the underlying Oracle database as well as its host operating system (OS). The company also wants to improve the availability of the Oracle database layer. 

Leverage multi-AZ configuration of Amazon RDS Custom for Oracle that allows the Database Administrator (DBA) to access and customize the database environment and the underlying operating system
For the given use-case, you need to use Amazon RDS Custom for Oracle as it allows you to access and customize your database server host and operating system, for example by applying special patches and changing the database software settings to support third-party applications that require privileged access. Amazon RDS Custom for Oracle facilitates these functionalities with minimum infrastructure maintenance effort. You need to set up the RDS Custom for Oracle in multi-AZ configuration for high availability.

#### A finance research company needs to perform data analytics on real-time lab results provided by a partner organization. The partner stores these lab results in an Amazon RDS for MySQL instance within the partner’s own AWS account. The research company has a private VPC that does not have internet access, Direct Connect, or a VPN connection. However, the company must establish secure and private connectivity to the RDS database in the partner’s VPC. The solution must allow the research company to connect from its VPC while minimizing complexity and complying with data security requirements.

Instruct the partner to create a Network Load Balancer (NLB) in front of the Amazon RDS for MySQL instance. Use AWS PrivateLink to expose the NLB as an interface VPC endpoint in the research company’s VPC
This is the correct and most secure solution. Since the RDS instance cannot be directly exposed via PrivateLink, the partner can create a Network Load Balancer (NLB) in front of a proxy or custom endpoint that connects to RDS (e.g., using RDS Proxy or an EC2-based MySQL proxy). The partner then creates a PrivateLink service (interface endpoint service) that the research company can connect to privately via an interface VPC endpoint in its own VPC. This architecture keeps traffic within the AWS network without requiring an internet gateway, VPN, or Direct Connect.

You cannot use Transit Gateway and VPC peering together for a single pair of VPCs—this is an architectural contradiction. You either use Transit Gateway to route traffic between VPCs or use VPC peering—not both.

#### The flagship application for a gaming company connects to an Amazon Aurora database and the entire technology stack is currently deployed in the United States. Now, the company has plans to expand to Europe and Asia for its operations. It needs the games table to be accessible globally but needs the users and games_played tables to be regional only.

Use an Amazon Aurora Global Database for the games table and use Amazon Aurora for the users and games_played tables

Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases. Amazon Aurora features a distributed, fault-tolerant, self-healing storage system that auto-scales up to 128TB per database instance. Aurora is not an in-memory database.

Amazon Aurora Global Database is designed for globally distributed applications, allowing a single Amazon Aurora database to span multiple AWS regions. It replicates your data with no impact on database performance, enables fast local reads with low latency in each region, and provides disaster recovery from region-wide outages. Amazon Aurora Global Database is the correct choice for the given use-case.

For the given use-case, we, therefore, need to have two Aurora clusters, one for the global table (games table) and the other one for the local tables (users and games_played tables).

Incorrect options:

Use an Amazon Aurora Global Database for the games table and use Amazon DynamoDB tables for the users and games_played tables

Use a Amazon DynamoDB global table for the games table and use Amazon Aurora for the users and games_played tables

Use a Amazon DynamoDB global table for the games table and use Amazon DynamoDB tables for the users and games_played tables

Here, we want minimal application refactoring. Amazon DynamoDB and Amazon Aurora have a completely different APIs, due to Amazon Aurora being SQL and Amazon DynamoDB being NoSQL. So all three options are incorrect, as they have Amazon DynamoDB as one of the components.

#### A ride-sharing company wants to use an Amazon DynamoDB table for data storage. The table will not be used during the night hours whereas the read and write traffic will often be unpredictable during day hours. When traffic spikes occur they will happen very quickly. Which of the following will you recommend as the best-fit solution?

Set up Amazon DynamoDB table in the on-demand capacity mode

Amazon DynamoDB has two read/write capacity modes for processing reads and writes on your tables:

On-demand

Provisioned (default, free-tier eligible)

Amazon DynamoDB on-demand is a flexible billing option capable of serving thousands of requests per second without capacity planning. DynamoDB on-demand offers pay-per-request pricing for read and write requests so that you pay only for what you use.

The on-demand mode is a good option if any of the following are true:

You create new tables with unknown workloads.

You have unpredictable application traffic.

You prefer the ease of paying for only what you use.

If you choose provisioned mode, you specify the number of reads and writes per second that you require for your application. You can use auto-scaling to adjust your table’s provisioned capacity automatically in response to traffic changes. This helps you govern your DynamoDB use to stay at or below a defined request rate to obtain cost predictability.

Provisioned mode is a good option if any of the following are true:

You have predictable application traffic.

You run applications whose traffic is consistent or ramps gradually.

You can forecast capacity requirements to control costs.

#### A company runs a popular dating website on the AWS Cloud. As a Solutions Architect, you've designed the architecture of the website to follow a serverless pattern on the AWS Cloud using Amazon API Gateway and AWS Lambda. The backend uses an Amazon RDS PostgreSQL database. Currently, the application uses a username and password combination to connect the AWS Lambda function to the Amazon RDS database. You would like to improve the security at the authentication level by leveraging short-lived credentials. What will you choose?

- Use IAM authentication from AWS Lambda to Amazon RDS PostgreSQL
- Attach an AWS Identity and Access Management (IAM) role to AWS Lambda

You can authenticate to your database instance using AWS Identity and Access Management (IAM) database authentication. IAM database authentication works with MySQL and PostgreSQL. With this authentication method, you don't need to use a password when you connect to a database instance. Instead, you use an authentication token.

An authentication token is a unique string of characters that Amazon RDS generates on request. Authentication tokens are generated using AWS Signature Version 4. Each token has a lifetime of 15 minutes. You don't need to store user credentials in the database, because authentication is managed externally using IAM. You can also still use standard database authentication.

IAM database authentication provides the following benefits: 1. Network traffic to and from the database is encrypted using Secure Sockets Layer (SSL). 2. You can use IAM to centrally manage access to your database resources, instead of managing access individually on each DB instance. 3. For applications running on Amazon EC2, you can use profile credentials specific to your Amazon EC2 instance to access your database instead of a password, for greater security.

#### The engineering team at a retail company manages 3 Amazon EC2 instances that make read-heavy database requests to the Amazon RDS for the PostgreSQL database instance. As an AWS Certified Solutions Architect - Associate, you have been tasked to make the database instance resilient from a disaster recovery perspective. Which of the following features will help you in disaster recovery of the database?

- Use cross-Region Read Replicas:In addition to using Read Replicas to reduce the load on your source database instance, you can also use Read Replicas to implement a DR solution for your production DB environment. If the source DB instance fails, you can promote your Read Replica to a standalone source server. Read Replicas can also be created in a different Region than the source database. Using a cross-Region Read Replica can help ensure that you get back up and running if you experience a regional availability issue.

- Enable the automated backup feature of Amazon RDS in a multi-AZ deployment that creates backups across multiple Regions. 
Amazon RDS provides high availability and failover support for database instances using Multi-AZ deployments. Amazon RDS uses several different technologies to provide failover support. Multi-AZ deployments for MariaDB, MySQL, Oracle, and PostgreSQL DB instances use Amazon's failover technology.

The automated backup feature of Amazon RDS enables point-in-time recovery for your database instance. Amazon RDS will back up your database and transaction logs and store both for a user-specified retention period. If it’s a Multi-AZ configuration, backups occur on standby to reduce the I/O impact on the primary. Amazon RDS supports Cross-Region Automated Backups. Manual snapshots and Read Replicas are also supported across multiple Regions.

#### Each Read Capacity Unit provisioned in a DynamoDB table translates to?

1 RCU (≤ 4 KB):
- 1 read/sec: Strongly consistent reads
- 2 reads/sec: Eventually consistent reads
- 0.5 reads/sec: Transactional reads

1 WCU (≤ 1 KB):
- 1 write/s: Standard writes
- 0.5 writes/sec: Transactional writes

#### Backup of rds, aurora, dynamodb, redshift and open search in another region

| Service                   | Primary Cross-Region Backup Options                                                              | Real-time?              | Fully Managed? | Notes                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------- | -------------- | --------------------------------------------- |
| Amazon RDS                | - Cross-region read replica<br>- Snapshot copy<br>- Automated backup replication<br>- AWS Backup | Replica: ✅<br>Others: ❌ | Yes            | Replica for DR, snapshots for periodic backup |
| Amazon Aurora             | - Global Database<br>- Cross-region read replica<br>- Snapshot copy<br>- AWS Backup              | Global DB: ✅            | Yes            | Global DB = fastest cross-region replication  |
| Amazon DynamoDB           | - Global Tables<br>- On-demand backup + cross-region copy via AWS Backup                         | Global Tables: ✅        | Yes            | Global Tables = active-active multi-region    |
| Amazon Redshift           | - Snapshot copy to another region<br>- AWS Backup                                                | ❌                       | Yes            | No real-time replication across regions       |
| Amazon OpenSearch Service | - Manual snapshots to Amazon S3 + replicate<br>- Cross-cluster replication                       | CCR: ✅                  | Partial        | Snapshot restore required in target region    |

#### In a multi-AZ RDS Deployment, automatic failover will not happen under this condition

Automatic failover will NOT happen in this condition:
- If the primary DB is: Slow or Under heavy CPU/memory usage or Running long queries
- RDS only triggers failover when there is a failure: Primary instance crash or AZ outage or Storage failure

#### Import data to rds, aurora, dynamodb, redshift and open search

| Service                   | Common Import Methods                                                                                    | Real-time Streaming? | Best For                    | Notes                             |
| ------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------- | --------------------------- | --------------------------------- |
| Amazon RDS                | - Native DB tools (mysqldump, pg_restore)<br>- Import from Amazon S3<br>- AWS Database Migration Service | Partial              | Traditional DB migration    | Uses engine-specific tools        |
| Amazon Aurora             | - Load from S3 (native integration)<br>- DMS<br>- mysqldump / pg_restore                                 | Partial              | Fast bulk import            | Aurora is optimized for S3 import |
| Amazon DynamoDB           | - Import from S3 (CSV/JSON)<br>- BatchWriteItem API<br>- DMS                                             | Yes                  | NoSQL bulk + streaming      | Native S3 import is serverless    |
| Amazon Redshift           | - **COPY command from S3**<br>- Kinesis Firehose<br>- DMS                                                | Yes                  | Large-scale analytics loads | COPY is fastest and most common   |
| Amazon OpenSearch Service | - Bulk API<br>- Logstash / Beats<br>- Kinesis Firehose<br>- Reindex from remote                          | Yes                  | Logs, search data           | Streaming ingestion is common     |

#### transactions in rds, aurora, dynamodb, redshift and open search

| Service                   | Transaction Support                        | ACID Compliance        | Scope                  | Notes                                          |
| ------------------------- | ------------------------------------------ | ---------------------- | ---------------------- | ---------------------------------------------- |
| Amazon RDS                | ✅ Full support (BEGIN / COMMIT / ROLLBACK) | ✅ Yes                  | Multi-row, multi-table | Depends on DB engine (MySQL, PostgreSQL, etc.) |
| Amazon Aurora             | ✅ Full support                             | ✅ Yes                  | Multi-row, multi-table | High performance, distributed storage          |
| Amazon DynamoDB           | ✅ Supported (Transactional APIs)           | ✅ Yes                  | Up to 25 items / 4 MB  | Uses `TransactWriteItems`, `TransactGetItems`  |
| Amazon Redshift           | ⚠️ Limited support                         | ✅ Yes (within session) | Single session         | Not designed for OLTP; more for analytics      |
| Amazon OpenSearch Service | ❌ No traditional transactions              | ❌ No                   | N/A                    | Eventually consistent, not ACID                |

#### explain database engine migration from older version for rds, aurora, dynamodb, redshift and open search

| Service                   | Engine Version Upgrade Support | How It’s Done                                                                                                     | Downtime                | Notes                                     |
| ------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------- | ----------------------- | ----------------------------------------- |
| Amazon RDS                | ✅ Supported                    | - Modify DB → upgrade version<br>- Manual or automatic (minor versions)<br>- Snapshot + restore for major changes | ⚠️ Usually yes          | Can enable **auto minor version upgrade** |
| Amazon Aurora             | ✅ Supported                    | - In-place upgrade<br>- Blue/Green deployment<br>- Snapshot restore                                               | ⚠️ Minimal (Blue/Green) | Faster upgrades vs RDS                    |
| Amazon DynamoDB           | ❌ Not applicable               | Fully managed (no engine versions exposed)                                                                        | ❌ None                  | AWS handles everything automatically      |
| Amazon Redshift           | ✅ Supported                    | - Automatic patching<br>- Manual maintenance window<br>- Cluster restore                                          | ⚠️ Minimal              | Versioning mostly abstracted              |
| Amazon OpenSearch Service | ✅ Supported                    | - In-place upgrade<br>- Blue/Green deployment                                                                     | ⚠️ Minimal              | Blue/Green reduces downtime risk          |


#### Aurora Blue-Green deployment

- Create Green environment
  - Aurora clones your production (Blue) cluster
  - This includes: Schema, Data, Configuration
- Continuous replication
  - Changes from Blue → Green are replicated
  - Keeps Green nearly up-to-date
- Make changes safely on Green
  - Upgrade engine version
  - Modify schema, Change parameters
- Test Green
  - Run queries, validate performance, check compatibility
- Switchover
  - Switch endpoints from Blue → Green
  - Takes seconds (minimal downtime)

#### A finance research company needs to perform data analytics on real-time lab results provided by a partner organization. The partner stores these lab results in an Amazon RDS for MySQL instance within the partner’s own AWS account. The research company has a private VPC that does not have internet access, Direct Connect, or a VPN connection. However, the company must establish secure and private connectivity to the RDS database in the partner’s VPC. The solution must allow the research company to connect from its VPC while minimizing complexity and complying with data security requirements.

- Use VPC Peering between the two VPCs.
  - Amazon VPC Peering allows two VPCs (even across accounts) to communicate privately using AWS network.

If you want to share a service in your VPC—like an Application Load Balancer (ALB)—with another AWS account or VPC, the best AWS-native solution is AWS PrivateLink:
- Create a Network Load Balancer (NLB)
  - Note: ALB cannot act as a PrivateLink endpoint itself, so traffic goes through an NLB in front of ALB.
- Register your service
  - Your NLB becomes the PrivateLink service endpoint
  - Enable “accept VPC endpoint connections” for other accounts.
- Other account creates a VPC Endpoint
  - Type: Interface Endpoint → points to your service
  - Connects securely to your NLB / service
- Configure security
  - Security groups allow only traffic from the VPC endpoint
  - You control access per account
- Other account uses private DNS
  - Optional: endpoint can have a private DNS hostname pointing to your service

#### If I use DAX with Dynamodb, will is cache new writes?

- Writes go to DynamoDB first
  - Any PutItem, UpdateItem, or DeleteItem operation is always written to the underlying DynamoDB table.
- DAX updates the cache asynchronously
  - After the write succeeds in DynamoDB, DAX invalidates or updates its cached item
  - Ensures read-after-write consistency for DAX reads

DAX is read-through / write-through for caching:
- Reads → DAX returns cached data if available
- Writes → DAX does not bypass DynamoDB; it updates its cache only after the DB write
- Result: new writes are eventually reflected in the cache immediately or shortly after, depending on how DAX propagates the update.
- Consistency mode:
  - DAX provides eventually consistent reads by default
  - Strongly consistent reads through DAX are not supported

#### How does DynamoDB handle transactional writes and what are its limitations?

DynamoDB supports ACID transactions using TransactWriteItems and TransactGetItems.

Limitations 
- Maximum 25 items per transaction
- Maximum 4 MB total payload
- Supports multi-table transactions
- Cannot span multiple AWS regions — must be within the same region
- High-latency if multiple items are in different partitions (partition-level locking occurs internally)

#### Explain how Redshift handles ACID transactions and why it’s different from RDS.

Redshift supports ACID transactions, but:
- Primarily optimized for analytics (OLAP), not high-concurrency OLTP.
- Transactions operate at the session level, using snapshot isolation.
- Long-running transactions can block other queries if they hold table locks.

#### relational database running on MySQL must be migrated to AWS and must be highly available.

use RDS MySQL and Configure a Multi-AZ standby node for high availability.

- Best option: Amazon RDS for MySQL
- or Amazon Aurora MySQL

Migration Strategy:
- Minimal downtime → AWS Database Migration Service
  - Replicates data continuously from source to AWS
  - Keeps source DB running during migration
  - Cutover happens with minimal downtime
- Simple migration (longer downtime): mysqldump + restore

#### An RDS DB has high query traffic that's causing performance degradation.

that's great for a read replica, and you must configure the application to use the reader endpoint for any database queries.

#### An RDS DB is approaching its storage capacity limits and or is suffering from high write latency.

you have to scale up the DB instance to an instance type that has more storage and CPU.
So that means changing the instance type rather than adding a read replica.

Increase Storage (Fastest Fix)
- Modify DB → increase allocated storage
- Takes effect online (no downtime in most cases)

Enable Storage Autoscaling
- Automatically increases storage when nearing limit
- Prevents future outages

yes, you can change the storage type with little to no interruption: 
- In most cases: No downtime (online modification)
- RDS supports storage scaling and type changes online
- Performance impact during modification
- however, if you change instance type - you will have brief downtime (30s) - good to have Multi-AZ setup

#### RDS database is unencrypted and you need a cross-region read replica, which must be encrypted.

create an encrypted snapshot of the main DB, create a new encrypted DB instance from the encrypted snapshot and then create an encrypted cross-region read replica.

or 
Use AWS Database Migration Service:
- Create new encrypted RDS
- Use DMS to replicate data from old DB
- Cut over with minimal downtime
- Then create cross-region replica

✔️ Yes, DMS can continuously synchronize data after the initial load.
This is called Change Data Capture (CDC).

#### Amazon Aurora DB deployed and requires a cross region replica.

use the Aurora MySQL replica type in the second region.

#### Aurora DB is deployed and requires a read replica in the same region with minimal synchronization latency.

use an aurora replica rather than a MySQL replica. And it could be in a different availability zone. And that will help your paycheck.

#### Aurora is deployed and an app in another region requires read only access with low latency. Synchronization latency must also be minimized.

use the Aurora global database and configure the app in the second region to use the reader endpoint, and that will help with the latency issues.

you can replicate Aurora data to another region without using Aurora Global Database, but there are some important caveats:
- Cross-Region Aurora Replication Without Global Database
  - Use case: DR or reporting.
  - Limitation: Latency is higher (tens to hundreds of milliseconds), not suitable for real-time use.
- If you need sub-second or fast cross-region replication, Aurora Global Database is the only native solution.
  - Typical lag: less than 1 second for low-latency networks, but it is not synchronous.

#### An application in DB migrated to Aurora and requires the ability to write to the DB across multiple nodes.

use Aurora Multi-Master for an in-region multi-master database.

#### An application requires a session state data store that provides low latency.

either ElastiCache or DynamoDB.

#### A multi-threaded in-memory datastore is required for unstructured data.

use ElastiCache with Memcached and that would be needed for the multi-threaded application, you wouldn't be able to use Redis.

#### An in-memory datastore required that offers microsecond performance for unstructured data.

use DynamoDB DAX, the DynamoDB Accelerator.

#### An in-memory datastore is required that supports data persistence and high availability.

use ElastiCache and you would need to use the Redis engine.

ElastiCache Memcached is not highly available (HA) by design

ElastiCache using Terraform:
```
resource "aws_elasticache_subnet_group" "redis_subnet" {
  name       = "redis-subnet-group"
  subnet_ids = ["subnet-xxxxxx", "subnet-yyyyyy"]
}

resource "aws_elasticache_replication_group" "redis_cluster" {
  replication_group_id          = "my-redis-cluster"
  replication_group_description = "Redis replication group with Multi-AZ"
  engine                        = "redis"
  engine_version                = "7.0"
  node_type                     = "cache.t3.medium"
  number_cache_clusters         = 2
  automatic_failover_enabled    = true
  multi_az_enabled              = true
  subnet_group_name             = aws_elasticache_subnet_group.redis_subnet.name
  security_group_ids            = [aws_security_group.elasticache_sg.id]
  parameter_group_name          = "default.redis7"
}
```

#### A serverless database is required that supports a NoSQL key value store workload.

Use Amazon DynamoDB.

#### A serverless database is required that supports MySQL or PostgreSQL.

use Amazon Aurora Serverless.

#### A relational database is required for a workload with an unknown usage pattern.

usage is expected to be low and variable., that would be Aurora Serverless

#### An application requires a key value database that can be written to from multiple regions.

DynamoDB Global Tables would be a good solution.

















## Analytics <a id="Analytics"></a>

### EMR <a id="EMR"></a>
- is a managed cluster platform that runs Apache Hadoop and Apache Spark.
- Its use for processing data for analytics and business intelligence.
- you can transform and move large amounts of data.
- performs ETL functions.

### Amazon Kinesis <a id="Kinesis"></a>

Kinesis is a collection of 4 services for processing streams of various data:
- Amazon Kinesis Data Streams
- Amazon Kinesis Data Firehose
- Amazon Kinesis Data Analytics
- Amazon Kinesis Video Streams

Data is processed in “shards” – with each shard able to ingest 1000 records per second. One shard provides a capacity of 1MB/sec data input and 2MB/sec data output

A record consists of a partition key, sequence number, and data blob (up to 1 MB)

Transient data store – default retention of 24 hours but can be configured for up to 7 days

#### Kinesis Data Streams <a id="KinesisDataStreams"></a> = Kafka

Records are organized in partitions (shards).

Throughput per shard 1 MB/sec (for ingestion) and 2 MB/sec (for reading).

Increase throughput by adding additional shards

Records with same partition key are added to same shard. 
All records for a sensor are available in a single shard.
Records are ordered by arrival time.

- enables you to build custom applications that process or analyze streaming data for specialized needs.
- enables real time processing of streaming big data.
- can move data off data producers and then process that data.
- Producers send data to Kinesis and it's stored in shards for __24 hours__, and that's the default, up to seven days.
  - Applications can push data directly using the Kinesis APIs such as PutRecord or PutRecords
  - Several AWS services can send data directly or via integration to Kinesis streams (Amazon CloudWatch, Amazon EventBridge, Lambda)
- Consumers then take the data and process it, and they can save it to another service
  - Lambda
  - Kinesis Data Analytics: reads streaming data from Kinesis and runs SQL or Apache Flink applications to analyze it in real time.
  - Amazon Kinesis Data Firehose can consume data from Kinesis Data Streams and deliver it to storage or analytics systems
- allows for the later processing by applications rather than with Firehose where it delivers the data directly to an AWS service.
- Kinesis data streams is real time with around 200 milliseconds of delay.
- The Client Library helps you consume and process data from the Kinesis Stream, and each shard is processed by exactly one KCL worker and has one corresponding record processor.
- One worker can process any number of shards, so it's fine if the number of shards exceeds the number of instances.
- A __shard is the base throughput unit__ of an Amazon Kinesis data stream.
- A __stream__ is composed of one or more shards
- __stores data__ for later processing by applications (__key difference with Firehose__ which delivers data directly to AWS services)
- Producers continually push data to Kinesis Data Streams.
- Kinesis Streams __applications are consumers that run on EC2 instances__.
- Kinesis Data Streams replicates synchronously across three AZs
- AWS now supports update-shard-count API – automatically adjusts the number of shards

Use Amazon Kinesis Data Streams to ingest the data, process it using AWS Lambda or run analytics using Amazon Kinesis Data Analytics

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable __real-time data streaming service__ with support for retry mechanism. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events. The data collected is available in milliseconds to enable real-time analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing, and more.

KDS makes sure your streaming data is available to multiple real-time analytics applications, to Amazon S3, or AWS Lambda within 70 milliseconds of the data being collected. Amazon Kinesis data streams scale from megabytes to terabytes per hour and scale from thousands to millions of PUT records per second. You can dynamically adjust the throughput of your stream at any time based on the volume of your input data.

#### Kinesis Data Firehose <a id="KinesisFirehose"></a> = Kafka Connectors

- No need to worry about shards and streams
- __captures, transforms, and load streaming data__.
- __Producers send the data to a Firehose, there are no shards, it's completely automated__, so scalability is elastic unlike data streams where you have to add shards.
- __Firehose data is sent to another service for storing and data can be optionally processed and transformed using Lambda__.
- It enables near real time analytics.
- it's near real time, so around 60 seconds of latency.
- Firehose destinations include Redshift, ElasticSearch, Amazon S3, Splunk, Datadog, MongoDB, and New Relic, as well as an HTTP endpoint.
- easiest way to load streaming data into data stores and analytics tools.
- Captures, transforms, and loads streaming data. It can also batch, compress, and encrypt.
- Kinesis Data Streams can be used as the source(s) to Kinesis Data Firehose
- No shards, totally automated

#### Kinesis data analytics <a id="KinesisDataAnalytics"></a> = Kafka streams

Use it to transform and __analyze incoming streaming data__ from Kinesis Data Streams in real time. Kinesis Data Analytics takes care of everything required to run streaming applications continuously, and __scales automatically__ to match the volume and throughput of your incoming data. With Amazon Kinesis Data Analytics, there are __no servers to manage, no minimum fee or setup cost__, and you only pay for the resources your streaming applications consume.

- easiest way to process and analyze real-time, streaming data.
- you get __real time SQL processing for streaming data__.
- It provides __analytics for data coming from data streams or data firehose__.
- Destinations can be data streams, data firehose or lambda.
- you can quickly author and run powerful __SQL__ code against those streaming sources.
- It can ingest data from both streams and firehose.
- A Kinesis Data Analytics application consists of three components:
  - Input – the streaming source for your application.
  - Application code – a series of SQL statements that process input and produce output.
  - Output – one or more in-application streams to hold intermediate results.

### Amazon Athena <a id="Athena"></a>

- is used for querying data in __S3__ using SQL.
- you can __connect it to other data sources with Lambda__.
- Data can be in various formats.
- uses a managed __data catalog__, AWS Glue to store information and schemas about the databases and tables.
- How do you optimize Athena for performance:
  - __partition__ your data,
  - bucket your data, so bucket the data within a single partition.
  - Use __compression__. AWS recommend using Apache Parquet or Apache ORC.
  - Optimize __file sizes__.
  - Optimize columnar data storage generation
  - Optimize order by and optimized group by,
  - use approximate functions
  - only include the columns that you actually need.

### AWS Glue <a id="Glue"></a>

- is a fully managed __extract, transform, and load__ service used for preparing data for analytics.
- It runs the ETL jobs on a fully managed __scale-out Apache Spark__ environment.
- Glue discovers data and stores the associated metadata in the __Glue data catalog__
- it works with data lake, so data on __S3, data warehouses like Redshift, and data stores, including on RDS and EC2__.
- You can use a __crawler__ to populate the Glue data catalog with tables.
  - the crawler can crawl multiple data stores in a single run.
  - Upon completion, the crawler creates or updates one or more tables in your data catalog.
- ETL jobs that you define in Glue use the data catalog tables as sources and targets.

#### AWS Glue DataBrew

AWS Glue DataBrew is a fully managed, serverless __data preparation tool__ that enables users to __visually clean, transform, and normalize__ raw datasets—all without writing any code. It is specifically designed for data analysts, business users, and data engineers who need to prepare data for analytics or machine learning workflows using an intuitive point-and-click interface

Typical Workflow
- Import data from a source
- Explore the dataset
- Apply transformations visually
- Save the transformation steps as a recipe
- Run the recipe as a data preparation job

Recipes are executed through DataBrew jobs, not standard Glue ETL jobs.
They run on DataBrew’s own service infrastructure, not Spark.

#### AWS Glue Studio

While AWS Glue Studio does offer a __low-code visual interface for building ETL workflows__, it is still primarily intended for developers and data engineers. 
The canvas generates and __manages Apache Spark scripts__, which may require customization and still involve code for advanced logic. 
More importantly, Glue Studio does not natively provide built-in data profiling or column-level statistics, unlike AWS Glue DataBrew. 
Additionally, Glue Studio is __less suited for collaboration__ among non-technical users, and lacks the ability to share visual "recipes" with reusable, human-readable steps like DataBrew offers.
AWS Glue Studio creates Glue ETL jobs.

Both DataBrew recipes and Glue Studio scripts belong to the AWS Glue ecosystem, but they run as different types of jobs and are not executed the same way.
They still be orchestrated together. Both can be part of pipelines using:
- AWS Glue Workflows
- AWS Step Functions
- Amazon EventBridge

#### AWS Glue Workflows

AWS Glue Workflows orchestrate data pipelines built with AWS Glue components.

They coordinate:
- AWS Glue jobs
- AWS Glue Crawlers
- Glue triggers

Both AWS Glue Workflows and AWS Step Functions are used to orchestrate workflows.
- Glue Workflows → orchestration specifically for Glue ETL pipelines
- Step Functions → orchestration for any AWS service or application


### Architecture Patterns

#### Amazon Athena is being used to analyze a large volume of data based on date ranges, and the performance must be optimized.

you can store data using Apache Hive partitioning with a key based on the data. And you can use Apache Parquet and ORC storage formats.

When using Amazon Athena on large datasets, especially when filtering by date ranges, you can optimize performance (and cost) using partitioning, bucketing, and file formats:
- Partitioning by Date
  - Athena reads all data in the table by default unless partitioned.
  - For date-based queries, create partitions by date, e.g., year, month, day.
  - Partitioning splits your table into folders on disk (e.g., year=2026/month=03/day=20/).
  ```
  s3://my-bucket/logs/year=2026/month=03/day=20/data1.parquet
  ```
- Use Columnar File Formats: Convert data to Parquet or ORC
- Bucket or Cluster Data (Optional)
  - For very large partitions, bucketing on high-cardinality columns (e.g., user_id) can help
  - Bucketing splits data within each partition into multiple files based on the hash of a column (like user_id).
  - reduces data scanned within large partitions (e.g., by user_id)
- Optimize S3 Layout
  - Avoid too many small files → increases query planning overhead.
  - Too large files → slower reads.
- Use Glue Data Catalog
  - Partition metadata stored in AWS Glue Catalog allows Athena to discover partitions efficiently
- Precompute Aggregates (Optional)
  - For extremely frequent queries over date ranges:

#### Lambda is processing streaming data from API Gateway and it's generating a too many requests exception as the volume increases.

stream the data into Kinesis data stream from API Gateway and then process it in batches.

#### A Lambda function is processing streaming data that must be analyzed with SQL.

load the data into a Kinesis data stream and then analyze it with Kinesis Data Analytics to get that SQL analysis.

to run SQL queries on data in a Kinesis stream, the format of the data matters
- Each record in the stream must conform to the format consistently.

#### Security logs generated by the AWS web application firewall must be sent to a third party auditing application.

send the logs to Kinesis Data Firehose and configure the auditing application using an HTTP endpoint.

#### Real time streaming data must be stored for future analysis.

use Kinesis data streams for the real time streaming and then Firehose to load the data to a data store where you might want to analyze it later on.

#### A company runs several production databases and must run complex queries across consolidated datasets for business forecasting.

load the data from the OLTP databases into a Redshift data warehouse for OLAP.

Option A: Data Warehouse (Redshift / Redshift Spectrum)
- Centralized analytics platform
- Steps:
  - ETL/ELT: Extract data from all production DBs → transform → load into Amazon Redshift
  - Can use AWS Glue, AWS DMS, or custom pipelines
  - Partition & optimize tables for large datasets
  - Run complex SQL queries efficiently
  - Connect BI tools (e.g., QuickSight, Tableau) for forecasting dashboards

Lakehouse Approach (S3 + Athena / Redshift Spectrum / EMR)
- Store all production data in S3 (raw or processed)
- Transform into columnar formats like Parquet or ORC
- Query with:
  - Athena → serverless, pay-per-query
  - Redshift Spectrum → integrates Redshift with S3 data
  - EMR Spark / Hive → for very complex transformations

#### A Big Data analytics company wants to set up an AWS cloud architecture that throttles requests in case of sudden traffic spikes. The company is looking for AWS services that can be used for buffering or throttling to handle such traffic variations. Which of the following services can be used to support this requirement?

Amazon API Gateway, Amazon Simple Queue Service (Amazon SQS) and Amazon Kinesis

To prevent your API from being overwhelmed by too many requests, Amazon API Gateway throttles requests to your API using the token bucket algorithm, where a token counts for a request. Specifically, API Gateway sets a limit on a steady-state rate and a burst of request submissions against all APIs in your account. In the token bucket algorithm, the burst is the maximum bucket size.

Amazon Simple Queue Service (Amazon SQS) - Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. Amazon SQS offers buffer capabilities to smooth out temporary volume spikes without losing messages or increasing latency.

Amazon Kinesis - Amazon Kinesis is a fully managed, scalable service that can ingest, buffer, and process streaming data in real-time.

Amazon Simple Notification Service (SNS) cannot buffer messages

When requests come in faster than your Lambda function can scale, or when your function is at maximum concurrency, additional requests fail as the Lambda throttles those requests with error code 429 status code.

#### A big data analytics company is using Amazon Kinesis Data Streams (KDS) to process IoT data from the field devices of an agricultural sciences company. Multiple consumer applications are using the incoming data streams and the engineers have noticed a performance lag for the data delivery speed between producers and consumers of the data streams. As a solutions architect, which of the following would you recommend for improving the performance for the given use-case?

Use Enhanced Fanout feature of Amazon Kinesis Data Streams

Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. 
KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.

By default, the 2MB/second/shard output is shared between all of the applications consuming data from the stream. 
You should use enhanced fan-out if you have multiple consumers retrieving data from a stream in parallel. 
With enhanced fan-out developers can register stream consumers to use enhanced fan-out and receive their own 2MB/second pipe of read throughput per shard, and this throughput automatically scales with the number of shards in a stream.

#### what databases can aws athena connect to?

Via Athena Federated Query (JDBC connectors), Athena can query some relational databases without moving all data to S3:

| Database Type                    | How Athena Accesses It                  |
| -------------------------------- | --------------------------------------- |
| Amazon RDS MySQL / PostgreSQL    | JDBC connector (Athena Federated Query) |
| Amazon Aurora MySQL / PostgreSQL | JDBC connector (Federated)              |
| Amazon Redshift                  | Federated Query or Redshift Spectrum    |
| SQL Server                       | JDBC connector (Federated)              |
| Oracle                           | JDBC connector (Federated)              |
| Teradata / other JDBC DBs        | Federated Query                         |

Redshift spectrum - what other databases can it connect to:

#### Your company has multiple relational databases (RDS MySQL, PostgreSQL, Aurora) and wants to run complex analytical queries across all of them. How would you design the solution on AWS?

- Extract & Consolidate Data:
  - Use AWS DMS to replicate data to S3 or Redshift.
  - Use AWS Glue for ETL / transformations.
- Storage:
  - S3 Data Lake for raw and processed data.
  - Redshift for structured, frequently queried analytics.
- Query & Analytics:
  - Use Athena for ad hoc queries directly on S3.
  - Use Redshift for complex joins, aggregations, and BI dashboards.

You can also use:
- Using AWS Glue ETL
- Using Redshift COPY Command directly: Export data from RDS/Aurora to S3 (CSV, Parquet, ORC).












## Messaging <a id="Messaging"></a>

Kinesis vs SQS vs SNS

![ Kinesis vs SQS vs SNS ](./images/kinesis_sns_sqs.png)
 
SNS, SQS: Redundant copies of a message are stored across multiple AZs

|                     | SQS                        | SNS, Event Bridge              | Kinesis Data Streams
|---------------------|----------------------------|--------------------------------|-----------------------------
| Poll or Push        | Polling                    | Push notification              | Polling
| Message Processing  | Message is processed once  | broadcast to all sub. consumers| Many consumers can read ALL messages
| Retention           | Unprocessed messages can   | Immediate Delivery with retry  | Default 1 day. Extended 1 year
|                     | be kept for up to 14 days  |                                |
| Processing Time     | Visibility Timeout dictates| Consumer can take as long as   | Consumers must process
|                     | how long a consumer can    | needed (each consumer gets a   | messages by retention duration
|                     | take to process a message. | copy of a message)             |
| Strength            | Buffer messages            | Broadcast messages for         | Time ordered messages
|                     |                            | time sensitive processing      | for real-time analytics


### SQS <a id="SQS"></a>

Consumers poll the queue for any new messages.

A message is processed once and removed.

Messages are replicated in multiple AZ (handles AZ and device failures).

Multiple producers and consumers can simultaneously use the queue

Simple Queue Service (SQS)
- Highly scalable, simple to use
- Recommended for new applications on AWS

Amazon MQ
- Support for Apache ActiveMQ, RabbitMQ
- Migrate existing applications to cloud

SQS Queue Types
![ SQS Queue Types ](./images/queue_types.png)


The MessageRetentionPeriod attribute in SQS allows you to set the message retention period, which is the length of time (in seconds) that Amazon SQS retains a message.

Retention: Keep unprocessed messages for up to 14 days (default 4 days)

Encryption: At-rest encryption using server-side encryption. Use AWS managed Key or specify your customer master key. Metadata not encrypted.

Maximum message size is 256 KB

We then have a dead-letter queue. This is designed for handling message failure. It lets you set aside and isolate messages so that you can look at them later on and process them.
It's not a queue type, it's a configuration of a queue.

Long polling versus short polling:
- Long polling as a way to retrieve messages from SQS queues and it waits for messages to arrive. Long polling can lower costs. Long polling is enabled at the queue level or at the API level with the wait time seconds parameter. Long polling is in effect when the receive message wait time is a value greater than zero up to 20 seconds.
- Short polling returns immediately even if the queue is empty. So that can turn out more expensive from an API cost perspective.

messages can have attributes

you can assign triggers to trigger lambda function


Timeouts:
- __Visibility Timeout__:
  - message temp. invisible: consumer must explicitly delete the message from the queue
  - Visibility timeout used for handling failures
  - Default timeout is 30 seconds, maximum is 12 hours
  - Queue level configuration
  - Consumer can increase timeout for a specific message
- __delivery delay__: delay delivery of the message to the queue. It is invisible until this time.
  - When your consumer application needs additional time to process messages. 
  - If you create a delay queue, any messages that you send to the queue remain invisible to consumers for the duration of the delay period. The default (minimum) delay for a queue is 0 seconds. The maximum is 15 minutes.
- __receive message wait time__
  - short polling: receive message wait time = 0 and you have to poll again
  - long polling: receive message wait time > 0 (max 20 s)


#### Standard Queue

- Multiple messages and multiple consumers
- Messages are processed concurrently
- Message arrival order and processing order is different in a standard queue
- Standard queues support a very high, nearly unlimited number of API calls per second, per action (SendMessage, ReceiveMessage, or DeleteMessage). 

Standard Queue - Lifecycle of a message:
1. Consumer received the message and receipt handle
2. Queue locked the message and started a timer (__Visibility Timeout__)
3. Consumer processed the message before timeout expired
4. Consumer deleted the message by providing the receipt handle

Failure scenario:
1. Consumer received the message along with receipt handle
2. Queue locked the message and started a timer (Visibility Timeout)
3. Consumer crashed
4. Queue waited until message visibility timeout expired
5. Message not deleted
6. Queue unlocked the message and assigns to next consumer

Retention Period:
- Default: 4 days
- Configurable range: 1 minute to 14 days

#### FIFO Queue

__FIFO queue__:
- strict ordering of messages
- require the __message group ID__ and __message deduplication ID__ parameters to be added to messages.
- The message group ID: is a tag that indicates that a message belongs to a certain group.
  - In a FIFO queue, messages are **ordered **within the same Message Group ID.
  - All messages with the same group ID are delivered in the exact order they were sent.
- The deduplication ID is used for deduplication of messages within a specific interval.
- Make sure that the name of the FIFO (First-In-First-Out) queue ends with the __.fifo suffix__
- You __can't convert an existing standard queue into a FIFO queue__. To make the move, you must either create a new FIFO queue for your application or delete your existing standard queue and recreate it as a FIFO queue.
- Each partition in a FIFO queue is limited to 300 transactions per second, per API action (SendMessage, ReceiveMessage, and DeleteMessage). This limit applies specifically to non-high throughput mode.
- If you use batching, non-high throughput FIFO queues support up to 3,000 messages per second, per API action 

FIFO Queue - Lifecycle of a message:
1. Consumer receives the message and receipt handle
2. Queue locks the __message group__ and starts a timer for the message(__Visibility Timeout__)
3. Consumer processes the message before timer expires
4. Consumer deletes the message by providing the receipt handle
5. Queue unlocks the message group
6. Another consumer can now receive the message

Failure Scenario:
1. Consumer crashed
2. FIFO Queue waits for visibility timeout to expire
3. FIFO Queue unlocks the message group
4. Assigns the first message to the next consumer

Less throughput when compared to Standard queue
- 300 messages per second
- 3000 messages per second (with batching)

### SNS <a id="SNS"></a>

Broadcast a message to many consumers.

Push notification and Event Driven Architecture

- When you publish a message to a topic, SNS sends the message to every subscribed queue.
- is a highly available, durable, secure, fully managed publisher/subscriber messaging service.
- it provides topics for high throughput, push-based, many-to-many messaging.
- can fan out messages to a large number of subscriber endpoints. And those include SQS queues Lambda functions, HTTP or HTTPS webhooks, mobile push, and SMS, and also, of course, email.
- Multiple recipients can be grouped using topics. And that's essentially an access point that allows the recipients to subscribe to get the same copy of a message.
- One topic can support deliveries to __multiple endpoint__ types
- simple APIs and easy integration with applications is available with SNS.
- you get flexible message delivery over multiple transport protocols.
- Publishers and consumers __can dynamically change__
- SNS decouples publishers and consumers
- SNS has __automatic retry__ if subscriber is not online
- __Filtering__: Use filtering to deliver messages to the correct subscriber
- cannot change topic name after creation

SNS plus SQS:
- fan out is where you subscribe one or more SQS queue to an SNS topic. 
- SQS Queue to hold the message until consumer is ready to consume
- Handles scenario where consumer is down possibly for an extended period

SNS Topic Types:
- Standard Topic: Out of order and duplicate messages possible
- FIFO Topic: Preserves order of messages Message group and deduplication (similar to SQS FIFO)
- An Amazon SNS FIFO topic always delivers messages to subscribed Amazon SQS queues in the exact order in which the messages are published to the topic, and only once.

Retention Period:
- SNS does not store messages long-term by default.
- For most subscribers (Lambda, HTTP/S, email, SMS), messages that can’t be delivered immediately are retried for a short duration:
  - HTTP/S endpoints: Retry for up to 4 days (configurable with a delivery policy).
  - Other endpoints (Lambda, SQS): Delivery is immediate; if the target is unavailable:
    - For SQS endpoints, the message stays in the queue subject to SQS retention, not SNS.
    - For Lambda endpoints, messages are retried based on the Lambda retry policy.

####  SNS vs SQS

- push (SNS) vs pull (SQS)
- fanout (SNS) vs decoupling (SQS)
- no persistence (SNS) vs persistent for max 2 weeks (SQS) 
- many consumers (SNS) vs 1 consumer (SQS)

### Step Functions <a id="StepFunctions"></a>

- allows you to build distributed applications as a series of steps
- in a visual workflow, so it's an orchestration service.
- You can run state machines to execute the steps of your application,
- it's a managed workflow and orchestration platform, scalable and highly available
- you get to define your app as what's called a state machine.
- You create the tasks, sequential steps, parallel steps, branching paths, or timers.

### Event Bridge <a id="EventBridge"></a>

- This is a serverless event bus for building event-driven applications.
- Events are generated by custom applications, SAS applications, or AWS services
- an event is a signal that a systems state has changed.
- it routes events to AWS service targets and API destinations via HTTP endpoints.
- targets include Lambda, SNS, SQS, and API Gateway.
- 24 hours retry event delivery
- Recommended when you need to process events from AWS services (90+)
- Well defined JSON structure for events
- Schema registry
- Generate code to process events

### SWF = Simple Workflow <a id="SWF"></a>

- task coordination
- Base on pooling: your code pulls tasks from SWF API (they wait in queues), recives a task, sends result back to SWF API, SWF keeps history of workflow (state)
- Tasks can run from aws or on-premises
- Entities
  - Domain: isolate executions, tasks
  - Worker: application that performs a task
    - Decider: makes decision (flow-chart)
    - Activity: performs task
  - Workflow starter: application that initiates workflow
  - Workflow type
  - Task: SWF interactis with Workers by providing them unit of work = task

#### AWS Simple Workflow Service (SWF) and AWS Step Functions

| Feature               | AWS SWF (Simple Workflow)                             | AWS Step Functions
|-----------------------|-------------------------------------------------------|-----------------------
| Service Type          | Low-level workflow engine                             | High-level state machine/orchestrator
| Developer Experience  | Code-driven workflows using workers and deciders      | Declarative workflows using Amazon States Language (ASL)
| Integration           | Manual integration via code                           | Built-in integrations with 200+ AWS services via SDKs
| Workflow Definition   | Procedural code (e.g., Java, Ruby)                    | JSON/YAML-based state machine
| Execution Model       | Long-running, externally hosted deciders/workers      | Fully managed, short-to-medium duration flows
| Use Cases             | Complex, long-running, customizable workflows         | Event-driven, serverless orchestration and automation
| Retries, Error Handli | Manual (you must code retries and timeouts)           | Built-in error handling, retries, timeouts
| Visual Workflow Design| ❌ None                                               | ✅ Yes (Visual editor in console)
| Pricing               | Based on tasks and duration                           | Based on number of state transitions
| Learning Curve        | Steep (more boilerplate, custom logic)                | Easy (declarative and visual tools)



### Architectural Patterns

#### An application polls SQS Standard Queue to process pending messages. The following parameters are specified in the ReceiveMessage call to the queue: The maximum number of messages is set to 10, and the wait time is 10 seconds. There is only one message currently available in the queue. What will be the response for a ReceiveMessage call?

Response to the ReceiveMessage request contains at least one of the available messages and up to the maximum number of messages specified in the ReceiveMessage action. 
Long polling also protects you from receiving empty responses from standard queue when small number of messages are available. 
This can happen with short polling due to distribute queue implementation. 
With short polling you have to simply repeat the request to receive message.

#### An application needs to process new objects added to S3. The average time taken to process an object is 24 hours. The solution also needs to handle the fault in consumers and restart the job in a different consumer. What messaging service can you use for this requirement?

Use Kinesis Data stream to store the new object details. 
Since the average processing time is 24 hours, we cannot use an SQS queue. 
The maximum visibility timeout for a message is 12 hours; so, a message cannot take longer than 12 hours to process. 
We also need to handle consumer faults. 
So, the message needs to be available until the object is fully processed. 
While SNS can push the message to the consumer, it does not handle the scenario of a consumer crashing immediately after receiving the message.

or

AWS Step Functions supports long-running workflows up to 1 year per execution (Standard Workflows).
You can orchestrate your S3 object processing in a fault-tolerant way:
S3 Event Notification → triggers a Step Function execution with the object key.
Step Function starts a worker task (EC2/ECS/Batch).
If the worker fails, Step Functions can retry or start the task on a different worker.
Step Function tracks the state until processing completes (~24 hours).

#### An enterprise uses a SaaS application to manage the ticketing process. When a ticket is created in the SaaS application, it must trigger a workflow on your AWS account. What messaging service would you use for this requirement?

Amazon EventBridge provides native integrations with a number of SaaS platforms, giving you the ability to build rich event-driven applications without writing custom code

#### An enterprise uses an SQS queue for support tickets (Account A). An application running in a different account (Account B) needs to publish a message to the queue. How would you manage access to the queue?

For cross-account access to work, both the resource owner and application owner needs to permit the access. 
Queue owner can grant access using resource-based policy and then application owner needs to delegate the permission to the application (using IAM role policy permission). 
Another option is to create an IAM role in queue owner account and add Account B as the trusted entity. 
Account B can now delegate AssumeRole permission to the application. 
PrivateLink is used for keeping the communication inside the AWS network. It does not address the permission issue asked in this question.

```
// Account A queue policy explicitly allows Account B to send messages.
resource "aws_sqs_queue" "support_tickets" {
  provider = aws.account_a
  name     = "support-tickets-queue"
}
resource "aws_sqs_queue_policy" "cross_account_policy" {
  provider = aws.account_a
  queue_url = aws_sqs_queue.support_tickets.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowAccountBToSendMessage"
        Effect    = "Allow"
        Principal = {
          AWS = "arn:aws:iam::ACCOUNT_B_ID:root"
        }
        Action    = "sqs:SendMessage"
        Resource  = aws_sqs_queue.support_tickets.arn
      }
    ]
  })
}

// Account B role has permission to sqs:SendMessage to the SQS queue.
provider "aws" {
  alias  = "account_b"
  region = "us-east-1"
  profile = "account_b"
}
resource "aws_iam_role" "sender_role" {
  name = "sqs-sender-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "sqs_send_policy" {
  name   = "SQSAccessPolicy"
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "sqs:SendMessage"
        ]
        Resource = "arn:aws:sqs:us-east-1:ACCOUNT_A_ID:support-tickets-queue"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_send_policy" {
  role       = aws_iam_role.sender_role.name
  policy_arn = aws_iam_policy.sqs_send_policy.arn
}
```

#### An SNS Topic needs to fanout message to a Lambda function and Kinesis Firehose. However, messages are not delivered to the subscribers. How will you troubleshoot this issue?

Topic logs all delivery failures to Delivery Status Log. 
As part of shared responsibility, the customer has to enable delivery status logging for supported subscriber protocols. 
Dead Letter Queue is useful to hold undelivered messages. 
However, to determine the root cause of message delivery failure, we need to look into delivery status logs. 
CloudWatch will report metrics, but metric alone is not sufficient to pinpoint the failure root-cause.

#### An application publishes records to a Kinesis Firehose. The Firehose then delivers the messages to Elasticsearch. How will you manage access for this scenario?

Kinesis does not support resource-based policies. 
You can grant permission to the application using an identity-based policy (assigned to IAM Role, User, or Groups). 
Firehose relies on IAM Role to deliver messages to the destination.

#### A ticketing system needs to route tickets based on the priority to an appropriate queue. Which solution would you use to implement a priority queue?

SNS and EventBridge support flexible routing using filtering capability to deliver messages only to relevant subscribers.
Using priority as a filter criteria, topic will deliver the message to the correct queue.
The FIFO queue decides which message is processed by the consumer.
Even though tickets are grouped by priority, it is up to FIFO to decide which ticket is processed next.
Kinesis data stream with one shard for each priority level might work. 
However, we don't know which priority is in which shard. 
Consumer application has to poll all the shards and map them to the processing priority

#### You are using Simple Queue Service to hold messages, and the consumer application processes the messages on a best effort basis. If the consumer application is down for extended periods, what is the maximum message retention period in the Simple Queue Service (SQS) before a message is automatically removed?

The MessageRetentionPeriod attribute in SQS allows you to set the message retention period, which is the length of time (in seconds) that Amazon SQS retains a message. You can set this value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). Messages that exceed the retention period are automatically deleted by SQS.

#### A major bank is using Amazon Simple Queue Service (Amazon SQS) to migrate several core banking applications to the cloud to ensure high availability and cost efficiency while simplifying administrative complexity and overhead. The development team at the bank expects a peak rate of about 1000 messages per second to be processed via SQS. It is important that the messages are processed in order.

Use Amazon SQS FIFO (First-In-First-Out) queue in batch mode of 4 messages per operation to process the messages at the peak rate

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS offers two types of message queues - Standard queues vs FIFO queues.

For FIFO queues, the order in which messages are sent and received is strictly preserved (i.e. First-In-First-Out). On the other hand, the standard SQS queues offer best-effort ordering. This means that occasionally, messages might be delivered in an order different from which they were sent.

By default, FIFO queues support up to 300 messages per second (300 send, receive, or delete operations per second). When you batch 10 messages per operation (maximum), FIFO queues can support up to 3,000 messages per second. Therefore you need to process 4 messages per operation so that the FIFO queue can support up to 1200 messages per second, which is well within the peak rate.

#### The engineering team at an e-commerce company wants to migrate from Amazon Simple Queue Service (Amazon SQS) Standard queues to FIFO (First-In-First-Out) queues with batching

Delete the existing standard queue and recreate it as a FIFO (First-In-First-Out) queue

Make sure that the name of the FIFO (First-In-First-Out) queue ends with the .fifo suffix

Make sure that the throughput for the target FIFO (First-In-First-Out) queue does not exceed 3,000 messages per second

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. Amazon SQS eliminates the complexity and overhead associated with managing and operating message oriented middleware, and empowers developers to focus on differentiating work. Using Amazon SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.

Amazon SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent.

By default, FIFO queues support up to 3,000 messages per second with batching, or up to 300 messages per second (300 send, receive, or delete operations per second) without batching. Therefore, using batching you can meet a throughput requirement of upto 3,000 messages per second.

The name of a FIFO queue must end with the .fifo suffix. The suffix counts towards the 80-character queue name limit. To determine whether a queue is FIFO, you can check whether the queue name ends with the suffix.

If you have an existing application that uses standard queues and you want to take advantage of the ordering or exactly-once processing features of FIFO queues, you need to configure the queue and your application correctly. You can't convert an existing standard queue into a FIFO queue. To make the move, you must either create a new FIFO queue for your application or delete your existing standard queue and recreate it as a FIFO queue.

#### How do you implement exactly-once processing for messages in AWS?

1. SQS FIFO Queues
  - Support exactly-once message delivery and message ordering.
  - Use MessageDeduplicationId to prevent duplicates.
2. Idempotent Consumers
  - Even with standard queues, make your consumer idempotent by storing processed message IDs in DynamoDB.
3. Deduplication in Lambda / Worker
  - Keep a cache or database of processed message IDs to ignore repeats.











## Deployment and Management <a id="Depolyment"></a>

### CloudFormation <a id="CloudFormation"></a>

- CloudFormation deploys infrastructure using code, and that code is in JSON or YAML.
- Infrastructure is provisioned consistently with fewer mistakes or less chance of human error.
- less time and effort than configuring resources manually.
- can use version control and peer review for your CloudFormation templates, and it's free to use,
- you only pay for the resources that are provisioned.
- It can be used to manage updates and dependencies, and you can roll back and delete the entire stack as well.
- The core components:
  - templates, which are JSON or YAML text files that contain the information to build out the environment.
  - stack is then created, and that's the entire environment as described by the templates.
  - Stack sets allow you to extend the functionality of stacks across accounts and across regions.
  - Change sets show you the proposed changes to a CloudFormation stack when you upload a new template so you can see what's going to happen before it does.
- Use AWS __CloudFormation StackSets__ to deploy the same template __across AWS accounts and regions__
  - AWS CloudFormation StackSet extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation. A stack set lets you create stacks in AWS accounts across regions by using a single AWS CloudFormation template. Using an administrator account of an "AWS Organization", you define and manage an AWS CloudFormation template, and use the template as the basis for provisioning stacks into selected target accounts of an "AWS Organization" across specified regions.
      
### Elastic Beanstalk <a id="ElasticBeanstalk"></a>

- can be used to quickly deploy and manage web applications in the cloud.
- It's considered to be a platform as a service solution.
- you upload code to Elastic Beanstalk and then it deploys the environment for you, including capacity provisioning, load balancing, auto scaling, and health monitoring.
- supports various different programming languages like Java, .Net, PHP, Node.js and so on.
- There are several layers to Beanstalk:
  - Applications: they contain the environments, the environment configurations, and application versions.
    - You can have multiple application versions within an application.
    - A version is a specific reference to a section of deployable code.
    - The application version will point typically to an S3 bucket, where the code is stored.
  - Environments: are an application version that's been deployed on AWS resources.
    - The resources are configured and provisioned by Elastic Beanstalk.
    - The environment is comprised of all resources created by Beanstalk and not just an EC2 instance with your uploaded code.
- In Beanstalk, we have web servers and workers:
  - Web servers are standard applications listening for and processing HTTP requests typically, over port 80.
  - Workers are specialized applications used for long running background tasks, and they use an SQS queue.
  - Workers should be used for any long running tasks.

### SSM Parameter Store <a id="SSMParameterStore"></a>

- provides secure hierarchical storage for configuration data and secrets.
- It's highly scalable, available and durable.
- can store things like passwords, database strings and license codes as parameter values.
- It stores values as plain text, unencrypted or encrypted ciphertext.
- You can reference values by using the unique name you specified when you created the parameter.
- There's no native rotation of keys with Parameter Store.

### AWS Config <a id="AWSConfig"></a>

AWS Config provides a __detailed view of the configuration__ of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time.

AWS Config provides AWS-managed rules, which are predefined, customizable rules that AWS Config uses to evaluate whether your AWS resources comply with common best practices. You can leverage an AWS Config managed rule to check if any ACM certificates in your account are marked for expiration within the specified number of days. Certificates provided by ACM are automatically renewed. ACM does not automatically renew the certificates that you import. The rule is NON_COMPLIANT if your certificates are about to expire.

- evaluates your resource configurations for desired settings.
- gives you a snapshot of the current configurations of resources that are associated with your account.
- You can retrieve the configuration of resources that exist.
- You can also retrieve historical configurations of one or more resources,
- you can receive a notification whenever a resource is created, modified or deleted.
- You can view relationships between resources as well.
- use historical configurations (config history) to rollback or troubleshoot
- AWS Config – Managed Rule Checks
  - aws managed rules (ebs encryption by default)
  - custom rules
  - Access key rotated periodically
  - ALB HTTP to HTTPS redirection configured
  - Unused EBS Volumes, unused Elastic IP
  - Check if multi-az is configured for RDS
  - Verify is S3 bucket has bucket-level encryption enabled
  - Check if EC2 instance is managed by systems manager

### Secrets Manager <a id="SecretsManager"></a>

- This is another way that you can store secrets.
- it will rotate them for you as well without the need for deploying your own code.
- Automatic rotation is built in for Amazon RDS with MySQL, Postgres, Aurora, Amazon Redshift, and DocumentDB.
- For any other services, you have to write your own Lambda function code to perform the automation of the rotation.
- So when you're comparing Secrets Manager with Parameter Store, you get automatic rotation with Secrets Manager built in for some services or use lambda for others.

### AWS OpWorks <a id="OpWorks"></a>

- is a configuration management service providing managed instances of Chef and Puppet.
- Updates include patching, updating, backup configuration, and compliance management.

### AWS Resource Access Manager <a id="ResourceAccessManager"></a>

AWS Resource Access Manager (RAM) is a service that lets you securely share AWS resources across accounts and within your organization in AWS Organizations.

- You can share resources with RAM across AWS accounts, within organizations or Ous and IAM rules, and IAM users.
- Resource shares are created with the RAM console, the RAM APIs, the CLIs or the SDKs.
- RAM can be used to share a variety of AWS services.

Supported AWS Resources:
- VPC subnets (for centralized VPC designs)
- Transit Gateways
- License Manager configurations
- Route 53 Resolver rules
- Cloud WAN core networks
- Amazon Aurora DB cluster snapshots
- AWS CodeBuild report groups


### AWS Billing and Cost Management <a id="Billing"></a>

- estimate, plan aws cost
- receive alerts
- assess biggest investments
- simplify accounting
- Services:
  - Cost Explorer service: reports, graphs: daily spend per filter: az, region, service etc.
  - AWS Budgets: track budget and cost, notifications
  - Simple monthly calculator
  - Simple Pricing Calculator: similar to above
- Data Transfer cost
  - inbound: 0
  - outbound: yes
    - to internet: yes
    - between regions: yes
    - between AZ: cost, but if using endpoint: free
    - same AZ: free


### Architecture Patterns

#### An application must authenticate to Amazon Aurora and needs to securely store credentials. Automatic credential rotation is required on a monthly basis.

use Secrets Manager to store the credentials and update the app to retrieve credentials from secrets manager. Enable automatic rotation on a monthly basis.
you can do that with parameter store, but it's not built-in for Aurora so you'd have to build out your own Lambda function to rotate the secrets.

#### A company currently uses Chef cookbooks to manage infrastructure and it's moving to the cloud and they need to minimize migration complexity.

use AWS OpsWorks for Chef Automate. And then they can use the existing cookbooks and they'll be familiar with the technology.

#### You need a managed environment for running a simple Web application. The app processes incoming data which can take several minutes per task.

use an Elastic Beanstalk environment with a web server for the app frontend and a decoupled worker tier for the long running processes.
Web applications often pushes you towards Beanstalk, and in this case, you need a worker tier for running those long running tasks.

#### A systems integrator deploys standardized Amazon VPC configurations for many customers and needs to increase efficiency and reduce errors.

use CloudFormation to automate the process by using a standardized template.

#### A company has experienced issues rolling out updates to the CloudFormation stack and needs to preview changes before the next update.

use a change set so that you can view what's going to happen before you actually push those changes out to the actual live stack.

#### A manager wishes to monitor and enforce configuration compliance for AWS resources, including S3 buckets and security groups.

use AWS Config to create rules to monitor compliance and use auto-remediation to enforce the compliance.

#### The corporate policy requires credential rotation every 90 days. While the users were promptly changing their passwords on time, an audit of access key age showed that keys were not rotated for several months. How can you enforce this policy and take corrective action?

Use AWS Config to automatically disable keys that are older than the specified max access key age
AWS Config has a managed rule to check if active access keys are rotated within the number of days specified in the maxAccessKeyAge parameter.

Trusted Advisor can alert about access keys that are older than 90 days. The max-age parameter in Trusted Advisor is not configurable. You can automate the remediation by monitoring EventBridge and triggering an action in response to the event.

Inspector is used for host-level vulnerability assessment

Amazon Detective is an interactive tool to investigate security findings and identify the root cause of potential security issues or suspicious activities. Detective can analyze trillions of events from multiple data sources such as Amazon Virtual Private Cloud (Amazon VPC) Flow Logs, AWS CloudTrail logs, Amazon Elastic Kubernetes Service (Amazon EKS) audit logs, and Amazon GuardDuty findings, and automatically creates a unified, interactive view of your resources, users, and the interactions between them over time.

#### The database credentials for an application are stored as a secure string parameter in the Systems Manager Parameter Store. The application uses IAM role with Get Parameter permission to access the database credentials. However, during testing, the application could not connect to the database. The developer verified and confirmed that the credential stored in parameter store are valid. What could be causing the connectivity problem?

Ensure IAM role has permission to access the KMS Keys used for secure string encryption
SecureString parameter uses KMS keys for encryption. Ensure the Application IAM Role has permission to use the keys and access the parameter.

#### What is the aws services to store and manage secrets, passwords etc? Tell me what should it be used for, use case, rotation, difference between them in table format

- Secrets Manager → secrets + automatic rotation ✅
- Parameter Store → config + secrets (cheaper) ✅
- KMS → encryption only 🔐

| Service                             | What It Stores                                  | When to Use                                           | Typical Use Cases                                         | Rotation                                                 | Key Differences                                                  |
| ----------------------------------- | ----------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------- |
| AWS Secrets Manager                 | DB credentials, API keys, tokens, OAuth secrets | When you need **secure storage + automatic rotation** | RDS/Aurora credentials, third-party API keys, app secrets | ✅ **Built-in automatic rotation (via Lambda)**           | Purpose-built for secrets, native rotation, tight DB integration |
| AWS Systems Manager Parameter Store | Config values + secrets (SecureString)          | When you want **low-cost config + secrets storage**   | App configs, feature flags, simple secrets                | ⚠️ **Manual or custom rotation**                         | Cheaper than Secrets Manager, but no native rotation             |
| AWS Key Management Service          | Encryption keys (KMS keys)                      | When you need to **encrypt secrets/data**             | Encrypting secrets in other services                      | ❌ Not applicable                                         | Does NOT store secrets, only manages encryption keys             |
| AWS IAM                             | Access keys, roles, credentials                 | For **identity and access control**                   | Managing users, roles, service permissions                | ⚠️ Manual rotation (best practice: avoid long-term keys) | Not for app secrets; controls authentication/authorization       |
| AWS CloudFormation (dynamic refs)   | References to secrets (not storage)             | When deploying infrastructure securely                | Inject secrets into stacks at deploy time                 | Depends on underlying service                            | Pulls from Secrets Manager/Parameter Store                       |
| AWS Lambda (env vars)               | Small secrets/config                            | Simple or temporary secrets in serverless apps        | API keys, config values                                   | ❌ No built-in rotation                                   | Must use KMS encryption; not ideal for sensitive secrets         |
| Amazon S3 (encrypted)               | Files containing secrets                        | Rare edge cases only                                  | Backup of secrets, encrypted blobs                        | ❌ No rotation                                            | Not recommended for active secret management                     |


#### Enforce key and password expiration automatically

Detect old access keys: AWS Config rule: access-keys-rotated

Amazon Config + EventBridge + AWS Lambda
- AWS Config - create event
- EventBridge gets event and sends it to Lambda
- Trigger Lambda:
  - Disable old access key
  - Notify user (SNS/email)
  - Optionally delete key after grace period

Prevent long-lived keys (best long-term fix)
- Replace IAM user keys with: IAM Roles + STS









## Observability = Monitoring, Logging and Auditing <a id="Observability"></a>

### CloudWatch for monitoring <a id="CloudWatch"></a>

- monitor AWS resources and applications that run on aws
- you can create alarms, send notifications
- send events to EventBridge
- create custom dashboards
- alarm: watches one metric and performs one or more actions

CloudWatch Use cases and benefits:
- it collects performance metrics from AWS and on-premises systems.
- can automate responses to operational changes.
- can improve operational performance and resource optimization,
- derive actionable insights from logs.
- can get operational visibility and insights.

CloudWatch core features:
- include CloudWatch metrics, where services send time-ordered data points to CloudWatch.
- CloudWatch Alarms, where CloudWatch monitors metrics and initiates actions.
- CloudWatch Logs is a centralized collection of system and application logs.
- CloudWatch Events is a stream of system events describing changes to AWS resources and can trigger actions.

EC2 metrics:
- go every 5 minutes by default, and that's free.
- Detailed monitoring is every 1 minute and that's chargeable.
- The Unified CloudWatch Agent sends system-level metrics for EC2 as well as on-premises service.
- System-level metrics include memory and disk usage,
- You can publish custom metrics using the CLI or the API.
- Custom metrics are one of the following resolutions:
  - standard with one minute granularity
  - high resolution with granularity of one second.
- Events such as those generated by Amazon EC2 are:
  - Not stored long-term
  - Kept only briefly inside the service (roughly 24 hours) for retry/delivery purposes
  - Dropped after delivery or retry window expires
- If you want to keep them, you must send them to a storage target:
  - Amazon CloudWatch Logs – searchable event history
  - Amazon S3 – cheap long-term archive
  - AWS Lambda – process events
  - Amazon SNS – notifications

![ CloudWatch metrics ](./images/cloudwatch_metrics.jpg)

#### Unified CloudWatch Agent:
- Collect __internal system-level metrics from EC2 instances__ across operating systems,
- collect system level metrics from __on-premises servers__
- retrieve custom metrics __from your applications using the StatsD and collectD__ the protocols.
- can __collect logs__ from EC2 instances and on-premises servers running Windows and Linux.
- The agent must be installed on the server and it can be installed on EC2, on-premises servers, Linux, Windows Server, or Mac OS.

### CloudWatch Alarms <a id="CloudWatchAlarms"></a>

- 2 types of alarms:
  - the __metric alarm__ for one or more actions based on a single metric
  - the __composite alarm__, which uses a rule expression and takes into account multiple alarms.
- The alarm states are:
  - __OK__, when a metric is within a threshold,
  - __Alarm__, when the metric is outside the threshold,
  - __insufficient data__ when there's simply not enough data to make a determination.

### CloudWatch logs <a id="CloudWatchLogs"></a>

- gathers application and system logs in CloudWatch.
- can define expiration policies and KMS encryption.
- can send them to S3 by exporting Kinesis Data Streams and Kinesis Data Firehose.

![ CloudWatch logs ](./images/cloudwatch_logs.jpg)

- Log Events: Activity recorded by an application or system
- Log Streams: Sequence of log events from the same source (application instance, resource)
- Log Groups: 
  - Group of Log Streams
  - Shares the same retention, monitoring, and access control settings
- Metric Filters convert log file events to CloudWatch data points
- Specify retention period for events kept in CloudWatch logs
- Expired log events are deleted automatically
- logs are retained indefinitely by default.

### CloudTrail <a id="CloudTrail"></a>

- logs API activity for auditing.
- By default, management events are logged and all retained for up to 90 days.
- You can create a ClaudTrail trail and then your events are logged to S3 with indefinite retention.
- Trails can be logged within a region or within all regions.
- actions taken by user, role, aws service are recorded as events
- events include actions taken in aws management console, aws cli, aws sdk, aws api
- enables governance, compliance, auditing
- it records: identity of user, start time, AWS API call, source IP, request parameters, response 
- you can analyze these events using: AWS EventBridge or AWS CloudWatch Logs
- 15 min delay
- by default  AWS CloudWatch Logs are encrypted with KMS

AWS Config vs CloudTrail:
- Config reports what has changed, CloudTrail reports who and when made the change, from what location
- Config: what has changed, CloundTrail: who made a change

AWS CloudWatch vs CloudTrail:
- CloudWatch: monitor and optimise resources vs CloudTrail: action taken and who did it

### CloudWatch events <a id="CloudWatchEvents"></a>
- can be triggered based on API calls in CloudTrail.
- Events can also be streamed to CloudWatch logs.
- types of events:
  - __management events__: this is information about management operations being performed on your resources.
  - __Data events__: provide lots more detailed information about resource operations performed on actual resources.
  - __Insights events__ are there to identify and respond to unusual activity associated with writes API calls.

### X-Ray

X-Ray collects traces of requests as they move through services in Amazon Web Services.

X-Ray automatically generates and propagates a Trace ID.

A trace represents one user request, and it is composed of segments from each service involved

```
User request
   ↓
API Gateway
   ↓
Lambda
   ↓
EC2 service
   ↓
RDS query
```

In the X-Ray console you get several visualizations:
- Service Map: Shows all services and latency between them.
- Trace timeline: For a single request, you can see a timeline like

tracing a single request in AWS using logs, traces, and infrastructure metrics:
- Identify the request in X-Ray
  - Open AWS X-Ray.
  - Use the trace search feature and filter by time (14:05).
- Correlate with CloudWatch Logs
  - In Amazon CloudWatch Logs, search for the request ID or X-Amzn-Trace-Id that X-Ray generated.
  - Look at application logs, error messages, or stack traces at 14:05.
  - Outcome: You get detailed error information that traces alone don’t show.
- Check infrastructure metrics
  - In Amazon CloudWatch, review metrics for the affected services around 14:05:
    - EC2: CPU, memory, disk I/O, network
    - ELB: target response time, 5XX counts, unhealthy hosts
    - Lambda: duration, error count, throttles
  -  Outcome: Confirms whether the error was caused by infrastructure limits or application logic.
- Synthesize the findings
  - Combine all three signals:
  - Trace → tells you where the request failed
  - Logs → tell you why it failed
  - Metrics → tell you if infrastructure contributed  
- Create a CloudWatch Alarm or X-Ray Insights rule to detect similar failures automatically.


### Architecture Patterns

#### need to stream logs from Amazon EC2 instances in an auto scaling group.

install the Unified CloudWatch Agent and that will collect the log files in Amazon CloudWatch.

#### You need to collect metrics from EC2 instances with a 1 second granularity.

create a custom metric with high resolution.

#### The application logs from on-premises servers must be processed by AWS Lambda in real time.

install the Unified CloudWatch Agent on the servers and use a subscription filter in CloudWatch to connect to the Lambda function.

#### CloudWatch logs entries must be transformed with Lambda and then loaded into S3.

configure a Kinesis Firehose destination, transform with Lambda, and then load into an S3 bucket.

#### Access auditing must be enabled and records must be stored for a minimum of five years. Any attempts to modify the log files must be identified.

create a trail in AWS CloudTrail that stores the data in an S3 bucket and also enable log file integrity validation.

#### API activity must be captured from all accounts in an AWS Organization. Admins in member accounts must not be able to modify or delete the trail.

create an organization trail in AWS CloudTrail that applies to the management accounts and all member accounts, and the member accounts cannot modify that trail.

#### A company requires API events that involve the root user account to generate a notification.

create a CloudTrail trail and an EventBridge rule that looks for API events that involve root and configure an SNS notification.

#### For compliance reasons, all S3 buckets must have encryption enabled and any non-compliant buckets must be auto remediated.

use AWS Config to check the encryption status of the buckets and use auto remediation to enable encryption as required.

#### You would like to monitor two different metrics in an AWS Service and take automated action based on the metric value.  How many CloudWatch alarms would you need?

Two. Alarm is associated with one metric. So, we need one alarm per metric.

#### How do you reset the alarm in the "in-alarm" state?

The alarm will reset when the underlying issue that triggered the alarm is resolved. 

For example, if there are is alarm based on CPU utilization, in-response to the alarm, an application may add EC2 instances to handle the workload. When CPU utilization reduces, the alarm will automatically go back to "OK" state

Alarm: Increase the alarm evaluation interval to detect persistent problems and to ignore the temporary issues. 
The application is handling transient spikes without requiring additional EC2 instances. 
To capture the persistent issues, increase the alarm evaluation interval so that the alarm is triggered only when the data point is outside the threshold for consecutive periods. 
If you lower the limit or the evaluation interval, the alarm will trigger more often. Another possible solution is to increase the threshold for triggering the alarm.
Alarms can stop the instance - but they cannot start an instance.

#### An organization uses Bastion Host (an EC2 instance) for the developers to connect to other AWS resources. You would like to maximize the availability of Bastion Host and automatically recover from issues related to Physical Host. What mechanism can you use to accomplish this?

With System Status Check Alarm, you can configure the instance to recover from underlying AWS issues automatically. Recover option is only available with System Status Check alarms.

#### I want to track all user and API activities in my account. What service should I use for this?

CloudTrail captures all user activity and API usage. When you enable a trail, CloudTrail publishes CloudWatch Events that you can use to enable automation workflow based on specific events. Guard Duty reports only suspicious events. VPC Flow log captures network traffic flow in your VPC. Macie is used for protecting sensitive data in S3

#### You have a pool of EC2 instances to manage application requests. Application has a metric that tracks pending requests and you would like to configure Autoscaling to add or remove instances based on this application metric. How can you accomplish this?

CloudWatch supports custom metrics and application can take advantage of this capability to push relevant metrics to CloudWatch. Once it is available in CloudWatch, you can use rest of the capabilities provided by CloudWatch to monitor based on that metric

#### Your application is generating several false alarms. The alarm is currently based on the CPU utilization metric. Upon investigation, you found that the false alarms can be reduced if you consider the pending items in the SQS Queue. How would you ensure the alarm goes into ALARM state only when both the CPU utilization and SQS Queue length metrics breach the threshold?

With CloudWatch, you can create two types of alarms: metric and composite. 

A metric alarm watches a single metric, and when the metric breaches the threshold, the alarm changes to an "ALARM" state. 

A composite alarm is a new capability that considers the state of multiple alarms. The outcome of a composite alarm depends on the rule expression you define. For example, let's say you have a metric alarm to monitor CPU utilization and another to monitor SQS Queue Length. 

You can create a composite alarm when you need to perform a certain action only when both CPU and SQS Queue Length alarms are in the ALARM state. Rule expression allows you to combine these underlying metric alarms or other composite alarms and create a new Alarm based on the state of these existing alarms.

#### You application runs in two different regions and you would like aggregate instance utilization metrics across regions. What is the mechanism that can be used for aggregating CloudWatch data across regions?

Use a script to pull data from different regions, and push it to CloudWatch Logs for analysis
You can perform aggregation only with a region.

#### While consolidating logs for the weekly reporting, a development team at an e-commerce company noticed that an unusually large number of illegal AWS application programming interface (API) queries were made sometime during the week. Due to the off-season, there was no visible impact on the systems. However, this event led the management team to seek an automated solution that can trigger near-real-time warnings in case such an event recurs. Which of the following represents the best solution for the given scenario?

Create an Amazon CloudWatch metric filter that processes AWS CloudTrail logs having API call details and looks at any errors by factoring in all the error codes that need to be tracked. Create an alarm based on this metric's rate to send an Amazon SNS notification to the required team

AWS CloudTrail log data can be ingested into Amazon CloudWatch to monitor and identify your AWS account activity against security threats, and create a governance framework for security best practices. You can analyze log trail event data in CloudWatch using features such as Logs Insight, Contributor Insights, Metric filters, and CloudWatch Alarms.

AWS CloudTrail integrates with the Amazon CloudWatch service to publish the API calls being made to resources or services in the AWS account. The published event has invaluable information that can be used for compliance, auditing, and governance of your AWS accounts. Below we introduce several features available in CloudWatch to monitor API activity, analyze the logs at scale, and take action when malicious activity is discovered, without provisioning your infrastructure.

For the AWS Cloudtrail logs available in Amazon CloudWatch Logs, you can begin searching and filtering the log data by creating one or more metric filters. Use these metric filters to turn log data into numerical CloudWatch metrics that you can graph or set a CloudWatch Alarm on.

Note: AWS CloudTrail Insights helps AWS users identify and respond to unusual activity associated with write API calls by continuously analyzing CloudTrail management events.

Insights events are logged when AWS CloudTrail detects unusual write management API activity in your account. If you have AWS CloudTrail Insights enabled and CloudTrail detects unusual activity, Insights events are delivered to the destination Amazon S3 bucket for your trail. You can also see the type of insight and the incident time when you view Insights events on the CloudTrail console. Unlike other types of events captured in a CloudTrail trail, Insights events are logged only when CloudTrail detects changes in your account's API usage that differ significantly from the account's typical usage patterns.

#### need to stream logs from Amazon EC2 instances in an auto scaling group.

```
[Auto Scaling EC2] --CloudWatch Agent--> [CloudWatch Logs Group]
                          \
                           --> [Kinesis Firehose] --> S3 / OpenSearch / Redshift
```

Default EC2 metrics (CPU, network, disk) are already collected by the EC2 infrastructure and visible in CloudWatch — these are basic EC2 metrics like CPUUtilization, NetworkIn, DiskReadOps

Unified agent for:
- Additional OS-level metrics: memory, disk usage, swap, TCP connections
- Application logs streaming to CloudWatch Logs
- Custom metrics via scripts or JSON config

| Metric Type          | Granularity                | Notes                                                    |
| -------------------- | -------------------------- | -------------------------------------------------------- |
| Basic EC2 metrics    | 5 minutes                  | Free, default, CPU, disk, network                        |
| Detailed monitoring  | 1 minute                   | Paid option, enables **1-minute metrics** via CloudWatch |
| **1-second metrics** | ❌ Not available by default | Need **custom metrics** or high-resolution metrics       |

#### CloudWatch logs entries must be transformed with Lambda and then loaded into S3

- Step 1: Create CloudWatch Logs Group
- Step 2: Create Lambda Function
  - Decode CloudWatch Logs data (it is gzip + base64 in the subscription event)
  - Transform/parse the log
  - Write result to S3
- Step 3: Create Subscription Filter (send logs to lambda or Kinessis firehose)
  ```
  aws logs put-subscription-filter \
      --log-group-name MyAppLogs \
      --filter-name LambdaTransform \
      --filter-pattern "" \
      --destination-arn arn:aws:lambda:us-east-1:123456789012:function:TransformLogsLambda
  ```
- Step 4: IAM Permissions: Lambda execution role must have
  ```
  {
    "Effect": "Allow",
    "Action": [
      "s3:PutObject",
      "logs:DescribeLogGroups"
    ],
    "Resource": "*"
  }
  ```

#### Access auditing must be enabled and records must be stored for a minimum of five years. Any attempts to modify the log files must be identified.

```
[AWS Services / User Actions]
        │
        ▼
[CloudTrail / CloudWatch Logs] 
        │
        ▼
[Log Delivery to S3 Bucket with Object Lock / Versioning]
        │
        ▼
[Glacier Deep Archive / Long-Term Storage]
        │
        ▼
[Monitoring / Alerting]
        ├─ AWS Config (detect changes)
        └─ CloudWatch / EventBridge Alarms for unauthorized modifications
```

- Enable CloudTrail
  - CloudTrail records all API activity, including PutObject, DeleteObject, ModifyBucketPolicy, etc.
  - Create a multi-region trail and send logs to an S3 bucket.
- Configure S3 Bucket for Immutable Storage
  - Enable Object Lock (WORM) to prevent modifications:
    - Must enable Object Lock at bucket creation
    - Set Retention Mode: Compliance (prevents deletions even by root)
- Enable Monitoring of Log Integrity
  - CloudTrail Integrity Validation: CloudTrail supports log file validation, which ensures logs are not tampered with
  - S3 Event Notifications
    - Detect failed or unauthorized modification attempts
    - Use EventBridge / CloudWatch to trigger alerts
- Optional: AWS Config rules
  - s3-bucket-versioning-enabled
  - s3-bucket-object-lock-enabled
- Optional Long-Term Storage: For cost optimization, move logs to: S3 Glacier Deep Archive for long-term retention

S3 Object Lock requires versioning to be enabled. You cannot use Object Lock without versioning.

#### API activity must be captured from all accounts in an AWS Organization. Admins in member accounts must not be able to modify or delete the trail.

Create S3 bucket with Object Lock:
```
resource "aws_s3_bucket" "trail_bucket" {
  bucket = "org-audit-logs-bucket"
  acl    = "log-delivery-write"

  force_destroy = false

  versioning {
    enabled = true
  }

  object_lock_configuration {
    object_lock_enabled = "Enabled"
    rule {
      default_retention {
        mode  = "COMPLIANCE"
        days  = 1825   # 5 years
      }
    }
  }

  lifecycle_rule {
    id      = "glacier-archive"
    enabled = true
    transition {
      days          = 30
      storage_class = "GLACIER_DEEP_ARCHIVE"
    }
  }
}
```

Apply S3 bucket policy to block member account admins:
```
resource "aws_s3_bucket_policy" "trail_bucket_policy" {
  bucket = aws_s3_bucket.trail_bucket.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "DenyDeleteForNonLoggingAccount"
        Effect    = "Deny"
        Principal = "*"
        Action    = [
          "s3:DeleteObject",
          "s3:PutObjectAcl",
          "s3:DeleteObjectVersion"
        ]
        Resource = "${aws_s3_bucket.trail_bucket.arn}/*"
        Condition = {
          StringNotEquals = {
            "aws:PrincipalAccount" = "123456789012"  # Central logging account
          }
        }
      }
    ]
  })
}
```

Create Organization CloudTrail
```
resource "aws_cloudtrail" "org_trail" {
  name                          = "org-audit-trail"
  s3_bucket_name                = aws_s3_bucket.trail_bucket.id
  is_multi_region_trail         = true
  include_global_service_events = true
  is_organization_trail         = true				// captures API activity from all accounts in the org
  enable_logging                = true

  event_selector {
    read_write_type           = "All"
    include_management_events = true
    data_resource {
      type = "AWS::S3::Object"
      values = ["arn:aws:s3:::"] # optional: capture S3 object-level API
    }
  }
}
```

#### A company requires API events that involve the root user account to generate a notification.

- CloudTrail logs all API activity in the account.
- CloudTrail can deliver logs to CloudWatch Logs.
- EventBridge rule filters events where the userIdentity.type = Root.
  ```
  {
    "source": ["aws.cloudtrail"],
    "detail-type": ["AWS API Call via CloudTrail"],
    "detail": {
      "userIdentity": {
        "type": ["Root"]
      }
    }
  }
  ```
- EventBridge triggers a notification (SNS email, SMS, or Lambda).

CloudTrail only records events; it doesn’t push alerts.

#### For compliance reasons, all S3 buckets must have encryption enabled and any non-compliant buckets must be auto remediated

- Enable AWS Config Rule: s3-bucket-server-side-encryption-enabled
- AWS Config → Auto Remediation → Lambda
- Configure Auto Remediation: Lambda Remediation
- Optional: Prevent Non-Compliant Buckets (Proactive Control): AWS Organizations + SCP (Service Control Policies)

#### To aggregate CloudWatch metrics across regions, the correct mechanism is:

Use CloudWatch Cross-Region Dashboards:
- CloudWatch dashboards are global (region-independent)
- You can add widgets that pull metrics from:
  - Multiple regions
  - Multiple accounts (if enabled)
- Dashboard queries multiple regions and displays them together

If You Need True Aggregation (single metric):
- Use Lambda or agent to push metrics into central region using PutMetricData
  - to Republish metrics to a central region (real aggregation):
    - Read metrics from Region A
    - Push them as custom metrics into Region B using PutMetricData
    - Region A metrics → Lambda → PutMetricData → Region B
- Use CloudWatch metric math in dashboard: Sum or average metrics from different regions

#### You need to monitor application latency across microservices. How do you design observability

- Use distributed tracing with AWS X-Ray
- Instrument all services (Lambda, ECS, EC2 apps)
- Capture:
  - Request flow
  - Latency per service
    - each lambda will create a log entry: latency = ... // use Embedded Metric Format (EMF) to Automatically converts logs → metrics
  - Downstream calls
- CloudWatch automatically aggregates based on: Namespace, Metric name, Dimensions
- Combine with:
  - Amazon CloudWatch metrics (latency percentiles p95/p99)
  - Structured logs for debugging

#### How do you monitor logs for specific patterns and trigger alerts?

Logs → Metric Filter → CloudWatch Metric → Alarm → SNS

#### You need near real-time log analytics at scale. What architecture?

CloudWatch Logs → Amazon Kinesis Data Firehose → Amazon OpenSearch Service

#### How do you debug intermittent failures in production?

- When did it happen? (time correlation) = Metrics
   - Error rate spikes
 - Latency spikes (p95/p99)
 - Throttles / saturation
- What failed? (error signals) = Logs
- Where did it fail? (service/component) = Trace
- Why did it fail? (root cause) = Identify pattern (load, randon, region, data)
- Reproduce

I start by analyzing CloudWatch metrics to identify when the intermittent failure occurs, focusing on error rates and latency percentiles. Then I correlate logs in CloudWatch Logs using timestamps and request or correlation IDs to find specific errors. Next, I use AWS X-Ray to trace the request path and identify which service or dependency is causing the failure. Finally, I look for patterns such as load-related issues, throttling, or dependency failures, and validate by reproducing the issue if possible.














## Security in the Cloud <a id="Security"></a>

| Service                                   | Use Case
|-------------------------------------------|-------------------------------------------
| AWS Identity and Access Management (IAM)  | Securely manage access to services and resources
| IAM Access Analyzer                       | Identify resources (such as S3 bucket, IAM Roles, KMS
|                                           | Keys, Lambda functions, SQS Queue) that are shared with 
|                                           | external accounts outside of your organization
| AWS Single Sign-On (SSO)                  | Cloud Single-sign-on Service
| Amazon Cognito                            | Identity management for your apps
| AWS Directory Service                     | Managed Active Directory
| AWS Resource Access Manager (RAM)         | Share AWS resources securely between accounts
| AWS Organizations                         | Central governance and management across AWS accounts


### Active Directory <a id="AD"></a>

#### Managed Microsoft AD

- This is a __fully managed AWS service__.
- It's the best choice if you have __more than 500 users__ and or you need a trust relationship set up,
- you can perform schema extensions.
- You can __set up trust relationships with on-premises active directories__:
  - on premise users and groups can access resources in either domain using SSO
  - once you have that trust relationship, it does require a VPN or DX connection.
- Managed Microsoft AD can be used as a stand-alone active directory in the AWS cloud
- AWS Managed Microsoft AD is your best choice __if you have more than 5,000 users and need a trust relationship__ set up between an AWS hosted directory and your on-premises directories. 
- AWS Directory Service for Microsoft Active Directory (aka AWS Managed Microsoft AD) is powered by an actual Microsoft Windows Server Active Directory (AD), managed by AWS. With AWS Managed Microsoft AD, you can run directory-aware workloads in the AWS Cloud such as SQL Server-based applications. You can also configure a trust relationship between AWS Managed Microsoft AD in the AWS Cloud and your existing on-premises Microsoft Active Directory, providing users and groups with access to resources in either domain, using single sign-on (SSO).

#### AD Connector

- __redirects directory requests to your on premises AD__.
- best choice when you want to use an __existing active directory__ with AWS services
- AD connector comes in two sizes:
  - small for organization up to 500 users and
  - large for up to 5000 users.
- __requires a VPN or DX connection__.
- You can join EC2 instances to your on premises a through a connector
- You can login into the management console using your on premises active directory, domain controllers for authentication.
- __Use AD Connector if you only need to allow your on-premises users to log in to AWS applications and services with their Active Directory credentials__. 

#### Simple AD

- is an __inexpensive AD compatible service with common directory features__.
- standalone fully managed directory on the AWS cloud.
- the least expensive option.
- best choice for __less than 500 users__ if you don't need those advanced AD features.
- Features include:
  - managing user accounts and groups,
  - applying group policies
  - Kerberos based SSO
  - supports joining Linux or Windows-baseded EC2 instances
- Simple AD provides a subset of the features offered by AWS Managed Microsoft AD. Simple AD is a standalone managed directory that is powered by a Samba 4 Active Directory Compatible Server. __Simple AD does not support features such as trust relationships with other domains. Use it if you have 5,000 or fewer users__

### Identity providers <a id="IdentityProviders"></a>

Identity providers and federation :
- IDP you can manage user identities outside of AWS and give these identities permissions to use resources in your account.
- For example:
  - your organization already has its own identity system such as a corporate user directory.
  - You're __creating a mobile app or web application that requires access to AWS resources__
- with an IAM identity provider there's no need to create custom signing code or manage your own identities. The IDP will do that for you.
- __External users sign in for a well known IDP such as login with Facebook, Amazon or Google__,
- IAM supports IDPs that are compatible with openID Connect or SAML 2.0.

__IAM Identity center__ = SSO for aws = Okta = Microsift Entra ID
- centrally manage access to multiple AWS accounts and business applications
- easily manage SSO access and user permissions to all your accounts in organizations centrally,
- IAM Identity Center also includes built in integrations to many business applications like Salesforce, Box and office 365.
- You can create and manage user identities in IAM Identity Center
- you can connect to existing identity stores such as Ad or Azure
- connect multiple AWS Account to Identity center and create IAM user in Identity center
- supports connectivity with AD and SAML 2.0
- Workforce Identity - any user who can access multiple AWS accounts. It can be:
  - IAM Identity center
  - AD
  - Saml 2.0
- AWS IAM Identity Center supports __one identity source at a time__
- You can use AWS IAM Identity Center and also have IAM users in your AWS accounts at the same time. They are independent identity management systems and can coexist.
- you can use AWS IAM Identity Center without AWS Organizations, but with limited functionality
  - Multi-account access management is not available.
  - You cannot assign users to other AWS accounts
- AWS Cloud Trail - logs everything

### KMS <a id="KMS"></a> = Key Management Service

- enables you to create and manage cryptographic keys.
- You can control your key usage across services and in applications.
- It allows you to centrally manage and securely store your
- KMS keys and it supports symmetric and asymmetric encryption.
- KMS keys are the primary resources in KMS.
- AWS Managed: fixed rotation 3 years, you cannot delete it
- Customer Managed: rotation period: >1 year
- can encrypt/decrypt up to 4KB
- can be used to encrypt data keys
- key is assigned to a region
- __You can share the AWS Key Management Service__ (AWS KMS) key that was used to encrypt the snapshot with any accounts that you want to be able to access the snapshot. You can share AWS KMS Key with another AWS account by adding the other account to the AWS KMS key policy.

KMS keys:
- contain the key material used to encrypt and decrypt data.
- KMS keys are created in AWS KMS
- symmetric KMS keys and the private keys of asymmetric KMS keys will never leave AWS KMS unencrypted
- by default KMS creates the key material for KMS key.
- You can also import your own key material
- KMS keys can only encrypt data up to four 4KB in size.
- KMS keys can generate encrypt and decrypt data encryption keys,
- data encryption keys can then be used for encrypting large quantities of data.

AWS managed KMS keys:
- are created managed and used on your behalf by a service that is integrated with KMS.
- You can't manage these keys, you can't rotate them or change their key policies.
- You also cannot use AWS managed KMS keys, encrypt graphic operations directly.
- The service uses them on your behalf,
- KMS - AWS Managed Keys are automatically rotated Every year

Data Encryption Keys:
- data keys are encryption keys that you can use to encrypt data, including large amounts of data and other data encryption keys.
- You can use KMS keys to generate encrypt and decrypt your data keys.
- KMS doesn't store manage or track your data keys or perform the operations with those data keys
- you must use and manage the data keys outside of KMS.

![ Kms keys ](./images/kms_keys.png)

KMS key types and how are they rotataed:
- __KMS – AWS Managed Keys__ are rotated: __automatically 1/year__
- __KMS - Customer Managed Keys__ with KMS key-material origin are rotated: __automatically every year if you enable rotation__
- __KMS – External Key Origin keys__ are rotated: __Never__. Automatic key rotation is not supported when you use External Key Origin
- __KMS – Custom key stores (CloudHSM)__ keys are rotated: __Never__. Automatic key rotation is not supported when you use CloudHSM

Data Keys:
- can be either symmetric or asymmetric depending on your encryption requirements.
- Encryption/Decryption: You use data keys to encrypt/decrypt data locally, and the KMS service can wrap these keys in a master key (CMK) for storage.
- Steps to Use KMS for Data Key Management:
  - Create a Key (CMK): You start by creating a customer-managed key (CMK) in KMS.
  - Generate Data Keys
  - Encrypt Data
  - Encrypt Data Key:
    - Use Encrypt in KMS to wrap the data key with the master key (CMK).
    - Store the encrypted data key alongside the encrypted data.
      - If you're storing encrypted data in DynamoDB, you would likely need to store the encrypted data key as an additional attribute of the item (typically a "data_key" attribute).
  ```
  import boto3

  # Initialize KMS client
  kms = boto3.client('kms')

  # Generate a data key
  response = kms.generate_data_key(
      KeyId='arn:aws:kms:region:account-id:key/key-id',  # Your CMK ARN
      KeySpec='AES_256'
  )

  data_key = response['Plaintext']  # The plaintext data key
  encrypted_data_key = response['CiphertextBlob']  # The encrypted data key

  # Use the data key to encrypt your data
  encrypted_data = encrypt_data(data_key, data_to_encrypt)

  # Store encrypted data and encrypted data key
  ```

#### difference between aws ssm parameter store and kms and secrets manager

| Service                     | Primary Purpose                                                        |
| --------------------------- | ---------------------------------------------------------------------- |
| **AWS SSM Parameter Store** | __Store configuration data__ and secrets (e.g., strings, passwords)    |
| **AWS Secrets Manager**     | Securely store, rotate, and manage **secrets** like __DB credentials__ |
| **AWS KMS**                 | Create and manage **encryption keys** used to encrypt/decrypt data     |
  

| Feature                       | **SSM Parameter Store**                   | **Secrets Manager**                         | **AWS KMS**                              |
| ----------------------------- | ----------------------------------------- | ------------------------------------------- | ---------------------------------------- |
| **Stores Secrets?**           | ✅ Yes (`SecureString` type)               | ✅ Yes (designed for secrets)                | ❌ No (stores encryption keys, not data)  |
| **Encryption Support**        | ✅ Yes (via **KMS**)                       | ✅ Yes (automatic, uses **KMS**)             | ✅ Yes (core purpose is encryption)       |
| **Automatic Secret Rotation** | ❌ No (manual only)                        | ✅ Yes (built-in, with Lambda)               | ❌ Not applicable                         |
| **Versioning**                | ✅ Yes (basic)                             | ✅ Yes (with detailed tracking)              | ✅ Key versions & rotation supported      |
| **Access Control**            | IAM policies                              | IAM + fine-grained secret policies          | IAM + key policies + grants              |
| **Cost**                      | ✅ Free (standard), small fee for advanced | ❌ Paid (\~\$0.40 per secret per month)      | ❌ Paid per CMK and usage                 |
| **API/SDK Support**           | ✅ Yes                                     | ✅ Yes                                       | ✅ Yes                                    |
| **Secret Rotation Use Case**  | Manual rotation via Lambda or automation  | Automatic rotation supported out-of-the-box | Not used for secret rotation             |
| **Intended for**              | App config, env vars, small secrets       | DB credentials, API keys, tokens            | Encrypting S3, EBS, RDS, Parameter Store |


### Cloud HSM <a id="HSM"></a>

- cloud based hardware security module
- You can generate and use your own encryption keys on the AWS cloud.
- runs in your VPC
- uses FIPS 140-2 level three validated HSMs.
- It's a managed service and automatically scales
- You retain control over your encryption keys and you control access with no visibility for AWS.
- Use cases:
  - offload SSL/TLS processing from web servers,
  - protect private keys from issuing CA,
  - store the master key for oracle DB transparent data encryption
  - custom key store for KMS, so you can retain control of the HSM that protects the master keys.

### Certificate Manager <a id="CertificateManager"></a>

- create, store and renew SSL/TLS X 509 certificates that supports single domains, multiple domain names and wild cards
- integrates with several services like elbs, cloudfront, Elastic beanstalk, Nitro enclaves and AWS cloud formation.
- Public certificates are signed by the AWS public CA.
- You can also create a private CA with ACM, then you can issue private certificates.
- You can also import certificates from third party issuers as well.
- used by: LB, CloudFront, API Gateway, Beanstalk
- need to provide domain name
- validate: create provided DNS record
- configure HTTPS ALB and provide certificate from CM
- create record in DNS (Route 53)

### Web Application Firewall - WAF <a id="WAF"></a>

- This service lets you create rules to filter web traffic based on conditions such as __IP addresses, http headers and body or custom URIs__.
- It makes it easy to create rules that block common web exploits like __sequel injection__ and cross site scripting.
- Web Application Firewall allows you to enforce country-specific rules. You can block or allow traffic from specific countries.
- Monitor requests to __Application Load Balancer, CloudFront, API Gateway__ (and more)
- Secure at the edge (with CloudFront, CloudFront query parameter whitelist)
- Only in fort of (protects): ALB, CloudFront, API Gateway, AppSync API
- __block: IP (need to create IP Sets), Country, String in request__
- actions: block all, count, allow all 
- 1 rule = 1 capacity unit. Max 1500
- many managed rules - you pay for them.
- Concepts:
  - __web ACLS__, are used to protect a set of resources
  - __rules__: that define the inspection criteria and actions to take if a web request meets your defined criteria
  - __rule groups__:  reusable rule groups.
  - __IP set__ provides a collection of IP addresses and IP address ranges that you want to use together in a rule statement.
  - __regeX pattern set__ provides a collection of regular expressions you want to use together in a rule statement.
  - __rule action__ tells WAS what to do with a web request. When it matches the criteria defined in the rule:
    - count,
    - allow
    - block the request.
  - A match statement compares the web request or its origin against conditions that you provide:
    - geographic,
    - IP sets
    - regex size constraints,
    - sequel injection attacks,
    - string, match and
    - cross site scripting attacks.
- Monitor requests to Application Load Balancer, CloudFront, API Gateway (and more)
- Secure at the edge (with CloudFront, CloudFront query parameter whitelist)

Web Application Firewall allows for access limitation by IP address. 
It's important to highlight that __WAF integration is exclusive__ to:
- Application Load Balancer, 
- CloudFront distribution, and 
- API Gateway. 
- You cannot use CIDRs

These are various different ways of identifying traffic that could be malicious in nature:

![ Malicious attack ](./images/malicious_assack.png)

#### WAF – Managed Rule Groups

__Preconfigured set of rules__ managed by AWS and Marketplace Sellers:
- OWASP Top 10
- Common Vulnerabilities and Exposure (CVE)
- AWS IP Reputation List – Block addresses associated with bots and other threats
- AWS IP Anonymous List – Block requests from services that obfuscate caller identity (VPN, Proxies, Tor nodes)


### AWS shield <a id="Shield"></a>

- Protection against __Layer 3 and 4 attacks__
- managed distributed denial of service (__DDOS__) protection service.
- It safeguards web applications running on AWS with always on detection and automatic in line mitigations.
- It helps to minimize application downtime and latency.
- Protection against regional and global resources
- Includes WAF
- 2 tiers:
  - the standard which is no cost at all
  - advance which comes for a monthly fee and a one year commitment.

![ Secure Architecture ](./images/secure_architecture.png)

### Amazon Cognito <a id="Cognito"></a>

AWS Cognito works with external identity providers that support __SAML__ or __OpenID Connect__, social identity providers (such as Facebook, Twitter, Amazon)

Federation allows __users to authenticate with a Web Identity Provider__ (e.g. Google, Facebook, Amazon).

The user authenticates first with the Web ID provider and receives an authentication token, which is then exchanges for temporary AWS credentials allowing them to assume an IAM role allowing access to the required resources.

Cognito is an Identity Broker which handles interaction between your applications and the Web ID provider

- add user sign-up and sign-in and access control to your web and mobile apps.
- A __user pool__ is a directory for managing sign-in and sign-up
- users can be stored in a user pool or can sign in using social IDPs.
- It supports __SAML__ and __OIDC__ compatible IDPs.
- Cognito acts as an identity broker between the IDP and AWS.
- __Identity pools__ are used to obtain temporary limited privilege credentials for AWS services using the STS service.
- IAM role is assumed providing access to those services.

User pools:
- Cognito User Pools are user directories used to manage sign-up and sign-in functionality for mobile and web applications.
- With a user pool, users can sign in to your web or mobile app through Amazon Cognito
- Users can also sign in through social identity providers like Facebook or Amazon, and through SAML identity providers.

Identity Pools:
- With an identity, you can obtain temporary, limited-privilege AWS credentials to access other AWS services.
- Cognito tracks the association between user identity and the various different devices they sign-in from
- In order to provide a seamless user experience for your application, Cognito uses Push Synchronization to push updates and synchronize user data across multiple devices

### Amazon Inspector <a id="Inspector"></a>
- automated security assessment service for ec2 instances
- assesses applications for exposure, vulnerabilities
- creates a list of security findings and severity
- performance network 
- host assessment: requires agent
- free, can be scheduled

### Trusted Advisor <a id="TrustedAdvisor"></a>

AWS Trusted Advisor is an online tool that provides you __real-time guidance to help you provision your resources following AWS best practices__. Whether establishing new workflows, developing applications, or as part of ongoing improvement, take advantage of the recommendations provided by AWS Trusted Advisor regularly to help keep your solutions provisioned optimally. AWS Trusted Advisor just provides recommendations rather than creating reusable infrastructure templates.

- inspects AWS environment and makes recommendations: save money, HA, performance, security
- agent-less
- broader scope: aws account (not only ec2)
- real-time, no schedule

### STS = security token service <a id="STS"></a>

- temporary security credentials: max few hours
- provided dynamically when requested
- identity federation, supports SAML2
- web identity federation: Open ID Connect 2

### Amazon Macie <a id="Macie"></a>

Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data on Amazon S3. Macie automatically detects a large and growing list of sensitive data types, including personally identifiable information (PII) such as names, addresses, and credit card numbers. It also gives you constant visibility of the data security and data privacy of your data stored in Amazon S3.

### GuardDuty <a id="GuardDuty"></a>

Use Amazon GuardDuty to monitor any malicious activity on data stored in Amazon S3. Use Amazon Macie to identify any sensitive data stored on Amazon S3
Amazon GuardDuty offers threat detection that enables you to continuously monitor and protect your AWS accounts, workloads, and data stored in Amazon S3. GuardDuty analyzes continuous streams of meta-data generated from your account and network activity found in AWS CloudTrail Events, Amazon VPC Flow Logs, and DNS Logs. It also uses integrated threat intelligence such as known malicious IP addresses, anomaly detection, and machine learning to identify threats more accurately.

### Architectural Patterns

#### you need to enable a custom domain name and encryption in transit for an application that's running behind an ALB.

you can use Route 53 to create an alias record to the ALBs DNS name, and then attach an SSL/TTLS certificate issued by Amazon Certificate Manager, ACM.

#### A website running on EC2 instances behind an ALB must be protected against well-known web exploits.

think about the Web Application Firewall. So you'd create a web ACL in WAF to protect against those web exploits and you can attach that to the ALB.

#### You need to block access to an application running on an ALB from connections originating in a specific list of countries.

create a web ACL in WAF with a geographic match and block traffic that matches the list of countries.

#### A company needs to encrypt large volumes of data using a CMK in AWS KMS.

For this, you need to create a data encryption key using the CMK to encrypt the large volumes of data.

#### A mobile app requires authorized access to AWS services. Users authenticate using social IDPs and a preconfigured web UI is required for logging in.

use a Cognito user pool that leverages the social IDPs and an identity pool for gaining temporary credentials for AWS. 
And the user pool will give you that pre-configured web UI, it has that out of the box.

- User authentication with social IDPs
  - Cognito supports federated login via providers like: Google, Facebook, Apple and others via OpenID Connect / SAML
- Preconfigured web UI for login
  - Cognito provides a Hosted UI, which is a ready-to-use, customizable login page. No need to build your own frontend for authentication.
- Authorized access to AWS services
  - After login:
    - Cognito issues tokens (ID, access, refresh)
    - You can exchange these for AWS credentials via Cognito Identity Pools
    - These credentials allow controlled access to services like Amazon S3 or Amazon DynamoDB

oAuth2:
- Resource Owner → the user of your mobile app
- Client → your mobile app
- Authorization Server → Amazon Cognito (User Pool + Hosted UI)
- Resource Server → your AWS services (e.g., Amazon S3, Amazon DynamoDB)

#### A company has an on-premises Microsoft AD and a Direct Connect connection. They require the ability to join EC2 instances to the on-premises domain.

use an AD connector that uses

#### How often is the KMS-CMK rotated? 

Every year when automatic rotation is enabled.

Does the customer need to provide a new key?
- No — not in normal automatic rotation.
  - AWS handles everything:
    - Generates new cryptographic material
    - Associates it with the same KMS key

If you are using imported key material: Automatic rotation is NOT supported

#### A web application uses Network Load Balancer (NLB) to route traffic to the compute instances. Which of these configurations would offer comprehensive protection against Layer 7 attacks?

With AWS __WAF__, you can subscribe to ready-to-use managed rule groups provided by AWS and marketplace sellers. 
With this option, you get comprehensive protection against known application layer (Layer 7) vulnerabilities and exploits. 
AWS WAF does not support NLB. 
One option is to configure CloudFront distribution with NLB as the origin and associate AWS WAF to the CloudFront distribution

#### A financial company needs to limit access to the web application only for users from specific regions where they have a presence. Which of these options would enable you to that?

AWS __WAF__ has the option to __allow or block based on the request originating countries__. 
With this option, AWS automatically manages the IP to country mapping and keeps the information up-to-date. 
You can also use Amazon’s Anonymous IP Address managed rule group to block requests from services that hide caller identity (VPNs, Proxies, Tor nodes). 
All other options require you to maintain IP Blocks – which is a lot of overhead to keep track and maintain.

#### A web-based SaaS provider offers a solution for auto service centers and dealerships. To protect against attackers, the SaaS provider whitelists all CIDR IP blocks belonging to subscribed auto dealers. The number of CIDR entries is in several hundred.  Which of these options provide would you use for this scenario?

With __WAF IP Address sets__, you have a scalable solution for whitelisting or blacklisting. 
This solution __supports 1000s of IP address blocks__. 
The WAF IP Address sets and Regex Pattern Sets are reusable across different Web ACLs. 

Security Group has a limit of a few hundred entries, and Network ACL has a limit of a few 10s of entries.

#### Which of these solutions provide extensive visibility into layer 3, 4, and 7 attacks on your AWS resources?

With AWS __Shield Advanced__, you get access to real-time metrics and reports for extensive visibility into attacks on your AWS resources. 
You can also configure CloudWatch alarms to notify you of an attack in progress. 

__WAF__ provides full visibility into rules and requests that match your rules using CloudWatch metrics. 
These metrics are useful for tracking the application layer (Layer 7) attacks that were blocked by your rules

#### An organization wants to rotate database credentials automatically. The credentials must be stored in a secure data store. Which of these services provides built-in credential rotation support for this requirement?

With __Secrets manager__, you can easily __rotate__, manage, and retrieve secrets. 

Secrets Manager __encrypts the secrets using KMS keys__ that you specify. 

Systems Manager __Parameter Store__ supports the storage of encrypted passwords; however, by default, they store unencrypted. 
- Parameter Store does not have an automated mechanism for credential rotation
- Parameter Store has two main parameter types:
  - String (default): Stored as plain text (unencrypted)
    - This is what you get if you don’t specify encryption
  - SecureString: Stored encrypted using AWS Key Management Service

#### I need a tool that automatically scans CloudTrail Logs, VPC Flow Logs, and DNS logs and identifies suspicious events that are not part of normal baseline activities in my account. Which service should I use?

__Guard Duty__ is a managed threat detection service. 
It learns by reviewing the CloudTrail events, VPC Flow Log, and DNS logs to build a baseline of normal activities. 
It checks network activity, data access patterns, account behavior. 
Any abnormal and suspicious activities are flagged and reported by Guard Duty. 
You can use CloudWatch Events and Lamda for automated remediation.

#### Our application requires several third-party and open-source software libraries. How do I automatically check for vulnerabilities in these libraries? The solution should also check for any newly reported vulnerabilities. What capability can I use for this?

__Inspector__ can analyze your instance and application libraries for known vulnerability reported in the CVE database, CIS host hardening standards, network reachability assessment, and processes reachable over the exposed ports.

#### Developers require a new version of the framework installed on the servers. I need to make sure all development servers have the latest version installed. What service should I use for this?

With the Systems Manager’s __Patch Manager__ capability, you can define baseline patch levels, and __patch manager automatically patches the instances__.

#### Web Application Firewall allows for access limitation by IP address. However, it's important to highlight that WAF integration is exclusive to Application Load Balancer, CloudFront distribution, and API Gateway.

Any of these:
- Enable Advanced Shield on Network Load Balancer
- Protect CloudFront using AWS WAF: A common strategy is to use CloudFront in front of NLB and protect CloudFront with WAF

Cannot use:
- GuardDuty is an intrusion detection system that can detect suspicious activities
- AWS Inspector identifies software vulnerabilities in your EC2 instances and container images. Inspector does not block attacks.

#### An online retailer is looking for an automated solution to alert about fraudulent transactions, fake and spam accounts. Which solution would you recommend?

Amazon __Fraud Detector__ can detect online frauds with machine learning. 
For example, this service can flag suspicious online payments, detect new account fraud and incorporate additional verification steps, account takeover detection, and so forth

#### Apache Log4j vulnerability, which allows remote code execution and the ability to download and run arbitrary code on your servers. Let’s assume an issue like this vulnerability is reported and you want to assess the impact to your environment consisting of 1000s of servers and containers. What tools would you use to identify vulnerable systems and apply the fix?

Use:
- __Inspector__ can scan hosts and container images and report Security exposures and vulnerabilities. This tool assigns a risk score to prioritize your remediation.
- Systems Manager __Patch Manager__, you can automatically patch the vulnerable systems at scale. For patching container image, you may need additional CI/CD pipeline and tools to build a new image.

The following will not help:
- GuardDuty is an intrusion detection system that alerts about malicious activities in your environment.
- Control Tower provides a blueprint that follows AWS security and compliance best practices and sets up a multi-account environment for you, called a Landing Zone.
- Amazon Macie scans your S3 buckets and flags them if it contains sensitive data. Macie can also alert you when policies or settings in S3 buckets are changed in a way that reduces the security

#### An IT security consultancy is working on a solution to protect data stored in Amazon S3 from any malicious activity as well as check for any vulnerabilities on Amazon EC2 instances. As a solutions architect, which of the following solutions would you suggest to help address the given requirement?

- Use Amazon GuardDuty to monitor any malicious activity on data stored in Amazon S3. Use security assessments provided by Amazon Inspector to check for vulnerabilities on Amazon EC2 instances
Amazon GuardDuty offers threat detection that enables you to continuously monitor and protect your AWS accounts, workloads, and data stored in Amazon S3. GuardDuty analyzes continuous streams of meta-data generated from your account and network activity found in AWS CloudTrail Events, Amazon VPC Flow Logs, and DNS Logs. It also uses integrated threat intelligence such as known malicious IP addresses, anomaly detection, and machine learning to identify threats more accurately.

- Amazon Inspector security assessments help you check for unintended network accessibility of your Amazon EC2 instances and for vulnerabilities on those EC2 instances. Amazon Inspector assessments are offered to you as pre-defined rules packages mapped to common security best practices and vulnerability definitions.

#### A retail company uses Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon API Gateway, Amazon RDS, Elastic Load Balancer and Amazon CloudFront services. To improve the security of these services, the Risk Advisory group has suggested a feasibility check for using the Amazon GuardDuty service. Which of the following would you identify as data sources supported by Amazon GuardDuty?

VPC Flow Logs, Domain Name System (DNS) logs, AWS CloudTrail events

#### The team suspect the application is being targeted by distributed denial-of-service (DDoS) attacks coming from a wide range of IP addresses. The team needs a solution that provides DDoS mitigation, detailed logs for audit purposes, and requires minimal changes to the existing architecture.

Subscribe to AWS Shield Advanced to gain proactive DDoS protection. Engage the AWS DDoS Response Team (DRT) to analyze traffic patterns and apply mitigations. Use the built-in logging and reporting to maintain an audit trail of detected events

AWS Shield Advanced provides advanced, always-on DDoS protection for resources like ALBs, CloudFront, and Route 53. It includes detailed telemetry, real-time detection, automated application-layer DDoS mitigation, and most importantly, access to the AWS DDoS Response Team (DRT). 
The DRT can assist with rule creation and response during active events. Shield Advanced also supports detailed logging and event reports through AWS CloudWatch and AWS WAF logs, enabling complete auditing of DDoS attempts.

#### A global insurance company is modernizing its infrastructure by migrating multiple line-of-business applications from its on-premises data centers to AWS. These applications will be deployed across several AWS accounts, all governed under a centralized AWS Organizations structure. The company manages all user identities, groups, and access policies within its on-premises Microsoft Active Directory and wants to continue doing so. The goal is to enable seamless single sign-in across all AWS accounts without duplicating user identity stores or manually provisioning accounts. Which solution best meets these requirements in the most operationally efficient manner?

Deploy AWS __IAM Identity Center__ and configure it to use AWS Directory Service for Microsoft Active Directory (Enterprise Edition). 
Establish a two-way trust relationship between the managed directory and the on-premises Active Directory to enable federated authentication across all AWS accounts

This solution meets all key requirements: centralized SSO across multiple AWS accounts, integration with AWS Organizations, and continued use of the on-premises Active Directory. AWS Directory Service for Microsoft Active Directory (Enterprise Edition) supports two-way forest trust relationships with the company’s self-managed Active Directory. Once the trust is established, AWS IAM Identity Center can be configured to use the AWS Managed AD as its identity source, allowing federated login with on-prem AD users and groups. IAM Identity Center then centrally manages SSO access and permission sets across all AWS accounts—without duplicating identities.

#### you need to enable a custom domain name and encryption in transit for an application that's running behind an ALB.

- Register a Domain Name
- Create / Import an SSL/TLS Certificate. Use AWS Certificate Manager (ACM)
  - Region: same as your ALB
- Configure ALB to Use HTTPS and Add HTTPS Listener
- Update DNS to Point to ALB
  - Hosted Zone → Create Record
  - Record type: A (alias)
  - Alias target → ALB DNS name
  - TTL: Optional, e.g., 60s
- Encryption in Transit: TLS terminates at ALB by default
  - ALB → backend (EC2 / Lambda / ECS) options: HTTP (unencrypted, simplest) OR  HTTPS (encrypted end-to-end) → requires certificates on backend

#### A company needs to encrypt large volumes of data using a CMK in AWS KMS.

For encrypting large volumes of data with a CMK in AWS KMS, the standard approach is envelope encryption, because KMS cannot encrypt large data directly (max 4 KB per request)

- Generate a data key using the CMK.
Use the data key to encrypt the large data locally (AES-256 or AES-GCM).
Store the encrypted data key alongside the encrypted data.
When decrypting:
Use KMS to decrypt the data key.
Use the decrypted key to decrypt the data.

#### How do you securely grant a mobile app access to AWS resources without embedding credentials?

1. User logs in (Authentication): The mobile app redirects to Cognito Hosted UI:
  - ID Token (JWT)
  - Access Token
2. Exchange token for AWS credentials
  - The app sends the ID token to Cognito Identity Pool.
  - Identity Pool calls STS that returns: AccessKeyId, SecretAccessKey, SessionToken
3. App accesses AWS resources:
  - The mobile app uses temporary credentials to call AWS: Upload file to S3

#### How would you protect against data exfiltration from S3?

- Block Public Access (account + bucket level)
- Use bucket policies with explicit deny (e.g., deny non-TLS, deny outside VPC)
- Enable VPC endpoints for private access
- Use AWS CloudTrail + S3 access logs
- Add Amazon Macie for sensitive data detection
- Restrict via IAM conditions (IP, VPC, MFA)

#### How do you securely allow cross-account access?

Create IAM Role in Target Account (Account B)
```
resource "aws_iam_role" "cross_account_role" {
  name = "cross-account-access-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::ACCOUNT_A_ID:root"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}
```

Attach Least-Privilege Policy (Target Account)
```
resource "aws_iam_role_policy" "s3_access" {
  name = "s3-access-policy"
  role = aws_iam_role.cross_account_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = ["s3:GetObject", "s3:PutObject"]
        Resource = "arn:aws:s3:::my-secure-bucket/*"
      }
    ]
  })
}
```

Allow AssumeRole in Source Account (Account A)
```
resource "aws_iam_policy" "assume_role_policy" {
  name = "allow-assume-cross-account-role"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = "sts:AssumeRole",
        Resource = "arn:aws:iam::ACCOUNT_B_ID:role/cross-account-access-role"
      }
    ]
  })
}
resource "aws_iam_user_policy_attachment" "attach" {
  user       = "app-user"
  policy_arn = aws_iam_policy.assume_role_policy.arn
}
```










## Migration and Transfer <a id="Migration"></a>

Tools:
- DataSync
- Storage Gateway
- Snowball
- S3 sync, cp

### Service Migration Service – SMS <a id="SMS"></a>

 VMware, Hyper-V or Azure -> SMS connector -> Server volumes -> AMIs -> EC2

- automate migration of VM (virtual machine) from on-premises VMWare or Mcrosoft Hyper-V to Azure to AWS Cloud
- creates AMI
- up to 50 VMs at a time (concurrently)
- agentless service for migrating on-premises and cloud-based VMs to AWS.
- Source platforms can be VMware, Hyper-V or Azure.
- The Server Migration Service connector is installed on the source's platform.
- Server volumes are replicated and it's encrypted with TLS and saved as AMIs, which can then be launched as EC2 instances.
- You can use application groupings and SMS will launch servers in a CloudFormation stack.
- you can replicate your on-premises service to AWS for up to 90 days per server.
- It provides automated live incremental server replication and AWS console support.

### Database Migration Service – DMS <a id="DMS"></a>

Database Migration Service: to transfer data between __on-premises databases and cloud-based__ RDS

Supports __homogeneous__, so Oracle to Oracle, as well as __heterogeneous__. 
You can move to the managed data to Amazon Redshift, NoSQL platforms like Amazon DynamoDB, or low-cost storage platforms like Amazon Simple Storage Service (Amazon S3).
Application is live, minimizing downtime.

- used for migrating databases from on-premises, Amazon EC2 or Amazon RDS.
- supports homogeneous, so Oracle to Oracle, as well as heterogeneous, example, Oracle to Amazon Aurora.
- Data is continuously replicated while the application is live, minimizing downtime.
- You pay based on the compute resources used during the migration and the log storage.
- fully managed migration process.
- you can use it along with the schema conversion tool for converting schemas.
- DMS use cases include cloud to cloud, so EC2 to RDS, RDS to RDS, or RDS to Aurora, on premises to cloud and homogeneous migrations like Oracle to Oracle, MySQL to RDS MySQL, and so on.
- Also, heterogeneous migration:  moving from Oracle to Aurora, Oracle to Postgres, or Microsoft SQL to RDS MySQL. And then you'll need to use the schema conversion tool.
- It's also useful for development and test, so you can use the cloud for dev/test workloads and database consolidation.
- consolidating multiple source DBs to a single target DB.
- does continuous data replication so you can use it for DR, dev/test, or single source multi target or multi-source single target.

### DataSync <a id="DataSync"></a>

- Moves data (agent) between on-premises storage and AWS service.
- Copy data FROM: NFS, SMB, HDFS, between AWS storage services TO: S3, EFS, or FSx for Windows File Server.
- A secure, online service that automatically moves data between on-premises storage and AWS services. __uses TLS__
- __schedule a task__
- __Agent-based data mover__ - it is s a virtual appliance (vm image that you install)
- good for: data migration, archive, data protection, data movement
- Common targets: S3, EFS, FSx

It __uses AWS Direct Connect__ to move data between on-premises storage systems and AWS storage services

Can copy data between Network File System (NFS), Server Message Block (SMB), and Hadoop Distributed File Systems (HDFS)

Can also transfer data between AWS storage services

Uses in-flight encryption and end-to-end data validation

- software agent to connect to on-premises NAS storage systems.
- The NAS can use NFS or SMB protocols, and it synchronizes data into AWS using a scheduled automated data transfer with TLS encryption.
- Destinations can be S3, EFS, or FSx for Windows File Server.
- can improve performance for data transfers.
- Permissions and metadata are preserved.
- you pay per gigabyte transferred.

Steps to move data using AWS DataSync:
- Deploy and activate an AWS DataSync agent virtual machine
- Gather configuration data from your data center
- Validate network connectivity
- Create an AWS DataSync task
- Run the task to copy data to your Amazon S3 bucket


### Snowball <a id="Snowball"></a>

- are used for migrating large volumes of data to AWS.
- The __Snowball Edge Compute Optimized__:
  - provides block and object storage and an optional GPU.
  - You can use the data collection, machine learning and processing and storage in environments with intermittent connectivity, so edge use cases.
- __Snowball Edge Storage Optimized__:
  - This provides block storage and S3 compatible object storage.
  - You can use it for local storage and large scale data transfer.
- __Snowcone__:
  - This is a small device used for edge computing storage and data transfer.
  - You can transfer data offline or online with the AWS DataSync agent.
- Snowball uses secure storage devices for physical transportation,
- you have some client software that you install on a local machine and that can be used to identify the data that you want to transfer, compress it, encrypt it, and then actually transfer it.
- Snowball uses 256-bit encryption with managed KMS keys and tamper resistant enclosures with TPM.
- different devices:
  - Snowball: is capable of 80 terabytes or 50 terabytes depending on your model, and that's petabyte scale.
  - Snowball Edge: goes up to 100 terabytes and that's also known as petabyte scale.
  - Snowmobile: This is known as being exabyte scalable up to 100 petabytes per Snowmobile.
- There are a few ways to optimize the performance of Snowball transfers:
  - You can use the latest Mac or Linux Snowball client, batch small files together, perform multiple copy operations at one time, copy from multiple workstations, and transfer directories, not individual files.
- Use cases for Snowball are cloud data migration, so migrating data to the cloud. Content distribution, sending data to clients or customers.

Optimal data migration per data size comparison:
- Snowball: > 10TB
  - Snowball: 80TB
  - Snowball Edge: 100TB, block and object storage
  - SnowCone: device used for edge computing storage and data transfer
  - SnowMobile: 100PB
- Site-to-Site VPN < 100GB
- Direct Connect < 10TB

### AWS Data Transfer <a id="DataTransfer"></a>

- Site-to-Site VPN
  - For small to moderate amounts of data (< 100 GB) that need infrequent transfers
- AWS Direct Connect
  - For large amounts of data (< 10 TB) that need frequent transfers and a consistent connection with low latency
  - Direct Connect bypasses the public internet and provides a secure and dedicated connection to AWS.
- Snow family
  - For very large amounts of data ( > 10s of TBs) and infrequent transfers


### Amazon AppFlow <a id="AppFlow"></a>

It is used for __data movement and basic transformation__ __between SaaS applications__ (like Salesforce, Zendesk) and __AWS services__, but it does not support transforming or managing datasets already in S3 at scale

AppFlow is a __no-code solution__ to automate data flow by __securely__ integrating third-party applications and AWS services and securely transferring data from SaaS applications like Salesforce, SAP, Zendesk, Slack, and ServiceNow.

AppSync is used for building applications with serverless GraphQL and Pub/Sub APIs.

Amazon AppFlow is a fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications, such as Salesforce, and AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon Redshift.

### Architectural Patterns

#### company is migrating Linux and Windows VMs to in VMWARE to the cloud and they need to determine the performance requirements for right-sizing.

you can install the application discovery service discovery connector in vmware V center to gather the data.

#### A company has a mixture of VMware VMs and physical servers to migrate to AWS and dependencies exist between application components.

you might install the MGN replication agent and create application groups to migrate the servers in waves.

#### You need to migrate an oracle data warehouse to AWS.

AWS DMS and the schema conversion tool to a Redshift data warehouse.

#### we have snowball edge being used to transfer millions of small files using a shell script and transfer times are very slow.

you can perform multiple copy operations at one time by running each command from a separate terminal. In separate instances of the Snowball client,

#### you need to minimize downtime for servers that must be migrated to AWS.

use the MGN and perform a final synchronization before cutting over in a short outage window.

#### you need to migrate 50 terabytes of data and the company only has a one gigabits per second internet link.

Use AWS Snowball to transfer data

####  AWS Transfer Family: Your environment has several existing clients that use SFTP, FTP, FTPS, and AS2 protocols for file transfer. Which service offers a fully managed solution to move data into and out of AWS Storage services using these protocols?

#### Customer needs to migrate 50 TB of data from on-premises systems to AWS cloud Incremental data needs to be in sync until cutover to cloud What cloud storage and data transfer service would you use for this?

DataSync for initial transfer (if network is not a constraint) and for incremental loading

| Factor                | File Gateway                                                                                   | DataSync                                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Initial bulk transfer | Can do it, but **writes happen via network over time**, so 50 TB could take **weeks** over WAN | Optimized for large-scale transfer, uses **parallelization** and **incremental updates**, much faster |
| Incremental sync      | File Gateway uploads changes as they happen, but scheduling large batch syncs is less flexible | DataSync supports **scheduled, incremental, and bandwidth-controlled syncs**                          |
| Cutover planning      | File Gateway is meant for **ongoing hybrid storage**, not one-time migrations                  | DataSync + S3 allows a clean **initial sync + repeated incremental sync + final cutover**             |
| Large datasets        | Could be slow over WAN; high upfront traffic might overwhelm local network                     | Handles large datasets efficiently; supports **encryption and compression**                           |


#### Customer needs to migrate 50 TB from on-premises file shares to AWS cloud and make data available to on-premises applications. Customer is interested in reducing the storage footprint on-premises. What storage service and data transfer solution would you use?

__DataSync__ for initial transfer (if network is not a constraint)

__Storage Gateway__ for incremental loading and for replacing on-premises storage (block, file share, tape)

#### Customer has on-premises Linux and windows applications that use NFS, SMB file shares. Customer is migrating the application to cloud. What storage service and data transfer service would you use that minimizes changes to the application?

DataSync for initial transfer (if network is not a constraint) and, for incremental transfer

#### Customer needs to migrate 50 TB of data from on-premises systems to AWS cloud. Incremental data needs to be in sync until cutover to the cloud. What cloud storage and data transfer service would you use for this?

Storage Gateway

#### Your environment has several existing clients that use SFTP, FTP, FTPS, and AS2 protocols for file transfer. Which service offers a fully managed solution to move data into and out of AWS Storage services using these protocols?

AWS Transfer family

AWS Transfer Family is a secure transfer service that enables you to transfer files into and out of AWS storage services.

AWS Transfer Family offers fully managed support for the transfer of files over SFTP, AS2, FTPS, FTP, and web browser-based transfers

AWS Transfer Family supports transferring data from or to the following AWS storage services:
- Amazon Simple Storage Service (Amazon S3) storage.
- Amazon Elastic File System (Amazon EFS)
- Network File System (NFS) file systems

#### You are consolidating data from multiple SaaS partners like Salesforce, SAP, and Zendesk. Which service would you use for this?

__AWS AppFlow__.

AppFlow is a no-code solution to automate data flow by securely integrating third-party applications and AWS services and securely transferring data from SaaS applications like Salesforce, SAP, Zendesk, Slack, and ServiceNow.

AppSync is used for building applications with serverless GraphQL and Pub/Sub APIs.

Amazon AppFlow is a fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications, such as Salesforce, and AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon Redshift.

For example, you can ingest contact records from Salesforce to Amazon Redshift or pull support tickets from Zendesk to an Amazon S3 bucket

#### You plan to migrate over 100 TB of data from your data warehouse system to the Amazon Redshift database. The network bandwidth from on-premises to the internet for this data migration is 250 Mbps. What option would you use to transfer data to AWS quickly?

Snowball

With a 250 Mbps link, it will take 40 days to transfer 100 TB data. Whereas, snowball turn around time is less than 1 week

#### Customer has on-premises Linux and windows applications that use NFS, SMB file shares. Customer is planning a lift and shift migration to cloud. What storage service would you use that minimizes changes to the application

FSx for Windows or EFS

#### The Fruit company needs to analyze data generated by sensors of their autonomous car. The dataset size in 100s of TBs and stored in S3 standard storage. To analyze all this data, data science team needs a high-performance cluster with over 1000 servers with very low latency and very high throughput network connectivity. The servers also need low latency data access. How should they design the system?

Use
- Use FSx for Lustre linked to an S3 bucket
  FSx for Lustre is a high-performance file share that offers low latency data access. This is optimized for high performance computing and fast processing. FSx for Lustre can operate as a standalone file share or you can link it to S3 bucket and present the content of S3 bucket as a file share. Any changes you make to the file system is automatically updated to S3. Similarly, the linked file system is automatically updated as objects are changed in S3.
- Create cluster using Cluster Placement Group
With EC2’s Cluster Placement Group, the instances are packed closely together in a single availability zone. These instances may share the same rack and networking infrastructure to achieve low latency.
Another option is the Partition Placement Group. This option minimizes the impact to your application due correlated hardware failure.

#### The customer needs to migrate 50 TB of data from on-premises file shares to S3 Any new changes in on-premises (incremental data) need to be in sync with S3 until cutover to the cloud. What data transfer service would you use for this?

- Data Sync: Data Sync is an AWS tool optimized for moving large amounts of data.
  You can use this to transfer from on-premises to AWS Storage services (S3, EFS, FSx for Windows).
  Data Sync supports both one-time migration and scheduled incremental transfer. Data Sync automatically tracks changes to perform incremental transfers efficiently
- Snowball Edge Storage Optimized.
  remember this information: 100 Mbps network link can transfer 1 TB/day
  transferring 50 TB can take 50 days using a 100 Mbps link.
  Snowball Edge: end-to-end time to transfer is approximately one-week

#### You would like to use AWS Snowball to move on-premises backups into a long term archival tier on AWS. Which solution provides the MOST cost savings?

Create an AWS Snowball job and target an Amazon S3 bucket. Create a lifecycle policy to transition this data to Amazon S3 Glacier Deep Archive on the same day

AWS Snowball, a part of the AWS Snow Family, is a data migration and edge computing device that comes in two options. Snowball Edge Storage Optimized devices provide both block storage and Amazon S3-compatible object storage, and 40 vCPUs. They are well suited for local storage and large scale data transfer.

For this scenario, you will want to minimize the time spent in Amazon S3 Standard for all files to avoid unintended Amazon S3 Standard storage charges. To do this, AWS recommends using a zero-day lifecycle policy. From a cost perspective, when using a zero-day lifecycle policy, you are only charged Amazon S3 Glacier Deep Archive rates. When billed, the lifecycle policy is accounted for first, and if the destination is Amazon S3 Glacier Deep Archive, you are charged Amazon S3 Glacier Deep Archive rates for the transferred files.

You can't move data directly from AWS Snowball into Amazon S3 Glacier, you need to go through Amazon S3 first, and then use a lifecycle policy. So this option is correct.

#### A global pharmaceutical company wants to move most of the on-premises data into Amazon S3, Amazon Elastic File System (Amazon EFS), and Amazon FSx for Windows File Server easily, quickly, and cost-effectively. As a solutions architect, which of the following solutions would you recommend as the BEST fit to automate and accelerate online data transfers to these AWS storage services?

Use AWS DataSync to automate and accelerate online data transfers to the given AWS storage services

AWS DataSync is an online data transfer service that simplifies, automates, and accelerates copying large amounts of data to and from AWS storage services over the internet or AWS Direct Connect.

AWS DataSync fully automates and accelerates moving large active datasets to AWS, up to 10 times faster than command-line tools. It is natively integrated with Amazon S3, Amazon EFS, Amazon FSx for Windows File Server, Amazon CloudWatch, and AWS CloudTrail, which provides seamless and secure access to your storage services, as well as detailed monitoring of the transfer.

AWS DataSync uses a purpose-built network protocol and scale out architecture to transfer data. A single DataSync agent is capable of saturating a 10 Gbps network link.

AWS DataSync fully automates the data transfer. It comes with retry and network resiliency mechanisms, network optimizations, built-in task scheduling, monitoring via the DataSync API and Console, and Amazon CloudWatch metrics, events, and logs that provide granular visibility into the transfer process. AWS DataSync performs data integrity verification both during the transfer and at the end of the transfer.

The AWS Transfer Family provides fully managed support for file transfers directly into and out of Amazon S3 and Amazon EFS. Therefore, it cannot support migration into the other AWS storage services mentioned in the given use-case (Amazon FSx for Windows File Server).

#### A Big Data analytics company writes data and log files in Amazon S3 buckets. The company now wants to stream the existing data files as well as any ongoing file updates from Amazon S3 to Amazon Kinesis Data Streams. As a Solutions Architect, which of the following would you suggest as the fastest possible way of building a solution for this requirement?

Leverage AWS Database Migration Service (AWS DMS) as a bridge between Amazon S3 and Amazon Kinesis Data Streams

You can achieve this by using AWS Database Migration Service (AWS DMS). AWS DMS enables you to seamlessly migrate data from supported sources to relational databases, data warehouses, streaming platforms, and other data stores in AWS cloud.

The given requirement needs the functionality to be implemented in the least possible time. You can use AWS DMS for such data-processing requirements. AWS DMS lets you expand the existing application to stream data from Amazon S3 into Amazon Kinesis Data Streams for real-time analytics without writing and maintaining new code. AWS DMS supports specifying Amazon S3 as the source and streaming services like Kinesis and Amazon Managed Streaming of Kafka (Amazon MSK) as the target. AWS DMS allows migration of full and change data capture (CDC) files to these services. AWS DMS performs this task out of box without any complex configuration or code development. You can also configure an AWS DMS replication instance to scale up or down depending on the workload.

AWS DMS supports Amazon S3 as the source and Kinesis as the target, so data stored in an S3 bucket is streamed to Kinesis. Several consumers, such as AWS Lambda, Amazon Kinesis Data Firehose, Amazon Kinesis Data Analytics, and the Kinesis Consumer Library (KCL), can consume the data concurrently to perform real-time analytics on the dataset. Each AWS service in this architecture can scale independently as needed.








## AWS Reference Architectures <a id="ReferenceArchitectures"></a>


### Web Application Hosting (Multi‑Tier)

- Amazon Route 53 (DNS)
- Amazon CloudFront (CDN)
- Application Load Balancer (ALB)
- Amazon EC2 / Auto Scaling or AWS Elastic Beanstalk
- Amazon RDS (DB)
- Amazon S3 (static content)
- How it works: Requests → CloudFront → ALB → EC2 app instances → RDS for persistent data.
- Benefits: Scalability, high availability, caching.

Q:
- how dns sends requests to cloudfront?
  - You own a domain, e.g., www.example.com.
  - In Amazon Route 53, you create a hosted zone for this domain.
  - When you create a CloudFront distribution, AWS assigns a domain like: d1234abcd.cloudfront.net
  - CloudFront points to your origin (EC2 instances, S3 bucket, ALB, or Elastic Beanstalk app).
  - In Route 53, you create a DNS record for www.example.com:
    - Type: A – IPv4 address
    - Alias: Yes
    - Alias target: your CloudFront distribution
- can ALB cache the content?
  - NO!
  - CDN cache at global edge locations. Can cache static and dynamic content based on rules.

### Serverless Web App (API + Frontend)

- Amazon S3 & CloudFront (frontend hosting)
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon Cognito (user auth)
- How it works: Static web files served from S3→CloudFront; API calls go to API Gateway→Lambda→DynamoDB.
- Benefits: No servers, auto‑scale, pay per use.

Q:
- can API Gateway accept internet traffic by default?
  - When you create an HTTP API or REST API in API Gateway, AWS automatically gives it a public endpoint like: https://abcd1234.execute-api.us-east-1.amazonaws.com/prod/
  - Even though it’s public, you usually secure API Gateway with:
    - authentication: cognito user-pools
    - WAF (prefent DDos, throtteling)
  - all traffic to Amazon API Gateway is HTTPS by default
- Why there is no DNS?
  - You can use Route 53 if you want a custom domain, e.g., www.example.com.
- How Cognito works with Lambda or API Gateway?
  - When a client (user) wants to access an API endpoint, Amazon API Gateway can authenticate the request using Amazon Cognito User Pools for user authentication.
  - A user signs in (via Cognito User Pool or through a federated identity provider like Facebook or Google).
  - Cognito returns a JWT Token (JSON Web Token) after successful authentication.
  - The client app sends a request to the API Gateway endpoint.
  - The API request includes the JWT Token in the Authorization header
  - API Gateway is configured to use Cognito User Pool Authorizer to validate the JWT token.
  - It checks the token’s signature against the Cognito User Pool's public keys to verify the user’s identity and permissions.
  - If the token is valid, the API request proceeds to the appropriate Lambda function or resource.

### Event‑Driven Architecture

- Amazon EventBridge
- AWS Lambda
- Amazon SNS
- Amazon SQS
- Downstream services
- How it works: Events from apps → EventBridge → lambda/queues → processing.
- Benefits: Loose coupling, asynchronous integration.

### REST API Backend

- API Gateway
- AWS Lambda
- Amazon Cognito / IAM (security)
- VPC + RDS / DynamoDB
- How it works: API Gateway routes API requests, enforces auth, invokes Lambda which interacts with DB.

### User Authentication with Cognito

- Amazon Cognito User Pools
- Cognito Identity Pools
- Federated identity (Google, Facebook, SAML)
- Backend services (API Gateway, Lambda)
- How it works: Cognito manages sign‑up/sign‑in, tokens are used to access APIs.

Q:
- how client app can call cognito?
- what are cognito user pools and how they work? Can it manage 1000s of users?
  - User Registration: Allows users to register and sign up for your application.
  - User Authentication: Verifies user credentials and authenticates them.
  - Access Control: You can define and manage groups and roles to control user access to resources (e.g., admin, guest).
  - Multi-Factor Authentication (MFA): Supports extra layers of security.
  - Cognito is designed to handle millions of users. Here's how it can scale:

### Big Data Analytics Pipeline

- Amazon Kinesis Data Firehose / Data Streams
- AWS Glue (ETL)
- Amazon S3 (data lake)
- Amazon Athena (query)
- Amazon Redshift (data warehouse)
- QuickSight (visualization)
- How it works: Streaming data ingested → Firehose → S3 → cleaned/curated → analyzed/query.

### Data Lake (Lake Formation)

- AWS Lake Formation
- Amazon S3
- AWS Glue Data Catalog
- IAM permissions
- How it works: Central metadata/catalog, fine‑grained access, ingestion from many sources.

Q:
- what are main features of data lake formation?
  - Centralized Storage in Amazon S3:
  - Ingestion of Data from Various Sources:
  - Fine-Grained Access Control: who can access specific datasets
  - Data Lake Permissions:
  - Supports Encryption and Data Masking
  - Cross-Account Data Sharing

### Machine Learning Platform

- Amazon SageMaker
- S3 (data)
- IAM
- (Optional) Lambda/Step Functions for workflows
- How it works: Data stored in S3 → SageMaker training → model hosting → inference via endpoints.

### Data Warehouse with Redshift

- Amazon Redshift
- S3
- AWS Glue
- BI tools (QuickSight)
- How it works: ETL into Redshift → fast SQL analytics.

Q:
- how to efficiently insert data from s3 to Redshift using aws glue?
  - Use the COPY command to load data from S3 into Redshift, but make sure the schema matches the S3 data structure ((Recommended for Large Data))
  - AWS Glue has a native connector for Redshift that allows you to perform the Insert/Update or Upsert operations efficiently.


### Microservices on Containers

- Amazon ECS / Fargate or Amazon EKS
- ALB
- Service Discovery
- VPC
- Databases (RDS/DynamoDB)
- How it works: Services deployed in containers, scale independently.

Q:
- can I use ALB with ECS, fargate or EKS? What is the advantage? Can I throttle?
  - Yes, you can use Application Load Balancer (ALB) with Amazon ECS, AWS Fargate, and Amazon EKS. Each of these services can integrate with an ALB to distribute traffic across your containers or services.
  - For EKS: ALB can be used as the Ingress Controller to manage the traffic routing from external clients to services running in EKS.
  - Advantages of Using ALB with ECS, Fargate, or EKS:
    - Simplified Traffic Management: route traffic to multiple microservices based on the domain, path, or other
    - ALB integrates tightly with AWS services like ECS, EKS, and Fargate, providing native support for service discovery, health checks, and auto scaling.
    - TLS Termination
  - ALB does not provide built-in throttling capabilities. Use AWS WAF or API Gateway
- How do I do service discovery using this setup?
  - Service Discovery for ECS (with ALB):
    - In ECS, you can configure service discovery by using __AWS Cloud Map__. Cloud Map enables services to register their locations (IP addresses) so that other services can discover and connect to them.
    - Service Discovery for EKS (with ALB)
      - EKS supports service discovery using CoreDNS for internal Kubernetes services, but when using ALB

### Hybrid Cloud with AWS Direct Connect

- AWS Direct Connect
- VPN
- Transit Gateway
- On‑prem routers
- VPC resources
- How it works: Dedicated network link to AWS for low latency and secure hybrid workloads.

### Secure VPC Architecture

- VPC (public/private subnets)
- NAT Gateway
- Security Groups + NACLs
- Bastion Host
- Private endpoints (AWS PrivateLink)
- How it works: Public facing only where needed; most resources are private.

### High Availability (Multi‑AZ)

- Auto Scaling Groups
- Multi‑AZ RDS
- Load Balancers
- Route53 health checks
- How it works: Traffic routed to healthy resources across AZs.

### Batch ETL with Step Functions

- AWS Step Functions
- AWS Lambda
- AWS Glue / EMR
- CloudWatch Events
- How it works: Step Functions defines workflow steps, retries, and branching.


### Security & Compliance Logging

- AWS CloudTrail
- AWS Config
- Amazon GuardDuty
- CloudWatch Logs
- (Optional) Lake Formation for analysis
- How it works: Capture all API calls, evaluate compliance rules, alert/detect threats.

Q:
- explain this setup

