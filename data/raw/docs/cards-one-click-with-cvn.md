---
url: https://docs.xendit.co/docs/cards-one-click-with-cvn
title: One-click payment with CVN
description: ''
section: docs
scraped_at: '2026-04-23T06:19:46.605845Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guideCard Payments via APIUse case integration
  guides
- Documentation
- Accept payments
- Integration guide
- Card Payments via API
- Use case integration guides
---
# One-click payment with CVN

Including the **Card Verification Number (CVN)** is crucial for successful card transactions. While often optional, providing the CVN significantly improves approval rates, especially for European cards which commonly decline without it. To facilitate secure, one-click payments, you can enable end-users to reuse their stored card details while still requiring CVN and authentication for every transaction.

## One-click payment flow

[Once a card is stored](/v1/docs/store-a-card-for-one-click), you can use the **payment\_token\_id** for future payments. For added security, your customers may be required to re-enter their CVN during one-click payments, ensuring compliance and reducing fraud risk.

![](https://cdn.document360.io/217abc43-8677-41fb-a81d-fceeb1fa0358/Images/Documentation/Untitled diagram-2025-01-02-151639.png?sv=2022-11-02&spr=https&st=2026-04-23T06%3A19%3A43Z&se=2026-04-23T06%3A33%3A43Z&sr=c&sp=r&sig=Uu4rCvPAq7oFeFWbCVKDELtY1I5ZeswBzFTcuqfaZzs%3D)

## How to Implement

1. **Create a payment session**

   Initiate a payment session by sending a POST request to the `/sessions` endpoint. This request should include the `card_payment_token_id` of the stored card.

   Request - POST /sessions

   ```
   {
       "reference_id": "YOUR_PAYMENT_REFERENCE_ID",
       "session_type": "PAY",
       "mode": "CARDS_SESSION_JS",
       "amount": 100000,
       "currency": "IDR",
       "country": "ID",
       "customer": {
           "reference_id": "YOUR_CUSTOMER_REFERENCE",
           "type": "INDIVIDUAL",
           "email": "test@yourdomain.com",
           "mobile_number": "+6212345678",
           "individual_detail": {
               "given_names": "Jaap",
               "surname": "Stam"
           }
       },
       "cards_session_js": {
           "card_payment_token_id":"pt-a15a6c28-c65a-4ede-a6cc-10ff3b1d093e",
           "success_return_url": "https://yourcompany.com/success",
           "failure_return_url": "https://yourcompany.com/failure"
       }
   }
   ```

   JSON

   Copy

   Response - POST /sessions

   ```
   {
       "payment_session_id": "ps-6746c1006b7752b4d91725af",
       "created": "2024-11-27T06:49:36.535Z",
       "updated": "2024-11-27T06:49:36.535Z",
       "status": "ACTIVE",
       "reference_id": "YOUR_PAYMENT_REFERENCE_ID",
       "currency": "IDR",
       "amount": 10000,
       "country": "ID",
       "customer_id": "XENDIT_GENERATED_CUSTOMER_ID",
       "expires_at": "2024-11-27T07:19:36.434Z",
       "session_type": "PAY",
       "mode": "CARDS_SESSION_JS",
       "locale": "en",
       "business_id": "YOUR_BUSINESS_ID",
       "cards_session_js": {
           "card_payment_token_id":"pt-a15a6c28-c65a-4ede-a6cc-10ff3b1d093e",
           "success_return_url": "https://yourcompany.com/success",
           "failure_return_url": "https://yourcompany.com/failure"
       }
   }
   ```

   JSON

   Copy

2. **Collect the CVN**

Implement [card\_session.js](https://js.xendit.co/cards-session.min.js) in the head element of your payment page

```
<head>
     <script type="text/javascript" src="https://js.xendit.co/cards-session.min.js">
</head>
```

HTML, XML

Copy

Then, collect the CVN information

```
<head>
    <script type="text/javascript" src="https://js.xendit.co/cards-session.min.js">
</head>

<body>
    <div class="credit-card-form">
        <form id="credit-card-form">
            <div class="form-group">
                <label for="cvn">CVN</label>
                <input type="text" id="cvn" name="cvn" placeholder="123" />
            </div>
        </form>
    </div>
    <script type="text/javascript">

    </script>
</body>
```

HTML, XML

Copy

Request - to card\_session\_js

```
{
    "cvn": "123",
    "payment_session_id": "YOUR_PAYMENT_SESSION_ID"
}
```

JSON

Copy

Response - from card\_session\_js

```
{
    "message": "Status updated. Wait for a callback or get the status using the Get API.",
    "payment_request_id": "PAYMENT_REQUEST_ID",
    "action_url": "AUTHENTICATION_PAGE_URL"
}
```

JSON

Copy

**Important:** **Store the** `payment_request_id` as it is crucial for tracking the transaction status and will be included in the payment webhook.

**3. Redirect to the authentication page**

Redirect your customer to the [authentication page](/docs/authentication-3ds2) provided by the `action_url` from the response object. This is where the cardholder completes the 3D Secure authentication.

**4. Customer completes authentication**

After successfully authenticating, your customer will be redirected to your `success_return_url`. If authentication fails, they will be redirected to your `cancel_return_url`.

**5. Receive the webhook**

Xendit will send a payment [webhook](/docs/payments-api-webhooks) to your configured webhook endpoint, indicating the final status of the transaction. You can match this webhook with the `payment_request_id` you stored earlier.

Example `payment.capture` webhook

```
{
    "created": "2024-12-18T05:46:35.109Z",
    "business_id": "62440e322008e87fb29c1fd0",
    "event": "payment.capture",
    "data": {
        "type": "PAY",
        "status": "SUCCEEDED",
        "country": "ID",
        "created": "2024-12-18T05:46:08.192Z",
        "updated": "2024-12-18T05:46:30.627Z",
        "captures": [
            {
                "capture_id": "cptr-08f17fa3-e80c-4d8e-8c34-17aa3400bc1c",
                "capture_amount": 10000,
                "capture_timestamp": "2024-12-18T05:46:34.234Z"
            }
        ],
        "currency": "IDR",
        "payment_id": "py-3f57d678-2448-4c9f-a433-8468d366fb5c",
        "business_id": "62440e322008e87fb29c1fd0",
        "customer_id": "cust-7de9a9b4-37e8-40ad-b665-d97f42e538c5",
        "channel_code": "CARDS",
        "reference_id": "97ba0a32-b996-4abf-8a7b-6184a6644676_b8d18f2f-3",
        "capture_method": "AUTOMATIC",
        "request_amount": 10000,
        "payment_details": {
            "authorization_data": {
                "reconciliation_id": "7345007929096981703954",
                "authorization_code": "831000",
                "acquirer_merchant_id": "xendit_ctv_agg",
                "network_response_code": "00",
                "network_transaction_id": "016153570198200",
                "cvn_verification_result": "M",
                "retrieval_reference_number": "435205253972",
                "address_verification_result": "M",
                "network_response_code_descriptor": "Approved and completed sucessfully"
            },
            "authentication_data": {
                "flow": "CHALLENGE",
                "a_res": {
                    "eci": "05",
                    "message_version": "2.1.0",
                    "authentication_value": "AAIBBYNoEwAAACcKhAJkdQAAAAA=","directory_server_trans_id": "e537f539-d59f-4ebe-8d56-7fdc31a8e9b4"
                }
            }
        },
        "payment_request_id": "pr-5593127f-8c7b-4d2f-b487-c785ffc21e2f"
    },
    "api_version": "v3"
}
```

JSON

Copy

It's recommended to save the`payment_id`and`payment_details` from the webhook, correlated with the `payment_request_id`, as proof of payment.\

### **Example implementation**

For a practical demonstration of collecting CVN using `card_session.js` on your frontend, refer to our example page:

🔗 [card\_session.js example to collect CVN](https://js.xendit.co/test_collect_cvn.html)
