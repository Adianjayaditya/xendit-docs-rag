---
url: https://docs.xendit.co/docs/accepting-payments-for-sub-accounts
title: Accept payments for sub-accounts
description: ''
section: docs
scraped_at: '2026-04-23T06:06:36.629030Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationxenPlatformAccept & Route Payments
- Documentation
- xenPlatform
- Accept & Route Payments
---
# Accept payments for sub-accounts

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/accept-payment-for-eng.webp?sv=2022-11-02&spr=https&st=2026-04-23T06%3A06%3A33Z&se=2026-04-23T06%3A18%3A33Z&sr=c&sp=r&sig=2ww2byn5AfqRajf3MATpK1zC5xVh0DPevMHmE9mgP7s%3D)

Before creating payments on behalf of your merchants, you may need to confirm that the necessary payment channels are activated for each sub-account.

### Managed sub-account

Your merchants need to activate each payment channel through their own dashboard. They can activate any payment channel by going to Payment Channel Settings and clicking **Activate** on the respective payment channel.

### Owned sub-account

Owned sub-accounts use most payment methods that are active on the Master account. There are some channels that may not be supported yet, or require the sub-account to complete verification.

## Supported payment methods for Owned sub-accounts

| Symbol | Description |
| --- | --- |
| ✅ | Supported |
| ❌ | Not supported |
| ℹ️ | [Merchant verification](/docs/verify-sub-accounts) required |

| **Payment Methods** | **Indonesia** | **Philippines** | Thailand | Malaysia | Vietnam |
| --- | --- | --- | --- | --- | --- |
| Cards | ❌ | ℹ️ | ℹ️ | ❌ | ❌ |
| Virtual Accounts | ✅ |  |  |  | ✅ |
| Virtual Accounts (ID BCA) | ❌ |  |  |  |  |
| Direct Debit | ✅ | ✅ | ✅ | ✅ | ✅ |
| E-wallets | ✅ | ✅ | ✅ | ✅ | ✅ |
| E-wallets (PH GCash) |  | ℹ️ |  |  |  |
| QR Codes | ✅ | ✅ | ✅ | ✅ | ✅ |
| QR Code (ID Static) | ❌ |  |  |  |  |
| Over-The-Counter | ✅ | ✅ |  | ✅ |  |
| PayLater | ❌ | ❌ | ❌ | ❌ | ❌ |

## Flow & implementation

You or your merchants can use the Dashboard and our APIs to create payments. However Owned sub-accounts cannot create API keys and hence are unable to create their own API requests:

|  | Master Account | Managed Sub-accounts | Owned Sub-accounts |
| --- | --- | --- | --- |
| Create invoices via Dashboard | ✅ | ✅ | ✅ |
| Create payments via API | ✅ | ✅ | ❌ |

With the Master account API key, you can send `Create payments` requests via API on behalf of sub-accounts using a header parameter called `for-user-id`. The following flowcharts are some examples on what the process looks like.

### Payment Links

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/xp-invoice-eng.webp?sv=2022-11-02&spr=https&st=2026-04-23T06%3A06%3A33Z&se=2026-04-23T06%3A18%3A33Z&sr=c&sp=r&sig=2ww2byn5AfqRajf3MATpK1zC5xVh0DPevMHmE9mgP7s%3D)

### Fixed Virtual Accounts

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/xp-fva-eng.webp?sv=2022-11-02&spr=https&st=2026-04-23T06%3A06%3A33Z&se=2026-04-23T06%3A18%3A33Z&sr=c&sp=r&sig=2ww2byn5AfqRajf3MATpK1zC5xVh0DPevMHmE9mgP7s%3D)

## Merchant name displayed to customers

When customers pay, they will see the name of your merchant in various touch points. Whose name gets displayed name depend on the sub-account type as well as the interface that the customer is on.

- For Managed Sub-Accounts, all payment methods will display your merchant’s name, except for channels that allow for customization in the transaction request (Virtual Accounts, Over-The-Counter).
- Since Owned Sub-Accounts are not verified and only has a Xendit business name, the name displayed outside of Xendit interfaces will be the Platform’s registered business or legal name

  - Xendit Invoice: Sub-account business name
  - Payment channel application or web checkout: Master Account’s business name or legal entity name
  - Cards authorization: Master Account’s legal entity name
  - Bank Statements: Master Account’s legal entity name

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/xp-name-displayed_f9eafe.webp?sv=2022-11-02&spr=https&st=2026-04-23T06%3A06%3A33Z&se=2026-04-23T06%3A18%3A33Z&sr=c&sp=r&sig=2ww2byn5AfqRajf3MATpK1zC5xVh0DPevMHmE9mgP7s%3D)

## Receiving payment event webhooks

To receive webhooks on events occurring on your merchant’s accounts, you may need to set relevant webhook URLs on the sub-account depending on its type. For example, to receive Payment Status webhook for your merchant, you have to make sure that your merchant’s sub-account has already been set for Payment Status webhook URL.

### Owned sub-accounts

Once the master account has set a webhook URL, all Owned sub-accounts will use the same webhook URL automatically. For example:

- The Master Account has set an Payment Status webhook URL.
- When a sub-account’s payment is paid by a customer, the webhook will be sent to the same webhook URL set on the Master Account.

### Managed sub-accounts

There are two methods to set webhook URLs for Managed sub-accounts:

- Your merchants can log in and set their own webhook URL by navigating to Webhook Settings
- The Master Account can request [Set webhook URL](https://docs.xendit.co/apidocs/set-webhook-url) via API, and provide the sub-account’s ID in the `for-user-id` header
