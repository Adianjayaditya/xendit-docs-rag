---
url: https://docs.xendit.co/docs/xenplatform-monitoring-transactions
title: Monitoring transactions
description: ''
section: docs
scraped_at: '2026-04-23T06:19:22.412162Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformMonitoring & Reporting
- Documentation
- xenPlatform
- Monitoring & Reporting
---
# Monitoring transactions

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/xp-step-3.webp?sv=2022-11-02&spr=https&st=2026-04-23T06%3A19%3A19Z&se=2026-04-23T06%3A30%3A19Z&sr=c&sp=r&sig=HyAlifzlv87X6KZ1JVrDc8WCAbYYVXNuOPSBPD3zO6Y%3D)

You can monitor transactions in real-time and generate reports for all your accounts for reconciliation purposes.

1. Log in to your Xendit dashboard
2. View a snapshot of your platform's payment volumes and performance over time
3. Navigate to each sub-account and track their activities

## Accounts overview

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/xp-accounts-new.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A19%3A19Z&se=2026-04-23T06%3A30%3A19Z&sr=c&sp=r&sig=HyAlifzlv87X6KZ1JVrDc8WCAbYYVXNuOPSBPD3zO6Y%3D)

The Accounts Overview shows all the sub-accounts you created along with their status and current Cash Balances. By default it shows the most recently-created sub-accounts first, and you can filter the list by account status and date created. You can also search for sub-accounts by their business names, unique IDs, or business email.

## Account profile page

1. Navigate to the xenPlatform Accounts
2. Click on a specific sub-account to view more details

The Account Profile Page shows basic information for the sub-account:

- Name
- Email
- Account ID
- Date Created
- Account Status
- Account Type (Owned, Managed)
- Cash Balance
- Available Payment Channels

## Account Activity Page

You can view the Balance and Transaction history for the sub-account your choose

1. Navigate to the xenPlatform Accounts
2. Click on more options for specific sub-account and select **View Activity**

   1. You can also switch to this tab from the Account Profile page

## Monitoring via API

You can also use your API key and utilize the following endpoints to retrieve and display information on your sub-accounts. Use the `for-user-id` header parameter to retrieve information for a sub-account.

```
{
  "for-user-id": "my-sub-account-id-12345"
}
```

JSON

Copy

| API | Description | Use Case |
| --- | --- | --- |
| [GET Sub-accounts List](https://docs.xendit.co/apidocs/list-accounts) | Retrieves a list of sub-accounts | Display a list of all sub-accounts in your application’s dashboard |
| [GET Account](https://docs.xendit.co/apidocs/get-account) | Retrieves a sub-account | Display detailed account information for one sub-account |
| [GET Balance](https://docs.xendit.co/apidocs/get-balance) | Displays the current balance for an account | Check the current live Balance for a sub-account |
| [GET Transactions List](https://docs.xendit.co/apidocs/list-transactions) | Retrieves a list of transactions. | Display recent transactions completed by a merchant |
| [GET Transaction](https://docs.xendit.co/apidocs/get-transaction) | Retrieves a specific transaction | Check a specific transaction that was settled to a merchant |
| [Generate Reports](https://docs.xendit.co/apidocs/generate-report) | Generates a transaction or balance report | Monthly reconciliation |
