---
url: https://docs.xendit.co/docs/how-payments-api-work
title: How Payments API work
description: ''
section: docs
scraped_at: '2026-04-23T06:22:28.260880Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsPayment productsPayments API
- Documentation
- Accept payments
- Payment products
- Payments API
---
# How Payments API work

Our payments API is designed for our merchants to scale their payments with more channels or more volume while enjoying diminishing development work for every new addition. The integration concepts are designed to be simple and reusable. On average, merchants can expect a quick go to market in weeks for simple use cases while more complex use cases can take up to a month.

## Endpoints

There are 3 integration endpoints that helps to serve our Payments API features:

1. `v3/payment_requests` - to initiate a payment and configure the payment flow
2. `v3/payment_tokens` - to save payment information for reuse
3. `/refunds` - to return money back to the end user

\
You can connect to these endpoints based on your needs. For the majority of payments use cases, we recommend `v3/payment_requests` as it covers a wide coverage of payment scenarios.

## Creating a payment

Creating a payment is as simple as hitting our `v3/payment_requests` endpoint with a few lines of code. [You can find our detailed integration guides here](/v1/docs/payments-via-api-overview).

*Example of a request payload*

Request - POST /payment\_requests

Code snippet

```
{
    "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
    "type": "PAY",
    "country": "PH",
    "currency": "PHP",
    "request_amount": 10000.01,
    "capture_method": "AUTOMATIC",
    "channel_code": "GCASH",
    "channel_properties": {
      "failure_return_url": "https://xendit.co/failure",
      "success_return_url": "https://xendit.co/success"
    },
    "description": "Description examples",
    "metadata": {
      "metametadata": "metametametadata"
    }
  }
```

JSON

Copy

Response - POST /payment requests

Code snippet

```
{
    "business_id": "5f27a14a9bf05c73dd040bc8",
    "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
    "payment_request_id": "pr-90392f42-d98a-49ef-a7f3-abcezas123",
    "type": "PAY",
    "country": "PH",
    "currency": "PHP",
    "request_amount": 10000.01,
    "capture_method": "AUTOMATIC",
    "channel_code": "GCASH",
    "channel_properties": {
      "failure_return_url": "https://xendit.co/failure",
      "success_return_url": "https://xendit.co/success"
    },
    "actions": [
      {
        "type": "REDIRECT_CUSTOMER",
        "value": "xendit.co/example",
        "descriptor": "WEB_URL"
      }
    ],
    "status": "REQUIRES_ACTION",
    "description": "Description examples",
    "metadata": {
      "metametadata": "metametametadata"
    },
    "created": "2021-12-31T23:59:59Z",
    "updated": "2021-12-31T23:59:59Z"
  }
```

JSON

Copy

\

\
Our `v3/payment_requests` endpoint follows REST API standards and covers the ability to collect payments for the following scenarios:

- `PAY` - [collect a regular payment from the end user.](/v1/docs/pay-one-off-payment)
- `PAY` with token - [collect a regular payment from the end user using saved payment information.](/v1/docs/pay-with-tokens)
- `PAY_AND_SAVE` - [collect a regular payment from the end user while saving their payment information as a token for future use.](/v1/docs/pay-and-save)
- `REUSABLE_PAYMENT_CODE` - [collect multiple payments using an allocated payment code for a user or a store.](/v1/docs/reusable-payment-codes) An example could be a static QR code or a fixed bank account number.

Once the endpoint is called to create a payment transaction, our API will dynamically guide your system on the next step to take with the end user.

- *For payments over Card networks (e.g. Visa, Mastercard), there are additional requirements when it comes to integration.* [*You can find the information here*](/v1/docs/cards-api-overview)*.*

## Payment confirmation

Our API provides real-time payment confirmation to keep your system synchronized. When a payment requires no further action from the end-user and is completed, our API instantly notifies your system synchronously on our endpoint and currently sends a webhook notification to your system. For payments requiring end-user action, such as 3D Secure authentication, we’ll send a webhook notification to your system the moment the payment is completed. [You can find our recommendations for handling webhooks here](/v1/docs/handling-webhooks). \
\
We strive for instant payment confirmation and relay the confirmation from the payment provider to you as soon as we receive it. Please note that some payment providers may have delayed confirmation flows, which may impact the immediacy of the notification.
