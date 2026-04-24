---
url: https://docs.xendit.co/docs/how-payment-links-work
title: How payment links work
description: ''
section: docs
scraped_at: '2026-04-23T06:23:03.441612Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsPayment productsPayment Links (Legacy)
- Documentation
- Accept payments
- Payment products
- Payment Links (Legacy)
---
# How payment links work

> Use our new [Payment Session features](/v1/docs/how-payment-sessions-work#payment-link) and see our [migration guide page here](/v1/docs/migrate-to-payment-session)

Payment Links offer a simple, no-code solution for businesses to collect payments with ease. Our product enhances the payment experience for your customers, making them ideal for businesses looking for an optimized checkout experience while maintaining a cost-effective integration.

*Actual user interface for reference*

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image(18).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A22%3A59Z&se=2026-04-23T06%3A33%3A59Z&sr=c&sp=r&sig=LSsVM5YoT8sA%2FATAakWrt6TvTSvBTijqCV973aiaVM8%3D "image(18).png")

## Solutions

### No-code solution

Using a simple guided interface on the Xendit Dashboard, you can create payment links without any technical knowledge. Xendit also support delivery of payment links via email and WhatsApp to your customers. Alternatively, you can share these links through any communication channel of your choice.

Follow these steps to create a Payment Link using the Xendit Dashboard:

1. Go to the **Payment Links** page on your dashboard
2. Click **Create Payment Link**
3. Fill in the **payment details**
4. (Optional) Leave the amount blank for donations or multiple payment link
5. (Optional) Configure customer details and notification channels
6. Click **Create Payment Link**
7. **Share the link** with your customers to redirect them to the Xendit-hosted checkout page
8. Monitor payments via email notifications or generate a report for status updates

### API integration

If you have a more complex use case that requires your system to create payment links dynamically, our product is also available via an API-based integration. This integration method allows you to sync up your order management system to our hosted payments collection system. [You can find our detailed integration guides here](/v1/docs/payment-links-api-overview).

#### How it works

#### Endpoints

1. `v2/invoices` - to generate payment links with minimal lines of code.

#### Creating a payment link

Example API request payload:

```
{  "external_id": "payment-link-example",
  "amount": 100000,
  "items": [
    {
      "name": "Air Conditioner",
      "quantity": 1,
      "price": 100000,
      "category": "Electronic",
      "url": "https://yourcompany.com/example_item"
    }
  ]
}
```

JSON

Copy

The API response includes a URL that you can use to redirect your customers to a Xendit-hosted page.

#### Payment confirmation

Subscribe to Payment Link webhooks to receive real-time payment status updates.
