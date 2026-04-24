---
url: https://docs.xendit.co/docs/sub-accounts
title: Sub-account types
description: ''
section: docs
scraped_at: '2026-04-23T06:17:46.489865Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformSet up sub-accounts
- Documentation
- xenPlatform
- Set up sub-accounts
---
# Sub-account types

Sub-accounts are Xendit accounts that represent your merchants, similar to setting up individual bank accounts for each of them within your platform. This helps you organize and track each merchant’s money separately. There are two different sub-account types available in xenPlatform.

## Types of Sub-Accounts

Before creating your sub-accounts, you will first need to identify which configuration fits your merchants or the overall business flow. There are two types of sub-accounts: **Owned and Managed**.

> Exceptions for sub-account type support
>
> Owned sub-accounts are currently disabled for **Indonesia**-based accounts by default. Please contact support to request for this capability.

|  | Owned sub-account | Managed sub-accounts |
| --- | --- | --- |
| **Description** | A sub-account that represents businesses you own, and does not require separate verification. | A sub-account that represents third-party merchants that you are transacting on behalf of. |
| **Best for** | Platforms that transact with customers on behalf of their merchants, and need to separate each partner's balances | Platforms that transact with customers on behalf of their merchants or when customers transact directly with your merchants |
| **Verification Requirements** | Is live and is ready to transact without verification. When necessary, you may still submit verification via API. | You can invite merchants to complete the onboarding process our dashboard. Merchants can start accepting payments once they pass verification. |
| **Visibility** | Users cannot see or access these accounts unless they are invited | The merchants you invite to the sub-account can see and manage their funds, while you maintain full control |
| **Payout Options** | Disbursements | Disbursements and Withdrawals |
| **Whose information is displayed to the customer during payment?** | Master Account | Sub-Account |
| **Whose balance are transaction fees deducted from?** | Sub-Account | Sub-Account |
| **Who receives invoices from Xendit?** | Master Account | Sub-Account |
| **How do I set webhook URLs for sub-accounts?** | The webhook settings on the Master account will automatically synchronize to your Owned sub-accounts | Sub-accounts can manage their webhook settings independently from the dashboard. The Master account can also set this via API. |

Once you have a better idea on which type is better suited for your merchants, you can get started and [create your sub-account](/docs/create-sub-accounts#how-to-create-subaccounts-via-dashboard).

### Custom Configurations

When creating your account via API, you can set different configurations below instead of choosing a type. [The next section](/docs/create-sub-accounts#creating-subaccounts-via-api) explains how this can be done.
