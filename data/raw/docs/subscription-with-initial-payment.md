---
url: https://docs.xendit.co/docs/subscription-with-initial-payment
title: Subscription with initial payment
description: ''
section: docs
scraped_at: '2026-04-23T06:30:24.479935Z'
source: https://docs.xendit.co
breadcrumbs:
- DocumentationAccept paymentsIntegration guideSubscriptions
- Documentation
- Accept payments
- Integration guide
- Subscriptions
---
# Subscription with initial payment

## Overview

Some business models require a one-time payment at the start of a subscription. Instead of just linking a payment method, the user pays for an initial item or service fee and simultaneously authorizes Xendit to save their payment method for future recurring billings.

This is achieved by using a **Payment Session** with the session type to `PAY_AND_SAVE` followed by the creation of a **Subscription Plan** from the generated payment token from payment session.

### Use Cases

- **ISP / Telecom**: Paying for a router or installation fee upfront, followed by monthly internet service fees.
- **Gym Memberships**: Paying an initial registration/joining fee followed by monthly dues.
- **SaaS with Setup Fees**: Paying for professional services or data migration upfront, then a monthly software subscription.

## How to integrate

The integration follows a two-stage process:

1. Initial Payment: Collect the one-time fee and tokenize the payment method.
2. Plan Creation: Use the authorized token to start the automated subscription schedule.

Example payload:

1. Create the payment session with `"session_type": "PAY"` and `"allow_save_payment_method": "FORCED"` to the payment with saving the payment as mandatory process. The amount created here should follow the upfront payment to the end user

| Request - POST /sessions  Custom  ``` {     "reference_id": "TEST_{{$timestamp}}",     "customer": {         "reference_id": "test-{{$timestamp}}",         "type": "INDIVIDUAL",         "individual_detail": {             "given_names": "TEST"         }     },     "session_type": "PAY",     "allow_save_payment_method": "FORCED", "currency": "IDR", "amount": 20000, "mode": "PAYMENT_LINK", "country": "ID", "locale": "en", "description": "Insurance Plan Registration", "success_return_url": "https://xendit.co/success", "cancel_return_url": "https://xendit.co/failure" } ```   JSON  Copy | Response - POST /sessions  Custom  ``` {     "payment_session_id": "ps-69d6110ada22a3584993eb78",     "created": "2026-04-08T08:25:46.775Z",     "updated": "2026-04-08T08:25:46.775Z",     "status": "ACTIVE",     "reference_id": "TEST_1775636746",     "currency": "IDR",     "amount": 20000,     "country": "ID",     "expires_at": "2026-04-08T08:55:46.413Z",     "session_type": "PAY",     "mode": "PAYMENT_LINK",     "locale": "en",     "business_id": "5f1e60a0abb3a70ffd45e485",     "customer_id": "cust-dad50e22-8d62-4d56-b888-5f66bfdf5627",     "capture_method": "AUTOMATIC",     "description": "Insurance Plan Registration",     "success_return_url": "https://xendit.co/success",     "cancel_return_url": "https://xendit.co/failure",     "payment_link_url": "https://dev.xen.to/1aNZ0Iq7",     "allow_save_payment_method": "FORCED" } ```   JSON  Copy |
| --- | --- |

2. You will receive webhooks `payment.succeeded` to indicate the payment process success and `payment_token.activated` to retrieve the `payment_token_id`
3. Create the subscription plan using the retrieved `payment_token_id`  and the same customer\_id\

   | Request - POST /recurring/plans  Custom  ``` {     "reference_id": "plan-{{$timestamp}}",       "customer_id": "cust-dad50e22-8d62-4d56-b888-5f66bfdf5627",     "currency": "IDR",     "amount": 10000,     "payment_tokens": [         {             "payment_token_id": "pt-8e6dc396-3a83-4829-900d-b9baac71ccc0",             "rank": 1         }     ],     "schedule": {         "interval": "MONTH",         "interval_count": 1,         "anchor_date": "2026-04-09T23:23:52+07:00",         "total_recurrence": 100,         "retry_interval": "DAY",         "retry_interval_count": 5,         "total_retry": 7,         "failed_attempt_notifications": [             1,             3,             5         ]     },     "immediate_payment": false,     "failed_cycle_action": "RESUME",     "notification_channels": [         "EMAIL",         "EMAIL"     ],     "locale": "en",     "payment_link_for_failed_attempt": true,       "metadata": {         "customKey": "customValue"       },     "description": "Subscription Example 01" } ```   JSON  Copy | Response - POST /recurring/plans  Custom  ``` {     "id": "repl_88583554-7e7b-47ec-9b2b-6dcdda984402",     "reference_id": "plan-1775640035",     "customer_id": "cust-dad50e22-8d62-4d56-b888-5f66bfdf5627",     "failed_cycle_action": "RESUME",     "recurring_cycle_count": 0,     "country": "ID",     "currency": "IDR",     "amount": 10000,     "status": "ACTIVE",     "created": "2026-04-08T09:20:35.704Z",     "updated": "2026-04-08T09:20:35.704Z",     "payment_tokens": [         {             "payment_token_id": "pt-8e6dc396-3a83-4829-900d-b9baac71ccc0",             "rank": 1         }     ],     "schedule": {         "interval": "MONTH",         "interval_count": 1,         "total_recurrence": 100,         "anchor_date": "2026-04-09T23:23:52+07:00",         "retry_interval": "DAY",         "retry_interval_count": 5,         "total_retry": 7,         "failed_attempt_notifications": [             1,             3,             5         ],         "created": "2026-04-08T09:20:35.704Z",         "updated": "2026-04-08T09:20:35.704Z"     },     "immediate_payment": false,     "locale": "en",     "notification_channels": [         "EMAIL",         "EMAIL"     ],     "metadata": {         "customKey": "customValue"     },     "description": "Subscription Example 01",     "items": null,     "payment_link_for_failed_attempt": true,     "failure_code": null } ```   JSON  Copy |
   | --- | --- |
4. Once the end user successfully links their payment method, Xendit will send a `recurring.plan.activation` webhook to confirm the activation of the subscription plan.
5. Listen to the cycle webhooks `recurring.cycle`) to track the status of each subscription cycle. Continue monitoring until all cycles are completed to ensure seamless execution and visibility into the subscription process.
