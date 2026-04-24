---
url: https://docs.xendit.co/docs/merchant-initiated-transaction-1
title: Pay without authentication (no 3DS2)
description: ''
section: docs
scraped_at: '2026-04-23T06:29:09.646720Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guideCard Payments via APIFull PAN integration
- Documentation
- Accept payments
- Integration guide
- Card Payments via API
- Full PAN integration
---
# Pay without authentication (no 3DS2)

> Skipping authentication (3DS2) requires additional risk checks due to it’s risky nature.
>
> Xendit recommends to perform authentication (3DS2) when the shopper is present, to prevent potential [chargebacks](/docs/understanding-chargebacks#3d-secure-3ds-transactions).
>
> To enable optional authentication, request **Optional 3DS** on the [Xendit dashboard](https://dashboard.xendit.co/settings/payment-methods/cards-configuration).

Perform a card payment without 3D Secure. Useful for trusted transactions, or transactions on cards for which authentication (3DS2) is not available. You will not be able to detect whether a card supports 3DS2 before attempting to do 3DS2.\
Do take into account that cards from Canada, The United Kingdom and the United States sometimes do not support 3DS2, for these cards we suggest adding billing details to be verified by the [address verification service](/docs/cards-address-verification-service).

Request - POST /v3/payment\_requests

Custom

```
{
  "reference_id": "UNIQUE_REFERENCE_ID",
  "type": "PAY",
  "country": "ID",
  "currency": "IDR",
  "request_amount": 10000,
  "capture_method": "AUTOMATIC",
  "channel_code": "CARDS",
  "channel_properties": {
    "card_details": {
      "card_number": "4000000000001091",
      "cvn": "123",
      "cardholder_first_name": "shopperFirstName",
      "cardholder_last_name": "shopperLastName",
      "cardholder_email": "shopper_email@domain.co",
      "expiry_month": "12",
      "expiry_year": "2029"
    },
    "skip_three_ds": true,
    "failure_return_url": "https://xendit.co/failure",
    "success_return_url": "https://xendit.co/success",
    "statement_descriptor": "Goods"
  },
  "description": "Description examples",
  "metadata": {
    "metametadata": "metametametadata"
  }
}
```

JSON

Copy

Response - POST /v3/payment\_requests

Custom

```
{
    "payment_request_id": "pr-PAYMENT_REQUEST_ID",
    "country": "ID",
    "currency": "IDR",
    "business_id": "YOUR_BUSINESS_ID",
    "reference_id": "UNIQUE_REFERENCE_ID",
    "description": "Description examples",
    "metadata": {
        "metametadata": "metametametadata"
    },
    "created": "2025-07-31T02:56:10.879Z",
    "updated": "2025-07-31T02:56:10.879Z",
    "status": "SUCCEEDED",
    "capture_method": "AUTOMATIC",
    "latest_payment_id": "PAYMENT_ID",
    "channel_code": "CARDS",
    "request_amount": 10000,
    "channel_properties": {
        "success_return_url": "https://xendit.co/success",
        "failure_return_url": "https://xendit.co/failure",
        "skip_three_ds": false,
        "statement_descriptor": "Goods",
        "card_details": {
            "masked_card_number": "400000XXXXXX1091",
            "expiry_month": "12",
            "expiry_year": "2029",
            "fingerprint": "61a443574a7d750020465c79",
            "type": "CREDIT",
            "network": "VISA",
            "country": "ID",
            "issuer": "PT BANK RAKYAT INDONESIA TBK",
            "cardholder_first_name": "shopperFirstName",
            "cardholder_last_name": "shopperLastName",
            "cardholder_email": "shopper_email@domain.co"
        },
        "billing_information": { // Fill these up for Address Verification Service
            "country": "",
            "street_line1": null,
            "street_line2": null,
            "city": null,
            "province_state": null,
            "postal_code": null
        }
    },
    "type": "PAY",
    "actions": []
}
```

JSON

Copy

If you receive the `SKIP_3DS_FORBIDDEN` error, you are not allowed to skip 3DS, request **Optional 3DS** from the [Xendit dashboard](https://dashboard.xendit.co/settings/payment-methods/cards-configuration).

Custom

```
{
    "error_code": "SKIP_3DS_FORBIDDEN",
    "message": "Non 3DS card payment requests is not allowed. Please activate the feature on Xendit dashboard before proceeding"
}
```

JSON

Copy

To retrieve the payment details (detailed error messages, codes and `network_transaction_id`) from the transaction, follow how to retrieve [authorization data](/docs/retrieving-authorization-and-decline-details) for card payments.
