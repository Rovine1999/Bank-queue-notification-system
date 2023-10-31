# Bank Queue Notification System 

This system allows the creation of branches, tellers (employees) to those branches, customers to given branches.

It also allows customers to get a service from any branch by joining a queue at a given branch.

Then the tellers can pick a customer who is in queue, the customer gets an email notification (Currently: 
Using file based email backend for django) and once the customer is served, the teller can finish serving the customer 
and be available for the next customer. 

A teller can only take a customer in queue only if the previous customer is not in queue as `NEW`. There are three stages
for a customer in queue that is `0` for `NEW`, `1` for `IN_SERVICE` and `2` for `DONE`.

## Setup

To setup, unzip the file and create.

Create a super user, login in to admin dashboard and create `2 groups`
## Group 1 - `employee` group

Add this permissions to this group
```text
admin | log entry | Can add log entry
admin | log entry | Can change log entry
admin | log entry | Can delete log entry
admin | log entry | Can view log entry
auth | user | Can add user
auth | user | Can change user
auth | user | Can delete user
auth | user | Can view user
authtoken | Token | Can add Token
authtoken | Token | Can change Token
authtoken | Token | Can delete Token
authtoken | Token | Can view Token
authtoken | token | Can add token
authtoken | token | Can change token
authtoken | token | Can delete token
authtoken | token | Can view token
mainapp | branch | Can add branch
mainapp | branch | Can change branch
mainapp | branch | Can delete branch
mainapp | branch | Can view branch
mainapp | customer | Can add customer
mainapp | customer | Can change customer
mainapp | customer | Can delete customer
mainapp | customer | Can view customer
mainapp | employee queue assignment | Can add employee queue assignment
mainapp | employee queue assignment | Can change employee queue assignment
mainapp | employee queue assignment | Can delete employee queue assignment
mainapp | employee queue assignment | Can view employee queue assignment
notification | Can add notification
notification | Can change notification
notification | Can delete notification
notification | Can view notification
mainapp | queue | Can add queue
mainapp | queue | Can change queue
mainapp | queue | Can delete queue
mainapp | queue | Can view queue
transaction | Can add transaction
transaction | Can change transaction
transaction | Can delete transaction
transaction | Can view transaction
sessions | session | Can add session
sessions | session | Can change session
sessions | session | Can delete session
sessions | session | Can view session
```

## Group 2 - `customer` group

Add this permissions to this group

```text
admin | log entry | Can add log entry
admin | log entry | Can change log entry
admin | log entry | Can delete log entry
admin | log entry | Can view log entry
auth | permission | Can view permission
auth | user | Can change user
auth | user | Can view user
authtoken | Token | Can add Token
authtoken | Token | Can change Token
authtoken | Token | Can view Token
authtoken | token | Can add token
authtoken | token | Can change token
authtoken | token | Can view token
mainapp | branch | Can view branch
notification | Can view notification
mainapp | queue | Can add queue
mainapp | queue | Can view queue
transaction | Can view transaction
sessions | session | Can add session
sessions | session | Can change session
sessions | session | Can delete session
sessions | session | Can view session
```

## About role based access

This allows to identify between tellers (Employees) and customers. Customers have both the common and queue related 
permissions only in which they can add and view a queue but can't update nor delete.

Tellers have the ability to manage customers and also manage queues.