---
url: https://docs.xendit.co/docs/google-pay
title: Google Pay
description: ''
section: docs
scraped_at: '2026-04-23T06:18:16.429120Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsSupported payment channels
- Documentation
- Accept payments
- Supported payment channels
---
# Google Pay

Google Pay™ allows customers to pay using cards and other supported payment methods stored in their Google Wallet across Android devices and supported web browsers.

When integrating Google Pay with Xendit, you can accept securely tokenized payment credentials while reducing checkout friction and improve conversion

Google Pay is **not a payment channel**, rather it facilitates transactions using another underlying channel (e.g. cards). The underlying funding source (for example, `CARDS`, `TOUCHNGO`) determines:

- Capability and channel features
- The recorded payment channel in transactions
- Pricing and processing fees
- Settlement and reporting behavior

If a payment is initiated via Google Pay, Xendit will provide an identifier indicating that the transaction originated from Google Pay.

# Supported use cases

|  |  |
| --- | --- |
| **Country** | Singapore, Phillipines, Malaysia, Thailand, Vietnam, Hongkong |
| **Currencies** | SGD, PHP, MYR, THB, VND, HKD |
| **Supported channels**  *(the transaction will be processed and reported under the selected funding source.)* | - Cards |
| **Supported use cases** | - One time payment - Recurring |

## Supported integration

Google Pay is supported in [**Payment Session** integrations](/v1/docs/how-payment-sessions-work), including:

- [**Xendit-hosted page (Payment Link mode)**](/v1/docs/payment-1)
- [**Xendit Components (embedded mode)**](/v1/docs/components-overview)

Google Pay will be available in a Payment Session when:

- The Session country supports Google Pay.
- At least one Google Pay–compatible funding source (e.g., Cards) is available.
- A valid Google Merchant ID has been provided in the Xendit Dashboard (required for Xendit Components integration).

Payment Links

Xendit Components

Google Pay is supported by **default** in Payment Session when using the Xendit-hosted page (Payment Link mode). The Google Pay button will automatically appear when the customer’s device and browser support Google Pay and the underlying funding source is activated on your account.

> You do **not** need to provide your own Google Merchant ID when using the Xendit-hosted page integration.

## How to integrate

1. You create a Payment Session via API.
2. The customer opens the Xendit-hosted payment page.
3. If the customer’s environment supports Google Pay, the button appears automatically.
4. The customer selects Google Pay, confirms the payment, and completes authentication.
5. The payment is processed using the selected funding source.

No additional frontend implementation is required.

To integrate Payment Links, see the documentation for our [Payment Session API](/v1/docs/how-payment-sessions-work).

Google Pay is supported in **Xendit Components** as a Digital Wallet within Payment Session. It can be rendered automatically in the Channel Picker or manually as a standalone button.

## Prerequisites

To integrate Google Pay using Xendit Components, you must:

- Have Google Pay enabled on your Xendit account
- Provide your own **Google Merchant ID** in the Xendit Dashboard
- Ensure at least one Google Pay–compatible funding source (for example, Cards) is available in the Session
- Use a Session country where Google Pay is supported

If you do not have a Google Merchant ID, register in the Google Pay & Wallet Console to obtain one before enabling Google Pay™ in Xendit.

## Compliance requirements

To use Google Pay, you must comply with Google’s policies and terms:

- Accept and follow the [**Google Pay & Wallet API Acceptable Use Policy**](https://payments.developers.google.com/terms/aup)
- Accept the [**Google Pay API Terms of Service**](https://payments.developers.google.com/terms/sellertos)
- Follow the official [**Google Pay™ brand guidelines**](https://developers.google.com/pay/api/web/guides/brand-guidelines)

Failure to comply with these requirements may result in Google Pay™ being disabled for your integration.

## How to integrate

1. Follow Xendit Components implementation guideline [here](/v1/docs/components-overview)
2. Load the Google Pay SDK. You must load the Google Pay JavaScript SDK on your website:

JavaScript

```
<script async src="https://pay.google.com/gp/p/js/pay.js"></script>
```

JavaScript

Copy

The Google Pay SDK is **not bundled** with Xendit Components, you must include it manually. There is no need to wait for the script to finish loading. If the SDK is still loading when the component is created, the Google Pay button will render with `display: none` until it becomes available.

3. Rendering Google Pay. There are 2 options:

   3. Automatic rendering (Channel Picker)

      If Google Pay is available for the Session, the Google Pay button will automatically appear at the top of the Channel Picker.
   4. Manual rendering

      You may manually render a Google Pay button:

JavaScript

```
createDigitalWalletComponent("GOOGLE_PAY")
```

JavaScript

Copy

Currently, Google Pay is the only supported digital wallet in Xendit Components.

When a customer completes payment using Google Pay:

- The submission flow begins automatically.
- The behavior is the same as calling `submit()` on the component.

## Liability shifts

Liability shift behavior for Google Pay depends on the **underlying funding source** used in the transaction. Google Pay itself does not independently determine [liability shift](/v1/docs/cards-authentication-3ds2#liability-shift). The rules are governed by the underlying payment rail (e.g., Cards, Touch ‘n Go, ShopeePay).

### Card Transactions (DPAN vs FPAN)

There are three main Google Pay card scenarios:

**1. Device Token (DPAN)**

If a customer adds a card to the Google Pay app on their mobile device, the card is stored as a **Device Primary Account Number (DPAN)**. Transactions considered strongly authenticated which typically does not require additional 3D Secure and have the liability as default

**2. Browser-Saved Card (FPAN)**

If a customer adds a card to Chrome or another Google property, it may be stored as a **Funding Primary Account Number (FPAN)**. Transactions will be treated similarly to a standard card-not-present transaction where 3D Secure is recommended to qualify for liability shift. Without 3D Secure, liability shift is generally not guaranteed.

### Alternative Payment Methods (APMs)

When Google Pay is used with alternative payment methods such as Touch ‘n Go, ShopeePay, etc. The liability and dispute handling rules follow the respective provider’s policies.

In most cases, wallet-based rails operate under their own authorization and dispute models rather than traditional card chargeback rules.

## **Refunds**

You can partially or fully refund any successful Google Pay payment. The refund process is the same as that for underlying rails payments. See our refund documentation to perform a refund.
