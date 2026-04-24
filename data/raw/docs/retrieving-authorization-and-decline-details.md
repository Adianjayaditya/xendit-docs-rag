---
url: https://docs.xendit.co/docs/retrieving-authorization-and-decline-details
title: How to Retrieve Authorization Data for Card Payments
description: ''
section: docs
scraped_at: '2026-04-23T06:20:14.856761Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guideCard Payments via API
- Documentation
- Accept payments
- Integration guide
- Card Payments via API
---
# How to Retrieve Authorization Data for Card Payments

To retrieve authorization data (e.g., `authorization_code`, `reconciliation_id`, `network_transaction_id`, `merchant_advice_code`) for a card payment made via our v3 APIs, you have **two options**:

---

## Option 1: Use the Webhook (Recommended for Real-Time Updates)

If you've set up webhook notifications, you can get the same data pushed to your server when the payment is captured.

Webhooks can be configured using the [following guide](/docs/payments-api-webhooks).

### Sample Webhook Payload: `payment.capture`

JSON

```
{
  "created": "2025-08-07T02:49:05.587Z",
  "business_id": "YOUR_BUSINESS_ID",
  "event": "payment.capture",
  "api_version": "v3",
  "data": {
    "type": "PAY",
    "status": "SUCCEEDED",
    "country": "ID",
    "created": "2025-08-07T02:49:02.830Z",
    "updated": "2025-08-07T02:49:02.844Z",
    "captures": [
      {
        "capture_id": "cptr-589bd334-99d7-4a4a-8582-57ffd9a1f16b",
        "capture_amount": 115100,
        "capture_timestamp": "2025-08-07T02:49:04.705Z"
      }
    ],
    "currency": "IDR",
    "payment_id": "py-37e924ed-d7eb-4d32-bcb7-111c7863cb22",
    "payment_details": {
      "authorization_data": {
        "reconciliation_id": "7545349437096281603814",
        "authorization_code": "831000",
        "acquirer_merchant_id": "xendit_ctv_agg",
        "network_response_code": "00",
        "network_transaction_id": "016153570198200",
        "retrieval_reference_number": "521802141667",
        "address_verification_result": "M",
        "network_response_code_descriptor": "Approved and completed sucessfully"
      }
    },
    ...
  }
}
```

JSON

Copy

Listen to this webhook and extract `authorization_data` from `payment_details`.\

---

## Option 2: Make Two GET Requests (Polling Method)

Follow these two steps to fetch the authorization details programmatically.

### Step 1: Get the Payment Request Details

Make a `GET` request to:

Plain text

```
GET https://api.xendit.co/v3/payment_requests/{payment_request_id}
```

Plain text

Copy

**Replace** `{payment_request_id}` with your actual Payment Request ID (e.g., `pr-e44b5974-32c9-4e86-a5ee-6b57683247fc`).

**Sample Request:**

Bash

```
curl -X GET https://api.xendit.co/v3/payment_requests/pr-e44b5974-32c9-4e86-a5ee-6b57683247fc \
  -u your-secret-api-key:
```

Bash

Copy

Look for the field:

JSON

```
"latest_payment_id": "py-37e924ed-d7eb-4d32-bcb7-111c7863cb22"
```

JSON

Copy

### Step 2: Get the Payment Details (Including Authorization Data)

Use the `latest_payment_id` from the previous step and make a `GET` request to:

Plain text

```
https://api.xendit.co/v3/payments/{latest_payment_id}
```

Plain text

Copy

**Sample Request:**

Bash

```
curl -X GET https://api.xendit.co/v3/payments/py-37e924ed-d7eb-4d32-bcb7-111c7863cb22 \
  -u your-secret-api-key:
```

Bash

Copy

### Where to find the Authorization Data

In the response, authorization-related fields are located under:

JSON

```
"payment_details": {
  "authorization_data": {
    "authorization_code": "...",
    "reconciliation_id": "...",
    "network_transaction_id": "...",
    ...
  }
}
```

JSON

Copy
