---
url: https://docs.xendit.co/docs/verify-sub-accounts
title: Verify sub-accounts
description: ''
section: docs
scraped_at: '2026-04-23T06:18:01.571488Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformSet up sub-accounts
- Documentation
- xenPlatform
- Set up sub-accounts
---
# Verify sub-accounts

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/xenplatform-step-1(1).webp?sv=2022-11-02&spr=https&st=2026-04-23T06%3A17%3A58Z&se=2026-04-23T06%3A28%3A58Z&sr=c&sp=r&sig=a1gmQnuAheU2hYIBuEvVw4AGPvU6qQ9X%2FdznblTK%2F4Y%3D)

Depending on the sub-account type you selected, your merchants may need to be verified before the sub-account can start accepting payments.

|  | Owned Accounts | Managed Accounts |
| --- | --- | --- |
| Use Case | Your own business | 3rd party merchants |
| Verification Required | No\* | Yes |
| Submission Methods | The Platform may submit sub-merchants’ verification information via API | You can invite your merchants to [sign up and submit](https://docs.xendit.co/docs/create-account) their information for verification. Note that you may invite your own users to submit on the merchants’ behalf. |

\*There are some cases when you may use Owned sub-accounts to represent 3rd party merchants and need to verify your sub-accounts. The conditions are explained below.

### Owned sub-account verification

Even if you are creating Owned sub-accounts, you may be required to verify your sub-accounts in either one or both of the following scenarios:

- You are a Payment Service Provider (reseller)

  - This means that you onboard non-affiliated Partner accounts to Xendit and provide them with access to money-in and/or money out payment flows
  - Example: PoS systems, Payment Resellers
- You would like to activate a payment channel that requires an additional verification for your sub-account

  - Some channels that require verification are Credit Cards and GCash (PH). Refer to this page for a complete list of requirements per channel.

If either of these cases apply to you, [here is a guide](https://docs.xendit.co/docs/submit-account-verification) you can follow to submit verification information for your sub-accounts.
