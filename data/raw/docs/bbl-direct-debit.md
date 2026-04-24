---
url: https://docs.xendit.co/docs/bbl-direct-debit
title: BBL Direct Debit
description: ''
section: docs
scraped_at: '2026-04-23T06:35:19.826060Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsSupported payment channelsThailand
- Documentation
- Accept payments
- Supported payment channels
- Thailand
---
# BBL Direct Debit

---

## Features & Requirements

|  |  |
| --- | --- |
| **Channel code** | `BBL_DIRECT_DEBIT` |
| **Currency** | THB |
| **Minimum amount** | 20 |
| **Maximum amount** | 700,000 |
| **User approval flow** | REDIRECT |
| **Save** | ✅ |
| **Recurring** | ✅ |
| **Display merchant name** | Xendit, |
| **Display user name** | ❌ |
| **Set expiry** | ❌ |
| **Settlement Time** | Instant |
| **Refund** | ❌ |
| **Partial refund** | ❌ |
| **Multiple partial refund** | ❌ |
| **Refund validity** | ❌ |
| **User data required by Bank\*** | - Mobile Number |
| **Compatible integration** | Payment API, Payment Session, Subscription, Recurring |

\*Bank will validate the login credential to the mobile phone number sent during Payment Request

## Account Linking flow

End customer select the bank to link on checkout page and process authorization (Account Linking)

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Payment%20session%20-%20DD%20linking.jpg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A35%3A16Z&se=2026-04-23T06%3A46%3A16Z&sr=c&sp=r&sig=hMrInegc15wbfOc4QLN4PBNAbMD55ux49xiGhEoAgd0%3D)

![Steps for linking a direct debit account through the bank's app interface.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/BBL DD.jpg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A35%3A16Z&se=2026-04-23T06%3A46%3A16Z&sr=c&sp=r&sig=hMrInegc15wbfOc4QLN4PBNAbMD55ux49xiGhEoAgd0%3D)
