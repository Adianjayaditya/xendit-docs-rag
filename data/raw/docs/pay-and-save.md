---
url: https://docs.xendit.co/docs/pay-and-save
title: Pay and save
description: ''
section: docs
scraped_at: '2026-04-23T06:18:31.510185Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guidePayments via API
- Documentation
- Accept payments
- Integration guide
- Payments via API
---
# Pay and save

Making a payment and saving the end user’s payment information at the same time is a simplified bundled flow we term as “Pay and Save”. This flow features collecting payment and saving payment information in one API call. This flow is often used by merchants with high number of repeat users and with strong brand trust for users to agree to saving their payment information.

In this article, we will walk through a basic integration with our payments API for paying and saving payment information under the `PAY_AND_SAVE` flow type of `/payment_requests`. Before you start, be sure to complete your integration environment setup.

## Integration Flow

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/payandsave_1.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A18%3A28Z&se=2026-04-23T06%3A33%3A28Z&sr=c&sp=r&sig=u4oPcuIGgtrIUr%2B%2BTj2Q8C1oPr%2Fmbo8Wbu2Rfn1UUhs%3D)

## How to integrate

1. **Create a checkout page**

   On your application, prepare a checkout flow to facilitate payment steps that the end user will go through. For the first step, create a checkout page where payment channels are displayed. The end user will pick their desired payment channel here. In the pay and save flow, it is also recommended for you to collect an end user agreement for your business to save their payment information.\
2. **Collect required data for the chosen payment channel** \
   Once the end user picks a channel, collect the data required to initiate a payment with the payment method provider.\
3. **Create a payment request** \
   Construct an [API request body](https://xendit-docs.document360.io/apidocs/create-payment-request) for `PAY_AND_SAVE` with information required by your selected channel. In this payment flow, you would also need to pass in either a `customer_id` or a customer object as an identifier for the end user.\

   Request - POST /payment\_requests

   Code snippet

   ```
   {
     "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
     "customer": {
       "reference_id": "demo_1475801962607",
       "type": "INDIVIDUAL",
       "individual_detail": {
         "given_names": "John",
         "surname": "Doe"
       },
       "email": "example@xendit.co",
       "mobile_number": "+628000000000008"
     },
     "type": "PAY_AND_SAVE",
     "country": "PH",
     "currency": "PHP",
     "request_amount": 10000.01,
     "capture_method": "AUTOMATIC",
     "channel_code": "MAYA",
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

   Response - POST /payment\_requests

   Code snippet

   ```
   {
     "business_id": "5f27a14a9bf05c73dd040bc8",
     "reference_id": "90392f42-d98a-49ef-a7f3-abcezas123",
     "payment_request_id": "pr-90392f42-d98a-49ef-a7f3-abcezas123",
     "customer_id": "cust-90392f42-d98a-49ef-a7f3-abcezas123",
     "type": "PAY_AND_SAVE",
     "country": "PH",
     "currency": "PHP",
     "request_amount": 10000.01,
     "capture_method": "AUTOMATIC",
     "channel_code": "MAYA",
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
   Additional features can be configured if the payment channel allows it. For example, you will be able to set statement descriptions if the channel properties fields accepts an statement\_descriptor parameter. \
4. **Handle the required actions**

   Upon successful creation of a payment request with Xendit, you will receive our payment request object. If the payment request status is `REQUIRES_ACTION`, you will need to perform some actions on the client app for the end user to complete payment. If no actions are required, the final payment status will be returned synchronously and a webhook with payment status update will be sent.\

   1. **Redirection**

      1. Action "type": "REDIRECT\_CUSTOMER"
      2. On the client app, redirect the user to the url in action’s value. To maximise payment success rates, you should handle the redirection based on the user’s device type. Note that for certain payment channels, there are redirections rules for pending or cancellation. Your application should be designed to handle such scenarios.\
5. **Receive a payment event webhook for payment confirmation**\
   Once the end user has completed their payment authentication step and the payment method provider notifies Xendit of an update, Xendit will proceed to send a webhook to the webhook url you configured in your Xendit dashboard settings page.\
   \
   In `PAY_AND_SAVE` flow, a `payment_token_id` will be included in the webhook payment if the payment was successfully collected.\

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
6. **Save the payment token for future use**

   In your system, save the `payment_token_id` to the associated user. For future payments, you can pass the  `payment_token_id` into payment requests for a more frictionless payment.\
7. **Display payment status to user**

   With the webhook status, you should be able to complete the payment journey for the end user by successfully completing the transaction or directing them back for a retry if it had failed. \
   \
   In all real time messaging systems, there is a chance that the webhook does not reach your system. Your application should also cater for the scenario where a webhook is not received while the end user is still waiting on their screen. In such cases, it is recommended for a pending payment notice to be given to the end user while you wait for a webhook from Xendit.

## Status Lifecycle

#### User action required

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Untitled Diagram-PAY AND SAVE.drawio.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A18%3A28Z&se=2026-04-23T06%3A33%3A28Z&sr=c&sp=r&sig=u4oPcuIGgtrIUr%2B%2BTj2Q8C1oPr%2Fmbo8Wbu2Rfn1UUhs%3D)

Here’s the **status lifecycle** for a payment request that requires user action:

| **Status** | **Description** | **Webhook Event** |
| --- | --- | --- |
| **REQUIRES\_ACTION** | The payment request enters this status synchronously upon API response if user action is required to complete authorization. Handle the `actions` object in this stage. | - |
| **SUCCEEDED** | The payment request transitions to this status when the payment is successfully completed. Xendit will send the **payment.capture** webhook as the payment identifier and the **payment\_token.activation** webhook for the payment token created. You should store the `payment_token_id` for use in future transactions. | - **payment.capture** - **payment\_token.activation** |
| **FAILED** | The payment request transitions to this status when the payment fails. Xendit will send the **payment.failure** webhook containing the `payment_request_id` to identify the request. Check the `failure_code` to determine the next action.    **Note**: Not all payment channels provide notifications for failed payment. | - **payment.failure** |
| **CANCELED** | You can cancel a payment request that is in the `REQUIRES_ACTION` status. Canceling immediately transitions the payment request to `CANCELED`, and the end user will no longer be able to complete the `actions`. | - |
| **EXPIRED** | The payment request transitions to this status when it expires due to the payment partner’s expiry. | - |

---

#### No action required

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Untitled Diagram-PAY AND SAVE auto debit.drawio.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A18%3A28Z&se=2026-04-23T06%3A33%3A28Z&sr=c&sp=r&sig=u4oPcuIGgtrIUr%2B%2BTj2Q8C1oPr%2Fmbo8Wbu2Rfn1UUhs%3D)

Here’s the **status lifecycle** for a payment request that has no action required:

| **Status** | **Description** | **Webhook Event** |
| --- | --- | --- |
| **SUCCEEDED** | The payment request transitions to this status synchronously when the payment is immediately successful. You will still receive the **payment.capture** webhook containing payment details and the payment\_token.activation webhook for the payment token created. | - **payment.capture** - **payment\_token.activation** |
| **FAILED** | The payment request transitions to this status synchronously when the payment is immediately failed. You will still receive the **payment.failure** webhook.    **Note**: Not all payment channels provide notifications for failed linking processes. | - **payment.failure** |
| **PENDING** | The payment request enters this status synchronously upon API response if the payment partner has not yet responded with a payment result. Wait for the payment webhook to arrive at your configured webhook URL. | - |

---
