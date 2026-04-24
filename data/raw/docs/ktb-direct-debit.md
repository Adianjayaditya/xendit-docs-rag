---
url: https://docs.xendit.co/docs/ktb-direct-debit
title: KTB Direct Debit
description: ''
section: docs
scraped_at: '2026-04-23T06:35:32.690365Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsSupported payment channelsThailand
- Documentation
- Accept payments
- Supported payment channels
- Thailand
---
# KTB Direct Debit

---

## Features & Requirements

|  |  |
| --- | --- |
| **Channel code** | `KTB_DIRECT_DEBIT` |
| **Currency** | THB |
| **Minimum amount** | 20 |
| **Maximum amount** | 700,000 |
| **User approval flow** | REDIRECT |
| **Save** | ✅ |
| **Recurring** | ✅ |
| **Display merchant name** | Xendit |
| **Display user name** | ❌ |
| **Set expiry** | ❌ |
| **Settlement Time** | Instant |
| **Refund** | ❌ |
| **Partial refund** | ❌ |
| **Multiple partial refund** | ❌ |
| **Refund validity** | ❌ |
| **User data required by Bank\*** | - Mobile Number - Identity Number or Passport Number |
| **Compatible integration** | Payment API, Payment Session, Subscription, Recurring |

\*Bank will validate the login credential to the mobile phone number & ID No. sent during Payment Request

## Account Linking flow

End customer select the bank to link on checkout page and process authorization (Account Linking)

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Payment session - DD linking.jpg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A35%3A29Z&se=2026-04-23T06%3A46%3A29Z&sr=c&sp=r&sig=oZ%2FF%2Fzd6CsRPiu3OBi0azesEGravZ5XHJOkIJrwRAr4%3D)

![Steps to link a bank account using Krungthai NEXT app for transactions.](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/KTB DD.jpg?sv=2022-11-02&spr=https&st=2026-04-23T06%3A35%3A29Z&se=2026-04-23T06%3A46%3A29Z&sr=c&sp=r&sig=oZ%2FF%2Fzd6CsRPiu3OBi0azesEGravZ5XHJOkIJrwRAr4%3D)
