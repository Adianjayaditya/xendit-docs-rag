---
url: https://docs.xendit.co/docs/reusable-payment-codes
title: Reusable payment codes
description: ''
section: docs
scraped_at: '2026-04-23T06:23:40.016293Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guidePayments via API
- Documentation
- Accept payments
- Integration guide
- Payments via API
---
# Reusable payment codes

Depending on the payment use case, you might opt to use reusable payment codes to collect multiple instances of payments. This could be the case where a virtual bank account number is tied to a single user’s account for multiple payments or a case where a single QR code is displayed in-store for multiple users to make multiple individual payments.

In this article, we will walk through a basic integration with our payments API for our guest checkout under the `REUSABLE_PAYMENT_CODE` flow type of `/payment_requests`. Before you start, be sure to complete your integration environment set up.

## Integration Flow

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/reusable payment code.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A23%3A35Z&se=2026-04-23T06%3A36%3A35Z&sr=c&sp=r&sig=ZWVzhE0dRsP1D6Og9EKz41g0Tc56dBdNPrBsgykXmjU%3D)

## How to integrate

1. **Create a page for users to retrieve payment code**

   On your application, prepare a page where the end user can obtain information on the reusable payment code. It is recommended that you include payment instructions alongside the payment code to reduce payment errors.

   If you are planning to use the payment code in-store, you can print out the payment code value for in-store display as well.\
2. **Create a payment request** \
   When the user enters the page to attempt payment, construct an [API request body](https://xendit-docs.document360.io/apidocs/create-payment-request) for `REUSABLE_PAYMENT_CODE` with information required by your selected channel. In this scenario, your payment request `type` should be `REUSABLE_PAYMENT_CODE`.\

   Request - POST /payment\_requests

   Code snippet

   ```
   {
     "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
     "type": "REUSABLE_PAYMENT_CODE",
     "country": "ID",
     "currency": "IDR",
     "request_amount": 10000.01,
     "channel_code": "BRI_VIRTUAL_ACCOUNT",
     "channel_properties": {
       "expires_at": "2024-12-31T23:59:59Z"
     },
     "description": "Description examples",
     "metadata": {
       "metametadata": "metametametadata"
     }
   }
   ```

   JSON

   Copy

   Response - POST /payment\_request

   Code snippet

   ```
   {
     "business_id": "5f27a14a9bf05c73dd040bc8",
     "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
     "payment_request_id": "pr-90392f42-d98a-49ef-a7f3-abcezas123",
     "type": "REUSABLE_PAYMENT_CODE",
     "country": "ID",
     "currency": "IDR",
     "request_amount": 10000.01,
     "capture_method": "AUTOMATIC",
     "channel_code": "BRI_VIRTUAL_ACCOUNT",
     "channel_properties": {
       "expires_at": "2024-12-31T23:59:59Z"
     },
     "actions": [
       {
         "type": "PRESENT_TO_CUSTOMER",
         "descriptor": "VIRTUAL_ACCOUNT_NUMBER",
         "value": "1251255"
       }
     ],
     "status": "ACCEPTING_PAYMENTS",
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
   Additional features can be configured if the payment channel allows it. For example, you will be able to set custom payment request expiry time if the channel properties fields accepts an expires\_at parameter. \
3. **Handle the required actions**

   Upon successful creation of a payment request with Xendit, you will receive our payment request object. If the payment request status is `REQUIRES_ACTION`, you will need to perform some actions on the client app for the end user to complete payment. If no actions are required, the final payment status will be returned synchronously and a webhook with payment status update will be sent.\

   1. **Present to customer**

      1. Action "type": "PRESENT\_TO\_CUSTOMER"
      2. On the client app, display the action’s value to the user. If it is a QR string, you might need to render it into a scannable QR code. To maximise payment success rates, you should include some payment instructions alongside the displayed values. \
4. **Receive a payment event webhook for payment confirmation**\
   Once the end user has completed their payment authentication step and the payment method provider notifies Xendit of an update, Xendit will proceed to send a webhook to the webhook url you configured in your Xendit dashboard settings page.

   Code snippet

   ```
   {
       "created": "2025-02-09T06:50:19.852Z",
       "business_id": "62440e322008e87fb29c1fd0",
       "event": "payment.capture",
       "data": {
           "type": "REUSABLE_PAYMENT_CODE",
           "status": "SUCCEEDED",
           "country": "ID",
           "created": "2025-02-09T06:50:18.000Z",
           "updated": "2025-02-09T06:50:18.000Z",
           "captures": [
               {
                   "capture_id": "cptr-fa2abf5c-b5e4-4cd5-95df-f2c949eba332",
                   "capture_amount": 10000,
                   "capture_timestamp": "2025-02-09T06:50:18.927Z"
               }
           ],
           "currency": "IDR",
           "payment_id": "py-4e0209e9-67a2-449a-9748-57df6a8bddad",
           "business_id": "62440e322008e87fb29c1fd0",
           "channel_code": "BNI_VIRTUAL_ACCOUNT",
           "reference_id": "test-1739083782",
           "capture_method": "AUTOMATIC",
           "request_amount": 10000,
           "payment_details": {},
           "payment_request_id": "pr-4f978be5-0e6a-4218-a281-155b362a9ffb"
       },
       "api_version": "v3"
   }
   ```

   JSON

   Copy
5. **Display payment status to user**

   For reusable payment codes, it is important to provide up-to-date information on payments for your users. To do so, your system should be designed to expect many payment web hooks coming in for a single reusable payment code and expect that these web hooks can happen any time. Often, merchants will prepare a page that can show the full list of payments recognized by the reusable payment code.

## Payment Lifecycle

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Payment API v3-Reusable payment code.drawio (1).png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A23%3A35Z&se=2026-04-23T06%3A36%3A35Z&sr=c&sp=r&sig=ZWVzhE0dRsP1D6Og9EKz41g0Tc56dBdNPrBsgykXmjU%3D)

Here’s the **status lifecycle** for a payment request for reusable payment code flow:

| **Status** | **Description** | **Webhook Event** |
| --- | --- | --- |
| **ACCEPTING\_PAYMENTS** | The payment request enters this status synchronously upon API response, indicating it is ready to accept multiple payments using the generated payment code. Each successful payment from an end user triggers a **payment.capture** webhook sent to your configured URL. | - **payment.capture** |
| **CANCELED** | You can manually cancel the payment request if you no longer wish to accept payments using the payment code. Triggering the cancel endpoint transitions the payment request to **CANCELED** status synchronously. | - |
| **EXPIRED** | The payment request transitions to this status when it reaches the expiry date specified in the request. | - |

---

####
