---
url: https://docs.xendit.co/docs/pay-with-tokens
title: Pay with tokens
description: ''
section: docs
scraped_at: '2026-04-23T06:18:35.310419Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guidePayments via API
- Documentation
- Accept payments
- Integration guide
- Payments via API
---
# Pay with tokens

With a previously saved payment token, you can create a payment request that requires less authentication actions from your user.

In this article, we will walk through a basic integration with our payments API for payments using a previously saved payment token under the `PAY` flow type of `/payment_requests`. Before you start, be sure to complete your integration environment set up.

## Integration Flow

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/pay w token.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A18%3A31Z&se=2026-04-23T06%3A32%3A31Z&sr=c&sp=r&sig=o7ZfIYBd2x6BWlmTP4PLHLMLfCcsdJeHqDz7D%2BbPODQ%3D)

## How to integrate

1. **Create a checkout page**

   On your application, prepare a checkout flow to facilitate payment steps that the end user will go through. For the first step, create a checkout page where payment channels are displayed. Since you have an existing payment token, it is advisable to highlight that to the end user or even display information such as balance (available for certain payment channels).\
2. **Collect required data for the chosen payment channel** \
   Once the end user picks a channel, collect the data required to initiate a payment with the payment method provider.\
3. **Create a payment request** \
   Construct an [API request body](https://xendit-docs.document360.io/apidocs/create-payment-request) for `PAY` with token and with information required by your selected channel. In this payment flow, you do not need to pass in `channel_code` or `customer_id` since they are already saved in the token.\

   Request - POST /payment\_requests

   Code snippet

   ```
   {
     "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
     "payment_token_id": "pt-90392f42-d98a-49ef-a7f3-abcezas123",
     "type": "PAY",
     "country": "TH",
     "currency": "THB",
     "request_amount": 10000.01,
     "capture_method": "AUTOMATIC",
     "channel_properties": {
       "mid_label": "mid_label_acquirer_1",
       "skip_three_ds": false,
       "card_on_file_type": "CUSTOMER_UNSCHEDULED",
       "failure_return_url": "https://xendit.co/failure",
       "success_return_url": "https://xendit.co/success",
       "statement_descriptor": "Goods & Services"
     },
     "description": "Description examples",
     "metadata": {
       "metametadata": "metametametadata"
     }
   }
   ```

   JSON

   Copy

   Response - POST /payment\_requests

   Code snippet

   ```
   {
     "business_id": "5f27a14a9bf05c73dd040bc8",
     "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
     "payment_token_id": "pt-90392f42-d98a-49ef-a7f3-abcezas123",
     "payment_request_id": "pr-90392f42-d98a-49ef-a7f3-abcezas123",
     "customer_id": "cust-90392f42-d98a-49ef-a7f3-abcezas123",
     "type": "PAY",
     "country": "TH",
     "currency": "THB",
     "channel_code": "CARDS",
     "request_amount": 10000.01,
     "capture_method": "AUTOMATIC",
     "channel_properties": {
       "mid_label": "mid_label_acquirer_1",
       "skip_three_ds": false,
       "card_on_file_type": "CUSTOMER_UNSCHEDULED",
       "failure_return_url": "https://xendit.co/failure",
       "success_return_url": "https://xendit.co/success",
       "statement_descriptor": "Goods & Services"
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
   Additional features can be configured if the payment channel allows it. For example, you will be able to set statement descriptions if the channel properties fields accepts a `statement_descriptor` parameter. \
4. **Handle the required actions**

   Upon successful creation of a payment request with Xendit, you will receive our payment request object. If the payment request status is `REQUIRES_ACTION`, you will need to perform some actions on the client app for the end user to complete payment. If no actions are required, the final payment status will be returned synchronously and a webhook with payment status update will be sent.\

   1. **Redirection**

      1. Action "type": "REDIRECT\_CUSTOMER"
      2. On the client app, redirect the user to the url in action’s value. To maximise payment success rates, you should handle the redirection based on the user’s device type. Note that for certain payment channels, there are redirections rules for pending or cancellation. Your application should be designed to handle such scenarios.\
5. **Receive a payment event webhook for payment confirmation**\
   Once the end user has completed their payment authentication step and the payment method provider notifies Xendit of an update, Xendit will proceed to send a webhook to the webhook url you configured in your Xendit dashboard settings page.\

   Code snippet

   ```
   {
     "event": "payment.capture",
     "business_id": "5f27a14a9bf05c73dd040bc8",
     "created": "2021-12-02T14:52:21.566Z",
     "data": {
       "payment_id": "py-1402feb0-bb79-47ae-9d1e-e69394d3949c",
       "business_id": "5f27a14a9bf05c73dd040bc8",
       "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
       "payment_request_id": "pr-1102feb0-bb79-47ae-9d1e-e69394d3949c",
       "payment_token_id": "pt-cc3938dc-c2a5-43c4-89d7-7570793348c2",
       "customer_id": "cust-b98d6f63-d240-44ec-9bd5-aa42954c4f48",
       "type": "PAY_AND_SAVE",
       "country": "PH",
       "currency": "PHP",
       "request_amount": 10000.01,
       "capture_method": "AUTOMATIC",
       "channel_code": "PAYMAYA",
       "channel_properties": {
         "success_return_url": "https://xendit.co/success",
         "failure_return_url": "https://xendit.co/failure"
       },
       "captures": [
         {
           "capture_timestamp": "2029-12-31T23:59:59Z",
           "capture_id": "cap-1502feb0-bb79-47ae-9d1e-e69394d3949c",
           "capture_amount": 10000.01
         }
       ],
       "status": "SUCCEEDED",
       "payment_details": {
         "remark": "example remark"
       },
       "metadata": {
         "metametadata": "metametametadata"
       },
       "created": "2029-12-31T23:59:59Z",
       "updated": "2029-12-31T23:59:59Z"
     }
   }
   ```

   JSON

   Copy

   \
6. **Display payment status to user**

   With the webhook status, you should be able to complete the payment journey for the end user by successfully completing the transaction or directing them back for a retry if it had failed. \
   \
   In all real-time messaging systems, there is a chance that the webhook does not reach your system. Your application should also cater for the scenario where a webhook is not received while the end user is still waiting on their screen. In such cases, it is recommended for a pending payment notice to be given to the end user while you wait for a webhook from Xendit.

## Status Lifecycle

#### User action required

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Payment API v3-PR w PT.drawio.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A18%3A31Z&se=2026-04-23T06%3A32%3A31Z&sr=c&sp=r&sig=o7ZfIYBd2x6BWlmTP4PLHLMLfCcsdJeHqDz7D%2BbPODQ%3D)

Here’s the **status lifecycle** for a payment request that requires user action:

| **Status** | **Description** | **Webhook Event** |
| --- | --- | --- |
| **REQUIRES\_ACTION** | The payment request enters this status synchronously upon API response if user action is required to complete authorization. Handle the `actions` object in this stage. | - |
| **SUCCEEDED** | The payment request transitions to this status when the payment is successfully completed. Xendit will send the **payment.capture** webhook containing the `payment_request_id` to identify the request. You should store the `payment_id` for payment proof. | **payment.capture** |
| **FAILED** | The payment request transitions to this status when the payment fails. Xendit will send the **payment.failure** webhook containing the `payment_request_id` to identify the request. Check the `failure_code` to determine the next action.    **Note**: Not all payment channels provide notifications for failed payment. | **payment.failure** |
| **CANCELED** | You can cancel a payment request that is in the `REQUIRES_ACTION` status. Canceling immediately transitions the payment request to `CANCELED`, and the end user will no longer be able to complete the `actions`. | - |
| **EXPIRED** | The payment request transitions to this status when it expires due to the payment partner’s expiry. | - |

---

#### No action required

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Payment API v3-PR w PT auto debit.drawio.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A18%3A31Z&se=2026-04-23T06%3A32%3A31Z&sr=c&sp=r&sig=o7ZfIYBd2x6BWlmTP4PLHLMLfCcsdJeHqDz7D%2BbPODQ%3D)

Here’s the **status lifecycle** for a payment request that has no action required:

| **Status** | **Description** | **Webhook Event** |
| --- | --- | --- |
| **SUCCEEDED** | The payment request transitions to this status synchronously when the payment is immediately successful. You will still receive the **payment.capture** webhook containing payment details. | **payment.capture** |
| **FAILED** | The payment request transitions to this status synchronously when the payment is immediately failed. You will still receive the **payment.failure** webhook.    **Note**: Not all payment channels provide notifications for failed payment. | **payment.failure** |
| **PENDING** | The payment request enters this status synchronously upon API response if the payment partner has not yet responded with a payment result. Wait for the payment webhook to arrive at your configured webhook URL. | - |

---
