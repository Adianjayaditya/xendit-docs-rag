---
url: https://docs.xendit.co/docs/payment-1
title: One Time Payment
description: ''
section: docs
scraped_at: '2026-04-23T06:20:27.853998Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guidePayment SessionsPayment Link
- Documentation
- Accept payments
- Integration guide
- Payment Sessions
- Payment Link
---
# One Time Payment

Payment Sessions allow you to securely collect a payment from your customer during checkout. This feature ensures regulatory compliance and provides a smooth, hosted payment experience through Xendit’s checkout page. It’s a common flow to accept one-time payments with a simple integration.

**Example usage:**

- eCommerce checkout: Collect immediate payment from customers when placing an order.
- Service booking: Confirm a reservation only after successful payment.

## **How to integrate**

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/image(145).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A20%3A24Z&se=2026-04-23T06%3A31%3A24Z&sr=c&sp=r&sig=qb3dgQ4UUgdH%2B1o6CrYA2oVO2eM7WNx%2FfdDCDB8W4i4%3D)

1. During checkout or whenever your customer is ready to make a one-time purchase, your system should **Create a Payment Session** with Xendit using the example payload provided below.

**Request - POST /sessions**

JSON

```
{
    "reference_id": "{{$YOUR_REFERENCE_ID}}",
    "session_type": "PAY",
    "mode": "PAYMENT_LINK",
    "amount": 150000,
    "currency": "IDR",
    "country": "ID",
    "customer": {
        "reference_id": "{{$randomUUID}}",
        "type": "INDIVIDUAL",
        "email": "customer@yourdomain.com",
        "mobile_number": "+628123456789",
        "individual_detail": {
            "given_names": "John",
            "surname": "Doe"
        }
    },
    "success_return_url": "https://yourcompany.com/order/complete",
    "cancel_return_url": "https://yourcompany.com/order/cancel"
}
```

JSON

Copy

**Response - POST /sessions**

JSON

```
{
    "payment_session_id": "ps-67527107dda8b2513acdaef0",
    "created": "2024-12-06T03:35:36.032Z",
    "updated": "2024-12-06T03:35:36.032Z",
    "status": "ACTIVE",
    "reference_id": "b767f88f-b5bc-4836-9c47-c14261909dec",
    "currency": "IDR",
    "amount": 150000,
    "country": "ID",
    "customer_id": "cust-fe8743c3-f554-4d25-a0e9-9980226c4b1b",
    "expires_at": "2024-12-06T04:05:35.049Z",
    "session_type": "PAY",
    "mode": "PAYMENT_LINK",
    "locale": "en",
    "business_id": "62440e322008e87fb29c1fd0",
    "success_return_url": "https://yourcompany.com/order/complete",
    "cancel_return_url": "https://yourcompany.com/order/cancel",
    "payment_link_url": "https://dev.xen.to/qZx5RD_7"
}
```

JSON

Copy

2. Once the Payment Session is created, redirect your end user to the **Xendit-hosted checkout page** using the `payment_link_url` from the response.
3. Your customer will complete the payment on the Xendit-hosted page using their preferred payment channel (e.g., cards, eWallets, bank transfer, QR, etc.).
4. Upon successful payment, Xendit will send a `payment_session.completed` webhook to your system. You should use these webhooks to update the order status in your system. **Optionally** you can also handle webhook of `payment.capture` to see the payment details. Both webhook has the correlation of `payment_id`.
